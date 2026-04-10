#!/usr/bin/env python3
"""
Generate HubSpot-friendly content data packs for first-wave v2 pages.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
INPUT = ROOT / "docs" / "generated" / "kuulu-first-wave-content-packs.json"
OUTPUT = ROOT / "docs" / "generated" / "kuulu-first-wave-hs-data.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def to_slug(label: str) -> str:
    return (
        label.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
        .replace(":", "")
        .replace(".", "")
    )


def page_to_hs_data(page: dict) -> dict:
    modules = []
    for index, section in enumerate(page["section_stack"], start=1):
        modules.append(
            {
                "order": index,
                "module": section["module"],
                "module_instance_key": f"{page['page_id']}__{section['module']}__{index}",
                "content_job": section["content_job"],
                "source_priority": section["source_priority"],
                "editor_notes": [
                    "Täytä sisältö moduulikohtaisten guardrailien mukaan.",
                    "Pidä CTA-tekstit lyhyinä ja toimintolähtöisinä.",
                    "Älä riko 95/5 / Brand DNA / Sisältökoneisto / Liidimoottori -linjaa sivun roolista riippuen.",
                ],
            }
        )

    return {
        "page_id": page["page_id"],
        "template": page["template"],
        "preview_slug": page["preview_slug"],
        "url": page["url"],
        "page_settings": {
            "title_strategy": "derive from approved copy",
            "meta_description_strategy": "write after content finalization",
            "noindex_preview": True,
            "canonical_strategy": "self canonical on preview, production canonical on cutover",
        },
        "hero_direction": page["hero_direction"],
        "mandatory_signals": page["mandatory_signals"],
        "modules": modules,
    }


def main():
    packs = load_json(INPUT)
    payload = {
        "version": 1,
        "description": "HubSpot-friendly structured content packs for Kuulu first-wave v2 pages.",
        "build_order": [
            "video-service-v2",
            "training-v2",
            "digimarkkinointi-v2",
            "case-studies-v2",
            "yhteystiedot-v2",
            "homepage-v2",
        ],
        "pages": [page_to_hs_data(page) for page in packs],
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
