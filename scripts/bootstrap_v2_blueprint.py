#!/usr/bin/env python3
"""
Generate a safe local blueprint from v2 manifests.

This does NOT try to mirror a real fetched HubSpot theme.
Instead it creates a local implementation-ready scaffold that can be
mapped into the real source theme after HubSpot auth/export is available.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
PAGES_PATH = ROOT / "docs" / "generated" / "kuulu-v2-page-manifest.json"
MODULES_PATH = ROOT / "docs" / "generated" / "kuulu-v2-module-manifest.json"
OUT = ROOT / "hubspot" / "kuulu-theme-v2-blueprint"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bootstrap_readme(pages, modules):
    return f"""# Kuulu theme v2 blueprint

Tämä hakemisto on paikallinen blueprint-runko Kuulun v2-teemalle.

Se on generoitu manifesteistä:

- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

## Tarkoitus

- antaa selkeä paikallinen runko ennen oikean HubSpot-teeman exportia
- helpottaa template- ja moduulirakenteen hahmottamista
- pienentää riskiä, että live-teemaan kosketaan ennenaikaisesti

## Sisältö

- {len(pages)} ensimmäisen aallon v2-sivua blueprint-muodossa
- {len(modules)} moduulia blueprint-muodossa

## Huomio

Tämä EI ole vielä oikea tuotantoteema. Kun HubSpot-auth/export on saatavilla:

1. haetaan nykyinen teema `hubspot/source-theme/`-hakemistoon
2. kloonataan siitä oikea `hubspot/kuulu-theme-v2/`
3. siirretään tämän blueprintin päätökset oikeaan v2-teemaan
"""


def bootstrap_theme_manifest():
    return {
        "name": "kuulu-theme-v2-blueprint",
        "type": "local-blueprint",
        "status": "pre-export",
        "source_of_truth": [
            "docs/kuulu-content-principles.md",
            "docs/kuulu-module-field-model.md",
            "docs/kuulu-first-wave-section-stacks.md",
            "docs/generated/kuulu-v2-page-manifest.json",
            "docs/generated/kuulu-v2-module-manifest.json",
        ],
        "notes": [
            "Do not upload this blueprint directly as production theme.",
            "Use this blueprint to map modules/templates into the real fetched source theme.",
        ],
    }


def template_placeholder(page):
    sections = "\n".join(f"  - {section}" for section in page["section_stack"])
    sources = "\n".join(f"  - {source}" for source in page.get("content_sources", []))
    return f"""<!--
Kuulu v2 blueprint template

Template: {page["template"]}
Source URL: {page["source_url"]}
Preview slug: {page["slug"]}
Page type: {page["page_type"]}
Criticality: {page.get("criticality", "unknown")}

Section stack:
{sections}

Content sources:
{sources}
-->
{{# Blueprint placeholder for {page["template"]} #}}
"""


def module_readme(module):
    depends = "\n".join(f"- {d}" for d in module.get("depends_on", []))
    groups = "\n".join(f"- {g}" for g in module.get("field_groups", []))
    used = "\n".join(f"- {u}" for u in module.get("used_on", []))
    guardrails = json.dumps(module.get("guardrails", {}), ensure_ascii=False, indent=2)
    return f"""# {module["module_key"]}

## Build wave

{module.get("build_wave")}

## Used on

{used}

## Depends on

{depends}

## Field groups

{groups}

## Guardrails

```json
{guardrails}
```
"""


def module_html_placeholder(module):
    return f"""<!--
Blueprint module placeholder: {module["module_key"]}
This file will be replaced with real HubL/HTML when the actual v2 theme is built.
-->
"""


def module_css_placeholder(module):
    return f"""/* Blueprint placeholder for {module["module_key"]}.
 * Move tokenized styles into the real v2 theme after source-theme export.
 */
"""


def module_js_placeholder(module):
    return f"""// Blueprint placeholder for {module["module_key"]}.
// Add only minimal progressive enhancement in the real implementation.
"""


def main():
    pages = load(PAGES_PATH)
    modules = load(MODULES_PATH)

    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "README.md", bootstrap_readme(pages, modules))
    write_json(OUT / "blueprint.json", bootstrap_theme_manifest())
    write_json(OUT / "manifests" / "pages.json", pages)
    write_json(OUT / "manifests" / "modules.json", modules)

    for page in pages:
        write(OUT / "templates" / f'{page["template"]}.html', template_placeholder(page))

    for module in modules:
        module_dir = OUT / "modules" / f'{module["module_key"]}.module'
        write(module_dir / "README.md", module_readme(module))
        write_json(module_dir / "spec.json", module)
        write(module_dir / "module.html", module_html_placeholder(module))
        write(module_dir / "module.css", module_css_placeholder(module))
        write(module_dir / "module.js", module_js_placeholder(module))

    print(f"Bootstrapped blueprint at {OUT}")


if __name__ == "__main__":
    main()
