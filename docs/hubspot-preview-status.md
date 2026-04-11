# HubSpot v2 preview -tilanne

## Yhteenveto

Turvallinen remote-v2-polku on nyt luotu HubSpotiin:

- `kuulu-theme-v2-preview`

Paikallinen v2-teema on uploadattu tähän remote-polkuun `watch`-prosessilla ilman, että nykyiseen live-teemaan tai etusivuun koskettiin.

## Mitä onnistui

### 1. Eristetty remote-v2-polku

Watch/upload kohdistettiin erilliseen kohteeseen:

- `kuulu-theme-v2-preview`

Tämä on erillään nykyisestä source-themestä ja nykyisestä live-etusivusta.

### 2. Paikallinen v2-klooni uploadattiin

Paikallinen lähde:

- `hubspot/kuulu-theme-v2/`

Uploadissa näkyi onnistuneita tiedostosiirtoja mm:

- `hero-cinematic-v2.module`
- `problem-grid-v2.module`
- `service-pillars-v2.module`
- `stats-trust-band-v2.module`
- `lead-capture-form-cta-v2.module`
- `homepage-v2.html`
- `base-cinematic-v2.html`
- `header-cinematic-v2.html`
- `footer-cinematic-v2.html`

### 3. Remote-listaus vahvistaa uploadin

Remote-listauksessa näkyvät nyt mm:

- `hero-cinematic-v2.module`
- `problem-grid-v2.module`
- `service-pillars-v2.module`
- `stats-trust-band-v2.module`
- `lead-capture-form-cta-v2.module`
- `homepage-v2.html`

## Mikä estää varsinaisen selaimessa avattavan previewn juuri nyt

Kun yritettiin käynnistää:

```bash
hs cms theme preview --src "/workspace/hubspot/kuulu-theme-v2" --dest "kuulu-theme-v2-preview" --port 4010
```

saatiin HubSpot API:lta 403 / missing scopes -virhe.

Keskeinen syy:

- nykyisellä access tokenilla ei ole kaikkia `cms-dev-server`-previewn vaatimia scopeja
- virhe tuli endpointtiin:
  - `cms/v3/functions/secrets`

Tämä tarkoittaa:

> Upload toimii, mutta HubSpotin oma paikallinen theme preview -serveri ei käynnisty tällä tokenilla.

## Tärkeä turvallisuushuomio

Tämä ei rikkonut liveä.

- live-teemaa ei muutettu
- nykyistä etusivua ei vaihdettu
- preview-polku on erillinen
- epäonnistuminen koski vain preview-serverin käynnistystä, ei tuotantoa

## Turvallinen fallback juuri nyt

Koska remote-v2-polku on olemassa ja upload on onnistunut, turvallisin jatkopolku on:

1. jatkaa v2-teeman paikallista rakentamista `hubspot/kuulu-theme-v2/`
2. käyttää remote-v2-polun listauksia varmistamaan, että tiedostot menevät oikeaan paikkaan
3. tarvittaessa käyttää muuta selaimessa katsottavaa polkua myöhemmin (esim. HubSpotin UI:n kautta, jos oikea preview-/testisivu luodaan)
4. pyytää tarvittavat lisäscopet, jos halutaan käyttää `hs cms theme preview` -toimintoa loppuun asti

## Paikallinen fallback-preview

Tällä hetkellä on käynnissä turvallinen paikallinen tiedostopohjainen preview-palvelin:

- `http://127.0.0.1:4020/`

Se palvelee hakemistoa:

- `hubspot/kuulu-theme-v2/`

Tämä EI renderöi HubL:ää oikeana HubSpot-sivuna, mutta sillä voi:

- selata paikallista teemarakennetta
- tarkistaa että v2-kloonin tiedostot ovat olemassa
- avata template- ja moduulitiedostoja nopeasti selaimessa

Sitä ei pidä sekoittaa oikeaan HubSpot preview -renderöintiin.

## Suora johtopäätös

Nykytila on:

- **upload turvalliseen v2-preview-polkuun toimii**
- **HubSpotin theme preview -serveri ei toimi nykyisillä scopeilla**

Eli v2-esikatselun seuraava käytännön askel on:

- joko lisäscopet preview-serverille
- tai remote-v2-polun päälle rakennettava UI-pohjainen preview/testisivu HubSpotissa
