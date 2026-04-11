#!/usr/bin/env python3
"""
Generate a public asset signature for kuulu.fi pages.

Purpose:
- capture the currently visible HubSpot-generated asset fingerprint
- help compare a fetched/exported source theme against the public site later
- provide a lightweight baseline even before HubSpot auth/export exists
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests


ROOT = Path("/workspace")
OUT_JSON = ROOT / "docs" / "generated" / "kuulu-public-asset-signature.json"
OUT_MD = ROOT / "docs" / "generated" / "kuulu-public-asset-signature.md"

TARGETS = [
    ("homepage", "https://www.kuulu.fi/"),
    ("video-service", "https://www.kuulu.fi/videotuotanto"),
    ("training", "https://www.kuulu.fi/koulutus"),
    ("service", "https://www.kuulu.fi/digimarkkinointi"),
    ("reference-index", "https://www.kuulu.fi/case-studies"),
]

ASSET_RE = re.compile(
    r"https://www\.kuulu\.fi/hubfs/hub_generated/(?:template_assets|module_assets)/[^\"']+",
    re.IGNORECASE,
)
PORTAL_RE = re.compile(r"portalId=(\d+)")


def fetch(url: str) -> str:
    return requests.get(url, timeout=20).text


def classify_theme(assets: list[str]) -> str:
    joined = " ".join(assets)
    if "template_cinematic.min.css" in joined:
        return "cinematic-uusi"
    if "template_styles.min.css" in joined:
        return "legacy-vaalea"
    return "muu/sekalainen"


def asset_name(url: str) -> str:
    return Path(urlparse(url).path).name


def build_signature():
    pages = []
    portal_ids = set()
    all_asset_urls = []
    asset_names = set()

    for label, url in TARGETS:
        html = fetch(url)
        assets = ASSET_RE.findall(html)
        all_asset_urls.extend(assets)
        asset_names.update(asset_name(a) for a in assets)

        portal_match = PORTAL_RE.search(html)
        if portal_match:
            portal_ids.add(portal_match.group(1))

        pages.append(
            {
                "label": label,
                "url": url,
                "theme_guess": classify_theme(assets),
                "asset_urls": assets,
                "asset_names": [asset_name(a) for a in assets],
            }
        )

    unique_assets = sorted(set(all_asset_urls))
    unique_names = sorted(asset_names)
    generated_assets = [
        {"url": asset_url, "filename": asset_name(asset_url)}
        for asset_url in unique_assets
    ]

    return {
        "portal_ids": sorted(portal_ids),
        "portal_id": sorted(portal_ids)[0] if portal_ids else None,
        "pages": pages,
        "generated_assets": generated_assets,
        "summary": {
            "page_count": len(pages),
            "unique_asset_count": len(unique_assets),
            "unique_asset_names": unique_names,
        },
        "match_strategy": {
            "primary": "Compare fetched source theme assets/templates/modules against unique asset names and page-specific theme_guess values.",
            "secondary": "Use page-level asset sets to identify likely templates or shared asset bundles after source theme export.",
        },
    }


def write_md(signature: dict):
    lines = [
        "# Kuulu.fi julkinen asset-signature",
        "",
        "Tämä tiedosto toimii julkisen sivuston asset-fingerprintinä ennen HubSpot-exportia tai authia.",
        "",
        f"- Portal ID:t: {', '.join(signature['portal_ids']) if signature['portal_ids'] else 'ei löydetty'}",
        f"- Tarkistettuja sivuja: {signature['summary']['page_count']}",
        f"- Uniikkeja assetteja: {signature['summary']['unique_asset_count']}",
        "",
        "## Uniikit asset-nimet",
        "",
    ]

    for name in signature["summary"]["unique_asset_names"]:
        lines.append(f"- `{name}`")

    lines.extend(["", "## Sivukohtainen erittely", ""])

    for page in signature["pages"]:
        lines.append(f"### {page['label']}")
        lines.append(f"- URL: `{page['url']}`")
        lines.append(f"- Theme guess: `{page['theme_guess']}`")
        lines.append("- Assetit:")
        for asset in page["asset_names"]:
            lines.append(f"  - `{asset}`")
        lines.append("")

    lines.extend(
        [
            "## Match-strategia",
            "",
            f"- Ensisijainen: {signature['match_strategy']['primary']}",
            f"- Toissijainen: {signature['match_strategy']['secondary']}",
            "",
        ]
    )

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    signature = build_signature()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(signature, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(signature)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
