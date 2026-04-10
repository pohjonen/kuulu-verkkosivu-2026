#!/usr/bin/env python3
"""
Validate consistency across generated pre-auth planning artifacts.

Purpose:
- catch drift between inventory, manifests, packets, source extracts and blueprint
- ensure the refresh pipeline leaves the workspace in a coherent state
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"

INVENTORY = GENERATED / "kuulu-public-site-inventory.json"
FIRST_WAVE_PACKS = GENERATED / "kuulu-first-wave-content-packs.json"
FIRST_WAVE_HS = GENERATED / "kuulu-first-wave-hs-data.json"
FIRST_WAVE_EXTRACTS = GENERATED / "kuulu-first-wave-source-extracts.json"
FIRST_WAVE_LINKS = GENERATED / "kuulu-first-wave-link-map.json"
FIRST_WAVE_PACKETS_INDEX = GENERATED / "first-wave-page-build-packets" / "index.json"
ALL_SOURCE_EXTRACTS = GENERATED / "kuulu-all-source-extracts.json"
ALL_PACKETS_INDEX = GENERATED / "all-page-build-packets" / "index.json"
REDIRECT_REGISTER = GENERATED / "kuulu-redirect-register.json"
CUTOVER_CHECKLIST = GENERATED / "kuulu-cutover-checklist.json"
IMPLEMENTATION_STATUS = GENERATED / "kuulu-v2-implementation-status.json"
PUBLIC_CMS_METADATA = GENERATED / "kuulu-public-cms-metadata.json"
PUBLIC_ASSET_SIGNATURE = GENERATED / "kuulu-public-asset-signature.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str):
    raise SystemExit(message)


def assert_condition(condition: bool, message: str):
    if not condition:
        fail(message)


def main():
    inventory = load_json(INVENTORY)
    first_wave_packs = load_json(FIRST_WAVE_PACKS)
    first_wave_hs = load_json(FIRST_WAVE_HS)["pages"]
    first_wave_extracts = load_json(FIRST_WAVE_EXTRACTS)
    first_wave_links = load_json(FIRST_WAVE_LINKS)
    first_wave_packets_index = load_json(FIRST_WAVE_PACKETS_INDEX)["packets"]
    all_source_extracts = load_json(ALL_SOURCE_EXTRACTS)
    all_packets_index = load_json(ALL_PACKETS_INDEX)["packets"]
    redirect_register = load_json(REDIRECT_REGISTER)
    cutover = load_json(CUTOVER_CHECKLIST)
    implementation = load_json(IMPLEMENTATION_STATUS)
    cms_metadata = load_json(PUBLIC_CMS_METADATA)
    asset_signature = load_json(PUBLIC_ASSET_SIGNATURE)

    inventory_urls = {item["url"] for item in inventory}
    inventory_page_types = {item["url"]: item["page_type"] for item in inventory}

    # First-wave consistency
    fw_ids = {item["page_id"] for item in first_wave_packs}
    assert_condition(fw_ids == {item["page_id"] for item in first_wave_extracts}, "First-wave content packs and source extracts are out of sync.")
    assert_condition(fw_ids == {item["page_id"] for item in first_wave_links}, "First-wave content packs and link maps are out of sync.")
    assert_condition(fw_ids == {item["page_id"] for item in first_wave_hs}, "First-wave content packs and HS data are out of sync.")
    assert_condition(fw_ids == {item["page_id"] for item in first_wave_packets_index}, "First-wave page packet index is out of sync.")

    # Full-site consistency
    assert_condition(inventory_urls == {item["url"] for item in all_source_extracts}, "All-source-extract URLs do not match inventory URLs.")
    assert_condition(inventory_urls == {item["url"] for item in redirect_register}, "Redirect register URLs do not match inventory URLs.")
    assert_condition(inventory_urls == {item["url"] for item in cms_metadata}, "Public CMS metadata URLs do not match inventory URLs.")

    # All-page packets should exist for every inventory row
    all_packet_ids = {item["page_id"] for item in all_packets_index}
    expected_packet_ids = set()
    for row in inventory:
        slug = row["preview_slug"].strip("/").replace("/", "__").replace("-", "_")
        if not slug:
            slug = "homepage_v2"
        expected_packet_ids.add(f"{slug}__{row['page_type']}".replace(".", "_"))
    assert_condition(all_packet_ids == expected_packet_ids, "All-page build packet index does not match inventory-derived packet IDs.")

    # Cutover waves should cover all redirect register URLs
    wave_urls = set()
    for items in cutover["waves"].values():
        wave_urls.update(item["url"] for item in items)
    assert_condition(wave_urls == inventory_urls, "Cutover checklist waves do not cover all inventory URLs.")

    # Implementation status sanity
    assert_condition(implementation["portal_id"] == "450584", "Implementation status portal_id drifted from expected value.")
    counts = {}
    for row in inventory:
        counts[row["page_type"]] = counts.get(row["page_type"], 0) + 1
    assert_condition(counts == implementation["page_type_counts"], "Implementation status page_type_counts do not match inventory.")

    # Asset signature sanity
    assert_condition(asset_signature["portal_id"] == "450584", "Public asset signature portal_id drifted from expected value.")
    assert_condition(asset_signature["summary"]["page_count"] == len(asset_signature["pages"]), "Asset signature page_count mismatch.")

    # Public CMS metadata sanity
    for item in cms_metadata:
        assert_condition(item["page_type"] == inventory_page_types[item["url"]], f"CMS metadata page_type drifted for {item['url']}")

    print("pre-auth artifacts validated successfully.")


if __name__ == "__main__":
    main()
