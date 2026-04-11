# Kuulu: URL-inventaario ja migraatiomatriisi

## Tarkoitus

Tämä dokumentti kokoaa yhteen:

- nykyiset julkiset ei-blogi-URL:t
- sivutyypit
- ensisijaiset sisältölähteet
- suositellut v2-templatet
- turvalliset preview-slugit

Tämä toimii siltana nykyisen julkisen sivuston, Notion-luonnosten, brand bookin ja tulevan HubSpot v2 -rakenteen välillä.

## Generoitu inventaario

Ajantasainen koneellisesti tuotettu inventaario löytyy tiedostoista:

- `docs/generated/kuulu-public-site-inventory.csv`
- `docs/generated/kuulu-public-site-inventory.json`

Generoiva skripti:

- `scripts/kuulu_public_audit.py`

## Lähdeprioriteetin periaate

### `live + notion + pdf`

Käytetään kun:

- nykyinen live-sivu sisältää olennaista rakennetta tai toiminnallisuutta
- Notionissa on jo uusi ehdotus tai merkittävä copyluonnos
- Zero Click -kasvukoneisto tuo sisältöön strategisen rungon

### `live + pdf`

Käytetään kun:

- Notionissa ei ole valmista ehdotusta
- mutta sivu pitää kytkeä selkeästi kasvukoneiston logiikkaan

### `live + brand`

Käytetään kun:

- sivu on enemmän visuaalisen / rakenteellisen yhtenäistämisen kohde
- strateginen sisältöydin tulee pääosin live-sivusta ja brandiohjeesta

### `live`

Käytetään kun:

- sivu on ensisijaisesti säilytettävä / normalisoitava
- eikä sille ole vielä vahvaa vaihtoehtoista sisältölähdettä

## Sivutyyppikohtainen template-kartta

| Sivutyyppi | V2-template | Rooli |
| --- | --- | --- |
| homepage | `homepage-v2` | Master-sivu: Zero Click, Brand DNA, Sisältökoneisto, Liidimoottori |
| service | `service-landing-v2` | Yhden pullonkaulan tai ratkaisun avaaminen |
| video-service | `video-service-landing-v2` | Kuvattu / hybridi / AI-tehostettu tuotanto |
| training | `training-landing-v2` | Osaamisvaje, agenda, käytännön hyöty |
| reference-index | `reference-index-v2` | Caset löydettäväksi ja vertailtavaksi |
| reference-detail | `reference-detail-v2` | Haaste → ratkaisu → tulokset |
| company-info | `company-info-v2` | Yhteys, ihmiset, toimistot, luottamus |
| person-profile | `person-profile-v2` | Asiantuntija + CTA ilman blogifeediä |
| legal | `legal-v2` | Kevyt juridinen sivu |

## Korkean prioriteetin ensimmäinen aalto

Nämä sivut kannattaa rakentaa ensimmäisessä v2-aallossa, koska ne muodostavat rungon koko sivuston suunnalle:

1. `/`
2. `/videotuotanto`
3. `/koulutus`
4. `/digimarkkinointi`
5. `/case-studies`
6. `/yhteystiedot`

Perustelu:

- ne määrittävät suurimman osan shared-moduulitarpeista
- niihin on jo osin Notion-lähteitä
- ne luovat rungon myöhemmille palvelu-, training- ja case-sivuille

## Erityishuomiot

### 1. Etusivu

- korkein regressioriski
- rakennetaan aina erillisenä `homepage-v2` + preview-sivuna
- ei suoraa muutosta nykyiseen etusivuun

### 2. Videotuotanto

- vahvin yksittäinen uusi sisältölähde löytyy Notionista
- pitää olla mallisivu koko captured / hybrid / AI-jaolle

### 3. Koulutus

- Notionissa jo valmis hyvä uudistusehdotus
- pitää kytkeä osaamisvajeeseen, ei pelkkään kurssilistaan

### 4. Henkilösivut

- nykyinen blogiriippuvuus purettava
- v2-sivuilla henkilöt toimivat luottamuksen rakentajina, eivät blogiarkistoina

### 5. Referenssit

- useita eri URL-rakenteita
- URL:t säilytetään, vaikka rakenne yhtenäistetään v2-templateen

## Käytännön käyttö toteutusvaiheessa

Kun teema on saatavilla:

1. ajetaan `scripts/kuulu_public_audit.py`
2. verrataan generoitu inventaario liveen
3. päätetään ensimmäisen aallon sivut
4. rakennetaan niitä vastaavat v2-moduulit ja v2-templatet
5. tehdään preview-sivut tämän matriisin mukaisilla väliaikaisilla slugeilla

## Nykyinen status

Tällä hetkellä matriisi on valmis suunnittelun tueksi, mutta HubSpot-teeman varsinainen auditointi odottaa vielä:

- `hs account auth` -autentikointia, tai
- teeman exportia / repoa workspaceen
