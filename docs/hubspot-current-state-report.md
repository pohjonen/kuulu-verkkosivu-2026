# HubSpot nykytila: authin jälkeinen current-state-raportti

## Yhteenveto

HubSpot-auth on nyt kunnossa ja accountiksi vahvistui:

- **kuulun**
- **portalId: 450584**

Turvallisen listauksen perusteella todennäköisimmät remote-teemakandidaatit olivat:

- `Kuulu-2026`
- `kuulu-theme-2025-live`
- `kuulu-theme-2025-staging`
- `Kuulu-theme-2025`

Näistä **todennäköisin tekninen lähdeteema jatkoauditille on tällä hetkellä `kuulu-theme-2025-staging`**, koska:

- se sisältää eniten cinematic-rakenteeseen viittaavia assetteja ja moduuleja
- siellä on selkeästi 2026-02-17 ympärillä tehtyjä cinematic-moduulipäivityksiä
- siinä on mukana:
  - `design-tokens.css`
  - `cinematic-main.css`
  - `cinematic-responsive.css`
  - `module-fixes.css`
  - suuri joukko `cinematic_*`-moduleita
  - nykyisen kaltaisia homepage-cinematic -templateja useina versioina

Samalla täytyy kuitenkin huomata, että public asset signature -vertailu **ei vielä vahvistanut filename-tason 1:1-osumaa** fetchatun sourcen ja julkisen tuotannon välillä.

Tämä tarkoittaa:

> source theme on nyt fetchattu ja auditoitu, mutta emme vielä voi käsitellä sitä lopullisesti “varmana tuotantolähteenä” ilman tarkempaa template- ja partial-tason vertailua.

---

## Vahvistettu auth-tila

### Account

- Default account: `kuulun [standard] (450584)`
- Auth type: `personalaccesskey`

### Saatavilla olevia scopeja

Auditin kannalta tärkeät:

- `cms.source_code.read`
- `cms.source_code.write`
- `cms.pages.site_pages.read`
- `cms.pages.landing_pages.read`
- `cms.domains.read`
- `files`

Tämä riittää turvalliseen fetch-/auditointiin sekä myöhempään v2-teeman rakentamiseen.

---

## Mitä remote-puolelta löytyi

Root-listauksessa näkyi useita Kuuluun liittyviä theme-/theme-like-kokonaisuuksia, mm:

- `Kuulu-2026`
- `kuulu-theme-2025-live`
- `kuulu-theme-2025-staging`
- `Kuulu-theme-2025`
- `kuulu-theme-header-test`
- `KuuluTemplate2025-V1`
- `VideoLandingPage_2025`

### Miksi `kuulu-theme-2025-staging` nousi kärkeen

Listaus sisälsi:

#### CSS
- `accessibility-performance.css`
- `cinematic-main.css`
- `cinematic-responsive.css`
- `cinematic.css`
- `design-tokens.css`
- `module-fixes.css`
- `theme-overrides.css`

#### Modulit
- `cinematic_hero.module`
- `cinematic_early_bird.module`
- `cinematic_two_engines.module`
- `cinematic_metrics.module`
- `cinematic_problem_list.module`
- `cinematic_koulutus_form.module`
- `cinematic_referenssit.module`
- `cinematic_rich_pricing.module`
- `global_header.module`
- `global_footer.module`

#### Templaatit
- useita `homepage-cinematic-*`-versioita
- `homepage-new.html`
- `video-production.html`
- `person-profile.html`
- suuri määrä testisivuja
- `templates/partials/`-hakemisto
- `templates/layouts/`-hakemisto

Näiden perusteella tämä näyttää teknisesti siltä rungolta, jossa nykyisen cinematic-linjan kehitys on todennäköisimmin elänyt.

---

## Fetchattu source theme

Fetchattiin:

```bash
bash scripts/hubspot_fetch_current_theme.sh "kuulu-theme-2025-staging" "/workspace/hubspot/source-theme"
```

Tulokset:

- paikallinen source theme olemassa: `hubspot/source-theme/`
- tiedostoja: **350**
- templateja auditin mukaan: **135**
- module rootteja: **39**
- assetteja auditin mukaan: **175**

Top-level rakenne:

- `css/`
- `docs/`
- `images/`
- `js/`
- `modules/`
- `templates/`
- `theme.json`
- sekä child-/fields-/README-tiedostoja

---

## Public signature match -tulos

Vertailu:

```bash
python3 scripts/compare_source_theme_to_public_signature.py hubspot/source-theme
```

Tulos:

- public asset filename matchit: **0**

Puuttuvia filename-osumia olivat mm:

- `template_cinematic.min.css`
- `template_cinematic-responsive.min.css`
- `template_design-tokens.min.css`
- `template_module-fixes.min.css`
- `template_main.min.js`
- `template_styles.min.css`
- `module_cinematic_early_bird.min.css`
- `module_cinematic_rich_pricing.min.css`
- `module_Vast_FAQ_Module.min.css`
- `module_Vast_FAQ_Module.min.js`

