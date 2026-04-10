# Kuulu: pre-auth artefaktien refresh-ohje

## Tarkoitus

Tämä dokumentti kertoo, miten kaikki ennen HubSpot-authia tuotetut suunnittelu- ja build-artefaktit päivitetään yhdellä ajolla.

Tavoite:

- pitää generated-data synkassa
- varmistaa että blueprint, manifestit, linkkikartat, extractit ja packetit perustuvat samaan nykytilaan
- helpottaa tilanteita, joissa julkinen kuulu.fi tai dokumentaatiolähteet muuttuvat ennen varsinaista HubSpot-fetchiä

---

## Yksi komento

Aja:

```bash
bash scripts/refresh_preauth_artifacts.sh
```

Tämä suorittaa koko pre-auth-pipelinein järjestyksessä.

---

## Mitä skripti päivittää

### 1. Public inventory

- `docs/generated/kuulu-public-site-inventory.csv`
- `docs/generated/kuulu-public-site-inventory.json`

### 2. V2-manifestit

- `docs/generated/kuulu-v2-page-manifest.json`
- `docs/generated/kuulu-v2-module-manifest.json`

Sekä validoi ne:

- `scripts/validate_v2_manifests.py`

### 3. Cutover- ja redirect-rekisterit

- `docs/generated/kuulu-redirect-register.json`
- `docs/generated/kuulu-cutover-checklist.json`
- `docs/generated/kuulu-v2-implementation-status.json`

### 4. Public asset signature

- `docs/generated/kuulu-public-asset-signature.json`
- `docs/generated/kuulu-public-asset-signature.md`

### 5. Public CMS metadata

- `docs/generated/kuulu-public-cms-metadata.json`
- `docs/generated/kuulu-public-cms-metadata.md`

### 6. First-wave sisältöpackit

- `docs/generated/kuulu-first-wave-content-packs.json`
- `docs/generated/kuulu-first-wave-hs-data.json`

### 7. Source extractit

- `docs/generated/kuulu-first-wave-source-extracts.json`
- `docs/generated/kuulu-first-wave-source-extracts.md`
- `docs/generated/kuulu-all-source-extracts.json`
- `docs/generated/kuulu-all-source-extracts.md`

### 8. Linkkikartat

- `docs/generated/kuulu-first-wave-link-map.json`
- `docs/generated/kuulu-first-wave-link-map.md`
- `docs/generated/kuulu-full-link-graph.json`
- `docs/generated/kuulu-full-link-graph.md`

### 9. Build packetit

- `docs/generated/first-wave-page-build-packets/`
- `docs/generated/all-page-build-packets/`

### 10. Blueprint

- `hubspot/kuulu-theme-v2-blueprint/`

sekä blueprint-validaatio:

- `scripts/validate_blueprint_scaffold.py`

---

## Milloin tämä kannattaa ajaa

Suositus:

- aina ennen uuden ison dokumentaatiomuutoksen commitointia
- kun julkinen kuulu.fi on muuttunut
- kun build packetit tai manifestit tuntuvat olevan epäsynkassa
- juuri ennen kuin auth / fetch -vaihe alkaa, jotta lähdedata on tuore

---

## Mitä tämä EI tee

Skripti ei:

- tee HubSpot-authia
- fetchaa source themeä
- muuta mitään remote HubSpotissa
- käytä `hs cms watch`- tai `hs cms upload` -komentoja

Se on turvallinen ajaa ennen authia, koska se käyttää vain julkista sivustoa ja paikallista repo-dataa.

---

## Yhteenveto

Tämä skripti on projektin “päivitä kaikki suunnittelu- ja scaffold-artefaktit” -komento.

Se auttaa pitämään tämän säännön totena:

> jos HubSpot-pääsyä ei vielä ole, paikallisen valmisteludatan pitää silti pysyä yhtenäisenä ja toistettavana.
