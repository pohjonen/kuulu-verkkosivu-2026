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
- `docs/hubspot-post-auth-handoff.md`
- `hubspot/README.md`
- `scripts/hubspot_bootstrap_status.sh`
- `scripts/hubspot_fetch_current_theme.sh`
- `scripts/hubspot_clone_v2_theme.sh`
- `scripts/hubspot_watch_v2.sh`

### Fetch- ja source-match -totuus

Nämä tiedostot varmistavat, että oikea HubSpot source theme on haettu ennen forkkausta:

- `docs/generated/kuulu-public-asset-signature.json`
- `docs/generated/kuulu-public-asset-signature.md`
- `docs/hubspot-source-theme-match-playbook.md`
- `scripts/generate_public_asset_signature.py`
- `scripts/compare_source_theme_to_public_signature.py`

---

## 2. Koneellinen työnkulku

### Vaihe A — inventaario

Nykyinen julkinen tila tuotetaan:

- `scripts/kuulu_public_audit.py`

Tuotokset:

- `docs/generated/kuulu-public-site-inventory.csv`
- `docs/generated/kuulu-public-site-inventory.json`

### Vaihe A2 — julkinen asset-signature

Nykyinen julkinen HubSpot-asset-fingerprint tuotetaan:

- `scripts/generate_public_asset_signature.py`

Tuotokset:

- `docs/generated/kuulu-public-asset-signature.json`
- `docs/generated/kuulu-public-asset-signature.md`

### Vaihe B — v2-manifestit

Ensimmäisen aallon koneellinen rakenne tuotetaan:

- `scripts/generate_v2_manifests.py`

Tuotokset:

- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

Validointi:

- `scripts/validate_v2_manifests.py`

### Vaihe B2 — first wave content packit

Ensimmäisen aallon sisältörunko tuotetaan:

- `scripts/generate_first_wave_content_packs.py`

Tuotokset:

- `docs/generated/kuulu-first-wave-content-packs.json`
- `docs/kuulu-first-wave-content-packs.md`

### Vaihe B3 — HubSpot-friendly first wave data

Ensimmäisen aallon HubSpot-työdata tuotetaan:

- `scripts/generate_first_wave_hs_data.py`

Tuotokset:

- `docs/generated/kuulu-first-wave-hs-data.json`
- `docs/hubspot-first-wave-build-checklist.md`

### Vaihe B2 — first wave content + HubSpot data

Ensimmäisen aallon sisältö- ja täyttödata tuotetaan:

- `scripts/generate_first_wave_content_packs.py`
- `scripts/generate_first_wave_hs_data.py`

Tuotokset:

- `docs/generated/kuulu-first-wave-content-packs.json`
- `docs/generated/kuulu-first-wave-hs-data.json`

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
- `scripts/validate_blueprint_scaffold.py`

Tuotos:

- `hubspot/kuulu-theme-v2-blueprint/`

Validointi:

- `python3 scripts/validate_blueprint_scaffold.py`

### Vaihe E — ensimmäisen aallon HubSpot-build-data

Ensimmäisen aallon sivujen HubSpot-ystävällinen build-data tuotetaan:

- `scripts/generate_first_wave_hs_data.py`

Tuotokset:

- `docs/generated/kuulu-first-wave-hs-data.json`

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
3. vertaile fetched themea julkiseen signatuuriin:
   - `python3 scripts/compare_source_theme_to_public_signature.py hubspot/source-theme`
   - `docs/hubspot-source-theme-match-playbook.md`
4. aja koottu post-auth audit runner:
   - `bash scripts/run_post_auth_audit.sh hubspot/source-theme`
5. auditoi fetched theme tämän avulla:
   - `docs/hubspot-theme-audit-checklist.md`
6. tee oikea v2-klooni:
   - `bash scripts/hubspot_clone_v2_theme.sh source-theme kuulu-theme-v2`
7. vertaa oikeaa kloonia blueprintiin:
   - `hubspot/kuulu-theme-v2-blueprint/`
8. käytä ensimmäisen aallon build-dataa:
   - `docs/generated/kuulu-first-wave-hs-data.json`
   - `docs/hubspot-first-wave-build-checklist.md`
9. siirrä blueprintin moduuli- ja templatepäätökset oikeaan `hubspot/kuulu-theme-v2/`-hakemistoon
10. käynnistä turvallinen watch oikeaan v2-polkuun:
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
3. julkinen asset-signature auttaa tunnistamaan oikean source themen
4. blueprint näyttää turvallisen v2-runon paikallisesti
5. vasta auth/exportin jälkeen oikea HubSpot-teema matchataan, auditoidaan ja kloonataan
6. ensimmäisen aallon HS-data ohjaa käytännön buildiä
7. blueprintin päätökset siirretään oikeaan v2-teemaan, ei toisin päin

## 6.1 Blueprintin hygieniasääntö

Blueprint pitää pystyä generoimaan aina puhtaaksi ilman jäämiä vanhoista tiedostoista.

Siksi käytetään:

- `scripts/bootstrap_v2_blueprint.py`
- `scripts/validate_blueprint_scaffold.py`

Toimintatapa:

1. blueprint-hakemisto siivotaan ennen uudelleengenerointia
2. scaffold generoidaan manifesteistä
3. validaattori tarkistaa:
   - template-määrän
   - globaalien partialien olemassaolon
   - global scaffoldit
   - moduulihakemistot
   - theme asset -rungon

Näin blueprint pysyy luotettavana välitasona eikä siihen jää vanhoista ajokerroista harhatiedostoja.

Tärkein sääntö:

> Dokumentaatio ja blueprint ohjaavat toteutusta, mutta oikeaan live-teemaan kosketaan vasta auditoinnin jälkeen.

Lisäsääntö:

> Blueprint regeneroidaan aina siivotusti. Vanhat placeholderit tai virheelliset tiedostonimet eivät saa jäädä elämään rinnalle ja hämärtää oikeaa rakennetta.

---

## 7. Post-auth handoff

Kun auth on tehty tai teema on exportoitu, käytä lisäksi:

- `docs/hubspot-post-auth-handoff.md`

Se toimii käytännön “ensimmäiset 60 minuuttia” -ohjeena execution-vaiheen käynnistämiseen oikeassa HubSpot-ympäristössä.
