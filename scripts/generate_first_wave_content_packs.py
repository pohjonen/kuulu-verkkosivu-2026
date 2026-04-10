#!/usr/bin/env python3
"""
Generate first-wave content packs for Kuulu v2 implementation.

These content packs are intentionally implementation-oriented:
- they bind section stacks to content goals
- they summarize the key messaging per page
- they map likely source inputs (live / notion / pdf)
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"
OUT = GENERATED / "kuulu-first-wave-content-packs.json"


CONTENT_PACKS = [
    {
        "page_id": "homepage-v2",
        "url": "https://www.kuulu.fi/",
        "preview_slug": "/v2-etusivu",
        "template": "homepage-v2",
        "primary_goal": "Explain the full Zero Click growth engine and create strategic demand.",
        "core_message": "Kukaan ei klikkaa. Ja kauppa käy. Brand DNA, Sisältökoneisto ja Liidimoottori rakennetaan yhdeksi kasvukoneistoksi.",
        "hero_direction": {
            "headline": "Kukaan ei klikkaa. Ja kauppa käy.",
            "supporting_angle": "Vanha klikkiajattelu ei enää riitä. Brändi, sisältö ja kysynnän kotiutus pitää rakentaa samaan koneistoon.",
            "cta_goal": "strategiakartoitus tai sparraus",
        },
        "section_stack": [
            {
                "module": "hero-cinematic-v2",
                "content_job": "Avaa paradigman muutos ja pysäyttää vahvalla väitteellä.",
                "source_priority": ["live", "notion:Etusivu", "pdf:Zero Click"],
            },
            {
                "module": "problem-grid-v2",
                "content_job": "Tunnistatko nämä -kitkat: hajanaisuus, mittaamisen puute, AI-paine, yhteisen kielen puute.",
                "source_priority": ["live", "notion:Etusivu", "pdf:Zero Click"],
            },
            {
                "module": "audience-split-v2",
                "content_job": "Selittää 95 % / 5 % -ajattelun.",
                "source_priority": ["pdf:Zero Click"],
            },
            {
                "module": "service-pillars-v2",
                "content_job": "Esittelee Brand DNA:n, Sisältökoneiston ja Liidimoottorin.",
                "source_priority": ["live", "pdf:Zero Click", "notion:Etusivu"],
            },
            {
                "module": "process-steps-v2",
                "content_job": "Näyttää miten lähdetään liikkeelle auditoinnista koneistoon.",
                "source_priority": ["live", "notion:Etusivu", "pdf:Zero Click"],
            },
            {
                "module": "stats-trust-band-v2",
                "content_job": "Todisteet, numerot, uskottavuus.",
                "source_priority": ["live", "brand"],
            },
            {
                "module": "reference-grid-v2",
                "content_job": "Nostaa tärkeimmät case-esimerkit nopeasti näkyviin.",
                "source_priority": ["live", "inventory"],
            },
            {
                "module": "final-cta-v2",
                "content_job": "Ohjaa strategiakartoitukseen / sparraukseen.",
                "source_priority": ["live", "pdf:Zero Click"],
            },
        ],
        "mandatory_signals": [
            "95/5-ajattelu näkyy",
            "Brand DNA näkyy",
            "Sisältökoneisto + Liidimoottori näkyvät",
            "Zero Click -murros näkyy",
        ],
    },
    {
        "page_id": "video-service-v2",
        "url": "https://www.kuulu.fi/videotuotanto",
        "preview_slug": "/v2-videotuotanto",
        "template": "video-service-landing-v2",
        "primary_goal": "Show how captured, hybrid and AI-enhanced production create measurable outcomes.",
        "core_message": "Muut myyvät videoita. Me myymme tuloksia. Sama tuotanto ruokkii sekä Sisältökoneistoa että Liidimoottoria.",
        "hero_direction": {
            "headline": "Muut myyvät videoita. Me myymme tuloksia.",
            "supporting_angle": "Video ei ole irrallinen tuotanto. Oikein rakennettuna se on kasvukoneiston polttoainetta.",
            "cta_goal": "sparraus tai tarjous",
        },
        "section_stack": [
            {
                "module": "hero-cinematic-v2",
                "content_job": "Avaa videon rooli tuloskoneistona.",
                "source_priority": ["live", "notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
            {
                "module": "problem-grid-v2",
                "content_job": "Purkaa tavallisen videotuotannon ongelmat: nähtyvyys, versiointi, budjetti, epäselvät paketit.",
                "source_priority": ["notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
            {
                "module": "video-model-comparison-v2",
                "content_job": "Näyttää captured / hybrid / AI-enhanced -mallit.",
                "source_priority": ["notion:Kuulu Videotuotanto — Sivuteksti v1", "pdf:Zero Click"],
            },
            {
                "module": "service-pillars-v2",
                "content_job": "Kytkee videon aitouteen, skaalaan ja versiointiin.",
                "source_priority": ["pdf:Zero Click", "notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
            {
                "module": "process-steps-v2",
                "content_job": "Tavoite → konsepti → tuotanto → versiointi.",
                "source_priority": ["live", "notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
            {
                "module": "stats-trust-band-v2",
                "content_job": "Tuotannot, katselut, asiakkaat, uskottavuus.",
                "source_priority": ["live", "notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
            {
                "module": "reference-grid-v2",
                "content_job": "Näyttää videon, brändin ja AI-tuotannon referenssit.",
                "source_priority": ["inventory"],
            },
            {
                "module": "faq-v2",
                "content_job": "Purkaa aikataulu-, omistajuus-, jakelu- ja AI-kysymykset.",
                "source_priority": ["notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
            {
                "module": "final-cta-v2",
                "content_job": "Ohjaa sparraukseen / tarjoukseen.",
                "source_priority": ["notion:Kuulu Videotuotanto — Sivuteksti v1"],
            },
        ],
        "mandatory_signals": [
            "Captured / hybrid / AI näkyvät selkeästi",
            "Aitous ja ihmisläheisyys näkyvät",
            "Versiointi ja skaala näkyvät",
            "Video kytkeytyy kasvuun eikä vain tuotantoon",
        ],
    },
    {
        "page_id": "training-v2",
        "url": "https://www.kuulu.fi/koulutus",
        "preview_slug": "/v2-koulutus",
        "template": "training-landing-v2",
        "primary_goal": "Position training as the practical answer to competence gaps in the Zero Click / AI shift.",
        "core_message": "Tiimisi osaa. Mutta osaako se tarpeeksi? Koulutus ei ole lisä, vaan kilpailuetu.",
        "hero_direction": {
            "headline": "Tiimisi osaa. Mutta osaako se tarpeeksi?",
            "supporting_angle": "Tekoäly, data ja algoritmit muuttavat tekemistä viikottain. Koulutuksen pitää näkyä käytännön tekemisessä.",
            "cta_goal": "tarjouspyyntö koulutuksesta",
        },
        "section_stack": [
            {
                "module": "hero-cinematic-v2",
                "content_job": "Avaa osaamisvaje ja kilpailuetu.",
                "source_priority": ["notion:Koulutus", "live", "pdf:Zero Click"],
            },
            {
                "module": "problem-grid-v2",
                "content_job": "Purkaa miksi nykyinen osaaminen ja geneeriset koulutukset eivät riitä.",
                "source_priority": ["notion:Koulutus"],
            },
            {
                "module": "service-pillars-v2",
                "content_job": "Esittää avoimet koulutukset, räätälöidyt koulutukset ja sparrauksen.",
                "source_priority": ["notion:Koulutus"],
            },
            {
                "module": "process-steps-v2",
                "content_job": "Kartoitus → räätälöinti → koulutus.",
                "source_priority": ["notion:Koulutus"],
            },
            {
                "module": "training-agenda-v2",
                "content_job": "Ryhmittelee aiheet ja trackit käytännönläheisesti.",
                "source_priority": ["notion:Koulutus", "live"],
            },
            {
                "module": "stats-trust-band-v2",
                "content_job": "Nostaa koulutusmäärät, suosittelun ja palautteet.",
                "source_priority": ["notion:Koulutus", "live"],
            },
            {
                "module": "faq-v2",
                "content_job": "Vastaa toteutus-, hinta-, aiheet- ja kenelle-kysymyksiin.",
                "source_priority": ["notion:Koulutus"],
            },
            {
                "module": "final-cta-v2",
                "content_job": "Ohjaa tarjouspyyntöön.",
                "source_priority": ["notion:Koulutus"],
            },
        ],
        "mandatory_signals": [
            "Osaamisvaje näkyy ennen agendaa",
            "Käytännön hyöty näkyy",
            "AI / Zero Click -murros näkyy",
            "Koulutus kytkeytyy tekemisen muutokseen",
        ],
    },
    {
        "page_id": "digimarkkinointi-v2",
        "url": "https://www.kuulu.fi/digimarkkinointi",
        "preview_slug": "/v2-digimarkkinointi",
        "template": "service-landing-v2",
        "primary_goal": "Explain how Kuulu connects visibility, trust, demand capture and measurement into one system.",
        "core_message": "Markkinointi ei saa jäädä yksittäisiksi toimenpiteiksi. Sisältö, näkyvyys ja liidit pitää rakentaa samaan koneistoon.",
        "hero_direction": {
            "headline": "Näy. Kuulu. Tee tulosta.",
            "supporting_angle": "Hajanaiset toimenpiteet eivät riitä. Tarvitaan koneisto, joka rakentaa muistijälkeä ja kotiuttaa kysyntää.",
            "cta_goal": "sparraus tai tarjous",
        },
        "section_stack": [
            {
                "module": "hero-cinematic-v2",
                "content_job": "Avaa markkinoinnin systemaattinen näkökulma.",
                "source_priority": ["live", "pdf:Zero Click"],
            },
            {
                "module": "problem-grid-v2",
                "content_job": "Purkaa hajanaisuuden, mittaamisen puutteen ja liidiongelman.",
                "source_priority": ["live", "pdf:Zero Click"],
            },
            {
                "module": "audience-split-v2",
                "content_job": "Näyttää tunnettuuden ja kysynnän kotiutuksen kaksijaon.",
                "source_priority": ["pdf:Zero Click"],
            },
            {
                "module": "service-pillars-v2",
                "content_job": "Esittelee Brand DNA:n, Sisältökoneiston ja Liidimoottorin palvelun sisällä.",
                "source_priority": ["pdf:Zero Click", "live"],
            },
            {
                "module": "process-steps-v2",
                "content_job": "Auditointi → koneisto → optimointi.",
                "source_priority": ["live", "pdf:Zero Click"],
            },
            {
                "module": "reference-grid-v2",
                "content_job": "Näyttää markkinoinnin, sisällön ja kasvun relevantit caset.",
                "source_priority": ["inventory"],
            },
            {
                "module": "faq-v2",
                "content_job": "Vastaa mitä sisältyy, miten mitataan ja kenelle sopii.",
                "source_priority": ["live", "pdf:Zero Click"],
            },
            {
                "module": "final-cta-v2",
                "content_job": "Ohjaa sparraukseen / tarjoukseen.",
                "source_priority": ["live", "pdf:Zero Click"],
            },
        ],
        "mandatory_signals": [
            "95/5-logiikka näkyy ainakin kevyesti",
            "Mittaus ja koneisto näkyvät",
            "Brand DNA näkyy palvelun perustana",
            "Liidit ja näkyvyys eivät ole erillisiä saarekkeita",
        ],
    },
    {
        "page_id": "case-studies-v2",
        "url": "https://www.kuulu.fi/case-studies",
        "preview_slug": "/v2-case-studies",
        "template": "reference-index-v2",
        "primary_goal": "Make proof easy to browse by problem, service and outcome.",
        "core_message": "Caset näyttävät, miten kitka poistuu, ratkaisu rakentuu ja tulokset syntyvät.",
        "hero_direction": {
            "headline": "Parhaat projektit haasteesta tuloksiin.",
            "supporting_angle": "Casejen pitää todistaa, ei vain näyttää hienolta.",
            "cta_goal": "sparraus / oma tarve",
        },
        "section_stack": [
            {
                "module": "hero-cinematic-v2",
                "content_job": "Kehystää caset tulos- ja oppinäkökulmasta.",
                "source_priority": ["live", "brand"],
            },
            {
                "module": "reference-grid-v2",
                "content_job": "Päätason case-kortit ongelman, palvelun ja tuloksen mukaan.",
                "source_priority": ["inventory"],
            },
            {
                "module": "reference-grid-v2",
                "content_job": "Tarvittaessa toinen näkymä esim. video / koulutus / AI / markkinointi.",
                "source_priority": ["inventory"],
            },
            {
                "module": "final-cta-v2",
                "content_job": "Ohjaa omaan tarpeeseen ja yhteydenottoon.",
                "source_priority": ["brand", "live"],
            },
        ],
        "mandatory_signals": [
            "Casejen pitää olla löydettäviä nopeasti",
            "Casejen pitää kertoa haaste → ratkaisu → tulos",
            "Indeksi ei saa olla arkistomainen",
        ],
    },
    {
        "page_id": "yhteystiedot-v2",
        "url": "https://www.kuulu.fi/yhteystiedot",
        "preview_slug": "/v2-yhteystiedot",
        "template": "company-info-v2",
        "primary_goal": "Remove the final friction from contact and make trust tangible through people and offices.",
        "core_message": "Yhteydenoton pitää tuntua helpolta, inhimilliseltä ja korkealaatuiselta.",
        "hero_direction": {
            "headline": "Ota yhteyttä.",
            "supporting_angle": "Selkeä yhteydenotto, oikeat ihmiset ja matala kitka.",
            "cta_goal": "lomake tai sparraus",
        },
        "section_stack": [
            {
                "module": "hero-cinematic-v2",
                "content_job": "Avaa yhteydenoton matalan kynnyksen näkökulman.",
                "source_priority": ["live", "brand"],
            },
            {
                "module": "lead-capture-form-cta-v2",
                "content_job": "Näyttää päälomakkeen / ensisijaisen yhteydenottoreitin.",
                "source_priority": ["live"],
            },
            {
                "module": "team-grid-v2",
                "content_job": "Tekee yhteyshenkilöistä konkreettisia ja helposti lähestyttäviä.",
                "source_priority": ["live"],
            },
            {
                "module": "contact-info-v2",
                "content_job": "Nostaa toimistot ja laskutustiedot rakenteisena datana.",
                "source_priority": ["live"],
            },
            {
                "module": "final-cta-v2",
                "content_job": "Viimeinen matalan kitkan yhteydenottopolku.",
                "source_priority": ["live", "brand"],
            },
        ],
        "mandatory_signals": [
            "Yhteydenotto tuntuu helpolta",
            "Ihmiset näkyvät luottamuksen rakentajina",
            "Sivu ei tunnu hallinnolliselta jäännökseltä",
        ],
    },
]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(CONTENT_PACKS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
