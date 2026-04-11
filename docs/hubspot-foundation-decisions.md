# Kuulu v2: foundation-moduulien lähdepäätökset

## Tarkoitus

Tämä dokumentti lukitsee ensimmäisen varsinaisen HubSpot-toteutuksen kannalta tärkeimpien **foundation-moduulien** päätökset fetchatun source themen pohjalta.

Päätösluokat:

- `protect` = ei kosketa suoraan, toimii vain vertailupisteenä
- `fork-to-v2` = kopioidaan ja kehitetään vain `hubspot/kuulu-theme-v2/`-puolella
- `reuse-candidate` = mahdollinen uudelleenkäyttö, mutta vahvistetaan toteutuksessa
- `replace` = ei käytetä pohjana, rakennetaan uusi
- `review-manually` = pidetään tarkkailussa, mutta ei foundation-aallon ensisijainen kohde

Pääperiaate:

> Käytämme nykyisen etusivun cinematic-teemaa ytimenä, mutta emme koskaan muokkaa source-themeä tai liveen liittyviä shared-rakenteita suoraan.

---

## 1. Foundation-aallon kannalta tärkeimmät source-kandidaatit

### 1.1 Hero

#### Source-kandidaatti

- `modules/cinematic_hero.module`

#### Päätös

- **fork-to-v2**

#### Peruste

- nimi, kategoria ja rakenteellinen rooli tukevat suoraan v2:n Hero Cinematic -tarvetta
- moduuli liittyy nykyiseen cinematic-ajatteluun
- tätä ei pidä reusea suoraan, koska:
  - kenttämalli pitää varmistaa v2-guardrailien mukaiseksi
  - CTA- ja media-logiikka pitää yhdenmukaistaa
  - mahdollinen kytkentä nykyiseen etusivuun pitää katkaista

#### V2-kohde

- `hero-cinematic-v2`

---

### 1.2 Problem / kipulista

#### Source-kandidaatti

- `modules/cinematic_problem_list.module`

#### Päätös

- **fork-to-v2**

#### Peruste

- tämä näyttää luonnollisimmalta lähteeltä Problem Grid / pain point -rakenteelle
- sopii hyvin Zero Click -rakenteen “tunnistatko nämä” -kohtiin
- nykyinen toteutus pitää silti irrottaa source/livestä ja muuttaa v2:n strukturoituun repeater-malliin

#### V2-kohde

- `problem-grid-v2`

---

### 1.3 Two engines / kaksimoottorinen rakenne

#### Source-kandidaatti

- `modules/cinematic_two_engines.module`

#### Päätös

- **fork-to-v2**

#### Peruste

- tämä on suoraan linjassa nykyisen etusivun “Kaksi konetta, yksi tavoite” -rakenteen kanssa
- sopii Brand DNA + Sisältökoneisto + Liidimoottori -logiikan esittämiseen
- v2:ssa pitää päättää:
  - jääkö tämä omaksi moduuliksi
  - vai jaetaanko sen logiikka `service-pillars-v2` + `audience-split-v2` -rakenteisiin

#### V2-kohde

- ensisijainen lähtö: `service-pillars-v2`
- mahdollinen lisälähtö: `audience-split-v2`

---

### 1.4 Metrics / trust

#### Source-kandidaatti

- `modules/cinematic_metrics.module`

#### Päätös

- **fork-to-v2**

#### Peruste

- mittarit ovat yksi nykyisen cinematic-kielen ytimistä
- sopii suoraan `stats-trust-band-v2`-moduulin lähtöpisteeksi
- v2:ssa pitää tarkistaa:
  - miten numerot, labelit ja konteksti on mallinnettu
  - voiko editori rikkoa rakenteen
  - ovatko spacingit / cardit v2-standardin mukaisia

#### V2-kohde

- `stats-trust-band-v2`

---

### 1.5 Koulutusformi / lead capture

#### Source-kandidaatti

- `modules/cinematic_koulutus_form.module`

#### Päätös

- **fork-to-v2**

#### Peruste

- tämä on selkein nykyinen lähde koulutus-/lomakelogiikalle
- erityisen tärkeä, koska käyttäjä haluaa ettei nykyiset formit / konversiopolut rikkoudu
- v2:ssa pitää normalisoida:
  - form valinta
  - CTA fallback
  - mediaoptio
  - editor guardrails

#### V2-kohde

- `lead-capture-form-cta-v2`

---

### 1.6 Palvelukortit / gridit

#### Source-kandidaatit

- `modules/services-grid.module`
- `modules/cinematic_cta_cards.module`
- `modules/cinematic_case_study_card.module`

#### Päätös

- `services-grid.module` → **fork-to-v2**
- muut → **review-manually**

#### Peruste

- `services-grid.module` on todennäköisesti lähimpänä v2:n palvelu-/pillar-korttirakennetta
- muut cinematic-kortit voivat myöhemmin täydentää referenssi- tai CTA-rakenteita, mutta niitä ei tarvitse lukita foundation-aallon ensimmäiseen toteutukseen

#### V2-kohde

- `service-pillars-v2`

---

