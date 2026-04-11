#!/usr/bin/env python3
"""
Generate machine-readable cutover support registers from the public site inventory.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"
INVENTORY_CSV = GENERATED / "kuulu-public-site-inventory.csv"
REDIRECT_JSON = GENERATED / "kuulu-redirect-register.json"
CUTOVER_JSON = GENERATED / "kuulu-cutover-checklist.json"
STATUS_JSON = GENERATED / "kuulu-v2-implementation-status.json"


def load_inventory():
    with INVENTORY_CSV.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def decision_for(row: dict) -> tuple[str, str]:
    url = row["url"]
    if url == "https://www.kuulu.fi/":
        return "replace-in-place", "Homepage switched last."
    if row["page_type"] == "reference-detail":
        return "keep-and-normalize", "Keep existing case URL, normalize into reference-detail-v2."
    if row["page_type"] == "legal":
        return "keep-and-normalize", "Keep slug, normalize to legal-v2."
    if url.endswith("/videotuotanto_vanha"):
        return "decide-later", "Assess traffic and internal links before redirect decision."
    if url.endswith("/asiakasreferenssit"):
        return "keep-separate-for-now", "Can stay separate from /case-studies until later consolidation."
    if "projektinhallinta-tekoalylla-perjantaipulssi" in url:
        return "keep-separate-for-now", "Campaign landing can remain separate in first wave."
    if row["page_type"] in {"training", "service", "video-service", "company-info", "person-profile", "reference-index"}:
        return "keep-and-normalize", "Keep current slug and publish v2 into same URL at cutover."
    return "replace-in-place", "Default safe decision."


def cutover_wave_for(row: dict) -> int:
    url = row["url"]
    if url == "https://www.kuulu.fi/":
        return 8
    if row["page_type"] == "video-service":
        return 1
    if row["page_type"] == "training":
        return 2
    if row["page_type"] == "service":
        return 3
    if row["page_type"] == "reference-index":
        return 4
    if row["page_type"] == "reference-detail":
        return 5
    if row["page_type"] in {"company-info", "legal"}:
        return 6
    if row["page_type"] == "person-profile":
        return 7
    return 9


def build_redirect_register(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        decision, reason = decision_for(row)
        out.append(
            {
                "url": row["url"],
                "preview_slug": row["preview_slug"],
                "page_type": row["page_type"],
                "current_theme": row["current_theme"],
                "v2_template": row["v2_template"],
                "decision": decision,
                "redirect_required": decision == "decide-later",
                "reason": reason,
                "cutover_wave": cutover_wave_for(row),
            }
        )
    return out


def build_cutover_checklist(rows: list[dict]) -> dict:
    waves = {}
    for row in rows:
        wave = str(cutover_wave_for(row))
        waves.setdefault(wave, []).append(
            {
                "url": row["url"],
                "preview_slug": row["preview_slug"],
                "page_type": row["page_type"],
                "v2_template": row["v2_template"],
                "must_check": [
                    "title",
                    "h1",
                    "cta-links",
                    "forms" if row["uses_hs_form"] == "yes" else "no-form-check",
                    "video-embed" if row["uses_video_embed"] == "yes" else "no-video-check",
                    "mobile-layout",
                ],
            }
        )

    return {
        "cutover_order_description": [
            "1 = video-service",
            "2 = training",
            "3 = service",
            "4 = reference-index",
            "5 = reference-detail",
            "6 = company-info and legal",
            "7 = person-profile",
            "8 = homepage last",
        ],
        "waves": waves,
    }


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path}")


def build_status_snapshot(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        counts[row["page_type"]] = counts.get(row["page_type"], 0) + 1

    return {
        "portal_id": "450584",
        "auth_status": "missing",
        "source_theme_status": "not_fetched",
        "v2_blueprint_status": "created",
        "public_inventory_status": "generated",
        "page_type_counts": counts,
        "first_wave_pages": [
            "https://www.kuulu.fi/",
            "https://www.kuulu.fi/videotuotanto",
            "https://www.kuulu.fi/koulutus",
            "https://www.kuulu.fi/digimarkkinointi",
            "https://www.kuulu.fi/case-studies",
            "https://www.kuulu.fi/yhteystiedot",
        ],
        "next_blocker": "Run hs account auth or provide current HubSpot theme export.",
    }


def main():
    rows = load_inventory()
    write_json(REDIRECT_JSON, build_redirect_register(rows))
    write_json(CUTOVER_JSON, build_cutover_checklist(rows))
    write_json(STATUS_JSON, build_status_snapshot(rows))


if __name__ == "__main__":
    main()
