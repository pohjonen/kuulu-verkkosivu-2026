#!/usr/bin/env python3
"""
Generate page build packets for all inventoried non-blog pages.

This expands the first-wave packet idea to the whole audited public site so that
every page has a machine-readable build brief available before HubSpot auth/export.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"

INVENTORY = GENERATED / "kuulu-public-site-inventory.json"
LINK_GRAPH = GENERATED / "kuulu-full-link-graph.json"
SOURCE_EXTRACTS = GENERATED / "kuulu-first-wave-source-extracts.json"
FIRST_WAVE_PACKETS = GENERATED / "first-wave-page-build-packets" / "index.json"
OUT_DIR = GENERATED / "all-page-build-packets"


DEFAULT_MODULE_STACKS = {
    "homepage": [
        "hero-cinematic-v2",
        "problem-grid-v2",
        "audience-split-v2",
        "service-pillars-v2",
        "process-steps-v2",
        "stats-trust-band-v2",
        "reference-grid-v2",
        "final-cta-v2",
    ],
    "service": [
        "hero-cinematic-v2",
        "problem-grid-v2",
        "audience-split-v2",
        "service-pillars-v2",
        "process-steps-v2",
        "reference-grid-v2",
        "faq-v2",
        "final-cta-v2",
    ],
    "video-service": [
        "hero-cinematic-v2",
        "problem-grid-v2",
        "video-model-comparison-v2",
        "service-pillars-v2",
        "process-steps-v2",
        "stats-trust-band-v2",
        "reference-grid-v2",
        "faq-v2",
        "final-cta-v2",
    ],
    "training": [
        "hero-cinematic-v2",
        "problem-grid-v2",
        "service-pillars-v2",
        "process-steps-v2",
        "training-agenda-v2",
        "stats-trust-band-v2",
        "faq-v2",
        "final-cta-v2",
    ],
    "reference-index": [
        "hero-cinematic-v2",
        "reference-grid-v2",
        "final-cta-v2",
    ],
    "reference-detail": [
        "hero-cinematic-v2",
        "stats-trust-band-v2",
        "reference-detail-sections-v2",
        "final-cta-v2",
    ],
    "company-info": [
        "hero-cinematic-v2",
        "lead-capture-form-cta-v2",
        "team-grid-v2",
        "contact-info-v2",
        "final-cta-v2",
    ],
    "person-profile": [
        "hero-cinematic-v2",
        "service-pillars-v2",
        "reference-grid-v2",
        "final-cta-v2",
    ],
    "legal": [
        "hero-cinematic-v2",
        "reference-detail-sections-v2",
        "final-cta-v2",
    ],
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slug_to_page_id(slug: str, page_type: str) -> str:
    cleaned = slug.strip("/").replace("/", "__").replace("-", "_")
    if not cleaned:
        return "homepage_v2"
    return f"{cleaned}__{page_type}".replace(".", "_")


def infer_primary_goal(page_type: str, title: str) -> str:
    return {
        "homepage": "Explain the full Zero Click growth engine and strategic model.",
        "service": f"Clarify how this service solves a specific growth bottleneck: {title}.",
        "video-service": f"Show how video production supports brand, trust and demand capture: {title}.",
        "training": f"Position this training page as a practical answer to competence gaps: {title}.",
        "reference-index": f"Make references easy to browse and compare: {title}.",
        "reference-detail": f"Prove the case logic through challenge, solution and results: {title}.",
        "company-info": f"Reduce friction and increase trust on the contact/company page: {title}.",
        "person-profile": f"Turn the expert profile into a trust and authority asset: {title}.",
        "legal": f"Preserve legal clarity while normalizing the layout: {title}.",
    }.get(page_type, f"Normalize and preserve the value of page: {title}.")


def infer_core_message(row: dict) -> str:
    title = row.get("title") or ""
    h1 = row.get("h1") or ""
    notes = row.get("notes") or ""
    return " ".join(part for part in [h1, title, notes] if part).strip()


def infer_hero_direction(row: dict) -> dict:
    page_type = row["page_type"]
    h1 = row.get("h1") or row.get("title") or ""
    supporting = {
        "homepage": "Vanha klikkiajattelu ei enää riitä. Brändi, sisältö ja kysynnän kotiutus pitää rakentaa samaan koneistoon.",
        "service": "Sivu näyttää miten palvelu ratkaisee kitkan eikä jää irralliseksi toimenpiteeksi.",
        "video-service": "Video ei ole irrallinen tuotanto, vaan kasvukoneiston polttoainetta.",
        "training": "Osaamisvaje, tekoäly ja muuttuvat alustat pakottavat päivittämään tekemisen.",
        "reference-index": "Referenssien pitää todistaa, ei vain näyttää hyvältä.",
        "reference-detail": "Case näyttää haasteen, ratkaisun ja mitattavan tuloksen.",
        "company-info": "Yhteydenoton pitää tuntua helpolta, inhimilliseltä ja korkealaatuiselta.",
        "person-profile": "Asiantuntija toimii luottamuksen ja osaamisen kantajana.",
        "legal": "Juridinen sisältö säilyy selkeänä ja helposti ylläpidettävänä.",
    }.get(page_type, "Sivun pitää tukea yhtenäistä v2-kokonaisuutta.")
    cta_goal = {
        "homepage": "strategiakartoitus tai sparraus",
        "service": "sparraus tai tarjous",
        "video-service": "sparraus tai tarjous",
        "training": "tarjouspyyntö tai ilmoittautuminen",
        "reference-index": "sparraus tai referensseihin tutustuminen",
        "reference-detail": "seuraava askel caseen liittyvästä kiinnostuksesta sparraukseen",
        "company-info": "yhteydenotto tai sparraus",
        "person-profile": "yhteydenotto tai profiilin osaamiseen liittyvä CTA",
        "legal": "ei pää-CTA:ta, pidä rauhallinen rakenne",
    }.get(page_type, "selkeä seuraava askel")
    return {
        "headline": h1,
        "supporting_angle": supporting,
        "cta_goal": cta_goal,
    }


def infer_mandatory_signals(row: dict) -> list[str]:
    page_type = row["page_type"]
    defaults = {
        "homepage": [
            "95/5-ajattelu näkyy",
            "Brand DNA näkyy",
            "Sisältökoneisto + Liidimoottori näkyvät",
            "Zero Click -murros näkyy",
        ],
        "service": [
            "Palvelu kytkeytyy selvästi pullonkaulaan",
            "Sisältö ei jää irralliseksi listaukseksi",
            "Seuraava askel on selkeä",
        ],
        "video-service": [
            "Captured / hybrid / AI näkyvät selkeästi",
            "Aitous ja skaala näkyvät yhtä aikaa",
            "Video kytkeytyy liiketoimintatuloksiin",
        ],
        "training": [
            "Osaamisvaje näkyy ennen agendaa",
            "Käytännön hyöty näkyy",
            "AI / Zero Click -murros näkyy",
        ],
        "reference-index": [
            "Caseja voi selata nopeasti",
            "Haaste / ratkaisu / tulos on löydettävissä",
        ],
        "reference-detail": [
            "Haaste näkyy",
            "Ratkaisu näkyy",
            "Tulokset näkyvät",
        ],
        "company-info": [
            "Luottamus syntyy nopeasti",
            "Yhteydenotto on helppo",
            "Ihmiset ja toimistot näkyvät",
        ],
        "person-profile": [
            "Asiantuntijuus näkyy",
            "Blogiriippuvuutta ei ole",
            "Seuraava askel on selkeä",
        ],
        "legal": [
            "Sisältö säilyy juridisesti selkeänä",
            "Rakenne on kevyt ja turvallinen",
        ],
    }
    return defaults.get(page_type, ["Sivu pysyy strategisesti yhtenäisenä."])


def source_priority_list(row: dict) -> list[str]:
    raw = row.get("source_priority", "")
    parts = [part.strip() for part in raw.split("+") if part.strip()]
    return parts or ["live"]


def build_module_plan(row: dict, modules: list[str]) -> list[dict]:
    priorities = source_priority_list(row)
    plan = []
    for idx, module in enumerate(modules, start=1):
        plan.append(
            {
                "order": idx,
                "module": module,
                "module_instance_key": f"{slug_to_page_id(row['preview_slug'], row['page_type'])}__{module}__{idx}",
                "content_job": f"Apply {module} to page type {row['page_type']} using the page's strategic role and source extracts.",
                "source_priority": priorities,
                "editor_notes": [
                    "Täytä sisältö moduulikohtaisten guardrailien mukaan.",
                    "Säilytä nykyisen sivun kriittiset CTA-polut.",
                    "Älä riko Zero Click / Brand DNA / Sisältökoneisto / Liidimoottori -linjaa sivun roolista riippuen.",
                ],
            }
        )
    return plan


def link_map_by_url(graph_payload: dict) -> dict[str, dict]:
    graph = graph_payload["graph"]
    items = []
    for url, payload in graph.items():
        items.append(
            {
                "url": url,
                "link_count": payload.get("outgoing_count", 0),
                "internal_links": [
                    {
                        "target_url": edge["target_url"],
                        "target_type": edge.get("target_type"),
                        "labels": edge.get("labels", []),
                        "strength": edge.get("strength"),
                    }
                    for edge in payload.get("outgoing", [])
                ],
            }
        )
    return {node["url"]: node for node in items}


def source_extract_by_url(extracts: list[dict]) -> dict[str, dict]:
    return {item["url"]: item for item in extracts}


def page_packet(row: dict, link_map: dict, source_extracts: dict) -> dict:
    modules = DEFAULT_MODULE_STACKS.get(row["page_type"], ["hero-cinematic-v2", "final-cta-v2"])
    page_id = slug_to_page_id(row["preview_slug"], row["page_type"])
    extract = source_extracts.get(row["url"], {})
    link_data = link_map.get(row["url"], {"link_count": 0, "internal_links": []})

    return {
        "page_id": page_id,
        "template": row["v2_template"],
        "preview_slug": row["preview_slug"],
        "url": row["url"],
        "page_type": row["page_type"],
        "current_theme": row.get("current_theme"),
        "primary_goal": infer_primary_goal(row["page_type"], row.get("title", "")),
        "core_message": infer_core_message(row),
        "hero_direction": infer_hero_direction(row),
        "mandatory_signals": infer_mandatory_signals(row),
        "page_settings": {
            "title_strategy": "derive from approved copy",
            "meta_description_strategy": "write after content finalization",
            "noindex_preview": True,
            "canonical_strategy": "self canonical on preview, production canonical on cutover",
        },
        "module_plan": build_module_plan(row, modules),
        "source_extract": {
            "title": extract.get("title"),
            "headings": extract.get("headings", []),
            "paragraphs": extract.get("paragraphs", []),
            "cta_candidates": extract.get("cta_candidates", []),
        },
        "link_map": {
            "link_count": link_data.get("link_count", 0),
            "internal_links": link_data.get("internal_links", []),
        },
    }


def main():
    inventory = load_json(INVENTORY)
    link_graph = load_json(LINK_GRAPH)
    source_extracts = load_json(SOURCE_EXTRACTS)

    OUT_DIR = GENERATED / "all-page-build-packets"
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    link_index = link_map_by_url(link_graph)
    extract_index = source_extract_by_url(source_extracts)

    packets_summary = []

    for row in inventory:
        packet = page_packet(row, link_index, extract_index)
        path = OUT_DIR / f"{packet['page_id']}.json"
        write_json(path, packet)
        packets_summary.append(
            {
                "page_id": packet["page_id"],
                "path": str(path.relative_to(ROOT)),
                "module_count": len(packet["module_plan"]),
                "link_count": packet["link_map"]["link_count"],
            }
        )

    write_json(OUT_DIR / "index.json", {"packets": packets_summary})
    print(f"Wrote {OUT_DIR}")


if __name__ == "__main__":
    main()