### Tulkinta

Tämä ei välttämättä tarkoita, että fetchattu theme on väärä.

Todennäköiset selitykset:

1. **HubSpot generoi julkaistut assetit eri nimillä kuin source-tiedostot**
   - esim. `design-tokens.css` → `template_design-tokens.min.css`
   - `cinematic-main.css` → `template_cinematic.min.css`

2. **Osa julkaistusta sivusta tulee build-pipeline / generated-assets -ketjusta**, jota source-kansio ei suoraan nimeä samalla tavalla

3. **Julkinen tuotanto voi käyttää live-teemaa**, joka on hyvin lähellä stagingiä mutta ei täysin sama

### Johtopäätös

Fetchattu theme on edelleen **todennäköinen, mutta ei filename-matchin perusteella varmistettu 1:1-lähde**.

Siksi jatkotoimissa pitää:

- vertailla erityisesti:
  - `design-tokens.css`
  - `cinematic-main.css`
  - `cinematic-responsive.css`
  - `module-fixes.css`
  - `js/main.js`
- etsiä homepage / video-production / training -templatejen käytännön site-page-kytkennät

---

## Fetched source audit -tulos

Auditointi:

```bash
python3 scripts/audit_fetched_source_theme.py hubspot/source-theme
```

Keskeinen tulos:

- **high risk items: 28**
- **matched public assets: 0**

### Theme signals

- `has_theme_json = true`
- `has_header_like_files = true`
- `has_footer_like_files = true`
- `has_navigation_like_files = true`
- `has_cinematic_signal = true`
- `has_token_signal = true`
- `has_legacy_style_signal = false`

Tämä tukee sitä ajatusta, että fetched theme on vahvasti cinematic-v2/moderni-haaraa, ei pelkkä legacy-light-pohja.

### Korkeimmat riskikohteet

Protected/high risk -ehdokkaiksi nousivat mm:

- `modules/global_header.module/*`
- `modules/global_footer.module/*`
- `templates/home.html`
- `templates/index.html`
- kaikki `templates/homepage-cinematic-*`
- `templates/homepage-new.html`
- `templates/partials/header-cinematic.html`
- `templates/partials/footer-cinematic.html`
- `js/mobile-menu.js`

### Käytännön johtopäätös

Näihin **ei kosketa suoraan** ennen kuin:

1. tiedetään mikä näistä todella on live-etusivun käytössä
2. reuse/fork/replace/protect -päätös on tehty
3. v2-klooni on tehty erilliseen hakemistoon

---

## Mitä nykytilasta voidaan nyt päätellä turvallisesti

### Vahvat päätelmät

1. **HubSpot account on oikea**
   - portalId 450584

2. **Source code -fetch toimii**
   - voimme auditoida remote CMS-rakenteita turvallisesti

3. **`kuulu-theme-2025-staging` on uskottava lähdeteemakandidaatti**
   - erityisesti cinematic-rakenteen osalta

4. **Julkisen tuotannon ja source-kansion välillä on build-/nimeämisero**
   - filename-match ei yksin riitä lopulliseen identifiointiin

5. **Etusivuun liittyvät tiedostot on nyt tunnistettu riskialueeksi**
   - tämä on hyvä, koska käyttäjän tärkein vaatimus on ettei mitään rikota

### Mitä ei vielä tiedetä varmasti

1. mikä yksittäinen template renderöi nykyisen live-etusivun
2. käyttääkö live `kuulu-theme-2025-live` vai `kuulu-theme-2025-staging` -haaraa vai jotain niiden lähisukua
3. mitkä `homepage-cinematic-*` versioista ovat oikeasti aktiivisia
4. miten generated/minified public assetit mapataan tarkasti source-tiedostoihin

---

## Suositeltu seuraava askel

Nyt kun auth on kunnossa ja source-theme on fetchattu, seuraava turvallinen vaihe olisi:

1. tehdä **reuse / fork / replace / protect** -päätös auditin perusteella
2. tehdä **oikea v2-klooni**:
   - `hubspot/source-theme/` → vertailupiste
   - `hubspot/kuulu-theme-v2/` → kaikki varsinainen työ
3. aloittaa foundation-moduulien oikea toteutus v2-kansiossa
4. rakentaa preview-sivut ensimmäisen aallon sivuille

### Ehdotus

Seuraava konkreettinen toteutustyö kannattaa aloittaa:

- `hero-cinematic-v2`
- `final-cta-v2`
- `problem-grid-v2`
- `service-pillars-v2`

mutta vasta **oikeassa `hubspot/kuulu-theme-v2/`-kloonikansiossa**, ei enää pelkässä blueprintissä.

---

## Yhteenveto yhdellä lauseella

**HubSpot-pääsy toimii, source-theme on nyt fetchattu ja auditointi on käynnissä, mutta varovaisuuden vuoksi fetched sourcea käsitellään vielä “todennäköisenä lähteenä”, ei lopullisesti vahvistettuna live-teeman 1:1-vastineena.**
