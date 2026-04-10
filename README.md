# kuulu-verkkosivu-2026

Valmistelurepo Kuulu.fi:n ei-blogi-sivuston turvalliseen HubSpot-v2-uudelleenrakennukseen.

## Nykytila

Tämä repo sisältää nyt:

- sivustoinventaarion
- Zero Click -sisältörungon
- modulaarisen v2-arkkitehtuurin
- turvallisen pseudo-staging / cutover-ajattelun
- koneellisesti generoidut manifestit, packetit ja linkkikartat
- paikallisen `kuulu-theme-v2-blueprint`-rungon
- HubSpot CLI -bootstrap-, fetch-, audit- ja watch-helperit

Suurin nykyinen blocker on edelleen:

1. `hs account auth`
   **tai**
2. nykyisen HubSpot-teeman export / repo tähän workspaceen

Vasta tämän jälkeen voidaan siirtyä oikeaan source-theme fetch → audit → clone → build -vaiheeseen.

## Aloita tästä

Lue ensin:

- `docs/START_HERE.md`

Se kertoo:

- mitä tiedostoja repo sisältää
- missä järjestyksessä niitä kannattaa käyttää
- mitkä komennot ajetaan ennen authia
- mitkä komennot ajetaan authin jälkeen

## Tärkeimmät komennot

### Päivitä kaikki pre-auth artefaktit

```bash
bash scripts/refresh_preauth_artifacts.sh
```

### Tarkista HubSpot-bootstrapin tila

```bash
bash scripts/hubspot_bootstrap_status.sh
```

### Käynnistä auth

```bash
bash scripts/start_hubspot_auth.sh
```

### Kun auth on valmis: fetchaa source theme

```bash
bash scripts/hubspot_fetch_current_theme.sh "<REMOTE_THEME_PATH>"
```

### Kun source theme on fetchattu: aja post-auth audit

```bash
bash scripts/run_post_auth_audit.sh hubspot/source-theme
```

## Hakemistorakenne

### `docs/`

Sisältää ihmisluettavan suunnittelu- ja toteutushallinnan dokumentaation:

- sisältöperiaatteet
- moduulilogikan
- section stackit
- cutover- ja redirect-ajattelun
- auth/bootstrap-ohjeet
- build mapit

### `docs/generated/`

Sisältää koneellisesti luettavat artefaktit:

- inventoryt
- manifestit
- linkkigraafit
- packetit
- source extractit
- status-koosteet

### `scripts/`

Sisältää generaattorit, validaattorit ja HubSpot-helperit.

### `hubspot/`

Sisältää paikallisen HubSpot-työrakenteen:

- blueprintin
- myöhemmin fetchatun `source-theme/`
- myöhemmin oikean `kuulu-theme-v2/`

## Turvasääntö

Nykyiseen live-teemaan tai nykyiseen etusivuun ei kosketa ennen kuin:

- source theme on fetchattu
- audit on tehty
- v2-haara on erotettu
- preview-sivut on rakennettu
- cutover on erikseen hyväksytty
