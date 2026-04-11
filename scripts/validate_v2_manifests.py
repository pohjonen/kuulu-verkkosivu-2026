#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path("/workspace")
PAGES_PATH = ROOT / "docs/generated/kuulu-v2-page-manifest.json"
MODULES_PATH = ROOT / "docs/generated/kuulu-v2-module-manifest.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_condition(condition: bool, message: str):
    if not condition:
        raise SystemExit(message)


def main():
    pages = load_json(PAGES_PATH)
    modules = load_json(MODULES_PATH)

    assert_condition(isinstance(pages, list) and pages, "Page manifest is empty or invalid.")
    assert_condition(isinstance(modules, list) and modules, "Module manifest is empty or invalid.")

    module_names = {m["module"] for m in modules}
    required_pages = {
        "https://www.kuulu.fi/": "homepage-v2",
        "https://www.kuulu.fi/videotuotanto": "video-service-landing-v2",
        "https://www.kuulu.fi/koulutus": "training-landing-v2",
        "https://www.kuulu.fi/digimarkkinointi": "service-landing-v2",
        "https://www.kuulu.fi/case-studies": "reference-index-v2",
        "https://www.kuulu.fi/yhteystiedot": "company-info-v2",
    }

    page_by_url = {p["source_url"]: p for p in pages}

    for url, template in required_pages.items():
        assert_condition(url in page_by_url, f"Missing required page in manifest: {url}")
        page = page_by_url[url]
        assert_condition(page["template"] == template, f"Unexpected template for {url}")
        assert_condition(page["section_stack"], f"Missing section stack for {url}")
        for module_name in page["section_stack"]:
            assert_condition(
                module_name in module_names,
                f"Section stack for {url} references unknown module {module_name}",
            )

    for module in modules:
        assert_condition(module["field_groups"], f"Module {module['module']} missing field groups")
        assert_condition(module["guardrails"], f"Module {module['module']} missing guardrails")
        assert_condition(module["depends_on"] is not None, f"Module {module['module']} missing depends_on")

    print("kuulu-v2 manifests validated successfully.")


if __name__ == "__main__":
    main()
