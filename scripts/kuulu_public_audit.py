#!/usr/bin/env python3
"""
Audit current public kuulu.fi non-blog pages and generate inventory files.

Outputs:
- docs/generated/kuulu-public-site-inventory.csv
- docs/generated/kuulu-public-site-inventory.json
"""

from __future__ import annotations

import csv
import json
import re
from html import unescape
from pathlib import Path
from typing import Dict, List

import requests


PAGES: List[Dict[str, str]] = [
    {
        "url": "https://www.kuulu.fi/",
        "page_type": "homepage",
        "v2_template": "homepage-v2",
        "notion_source": "Etusivu / Kuulu etusivu draft",
        "source_priority": "live + notion + pdf",
        "preview_slug": "/v2-etusivu",
        "notes": "Master page for Zero Click growth engine.",
    },
    {
        "url": "https://www.kuulu.fi/koulutus",
        "page_type": "training",
        "v2_template": "training-landing-v2",
        "notion_source": "Koulutus",
        "source_priority": "live + notion + pdf",
        "preview_slug": "/v2-koulutus",
        "notes": "Should foreground competence gap and practical outcomes.",
    },
    {
        "url": "https://www.kuulu.fi/tekoalyn-mestarikurssi",
        "page_type": "training",
        "v2_template": "training-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-tekoalyn-mestarikurssi",
        "notes": "AI flagship training page.",
    },
    {
        "url": "https://www.kuulu.fi/tekoalyn-perjantaipulssi",
        "page_type": "training",
        "v2_template": "training-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-tekoalyn-perjantaipulssi",
        "notes": "Recurring training / pulse concept.",
    },
    {
        "url": "https://www.kuulu.fi/zero-click-ajan-digimarkkinointi",
        "page_type": "training",
        "v2_template": "training-landing-v2",
        "notion_source": "",
        "source_priority": "live + pdf",
        "preview_slug": "/v2-zero-click-ajan-digimarkkinointi",
        "notes": "Deep anchor page for Zero Click framework.",
    },
    {
        "url": "https://www.kuulu.fi/digimarkkinointi",
        "page_type": "service",
        "v2_template": "service-landing-v2",
        "notion_source": "Digimarkkinointi (placeholder)",
        "source_priority": "live + pdf",
        "preview_slug": "/v2-digimarkkinointi",
        "notes": "Should map to pullonkaulat and system logic.",
    },
    {
        "url": "https://www.kuulu.fi/energia-alan-markkinointi",
        "page_type": "service",
        "v2_template": "service-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-energia-alan-markkinointi",
        "notes": "Verticalized service page.",
    },
    {
        "url": "https://www.kuulu.fi/someagentti-eli-somekanavien-auditointi",
        "page_type": "service",
        "v2_template": "service-landing-v2",
        "notion_source": "",
        "source_priority": "live + pdf",
        "preview_slug": "/v2-someauditointi",
        "notes": "Audit / startti-type service.",
    },
    {
        "url": "https://www.kuulu.fi/google-ads-mainonta",
        "page_type": "service",
        "v2_template": "service-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-google-ads-mainonta",
        "notes": "Demand capture / 5 percent audience page.",
    },
    {
        "url": "https://www.kuulu.fi/videotuotanto",
        "page_type": "video-service",
        "v2_template": "video-service-landing-v2",
        "notion_source": "Kuulu Videotuotanto — Sivuteksti v1",
        "source_priority": "live + notion + pdf",
        "preview_slug": "/v2-videotuotanto",
        "notes": "Must show captured / hybrid / AI production models.",
    },
    {
        "url": "https://www.kuulu.fi/brandivideo",
        "page_type": "video-service",
        "v2_template": "video-service-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-brandivideo",
        "notes": "Premium captured storytelling angle.",
    },
    {
        "url": "https://www.kuulu.fi/tv-mainos-tuotanto",
        "page_type": "video-service",
        "v2_template": "video-service-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-tv-mainos-tuotanto",
        "notes": "Already closer to cinematic style.",
    },
    {
        "url": "https://www.kuulu.fi/videotuotanto_vanha",
        "page_type": "video-service",
        "v2_template": "video-service-landing-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-videotuotanto-vanha",
        "notes": "Decide later: preserve as legacy page or redirect.",
    },
    {
        "url": "https://www.kuulu.fi/case-studies",
        "page_type": "reference-index",
        "v2_template": "reference-index-v2",
        "notion_source": "Asiakas caset (placeholder)",
        "source_priority": "live + brand",
        "preview_slug": "/v2-case-studies",
        "notes": "Primary case index for structured filtering.",
    },
    {
        "url": "https://www.kuulu.fi/asiakasreferenssit",
        "page_type": "reference-index",
        "v2_template": "reference-index-v2",
        "notion_source": "Kokemuksia Kuulusta (placeholder)",
        "source_priority": "live",
        "preview_slug": "/v2-asiakasreferenssit",
        "notes": "May remain separate editorial index or be consolidated later.",
    },
    {
        "url": "https://www.kuulu.fi/yhteystiedot",
        "page_type": "company-info",
        "v2_template": "company-info-v2",
        "notion_source": "Ota yhteyttä (placeholder)",
        "source_priority": "live + brand",
        "preview_slug": "/v2-yhteystiedot",
        "notes": "High-trust conversion page with people, offices and forms.",
    },
    {
        "url": "https://www.kuulu.fi/tietosuojaseloste",
        "page_type": "legal",
        "v2_template": "legal-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-tietosuojaseloste",
        "notes": "Simple legal page, no overdesign.",
    },
    {
        "url": "https://www.kuulu.fi/tekoaly-markkinoinnin-ja-myynnin-tukena",
        "page_type": "training",
        "v2_template": "training-landing-v2",
        "notion_source": "",
        "source_priority": "live + pdf",
        "preview_slug": "/v2-tekoaly-markkinoinnin-ja-myynnin-tukena",
        "notes": "AI skills page tied directly to current market shift.",
    },
    {
        "url": "https://www.kuulu.fi/ihmiset/jonna-muurinen",
        "page_type": "person-profile",
        "v2_template": "person-profile-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-ihmiset-jonna-muurinen",
        "notes": "Remove blog feed dependency, keep authority and CTA.",
    },
    {
        "url": "https://www.kuulu.fi/ihmiset/ville-pohjonen",
        "page_type": "person-profile",
        "v2_template": "person-profile-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-ihmiset-ville-pohjonen",
        "notes": "Remove blog feed dependency, connect to video expertise.",
    },
    {
        "url": "https://www.kuulu.fi/projektinhallinta-tekoalylla-perjantaipulssi-17.4.2026-kuulu",
        "page_type": "training",
        "v2_template": "training-landing-v2",
        "notion_source": "",
        "source_priority": "live + brand",
        "preview_slug": "/v2-projektinhallinta-tekoalylla-perjantaipulssi",
        "notes": "Campaign-style training page already near new direction.",
    },
    {
        "url": "https://www.kuulu.fi/case-studies/solar-kaihdin-kymmenkertaisti-verkkokauppamyynnin-kuulun-avulla",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-solar-kaihdin",
        "notes": "Reference should highlight kitka -> ratkaisu -> tulos.",
    },
    {
        "url": "https://www.kuulu.fi/case-studies/kuulu-auttoi-elisaa-tavoittamaan-70000-nuorta-superdigikoululla",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-elisa-superdigikoulu",
        "notes": "Strong social proof for education and impact.",
    },
    {
        "url": "https://www.kuulu.fi/case-studies/kuulu-energiequelle-tehokas-visuaalinen-viestinta",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-energiequelle",
        "notes": "Useful bridge between brand and visual production.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/vestera-oy-markkinoinnin-kumppanuus",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-vestera",
        "notes": "Long-term partnership reference.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/haaga-helia-tekoalykuvapankki",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-haaga-helia",
        "notes": "Important AI visual production proof point.",
    },
    {
        "url": "https://www.kuulu.fi/ruokamies-sisaltopankki-ja-brandin-kirkastus-kiireiselle-kauppiaalle",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-ruokamies",
        "notes": "Good content engine case.",
    },
    {
        "url": "https://www.kuulu.fi/seta-vaikuttava-videoprojekti-nakyvyytta-sateenkaarijarjestoille",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-seta",
        "notes": "Values-driven video impact case.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/akateeminen-kirjakauppa-brandin-tarinan-selkeytys",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-akateeminen-kirjakauppa",
        "notes": "Strong Brand DNA / story case.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/sievinjalkine-cobrawoman-videotuotanto",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-sievi-cobra",
        "notes": "Video-led brand case.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/ruustinna-brandays-tarina-visuaalinen-ilme-ja-lanseerauskampanja",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-ruustinna",
        "notes": "Branding and launch case.",
    },
    {
        "url": "https://www.kuulu.fi/intersport-tripla-uskalla-olla-oma-itsesi",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-intersport-tripla",
        "notes": "Campaign concept case.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/sievin-jalkine-digimarkkinointi",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-sievin-jalkine",
        "notes": "Content + performance partnership case.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/nestor-cables-brandays-ja-yritysvideot",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-nestor-cables",
        "notes": "Brand and video combination case.",
    },
    {
        "url": "https://www.kuulu.fi/referenssit/lahitapiola",
        "page_type": "reference-detail",
        "v2_template": "reference-detail-v2",
        "notion_source": "",
        "source_priority": "live",
        "preview_slug": "/v2-case-lahitapiola",
        "notes": "Legacy reference to normalize into new case structure.",
    },
]


