#!/usr/bin/env python3
"""
Generate concrete seed data for the first foundation forks from fetched source modules.

Outputs machine-readable snapshots that help map source modules into the first
v2 fork implementations without touching live-connected structures.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
SOURCE = ROOT / "hubspot" / "source-theme" / "modules"
OUT_JSON = ROOT / "docs" / "generated" / "foundation-seed-data.json"
OUT_MD = ROOT / "docs" / "generated" / "foundation-seed-data.md"


MODULE_MAP = [
    {
        "source_module": "cinematic_hero.module",
        "target_module": "hero-cinematic-v2",
        "target_role": "hero",
        "field_highlights": [
            "background_type",
            "background_video_url",
            "background_video_file",
            "background_image",
            "section_tag",
            "headline",
            "headline_highlight",
            "lead_text",
            "sub_text",
            "cta_primary_text",
            "cta_primary_url",
            "cta_secondary_text",
            "cta_secondary_url",
        ],
    },
    {
        "source_module": "cinematic_problem_list.module",
        "target_module": "problem-grid-v2",
        "target_role": "problem-grid",
        "field_highlights": [
            "section_tag",
            "headline",
            "intro_text",
            "items",
            "item_title",
            "item_text",
            "item_icon",
        ],
    },
    {
        "source_module": "cinematic_two_engines.module",
        "target_module": "service-pillars-v2",
        "target_role": "two-engines-to-pillars",
        "field_highlights": [
            "section_tag",
            "headline",
            "intro_text",
            "left_title",
            "left_text",
            "right_title",
            "right_text",
            "cta_text",
            "cta_url",
        ],
    },
    {
        "source_module": "cinematic_metrics.module",
        "target_module": "stats-trust-band-v2",
        "target_role": "metrics",
        "field_highlights": [
            "section_tag",
            "headline",
            "metric_1_value",
            "metric_1_label",
            "metric_2_value",
            "metric_2_label",
            "metric_3_value",
            "metric_3_label",
        ],
    },
    {
        "source_module": "cinematic_koulutus_form.module",
        "target_module": "lead-capture-form-cta-v2",
        "target_role": "form-cta",
        "field_highlights": [
            "section_tag",
            "headline",
            "lead_text",
            "form_id",
            "cta_text",
            "cta_url",
            "background_variant",
        ],
    },
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def extract_fields(module_dir: Path, wanted: list[str]) -> list[dict]:
    fields_path = module_dir / "fields.json"
    if not fields_path.exists():
        return []

    data = load_json(fields_path)
    out = []
    for field in data:
        name = field.get("name") or field.get("id")
        if name in wanted:
            out.append(
                {
                    "name": name,
                    "label": field.get("label"),
                    "type": field.get("type"),
                    "default": field.get("default"),
                    "choices": field.get("choices"),
                    "help_text": field.get("help_text"),
                }
            )
    return out


def extract_meta(module_dir: Path) -> dict:
    meta_path = module_dir / "meta.json"
    if not meta_path.exists():
        return {}
    data = load_json(meta_path)
    return {
        "label": data.get("label"),
        "categories": data.get("categories"),
        "content_types": data.get("content_types"),
        "global": data.get("global"),
        "is_available_for_new_content": data.get("is_available_for_new_content"),
    }


def build_seed_entry(spec: dict) -> dict:
    module_dir = SOURCE / spec["source_module"]
    return {
        "source_module": spec["source_module"],
        "target_module": spec["target_module"],
        "target_role": spec["target_role"],
        "exists": module_dir.exists(),
        "meta": extract_meta(module_dir) if module_dir.exists() else {},
        "highlight_fields": extract_fields(module_dir, spec["field_highlights"]) if module_dir.exists() else [],
        "paths": {
            "module_dir": str(module_dir.relative_to(ROOT)) if module_dir.exists() else None,
            "fields_json": str((module_dir / "fields.json").relative_to(ROOT)) if (module_dir / "fields.json").exists() else None,
            "meta_json": str((module_dir / "meta.json").relative_to(ROOT)) if (module_dir / "meta.json").exists() else None,
            "module_html": str((module_dir / "module.html").relative_to(ROOT)) if (module_dir / "module.html").exists() else None,
        },
        "notes": [
            "Use this only as seed/reference data for v2 forking.",
            "Do not modify the source module directly.",
        ],
    }


def write_md(entries: list[dict]):
    lines = [
        "# Foundation seed data",
        "",
        "Tämä tiedosto kokoaa ensimmäisten foundation-forkkien tärkeimmät seed-tiedot source-theme-moduuleista.",
        "",
    ]

    for entry in entries:
        lines.extend(
            [
                f"## {entry['target_module']}",
                "",
                f"- Source module: `{entry['source_module']}`",
                f"- Target role: `{entry['target_role']}`",
                f"- Exists in source: `{entry['exists']}`",
            ]
        )
        if entry["meta"]:
            lines.extend(
                [
                    f"- Source label: `{entry['meta'].get('label')}`",
                    f"- Categories: `{entry['meta'].get('categories')}`",
                    f"- Content types: `{entry['meta'].get('content_types')}`",
                ]
            )
        lines.extend(["", "### Highlight fields", ""])
        for field in entry["highlight_fields"]:
            lines.append(
                f"- `{field['name']}` ({field['type']}) — label: `{field['label']}`"
            )
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    entries = [build_seed_entry(spec) for spec in MODULE_MAP]
    payload = {
        "version": 1,
        "source_theme": "hubspot/source-theme",
        "entries": entries,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(entries)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
