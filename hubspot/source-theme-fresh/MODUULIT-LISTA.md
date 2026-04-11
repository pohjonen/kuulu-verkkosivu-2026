# Cinematic-teema: kaikki moduulit – lista ja mitä ne tekevät

Vain `.module`-päätteiset kansiot ovat käytössä. Lista kattaa kaikki teeman moduulit.

---

## Ydinsivurakenne (etusivu / koulutus -putki)

| # | Label HubSpotissa | Kansio | Mitä tekee |
|---|-------------------|--------|------------|
| 01 | Hero-osio | `cinematic_hero.module` | Sivun yläosa: otsikko, alaotsikko, ingressi, 1–2 CTA-nappia, valinnainen taustakuva/video. Voi näyttää tilastot (esim. 300+ koulutusta). |
| 02 | Ilmoittautumislomake | `cinematic_early_bird.module` | Lomakeosio: HubSpot-lomake + myyntiteksti, valinnainen kuva/video. Early bird -ilmoittautumiset, uutiskirje, tarjouspyynnöt. |
| 03 | Listaus (kuvake + teksti) | `cinematic_problem_list.module` | Rivejä: kuvake (tai rasti/risti) + otsikko + kuvaus. Ongelmat, hyödyt, ominaisuudet, palvelulistaus. |
| 04 | Korttipari | `cinematic_two_engines.module` | Kaksi rinnakkaista korttia (otsikko, teksti, lista, CTA). Vertailu, kaksi palvelua, ennen/jälkeen. |
| 05 | Henkilön esittely / Teksti + kuva | `cinematic_text_image.module` | Teksti vasemmalla/oikealla, kuva toisella puolella. Henkilöprofiili, tiimiesittely, brändi- tai tarinablokki. |
| 06 | Askeleet / prosessi | `cinematic_steps.module` | Numeroidut vaiheet (1–4+): otsikko + kuvaus per vaihe. Prosessikuvaus, "näin toimimme", ohjeet. |
| 07 | Mittarit + kuva | `cinematic_metrics.module` | Numerotiedot + kuva (tai video). Tulokset, KPI:t, saavutukset, "mittaamme suppilon". |
| 08 | Tekstiosio (leveä) | `cinematic_authority.module` | Pelkkä teksti koko leveydellä. Taustatarina, filosofia, "miksi me", pitkä copy. |
| 09 | Kuva-CTA-kortit | `cinematic_cta_cards.module` | Kuvalinkkikortit ruudukossa (2–4). Palvelunavigaatio, kategoriat, suosituimmat koulutukset, CTA-grid. |
| 10 | Referenssit / caset | `cinematic_referenssit.module` | Asiakascaset: kuva/video + otsikko + teksti + linkki. Referenssit, case study -esittely. |
| 11 | CTA-osio | `cinematic_contact_cta.module` | Toimintakehotus: otsikko + lyhyt teksti + 1–2 nappia (esim. Ota yhteyttä, Pyydä tarjous). Sivun lopun CTA. |

---

## Teksti ja sisältö

| Label HubSpotissa | Kansio | Mitä tekee |
|-------------------|--------|------------|
| Tekstisisältö | `cinematic_rich_text.module` | Rich text -lohko: otsikko, 1–3 saraketta tekstiä, valinnainen kuva tai video vieressä. Monipuolinen tekstiosio. |
| Tarkistuslista | `cinematic_checklist.module` | Lista kohdista (rasti/risti) + otsikko + kuvaus. Plussat/miinukset, vaatimukset, checklist. |
| Cinematic Accordion Cards | `cinematic_accordion_cards.module` | Accordion: avattavat otsikot, sisällä tekstiä/linkkejä. UKK, kategoriat, koulutusaiheet. |
| Vertailutaulukko | `cinematic_comparison_table.module` | Taulukko vertailuun (esim. paketit, vaihtoehdot). Otsikot ja solut muokattavissa. |

---

## Visuaaliset ja erikoismoduulit