THEME_PATTERNS = {
    "cinematic-uusi": "template_cinematic.min.css",
    "legacy-vaalea": "template_styles.min.css",
}


def clean_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(unescape(value).split())


def parse_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return clean_html(match.group(1)) if match else ""


def parse_h1(html: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    return clean_html(match.group(1)) if match else ""


def parse_canonical(html: str) -> str:
    match = re.search(
        r"<link[^>]+rel=[\"']canonical[\"'][^>]+href=[\"']([^\"']+)",
        html,
        re.I,
    )
    return match.group(1) if match else ""


def infer_theme(html: str) -> str:
    for label, marker in THEME_PATTERNS.items():
        if marker in html:
            return label
    return "muu/sekalainen"


def fetch_page(session: requests.Session, item: Dict[str, str]) -> Dict[str, str]:
    response = session.get(item["url"], timeout=20)
    response.raise_for_status()
    html = response.text
    row = dict(item)
    row["status_code"] = str(response.status_code)
    row["title"] = parse_title(html)
    row["h1"] = parse_h1(html)
    row["canonical"] = parse_canonical(html)
    row["current_theme"] = infer_theme(html)
    row["uses_hs_form"] = "yes" if "hs-form-frame" in html else "no"
    row["uses_video_embed"] = "yes" if ("vimeo.com" in html or "youtube.com" in html) else "no"
    return row


def write_outputs(rows: List[Dict[str, str]]) -> None:
    output_dir = Path("/workspace/docs/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "kuulu-public-site-inventory.csv"
    json_path = output_dir / "kuulu-public-site-inventory.json"

    fieldnames = [
        "url",
        "status_code",
        "title",
        "h1",
        "canonical",
        "page_type",
        "current_theme",
        "v2_template",
        "notion_source",
        "source_priority",
        "preview_slug",
        "uses_hs_form",
        "uses_video_embed",
        "notes",
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=2)

    print(f"Wrote {csv_path}")
    print(f"Wrote {json_path}")


def main() -> None:
    session = requests.Session()
    session.headers.update({"User-Agent": "kuulu-public-audit/1.0"})
    rows = [fetch_page(session, item) for item in PAGES]
    write_outputs(rows)


if __name__ == "__main__":
    main()
