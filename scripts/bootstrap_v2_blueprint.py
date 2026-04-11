#!/usr/bin/env python3
"""
Generate a safe local blueprint from v2 manifests.

This does NOT try to mirror a real fetched HubSpot theme.
Instead it creates a local implementation-ready scaffold that can be
mapped into the real source theme after HubSpot auth/export is available.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path("/workspace")
PAGES_PATH = ROOT / "docs" / "generated" / "kuulu-v2-page-manifest.json"
MODULES_PATH = ROOT / "docs" / "generated" / "kuulu-v2-module-manifest.json"
OUT = ROOT / "hubspot" / "kuulu-theme-v2-blueprint"
BLUEPRINT_DIRS = ["assets", "global", "manifests", "modules", "partials", "templates"]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def reset_blueprint_root():
    if OUT.exists():
        for child in OUT.iterdir():
            if child.name in BLUEPRINT_DIRS:
                if child.is_dir():
                    shutil.rmtree(child)
                else:
                    child.unlink()


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

- {len(pages)} inventoidun ei-blogi-sivuston v2-sivua blueprint-muodossa
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
        "global_structure": {
            "header": "partials/header-v2.html",
            "footer": "partials/footer-v2.html",
            "navigation": "global/navigation-v2.json",
            "globals": [
                "global/brand-settings.json",
                "global/cta-defaults.json",
            ],
        },
    }


def blueprint_theme_json():
    return {
        "label": "Kuulu Theme V2 Blueprint",
        "preview_path": "./templates/homepage-v2.html",
        "version": 1,
        "author": "AI scaffold for Kuulu v2",
        "documentation": [
            "docs/hubspot-theme-token-map.md",
            "docs/hubspot-module-hubl-mapping.md",
        ],
        "token_strategy": {
            "background": {
                "primary": "#0a0a0a",
                "surface": "#141414",
            },
            "accent": {
                "primary": "#00FF87",
                "mid": "#00D46A",
                "deep": "#009F4E",
            },
            "text": {
                "primary": "#FFFFFF",
                "secondary": "#A0A0A0",
                "dim": "#6B6B6B",
            },
            "fonts": {
                "display": "Bebas Neue",
                "body": "Inter",
                "mono": "JetBrains Mono",
            },
        },
        "notes": [
            "Blueprint-only theme.json placeholder before real source theme export.",
            "Map these tokens into the fetched source theme, do not treat this file as production-ready.",
        ],
    }


ALL_TEMPLATE_FILES = [
    "homepage-v2.html",
    "service-landing-v2.html",
    "training-landing-v2.html",
    "video-service-landing-v2.html",
    "reference-index-v2.html",
    "reference-detail-v2.html",
    "company-info-v2.html",
    "person-profile-v2.html",
    "legal-v2.html",
]


def blueprint_base_css():
    return """/* Kuulu v2 blueprint base tokens
 * Replace and merge into the real fetched theme after audit.
 */

:root {
  --color-bg-primary: #0a0a0a;
  --color-bg-secondary: #141414;
  --color-accent-primary: #00FF87;
  --color-accent-mid: #00D46A;
  --color-accent-deep: #009F4E;
  --color-text-primary: #FFFFFF;
  --color-text-secondary: #A0A0A0;
  --color-text-dim: #6B6B6B;

  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-card: 24px;
  --radius-section: 32px;
  --radius-button: 50px;
  --radius-input: 8px;

  --glow-lg: 0 0 60px rgba(0,255,135,0.3);
  --glow-sm: 0 0 30px rgba(0,255,135,0.2);
  --shadow-card: 0 25px 50px -12px rgba(0,0,0,0.7);
  --transition-default: 0.3s ease;
}
"""


def blueprint_theme_base_css():
    return """/* Kuulu v2 blueprint base styles
 * Keep this layer lightweight and token-driven.
 */

html,
body {
  margin: 0;
  padding: 0;
  background: var(--color-bg-primary);
  color: var(--color-text-primary);
  font-family: var(--font-body);
}

a {
  color: var(--color-accent-primary);
}

