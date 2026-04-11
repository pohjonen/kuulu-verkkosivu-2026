# START HERE

Tämä tiedosto on nopein tapa hahmottaa, missä projektissa mennään ja mitä pitää tehdä seuraavaksi.

## 1. Mitä tässä repoossa on tehty

Repo sisältää jo valmiiksi:

- julkisen kuulu.fi:n ei-blogi-inventaarion
- modulaarisen v2-rakennesuunnitelman
- ensimmäisen aallon ja koko sivuston build-packetit
- linkkikartat ja redirect-/cutover-rekisterit
- HubSpot auth/fetch/clone/watch helperit
- paikallisen `kuulu-theme-v2-blueprint`-rungon

## 2. Suurin blocker juuri nyt

Projektin seuraava oikea askel vaatii toisen näistä:

1. `hs account auth`
   **tai**
2. nykyisen HubSpot-teeman export workspaceen

Ilman tätä repo pystyy tuottamaan vain valmisteludataa, ei vielä oikeaa HubSpot-v2-toteutusta source themen päälle.

## 3. Jos haluat vain tarkistaa tilanteen nopeasti

Katso:

- `docs/generated/kuulu-preauth-status-index.md`

Se näyttää nopeasti:

- auth-statuksen
- source-theme-statuksen
- inventaarion laajuuden
- packetien määrät
- seuraavan blocker-kohdan

## 4. Jos haluat päivittää kaiken generated-datan

Aja:

```bash
bash scripts/refresh_preauth_artifacts.sh
```

Tämä:

- regeneroi kaikki keskeiset JSON/CSV/MD-artefaktit
- validoi blueprintin
- validoi pre-auth artefaktien konsistenssin

## 5. Jos haluat käynnistää HubSpot-authin

Aja:

```bash
bash scripts/start_hubspot_auth.sh
```

Tai suoraan:

```bash
hs account auth
```

Kun auth on tehty, seuraava polku on:

1. `bash scripts/hubspot_bootstrap_status.sh`
2. `bash scripts/hubspot_fetch_current_theme.sh "<REMOTE_THEME_PATH>"`
3. `bash scripts/run_post_auth_audit.sh hubspot/source-theme`

## 6. Mitä tiedostoja kannattaa lukea missäkin tilanteessa

### Strateginen ymmärrys

- `docs/kuulu-content-principles.md`
- `docs/kuulu-migration-matrix.md`
- `docs/kuulu-first-wave-content-packs.md`

### Modulaarinen rakenne

- `docs/kuulu-module-field-model.md`
- `docs/kuulu-module-build-order.md`
- `docs/kuulu-first-wave-section-stacks.md`
- `docs/hubspot-module-hubl-mapping.md`

### HubSpot-rakenne ja turvallinen build

- `docs/hubspot-v2-structure-model.md`
- `docs/hubspot-theme-v2-build-map.md`
- `docs/hubspot-theme-token-map.md`
- `docs/hubspot-auth-bootstrap.md`
- `docs/hubspot-post-auth-handoff.md`

### Julkaisu ja linkkiturva

- `docs/kuulu-redirect-and-slug-register.md`
- `docs/kuulu-cutover-checklist.md`
- `docs/hubspot-link-map-usage.md`
- `docs/hubspot-link-graph-usage.md`

## 7. Missä generated-data sijaitsee

Kaikki koneellisesti tuotettu data löytyy:

- `docs/generated/`

Tärkeimmät alaryhmät:

- `kuulu-public-site-inventory.*`
- `kuulu-v2-*.json`
- `kuulu-*-source-extracts.*`
- `first-wave-page-build-packets/`
- `all-page-build-packets/`
- `kuulu-preauth-status-index.*`

## 8. Paikallinen blueprint

Paikallinen v2-blueprint on täällä:

- `hubspot/kuulu-theme-v2-blueprint/`

Tämä EI ole vielä oikea production-teema, vaan turvallinen scaffold:

- templatet
- moduulit
- fields/meta-rungot
- token/base assetit
- header/footer/navigation/global scaffoldit

## 9. Tärkein käytännön sääntö

Nykyiseen live-teemaan tai etusivuun ei kosketa ennen kuin:

- auth on tehty
- source theme on fetchattu
- audit on tehty
- v2-haara on erotettu
- preview-sivut ovat valmiit

## 10. Yhden lauseen yhteenveto

Repo on nyt erittäin pitkälle viety turvallinen valmistelupaketti, mutta seuraava oikea iso loikka on vasta silloin kun saadaan pääsy oikeaan HubSpot-source-themeen.
