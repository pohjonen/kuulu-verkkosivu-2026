# HubSpot-työhakemisto

Tämä hakemisto on varattu Kuulun HubSpot-v2-toteutuksen turvalliseen rinnakkaisrakentamiseen.

## Tavoite

Tänne tuodaan vasta autentikoinnin jälkeen:

- nykyisen teeman export
- siitä tehty v2-klooni
- mahdolliset preview-/watch-polut

## Suositeltu rakenne

```text
hubspot/
  README.md
  source-theme/
  kuulu-theme-v2/
  exports/
```

### `source-theme/`

Nykyinen HubSpotista haettu teema sellaisenaan. Tätä ei muokata.

### `kuulu-theme-v2/`

Nykyisestä teemasta tehty erillinen v2-kopio. Kaikki uusi työ tehdään tähän.

### `exports/`

Väliaikaiset fetch-exportit, jos niitä tarvitaan auditointiin tai vertailuun.

## Turvallisuussääntö

`source-theme/` toimii vertailupisteenä. Kaikki varsinainen kehitys tapahtuu `kuulu-theme-v2/`-hakemistossa, jotta nykyisen live-rakenteen ylikirjoittamisen riski pienenee.

## Bootstrap authin jälkeen

Kun HubSpot-auth on tehty onnistuneesti, etenemisjärjestys on tämä:

1. aja `hs doctor` ja tallenna diagnostiikka
2. varmista oikea account `hs account list` + `hs account info`
3. tee tarvittaessa paikallinen override:
   - `hs account create-override <account>`
4. hae nykyinen teema aina ensin `source-theme/`-hakemistoon
5. tee v2-klooni vasta tämän jälkeen erilliseen `kuulu-theme-v2/`-hakemistoon
6. käytä watch/upload-työtä vain v2-kohteeseen, ei koskaan lähdeteemaan

Suositellut helperit:

- `scripts/hubspot_fetch_current_theme.sh`
- `scripts/hubspot_clone_v2_theme.sh`
- `scripts/hubspot_watch_v2.sh`