:focus-visible {
  outline: 2px solid var(--color-accent-primary);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
"""


def blueprint_theme_utilities_css():
    return """/* Kuulu v2 blueprint utility styles */

.kuulu-container {
  width: min(1200px, calc(100% - 2rem));
  margin: 0 auto;
}

.kuulu-text-gradient {
  background: linear-gradient(135deg, var(--color-accent-primary), var(--color-accent-deep));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.kuulu-surface-glass {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(12px);
  border-radius: var(--radius-card);
}

.kuulu-aurora-soft {
  background:
    radial-gradient(circle at top left, rgba(0,255,135,0.12), transparent 40%),
    radial-gradient(circle at bottom right, rgba(0,212,106,0.08), transparent 42%),
    var(--color-bg-primary);
}
"""


def blueprint_theme_components_css():
    return """/* Kuulu v2 blueprint component defaults */

.kuulu-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.85rem 1.4rem;
  border-radius: var(--radius-button);
  background: linear-gradient(135deg, var(--color-accent-primary), var(--color-accent-deep));
  color: #0a0a0a;
  font-family: var(--font-display);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  box-shadow: var(--glow-sm);
  text-decoration: none;
}

.kuulu-card {
  border-radius: var(--radius-card);
  background: var(--color-bg-secondary);
  color: var(--color-text-primary);
  box-shadow: var(--shadow-card);
}
"""


def blueprint_base_js():
    return """// Kuulu v2 blueprint base JS
// Keep real implementation lightweight and progressive.

document.documentElement.dataset.kuuluV2Blueprint = 'true';
"""


def blueprint_partial_header():
    return """<!--
Blueprint header-v2 partial

Use this partial to isolate the future v2 header from current live header dependencies.
Do not bind this to production before cutover.
-->
"""


def blueprint_partial_footer():
    return """<!--
Blueprint footer-v2 partial

Use this partial to isolate the future v2 footer from current live footer dependencies.
Do not bind this to production before cutover.
-->
"""


def blueprint_partial_navigation():
    return """<!--
Blueprint navigation-v2 partial

Use this partial to keep v2 navigation isolated from the current live navigation.
Do not bind this to production before cutover.
-->
"""


def blueprint_navigation_json():
    return {
        "label": "navigation-v2",
        "notes": [
            "Blueprint-only navigation structure for v2.",
            "Keep separate from live navigation until approved cutover.",
        ],
        "items": [
            {"label": "Koulutus", "url": "https://www.kuulu.fi/koulutus"},
            {"label": "Digimarkkinointi", "url": "https://www.kuulu.fi/digimarkkinointi"},
            {"label": "Videotuotanto", "url": "https://www.kuulu.fi/videotuotanto"},
            {"label": "Referenssit", "url": "https://www.kuulu.fi/case-studies"},
            {"label": "Ota yhteyttä", "url": "https://www.kuulu.fi/yhteystiedot"},
        ],
    }


def blueprint_brand_settings():
    return {
        "label": "brand-settings",
        "token_source": "docs/hubspot-theme-token-map.md",
        "defaults": {
            "theme_mode": "cinematic-dark",
            "accent_mode": "green",
            "show_grain": True,
            "show_aurora": True,
        },
    }


def blueprint_cta_defaults():
    return {
        "label": "cta-defaults",
        "defaults": {
            "primary_variant": "kuulu-button-primary",
            "max_buttons_per_section": 2,
            "meeting_cta_copy": "VARAA SPARRAUS",
        },
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


def module_fields_blueprint(module):
    field_groups = []
    for group in module.get("field_groups", []):
        field_groups.append(
            {
                "name": group,
                "label": group.replace("-", " ").replace("_", " ").title(),
                "help_text": f"Blueprint group for {module['module_key']}: {group}",
            }
        )

    required_fields = module.get("required_fields") or []
    optional_fields = module.get("optional_fields") or []

    return {
        "module_label": module["module_key"],
        "build_wave": module.get("build_wave"),
        "field_groups": field_groups,
        "required_fields": [
            {
                "name": field,
                "label": field.replace("_", " ").title(),
                "required": True,
                "type_hint": "determine in real HubSpot implementation",
            }
            for field in required_fields
        ],
        "optional_fields": [
            {
                "name": field,
                "label": field.replace("_", " ").title(),
                "required": False,
                "type_hint": "determine in real HubSpot implementation",
            }
            for field in optional_fields
        ],
        "guardrails": module.get("guardrails", {}),
        "notes": [
            "Blueprint-only scaffold. Convert into valid HubSpot fields.json in the real v2 theme.",
            "Keep editor guardrails strict; do not expose free-form styling without a strong reason.",
        ],
    }


def module_meta_blueprint(module):
    return {
        "label": module["module_key"],
        "icon": "module",
        "categories": ["kuulu-v2", module.get("category", "uncategorized")],
        "is_available_for_new_content": False,
        "blueprint_only": True,
        "notes": [
            "Generated as a local planning scaffold before real HubSpot module implementation.",
        ],
    }


def main():
    pages = load(PAGES_PATH)
    modules = load(MODULES_PATH)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "README.md", bootstrap_readme(pages, modules))
    write_json(OUT / "blueprint.json", bootstrap_theme_manifest())
    write_json(OUT / "theme.json", blueprint_theme_json())
    write_json(OUT / "manifests" / "pages.json", pages)
    write_json(OUT / "manifests" / "modules.json", modules)
    write(OUT / "assets" / "css" / "theme-tokens.css", blueprint_base_css())
    write(OUT / "assets" / "css" / "theme-base.css", blueprint_theme_base_css())
    write(OUT / "assets" / "css" / "theme-utilities.css", blueprint_theme_utilities_css())
    write(OUT / "assets" / "css" / "theme-components.css", blueprint_theme_components_css())
    write(OUT / "assets" / "js" / "theme-base.js", blueprint_base_js())
    write(OUT / "partials" / "header-v2.html", blueprint_partial_header())
    write(OUT / "partials" / "footer-v2.html", blueprint_partial_footer())
    write(OUT / "partials" / "navigation-v2.html", blueprint_partial_navigation())
    write_json(OUT / "global" / "navigation-v2.global.json", blueprint_navigation_json())
    write_json(OUT / "global" / "header-v2.global.json", {"label": "header-v2", "partial": "partials/header-v2.html"})
    write_json(OUT / "global" / "footer-v2.global.json", {"label": "footer-v2", "partial": "partials/footer-v2.html"})
    write_json(OUT / "global" / "brand-settings.global.json", blueprint_brand_settings())
    write_json(OUT / "global" / "cta-defaults.global.json", blueprint_cta_defaults())

    written_templates = set()
    for page in pages:
        template_name = page["template"]
        if template_name not in written_templates:
            if not template_name.endswith(".html"):
                template_name = f"{template_name}.html"
            write(OUT / "templates" / template_name, template_placeholder(page))
            written_templates.add(template_name)

    for template_name in ALL_TEMPLATE_FILES:
        if template_name not in written_templates:
            write(
                OUT / "templates" / template_name,
                f"""<!--
Kuulu v2 blueprint template

Template: {template_name}
Source URL: n/a
Preview slug: n/a
Page type: inferred-only
Criticality: n/a

This template placeholder exists because the inventory expects this template
class in the eventual v2 theme even if it is not part of the current
first-wave page manifest.
-->
{{# Blueprint placeholder for {template_name} #}}
""",
            )
            written_templates.add(template_name)

    for module in modules:
        module_dir = OUT / "modules" / f'{module["module_key"]}.module'
        write(module_dir / "README.md", module_readme(module))
        write_json(module_dir / "spec.json", module)
        write_json(module_dir / "fields.json", module_fields_blueprint(module))
        write_json(module_dir / "meta.json", module_meta_blueprint(module))
        write(module_dir / "module.html", module_html_placeholder(module))
        write(module_dir / "module.css", module_css_placeholder(module))
        write(module_dir / "module.js", module_js_placeholder(module))

    print(f"Bootstrapped blueprint at {OUT}")


if __name__ == "__main__":
    main()
