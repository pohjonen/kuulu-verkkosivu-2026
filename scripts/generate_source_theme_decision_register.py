#!/usr/bin/env python3
"""
Derive a practical reuse/fork/replace/protect register from the fetched source theme audit.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
AUDIT_JSON = ROOT / "docs" / "generated" / "fetched-source-theme-audit.json"
OUT_JSON = ROOT / "docs" / "generated" / "source-theme-decision-register.json"
OUT_MD = ROOT / "docs" / "generated" / "source-theme-decision-register.md"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def decision_for_template(path: str, risk: str) -> tuple[str, str]:
    lower = path.lower()
    if "homepage" in lower or lower.endswith("templates/home.html") or lower.endswith("templates/index.html"):
        return "protect", "Homepage-related template, do not edit directly."
    if "partials/header" in lower or "partials/footer" in lower:
        return "protect", "Shared partial candidate, keep isolated until v2 fork."
    if "video-production.html" in lower or "person-profile.html" in lower:
        return "fork", "Likely useful base template for v2 mapping."
    if "-test-" in lower or "backup" in lower or "dev-" in lower:
        return "replace", "Test/dev/backup template; keep only as reference if needed."
    if risk == "high":
        return "protect", "High-risk template from audit."
    return "review", "Needs manual review during template mapping."


def decision_for_module(module_root: str, risk: str) -> tuple[str, str]:
    lower = module_root.lower()
    if "global_header" in lower or "global_footer" in lower:
        return "protect", "Global live structure; isolate before changes."
    if any(token in lower for token in ["cinematic_hero", "cinematic_problem_list", "cinematic_two_engines", "cinematic_metrics", "cinematic_koulutus_form", "person-profile", "video-showcase", "services-grid", "case-study-showcase"]):
        return "fork", "Promising source module for v2 adaptation."
    if any(token in lower for token in ["cinematic_footer", "cinematic_header", "sticky_nav"]):
        return "protect", "Navigation/global presentation risk."
    if risk == "low":
        return "review", "May be reusable, but needs manual check."
    return "replace", "Safer to rebuild than rely on unclear module."


def build_register(audit: dict) -> dict:
    templates = []
    for item in audit.get("templates", []):
        decision, reason = decision_for_template(item["path"], item["risk"])
        templates.append(
            {
                "path": item["path"],
                "risk": item["risk"],
                "decision": decision,
                "reason": reason,
            }
        )

    modules = []
    for item in audit.get("modules", []):
        decision, reason = decision_for_module(item["module_root"], item["risk"])
        modules.append(
            {
                "module_root": item["module_root"],
                "risk": item["risk"],
                "decision": decision,
                "reason": reason,
            }
        )

    summary = {
        "template_counts": {
            key: len([x for x in templates if x["decision"] == key])
            for key in ["protect", "fork", "review", "replace"]
        },
        "module_counts": {
            key: len([x for x in modules if x["decision"] == key])
            for key in ["protect", "fork", "review", "replace"]
        },
    }

    return {
        "source_theme_path": audit["source_theme_path"],
        "summary": summary,
        "templates": templates,
        "modules": modules,
    }


def write_json(path: Path, payload: dict):
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md(path: Path, register: dict):
    lines = [
        "# Source theme decision register",
        "",
        f"- Source path: `{register['source_theme_path']}`",
        "",
        "## Template decisions",
        "",
    ]
    for item in register["templates"]:
        lines.append(f"- `{item['path']}` → **{item['decision']}** ({item['risk']}) — {item['reason']}")

    lines.extend(["", "## Module decisions", ""])
    for item in register["modules"]:
        lines.append(f"- `{item['module_root']}` → **{item['decision']}** ({item['risk']}) — {item['reason']}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    audit = load_json(AUDIT_JSON)
    register = build_register(audit)
    write_json(OUT_JSON, register)
    write_md(OUT_MD, register)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
