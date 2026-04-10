#!/usr/bin/env python3
"""
Validate the local Kuulu v2 blueprint scaffold structure.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
BLUEPRINT = ROOT / "hubspot" / "kuulu-theme-v2-blueprint"
PAGES_MANIFEST = ROOT / "docs" / "generated" / "kuulu-v2-page-manifest.json"
MODULES_MANIFEST = ROOT / "docs" / "generated" / "kuulu-v2-module-manifest.json"


def fail(message: str):
    raise SystemExit(message)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    if not BLUEPRINT.exists():
        fail(f"Blueprint directory not found: {BLUEPRINT}")

    pages = load_json(PAGES_MANIFEST)
    modules = load_json(MODULES_MANIFEST)

    expected_templates = {page["template"] for page in pages}
    expected_templates.update(
        {
            "homepage-v2",
            "service-landing-v2",
            "training-landing-v2",
            "video-service-landing-v2",
            "reference-index-v2",
            "reference-detail-v2",
            "company-info-v2",
            "person-profile-v2",
            "legal-v2",
        }
    )
    expected_template_paths = {f"{name}.html" for name in expected_templates}

    actual_template_paths = {p.name for p in (BLUEPRINT / "templates").glob("*") if p.is_file()}
    if actual_template_paths != expected_template_paths:
        fail(
            "Template scaffold mismatch.\n"
            f"Expected: {sorted(expected_template_paths)}\n"
            f"Actual: {sorted(actual_template_paths)}"
        )

    expected_partials = {"header-v2.html", "footer-v2.html", "navigation-v2.html"}
    actual_partials = {p.name for p in (BLUEPRINT / "partials").glob("*") if p.is_file()}
    if actual_partials != expected_partials:
        fail(
            "Partial scaffold mismatch.\n"
            f"Expected: {sorted(expected_partials)}\n"
            f"Actual: {sorted(actual_partials)}"
        )

    expected_globals = {
        "navigation-v2.global.json",
        "header-v2.global.json",
        "footer-v2.global.json",
        "brand-settings.global.json",
        "cta-defaults.global.json",
    }
    actual_globals = {p.name for p in (BLUEPRINT / "global").glob("*.json")}
    if actual_globals != expected_globals:
        fail(
            "Global scaffold mismatch.\n"
            f"Expected: {sorted(expected_globals)}\n"
            f"Actual: {sorted(actual_globals)}"
        )

    expected_assets = {
        "css/theme-tokens.css",
        "css/theme-base.css",
        "css/theme-utilities.css",
        "css/theme-components.css",
        "js/theme-base.js",
    }
    actual_assets = {
        str(p.relative_to(BLUEPRINT / "assets"))
        for p in (BLUEPRINT / "assets").rglob("*")
        if p.is_file()
    }
    if actual_assets != expected_assets:
        fail(
            "Asset scaffold mismatch.\n"
            f"Expected: {sorted(expected_assets)}\n"
            f"Actual: {sorted(actual_assets)}"
        )

    module_keys = {module["module_key"] for module in modules}
    module_dirs = {p.name.replace(".module", "") for p in (BLUEPRINT / "modules").glob("*.module")}
    if module_dirs != module_keys:
        fail(
            "Module scaffold mismatch.\n"
            f"Expected: {sorted(module_keys)}\n"
            f"Actual: {sorted(module_dirs)}"
        )

    for module_key in sorted(module_keys):
        module_dir = BLUEPRINT / "modules" / f"{module_key}.module"
        expected_files = {"README.md", "spec.json", "fields.json", "meta.json", "module.html", "module.css", "module.js"}
        actual_files = {p.name for p in module_dir.glob("*") if p.is_file()}
        if actual_files != expected_files:
            fail(
                f"Module {module_key} file mismatch.\n"
                f"Expected: {sorted(expected_files)}\n"
                f"Actual: {sorted(actual_files)}"
            )

    print("kuulu-theme-v2 blueprint scaffold validated successfully.")


if __name__ == "__main__":
    main()
