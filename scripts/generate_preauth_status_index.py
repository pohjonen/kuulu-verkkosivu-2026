#!/usr/bin/env python3
"""
Generate a high-level index of all pre-auth planning/build artifacts.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"
OUT_JSON = GENERATED / "kuulu-preauth-status-index.json"
OUT_MD = GENERATED / "kuulu-preauth-status-index.md"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def summarize():
    inventory = load_json(GENERATED / "kuulu-public-site-inventory.json")
    module_manifest = load_json(GENERATED / "kuulu-v2-module-manifest.json")
    page_manifest = load_json(GENERATED / "kuulu-v2-page-manifest.json")
    first_wave_index = load_json(GENERATED / "first-wave-page-build-packets" / "index.json")
    all_pages_index = load_json(GENERATED / "all-page-build-packets" / "index.json")
    status = load_json(GENERATED / "kuulu-v2-implementation-status.json")

    return {
        "portal_id": status.get("portal_id"),
        "auth_status": status.get("auth_status"),
        "source_theme_status": status.get("source_theme_status"),
        "public_inventory_pages": len(inventory),
        "v2_page_manifest_count": len(page_manifest),
        "v2_module_manifest_count": len(module_manifest),
        "first_wave_packet_count": len(first_wave_index.get("packets", [])),
        "all_page_packet_count": len(all_pages_index.get("packets", [])),
        "key_artifacts": {
            "inventory": [
                "docs/generated/kuulu-public-site-inventory.csv",
                "docs/generated/kuulu-public-site-inventory.json",
            ],
            "manifests": [
                "docs/generated/kuulu-v2-page-manifest.json",
                "docs/generated/kuulu-v2-module-manifest.json",
            ],
            "build_packets": [
                "docs/generated/first-wave-page-build-packets/index.json",
                "docs/generated/all-page-build-packets/index.json",
            ],
            "safety": [
                "docs/generated/kuulu-redirect-register.json",
                "docs/generated/kuulu-cutover-checklist.json",
                "docs/generated/kuulu-full-link-graph.json",
                "docs/generated/kuulu-public-asset-signature.json",
                "docs/generated/kuulu-public-cms-metadata.json",
            ],
            "blueprint": [
                "hubspot/kuulu-theme-v2-blueprint/",
                "scripts/bootstrap_v2_blueprint.py",
                "scripts/validate_blueprint_scaffold.py",
            ],
        },
        "next_blocker": status.get("next_blocker"),
    }


def write_md(payload: dict):
    lines = [
        "# Kuulu pre-auth status index",
        "",
        f"- Portal ID: `{payload['portal_id']}`",
        f"- Auth status: `{payload['auth_status']}`",
        f"- Source theme status: `{payload['source_theme_status']}`",
        f"- Public inventory pages: `{payload['public_inventory_pages']}`",
        f"- V2 page manifest count: `{payload['v2_page_manifest_count']}`",
        f"- V2 module manifest count: `{payload['v2_module_manifest_count']}`",
        f"- First-wave packet count: `{payload['first_wave_packet_count']}`",
        f"- All-page packet count: `{payload['all_page_packet_count']}`",
        "",
        "## Key artifacts",
        "",
    ]

    for group, items in payload["key_artifacts"].items():
        lines.append(f"### {group}")
        for item in items:
            lines.append(f"- `{item}`")
        lines.append("")

    lines.extend(
        [
            "## Next blocker",
            "",
            payload["next_blocker"],
            "",
        ]
    )

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    payload = summarize()
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(payload)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
