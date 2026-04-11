#!/usr/bin/env python3
"""
Generate per-page build packets for Kuulu first-wave v2 pages.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"

CONTENT_PACKS = GENERATED / "kuulu-first-wave-content-packs.json"
HS_DATA = GENERATED / "kuulu-first-wave-hs-data.json"
LINK_MAP = GENERATED / "kuulu-first-wave-link-map.json"
SOURCE_EXTRACTS = GENERATED / "kuulu-first-wave-source-extracts.json"
OUT_DIR = GENERATED / "first-wave-page-build-packets"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def index_by(items: list[dict], key: str) -> dict[str, dict]:
    return {item[key]: item for item in items}


def build_packet(page_id: str, content_pack: dict, hs_data: dict, link_map: dict, source_extract: dict) -> dict:
    modules = []
    hs_modules = {m["module_instance_key"]: m for m in hs_data["modules"]}

    for idx, section in enumerate(content_pack["section_stack"], start=1):
        instance_key = f"{page_id}__{section['module']}__{idx}"
        modules.append(
            {
                "order": idx,
                "module": section["module"],
                "module_instance_key": instance_key,
                "content_job": section["content_job"],
                "source_priority": section["source_priority"],
                "editor_notes": hs_modules.get(instance_key, {}).get("editor_notes", []),
            }
        )

    return {
        "page_id": page_id,
        "template": content_pack["template"],
        "preview_slug": content_pack["preview_slug"],
        "url": content_pack["url"],
        "primary_goal": content_pack["primary_goal"],
        "core_message": content_pack["core_message"],
        "hero_direction": content_pack["hero_direction"],
        "mandatory_signals": content_pack["mandatory_signals"],
        "page_settings": hs_data.get("page_settings", {}),
        "module_plan": modules,
        "source_extract": {
            "title": source_extract.get("title"),
            "headings": source_extract.get("headings", []),
            "paragraphs": source_extract.get("paragraphs", []),
            "cta_candidates": source_extract.get("cta_candidates", []),
        },
        "link_map": {
            "link_count": link_map.get("link_count", 0),
            "internal_links": link_map.get("internal_links", []),
        },
    }


def main():
    content_packs = index_by(load_json(CONTENT_PACKS), "page_id")
    hs_pages = index_by(load_json(HS_DATA)["pages"], "page_id")
    link_pages = index_by(load_json(LINK_MAP), "page_id")
    source_pages = index_by(load_json(SOURCE_EXTRACTS), "page_id")

    packets_summary = []

    for page_id, content_pack in content_packs.items():
        packet = build_packet(
            page_id,
            content_pack,
            hs_pages[page_id],
            link_pages[page_id],
            source_pages[page_id],
        )
        path = OUT_DIR / f"{page_id}.json"
        write_json(path, packet)
        packets_summary.append(
            {
                "page_id": page_id,
                "path": str(path.relative_to(ROOT)),
                "module_count": len(packet["module_plan"]),
                "link_count": packet["link_map"]["link_count"],
            }
        )

    write_json(OUT_DIR / "index.json", {"packets": packets_summary})
    print(f"Wrote {OUT_DIR}")


if __name__ == "__main__":
    main()
