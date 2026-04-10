#!/usr/bin/env python3
"""
Audit a fetched HubSpot source theme directory and classify likely risk points.

This script is intentionally conservative: it does not try to understand every
HubSpot file format perfectly. Instead it creates a practical report for the
next implementation step by answering:

- what templates exist
- what modules exist
- what global/shared-looking files exist
- which files look risky for the live homepage and shared structures
- which fetched files match the current public asset signature by filename
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path("/workspace")
SIGNATURE_PATH = ROOT / "docs" / "generated" / "kuulu-public-asset-signature.json"
DEFAULT_OUT_JSON = ROOT / "docs" / "generated" / "fetched-source-theme-audit.json"
DEFAULT_OUT_MD = ROOT / "docs" / "generated" / "fetched-source-theme-audit.md"

TEMPLATE_SUFFIXES = {".html", ".html.j2", ".jinja", ".hubl.html"}
MODULE_SUFFIX = ".module"
ASSET_SUFFIXES = {".css", ".js", ".json"}


def load_signature() -> dict:
    return json.loads(SIGNATURE_PATH.read_text(encoding="utf-8"))


def list_files(base: Path) -> list[Path]:
    return [p for p in base.rglob("*") if p.is_file()]


def classify_risk(path: Path) -> tuple[str, list[str]]:
    rel = str(path)
    reasons: list[str] = []
    risk = "low"

    name_lower = path.name.lower()
    rel_lower = rel.lower()

    if "header" in name_lower or "footer" in name_lower or "global" in rel_lower:
        risk = "high"
        reasons.append("Likely shared/global structure")

    if "navigation" in name_lower or "menu" in name_lower:
        risk = "high"
        reasons.append("Likely navigation dependency")

    if "home" in name_lower or "index" in name_lower or "etusivu" in rel_lower:
        risk = "high"
        reasons.append("Could relate to homepage rendering")

    if path.suffix in {".css", ".js"} and any(
        token in name_lower
        for token in ["theme", "template", "global", "main", "tokens", "base", "navigation"]
    ):
        if risk != "high":
            risk = "medium"
        reasons.append("Shared asset or theme-level asset")

    if ".module/" in rel_lower and any(
        token in name_lower for token in ["hero", "cta", "faq", "reference", "card", "pricing"]
    ):
        if risk == "low":
            risk = "medium"
        reasons.append("Reusable module candidate")

    return risk, reasons


def looks_like_template(path: Path) -> bool:
    return path.suffix in TEMPLATE_SUFFIXES or path.name.endswith(".html")


def looks_like_asset(path: Path) -> bool:
    return path.suffix in ASSET_SUFFIXES


def module_root_for(path: Path, base: Path) -> str | None:
    parts = path.relative_to(base).parts
    for idx, part in enumerate(parts):
        if part.endswith(MODULE_SUFFIX):
            return "/".join(parts[: idx + 1])
    return None


def extract_theme_signals(files: list[Path], base: Path) -> dict:
    rel_names = [str(p.relative_to(base)) for p in files]
    joined = " ".join(rel_names).lower()
    return {
        "has_theme_json": any(p.name == "theme.json" for p in files),
        "has_header_like_files": any("header" in p.name.lower() for p in files),
        "has_footer_like_files": any("footer" in p.name.lower() for p in files),
        "has_navigation_like_files": any(
            token in p.name.lower() for p in files for token in ["navigation", "menu"]
        ),
        "has_cinematic_signal": "cinematic" in joined,
        "has_token_signal": any(token in joined for token in ["tokens", "design-tokens", "theme-tokens"]),
        "has_legacy_style_signal": "template_styles" in joined or "styles" in joined,
    }


def audit(base: Path) -> dict:
    files = list_files(base)
    signature = load_signature()
    public_names = {item["filename"] for item in signature.get("generated_assets", [])}

    templates = []
    modules = {}
    assets = []
    risk_items = []
    matched_public_assets = []

    for path in files:
        rel = path.relative_to(base)
        risk, reasons = classify_risk(path)

        if looks_like_template(path):
            templates.append(
                {
                    "path": str(rel),
                    "risk": risk,
                    "reasons": reasons,
                }
            )

        module_root = module_root_for(path, base)
        if module_root:
            entry = modules.setdefault(
                module_root,
                {
                    "module_root": module_root,
                    "files": [],
                    "risk": "low",
                    "reasons": [],
                },
            )
            entry["files"].append(str(rel))
            if risk == "high":
                entry["risk"] = "high"
            elif risk == "medium" and entry["risk"] == "low":
                entry["risk"] = "medium"
            for reason in reasons:
                if reason not in entry["reasons"]:
                    entry["reasons"].append(reason)

        if looks_like_asset(path):
            assets.append(
                {
                    "path": str(rel),
                    "filename": path.name,
                    "risk": risk,
                    "reasons": reasons,
                }
            )

        if risk in {"high", "medium"}:
            risk_items.append(
                {
                    "path": str(rel),
                    "risk": risk,
                    "reasons": reasons,
                }
            )

        if path.name in public_names:
            matched_public_assets.append(str(rel))

    templates.sort(key=lambda x: x["path"])
    assets.sort(key=lambda x: x["path"])
    risk_items.sort(key=lambda x: (x["risk"], x["path"]))
    module_list = sorted(modules.values(), key=lambda x: x["module_root"])
    matched_public_assets = sorted(set(matched_public_assets))

    protected_candidates = [
        item for item in risk_items if item["risk"] == "high"
    ]

    return {
        "source_theme_path": str(base),
        "summary": {
            "file_count": len(files),
            "template_count": len(templates),
            "module_count": len(module_list),
            "asset_count": len(assets),
            "high_risk_count": len([x for x in risk_items if x["risk"] == "high"]),
            "medium_risk_count": len([x for x in risk_items if x["risk"] == "medium"]),
            "matched_public_asset_count": len(matched_public_assets),
        },
        "theme_signals": extract_theme_signals(files, base),
        "matched_public_assets": matched_public_assets,
        "templates": templates,
        "modules": module_list,
        "assets": assets,
        "protected_candidates": protected_candidates,
    }


def write_json(path: Path, payload: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md(path: Path, report: dict):
    lines = [
        "# Fetched source theme audit",
        "",
        f"- Source path: `{report['source_theme_path']}`",
        f"- Files: {report['summary']['file_count']}",
        f"- Templates: {report['summary']['template_count']}",
        f"- Modules: {report['summary']['module_count']}",
        f"- Assets: {report['summary']['asset_count']}",
        f"- High risk items: {report['summary']['high_risk_count']}",
        f"- Matched public assets: {report['summary']['matched_public_asset_count']}",
        "",
        "## Theme signals",
        "",
    ]

    for key, value in report["theme_signals"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Matched public asset filenames", ""])
    for item in report["matched_public_assets"]:
        lines.append(f"- `{item}`")

    lines.extend(["", "## Protected candidates (high risk)", ""])
    for item in report["protected_candidates"]:
        reasons = ", ".join(item["reasons"]) if item["reasons"] else "no explicit reasons"
        lines.append(f"- `{item['path']}` — {reasons}")

    lines.extend(["", "## Template list", ""])
    for tpl in report["templates"]:
        lines.append(f"- `{tpl['path']}` ({tpl['risk']})")

    lines.extend(["", "## Module roots", ""])
    for module in report["modules"]:
        reasons = ", ".join(module["reasons"]) if module["reasons"] else "no explicit reasons"
        lines.append(f"- `{module['module_root']}` ({module['risk']}) — {reasons}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    if len(sys.argv) not in {2, 3}:
        raise SystemExit("Usage: audit_fetched_source_theme.py <local-theme-dir> [output-json-path]")

    base = Path(sys.argv[1]).resolve()
    if not base.exists() or not base.is_dir():
        raise SystemExit(f"Local theme dir not found: {base}")

    report = audit(base)
    if len(sys.argv) == 3:
        out_json = Path(sys.argv[2]).resolve()
        out_md = out_json.with_suffix(".md")
    else:
        out_json = DEFAULT_OUT_JSON
        out_md = DEFAULT_OUT_MD

    write_json(out_json, report)
    write_md(out_md, report)
    print(f"Wrote {out_json}")
    print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()