| Label HubSpotissa | Kansio | Mitä tekee |
|-------------------|--------|------------|
| 16 – Animoidut laskurit | `cinematic_animated_counter.module` | Numerot, jotka animoituvat (esim. 0 → 300+). Tilastot, count-up -efekti. |
| 17 – Scrollaavat logot | `cinematic_marquee_logos.module` | Logoja scrollaava nauha (marquee). Asiakkaat, yhteistyökumppanit. |
| 18 – Ennen/Jälkeen -vertailu | `cinematic_before_after.module` | Ennen/jälkeen -kuvavertailu (slider tai kuvapari). |
| 19 – Hinnoittelukortit (täysi) | `cinematic_rich_pricing.module` | Hinnoittelukortit: hinta, lista, CTA. Täysiverkko hinnoitteluosio. |
| 20 – Pystyaikajana | `cinematic_vertical_timeline.module` | Pystysuora aikajana (vaiheet, tapahtumat). |
| 21 – Bento Grid | `cinematic_bento_grid.module` | Bento-tyylinen ruudukko: erikokoiset laatat (kuvia/tekstiä). |
| Etenemispolku | `cinematic_timeline.module` | Aikajana / etenemispolku (vaaka tai rakenne). |
| Hinta ja ajankohta | `cinematic_pricing.module` | Yksittäinen hinta + ajankohta + CTA (esim. webinaari). |
| Cinematic ROI Calculator | `cinematic_roi_calculator.module` | ROI-laskuri: syötteet → laskenta → tulos. |
| Cinematic Horizontal Scroll | `cinematic_horizontal_scroll.module` | Vaakasuuntainen scrollaus (kortit tai sisältö). |
| Cinematic Before After | (sisältyy 18) | Ennen/jälkeen -vertailu. |

---

## Lomakkeet ja CTA

| Label HubSpotissa | Kansio | Mitä tekee |
|-------------------|--------|------------|
| 12 – Koulutusyhteydenotto (lomake) | `cinematic_koulutus_form.module` | Koulutustarjouspyynnön lomake + tilastot + teksti. Erityisesti koulutussivu. |
| Cinematic Floating CTA | `cinematic_floating_cta.module` | Kelluva CTA (esim. sivun reunassa kiinni). |
| Cinematic Sticky Navigation | `cinematic_sticky_nav.module` | Kiinn sticky -navigaatio (esim. sivun sisälinkit). |

---

## Palautteet ja referenssit

| Label HubSpotissa | Kansio | Mitä tekee |
|-------------------|--------|------------|
| Cinematic Testimonial Slider | `cinematic_testimonial_slider.module` | Asiakaspalautteet karusellina: lainaus + nimi + titteli. Ei sama kuin Referenssit (caset). |
| Case Study Showcase | `case-study-showcase.module` | Case study -näyttö (esim. isommat caset). |
| Cinematic Case Study Card | `cinematic_case_study_card.module` | Yksi case study -kortti (kuva, teksti, linkki). |

---

## Globaalit ja yleiskäyttö

| Label HubSpotissa | Kansio | Mitä tekee |
|-------------------|--------|------------|
| Globaali Header – Mega-Menu | `cinematic_header.module` | Header + mega-valikko. Käytetään jos moduulina; usein partiaali `header-cinematic.html` sijaan. |
| Globaali Footer | `cinematic_footer.module` | Sivun alatunniste. Voi olla partiaali `footer-cinematic.html` käytössä. |
| 🌐 GLOBAL – Header & Menu | `global_header.module` | Vaihtoehtoinen globaali header. |
| 🌐 GLOBAL – Footer | `global_footer.module` | Vaihtoehtoinen globaali footer. |

---

## Muut

| Label HubSpotissa | Kansio | Mitä tekee |
|-------------------|--------|------------|
| Hero Banner | `hero-banner.module` | Yksinkertaisempi hero-banneri (vaihtoehto cinematic_herolle). |
| Henkilökohtainen profiili | `person-profile.module` | Henkilöprofiilikortti (kuva, nimi, titteli, teksti). |
| Palvelut Grid | `services-grid.module` | Ruudukko palveluista (otsikko, kuvaus, linkki per palvelu). |
| Video Showcase | `video-showcase.module` | Videot esillä (soittolista tai showcase). |

---

## Käytössä olevat templatet (lyhyt viite)

- **Etusivu:** `homepage-modules.html` → moduulit 01–11 (hero → CTA).
- **Koulutus:** `koulutus-modules.html` → samat 01–11, sisältö täytetään editorissa.
- Header/footer useimmiten: `partials/header-cinematic.html`, `partials/footer-cinematic.html`.

---

Viimeksi päivitetty: 2026-03
