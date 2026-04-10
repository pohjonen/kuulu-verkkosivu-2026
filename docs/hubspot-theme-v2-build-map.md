# Kuulu v2: HubSpot-teeman build map

## Tarkoitus

Tämä dokumentti kertoo, miten nykyinen dokumentaatio, manifestit, helper-scriptit ja paikallinen blueprint liittyvät toisiinsa käytännön toteutuspolussa.

Tavoite:

- tehdä seuraava vaihe yksiselitteiseksi heti kun HubSpot-auth tai teeman export on käytettävissä
- näyttää mikä tiedosto on minkäkin päätöksen lähde
- estää tilanne, jossa v2-rakennetta aletaan tehdä väärästä lähteestä tai väärässä järjestyksessä

---

## 1. Lähdehierarkia

### Strateginen totuus

Nämä tiedostot määrittävät mitä sivuston pitää viestiä:

- `docs/kuulu-content-principles.md`
- `docs/kuulu-migration-matrix.md`
- `docs/kuulu-first-wave-section-stacks.md`
- käyttäjän toimittama Zero Click -ydinsisältö
- Notion-sivut (kun merkitty lähdeprioriteettiin)

### Modulaarinen totuus

Nämä tiedostot määrittävät miten rakenne pysyy hallittuna:

- `docs/kuulu-module-field-model.md`
- `docs/kuulu-module-build-order.md`
- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

### Riski- ja julkaisutotuus

Nämä tiedostot määrittävät mitä ei saa rikkoa ja miten julkaisu tehdään:

- `docs/hubspot-v2-structure-model.md`
- `docs/hubspot-theme-audit-checklist.md`
- `docs/kuulu-redirect-and-slug-register.md`
- `docs/kuulu-cutover-checklist.md`
- `docs/generated/kuulu-redirect-register.json`
- `docs/generated/kuulu-cutover-checklist.json`
- `docs/generated/kuulu-v2-implementation-status.json`

### Operatiivinen bootstrap-totuus

Nämä tiedostot ohjaavat HubSpotin käytännön bootstrap-vaihetta:

- `docs/hubspot-auth-bootstrap.md`
- `hubspot/README.md`
- `scripts/hubspot_bootstrap_status.sh`
- `scripts/hubspot_fetch_current_theme.sh`
- `scripts/hubspot_clone_v2_theme.sh`
- `scripts/hubspot_watch_v2.sh`

---

## 2. Koneellinen työnkulku

### Vaihe A — inventaario

Nykyinen julkinen tila tuotetaan:

- `scripts/kuulu_public_audit.py`

Tuotokset:

- `docs/generated/kuulu-public-site-inventory.csv`
- `docs/generated/kuulu-public-site-inventory.json`

### Vaihe B — v2-manifestit

Ensimmäisen aallon koneellinen rakenne tuotetaan:

- `scripts/generate_v2_manifests.py`

Tuotokset:

- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

Validointi:

- `scripts/validate_v2_manifests.py`

### Vaihe C — cutover-rekisterit

Julkaisun ja slug-päätösten koneellinen rekisteri tuotetaan:

- `scripts/generate_cutover_registers.py`

Tuotokset:

- `docs/generated/kuulu-redirect-register.json`
- `docs/generated/kuulu-cutover-checklist.json`
- `docs/generated/kuulu-v2-implementation-status.json`

### Vaihe D — paikallinen blueprint

Paikallinen turvallinen runko tuotetaan:

- `scripts/bootstrap_v2_blueprint.py`

Tuotos:

- `hubspot/kuulu-theme-v2-blueprint/`

---

## 3. Blueprintin rooli

`hubspot/kuulu-theme-v2-blueprint/` EI ole oikea lähdeteema eikä tuotantoteema.

Se on:

- paikallinen rakennerunko
- moduuli- ja templatekartan visualisointi
- turvallinen paikka nähdä v2-teeman alustava tiedostorakenne

Se EI ole:

- suoraan liveen työnnettävä teema
- oikea source theme
- lopullinen fork nykyisestä HubSpot-teemasta

---

## 4. Kun auth on kunnossa

Heti kun `hs account auth` onnistuu tai teeman export saadaan, käytännön eteneminen on tämä:

1. aja `scripts/hubspot_bootstrap_status.sh`
2. tee source-theme fetch:
   - `bash scripts/hubspot_fetch_current_theme.sh <remote-theme-path>`
3. auditoi fetched theme tämän avulla:
   - `docs/hubspot-theme-audit-checklist.md`
4. tee oikea v2-klooni:
   - `bash scripts/hubspot_clone_v2_theme.sh source-theme kuulu-theme-v2`
5. vertaa oikeaa kloonia blueprintiin:
   - `hubspot/kuulu-theme-v2-blueprint/`
6. siirrä blueprintin moduuli- ja templatepäätökset oikeaan `hubspot/kuulu-theme-v2/`-hakemistoon
7. käynnistä turvallinen watch oikeaan v2-polkuun:
   - `bash scripts/hubspot_watch_v2.sh <local-src> <remote-dest>`

---

## 5. Mitä EI pidä tehdä

Älä:

- rakenna suoraan `source-theme/`-hakemistoon
- työnnä blueprint-hakemistoa sellaisenaan HubSpotiin tuotantoteemaksi
- muuta live-teemaa ilman että fetched source on auditoitu
- oleta, että blueprint ja source-theme ovat 1:1-rakenteisia

Blueprint kertoo mitä haluamme rakentaa.
Source theme kertoo mistä on turvallista lähteä liikkeelle.

---

## 6. Yhteenveto

Tämän projektin build map on:

1. dokumentaatio määrittää strategian ja rakennepäätökset
2. generaattorit muuttavat päätökset koneellisiksi manifesteiksi
3. blueprint näyttää turvallisen v2-runon paikallisesti
4. vasta auth/exportin jälkeen oikea HubSpot-teema auditoidaan ja kloonataan
5. blueprintin päätökset siirretään oikeaan v2-teemaan, ei toisin päin

Tärkein sääntö:

> Dokumentaatio ja blueprint ohjaavat toteutusta, mutta oikeaan live-teemaan kosketaan vasta auditoinnin jälkeen.
