#!/usr/bin/env python3
"""
Prepare a safe local workspace inside hubspot/kuulu-theme-v2 for foundation module work.

This does not modify the fetched source theme. It only creates folders, copies
selected source module references into a dedicated audit/reference area, and
writes a manifest of the planned v2 targets.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path("/workspace")
SOURCE = ROOT / "hubspot" / "source-theme"
V2 = ROOT / "hubspot" / "kuulu-theme-v2"
OUT = V2 / "_foundation-workspace"


FOUNDATION_MAP = [
    {
        "source_module": "cinematic_hero.module",
        "target_module": "hero-cinematic-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "cinematic_problem_list.module",
        "target_module": "problem-grid-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "cinematic_two_engines.module",
        "target_module": "service-pillars-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "cinematic_metrics.module",
        "target_module": "stats-trust-band-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "cinematic_koulutus_form.module",
        "target_module": "lead-capture-form-cta-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "services-grid.module",
        "target_module": "service-pillars-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "video-showcase.module",
        "target_module": "reference-grid-v2",
        "decision": "fork-to-v2",
    },
    {
        "source_module": "person-profile.module",
        "target_module": "person-profile-v2",
        "decision": "fork-to-v2",
    },
]


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Source theme missing: {SOURCE}")
    if not V2.exists():
        raise SystemExit(f"V2 theme clone missing: {V2}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    copied = []

    for item in FOUNDATION_MAP:
        src = SOURCE / "modules" / item["source_module"]
        if not src.exists():
            continue
        dest = OUT / "source-module-references" / item["source_module"]
        shutil.copytree(src, dest)
        copied.append(
            {
                "source_module": item["source_module"],
                "target_module": item["target_module"],
                "decision": item["decision"],
                "copied_to": str(dest.relative_to(V2)),
            }
        )

    manifest = {
        "source_theme": str(SOURCE.relative_to(ROOT)),
        "v2_theme": str(V2.relative_to(ROOT)),
        "workspace_root": str(OUT.relative_to(ROOT)),
        "foundation_modules": copied,
        "notes": [
            "Source module references are copied here read-only for comparison.",
            "Do not edit hubspot/source-theme directly.",
            "Actual implementation work must happen in hubspot/kuulu-theme-v2 only.",
        ],
    }

    write_json(OUT / "foundation-workspace.json", manifest)
    write_text(
        OUT / "README.md",
        """# Foundation workspace

Tämä hakemisto on turvallinen paikallinen vertailutyötila foundation-moduuleille.

- `source-module-references/` sisältää read-only-kopiot source-themen foundation-kandidaateista
- varsinainen toteutus tehdään edelleen `hubspot/kuulu-theme-v2/`-hakemistossa
- `hubspot/source-theme/` pysyy koskemattomana
""",
    )

    print(f"Prepared foundation workspace at {OUT}")


if __name__ == "__main__":
    main()