### 1.7 Video showcase / referenssivideo

#### Source-kandidaatti

- `modules/video-showcase.module`

#### Päätös

- **fork-to-v2**

#### Peruste

- relevantti videotuotanto- ja referenssikäyttöön
- voi tukea `reference-grid-v2` tai video-case-osioita
- ei kuitenkaan yksin ratkaise kaikkea reference-detail-rakennetta

#### V2-kohde

- `reference-grid-v2`

---

### 1.8 Person profile

#### Source-kandidaatti

- `modules/person-profile.module`
- `templates/person-profile.html`

#### Päätös

- molemmat → **fork-to-v2**

#### Peruste

- nämä ovat selkeimmät lähdepisteet henkilöprofiilien v2-normalisointiin
- samalla pitää poistaa blogifeediriippuvuus tai vähintään estää sen keskeinen rooli
- nykyinen rakenne voi olla hyvä lähtö, mutta ei lopullinen toteutus

#### V2-kohde

- `person-profile-v2`

---

## 2. Shared/global-rakenteet

### 2.1 Global header

#### Source-kandidaatit

- `modules/global_header.module`
- `templates/partials/header-cinematic.html`
- `modules/cinematic_header.module`

#### Päätös

- `global_header.module` → **protect**
- `templates/partials/header-cinematic.html` → **protect**
- `cinematic_header.module` → **review-manually**

#### Peruste

- nämä ovat suoraan live- ja shared-riskialuetta
- näitä ei muokata lähteessä
- v2:een tehdään oma:
  - `header-v2`
  - `navigation-v2`

---

### 2.2 Global footer

#### Source-kandidaatit

- `modules/global_footer.module`
- `templates/partials/footer-cinematic.html`
- `templates/partials/footer-module.html`

#### Päätös

- kaikki → **protect**

#### Peruste

- footer on shared-kohde
- väärä muutos voi rikkoa koko tuotantoa
- v2 tekee oman footer-rakenteensa erillisenä

---

### 2.3 Navigation / mobile menu

#### Source-kandidaatit

- `js/mobile-menu.js`
- mahdolliset menu/partial-rakenteet

#### Päätös

- **protect**

#### Peruste

- navigaatio on korkean riskin alue
- nykyinen käytös kannattaa vain auditoida ja kopioida v2:een, ei muuttaa lähteessä

---

## 3. Etusivutemplatet

### Source-kandidaatit

- `templates/homepage-cinematic-v6.html`
- `templates/homepage-new.html`
- muut `homepage-cinematic-*`

### Päätös

- kaikki nykyiset homepage-cinematic -templaatit → **protect**
- `homepage-cinematic-v6.html` → **ensisijainen referenssilähde**
- `homepage-new.html` → **toissijainen referenssilähde**

### Peruste

- nykyinen etusivu on käyttäjän tärkein suojattava kohde
- näitä ei muokata suoraan
- v2-etusivu rakennetaan omalle template-haaralle käyttäen näitä vain lähdereferenssinä

---

## 4. Foundation-aallon päätökset yhteenvetona

| Lähdekohde | Päätös | V2-kohde |
| --- | --- | --- |
| `cinematic_hero.module` | fork-to-v2 | `hero-cinematic-v2` |
| `cinematic_problem_list.module` | fork-to-v2 | `problem-grid-v2` |
| `cinematic_two_engines.module` | fork-to-v2 | `service-pillars-v2` / `audience-split-v2` |
| `cinematic_metrics.module` | fork-to-v2 | `stats-trust-band-v2` |
| `cinematic_koulutus_form.module` | fork-to-v2 | `lead-capture-form-cta-v2` |
| `services-grid.module` | fork-to-v2 | `service-pillars-v2` |
| `video-showcase.module` | fork-to-v2 | `reference-grid-v2` |
| `person-profile.module` | fork-to-v2 | `person-profile-v2` |
| `templates/person-profile.html` | fork-to-v2 | `person-profile-v2` |
| `global_header.module` | protect | `header-v2` rakennetaan erikseen |
| `global_footer.module` | protect | `footer-v2` rakennetaan erikseen |
| `header-cinematic.html` | protect | referenssi vain |
| `footer-cinematic.html` | protect | referenssi vain |
| `homepage-cinematic-v6.html` | protect | etusivun referenssilähde |
| `homepage-new.html` | protect | etusivun referenssilähde |

---

## 5. Seuraava käytännön askel

Nyt kun nämä foundation-päätökset on lukittu, seuraava oikea tekninen vaihe on:

1. pitää `hubspot/source-theme/` koskemattomana
2. tehdä muutokset vain `hubspot/kuulu-theme-v2/`-kloonissa
3. aloittaa foundation-moduulien oikea vertailu tiedosto kerrallaan:
   - `meta.json`
   - `fields.json`
   - `module.html`
   - `module.css`
   - `module.js`
4. siirtää vain tarpeellinen logiikka v2-rakenteeseen

Tärkein sääntö:

> nykyisen etusivun cinematic-rakenne toimii ytimenä, mutta kaikki varsinainen työ tapahtuu erillisessä v2-kloonissa.
