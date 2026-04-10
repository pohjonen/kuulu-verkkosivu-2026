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
