# Kuulu v2: redirect- ja slug-päätösrekisteri

## Tarkoitus

Tämä dokumentti määrittää jokaiselle nykyiselle ei-blogi-URL:lle turvallisen päätöksen:

- säilytetäänkö slug ennallaan
- julkaistaanko uusi v2 samaan slugiin cutover-hetkellä
- säilytetäänkö vanha URL rinnalla
- tarvitaanko redirect
- missä kohtaa julkaisujärjestystä sivu kuuluu

Pääperiaate:

> Nykyistä slugia ei muuteta kevyesti. Redirect tehdään vain, jos siihen on selkeä rakenne- tai sisältösyy.

---

## Päätösluokat

### 1. `replace-in-place`

Nykyinen URL säilytetään.

Käytetään kun:

- URL on toimiva
- sillä on arvoa hakunäkyvyydessä tai sisäisessä linkityksessä
- v2-sivu voidaan julkaista turvallisesti samaan osoitteeseen cutoverissa

Tämä on oletusratkaisu suurimmalle osalle sivuista.

### 2. `keep-and-normalize`

Nykyinen URL säilytetään, mutta sivun rakenne normalisoidaan v2-templateen.

Käytetään kun:

- sisältö säilyy pitkälti samana
- ulkoasu ja rakenne halutaan yhtenäistää
- redirectiin ei ole tarvetta

### 3. `keep-separate-for-now`

Nykyinen URL pidetään erillisenä myös v2:ssa.

Käytetään kun:

- sivulla on oma toimituksellinen tai liiketoiminnallinen roolinsa
- sitä ei kannata yhdistää toiseen sivuun ensimmäisessä aallossa

### 4. `decide-later`

Ei tehdä redirect-päätöstä ennen kuin:

- HubSpotin nykyinen teema on auditoitu
- liikenne, sisäiset linkit ja mahdolliset konversiot on tarkistettu

Tätä käytetään vain poikkeustapauksiin.

---

## Ensimmäisen aallon slug-päätökset

| Nykyinen URL | V2-preview | Julkaisupäätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/` | `/v2-etusivu` | `replace-in-place` | Ei | Korkein riskikohde. Vaihdetaan viimeisenä. |
| `/videotuotanto` | `/v2-videotuotanto` | `replace-in-place` | Ei | Mallisivu captured/hybrid/AI-logiikalle. |
| `/koulutus` | `/v2-koulutus` | `replace-in-place` | Ei | Notion-ehdotus jo olemassa. |
| `/digimarkkinointi` | `/v2-digimarkkinointi` | `replace-in-place` | Ei | Tärkeä ydinpalvelusivu. |
| `/case-studies` | `/v2-case-studies` | `replace-in-place` | Ei | Pääreferenssi-indeksi. |
| `/yhteystiedot` | `/v2-yhteystiedot` | `replace-in-place` | Ei | Korkean luottamuksen konversiosivu. |

---

## Kaikki nykyiset ei-blogi-URL:t

### Homepage

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/` | `/v2-etusivu` | `replace-in-place` | Ei | Vaihdetaan viimeisenä. |

### Koulutus / landing

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/koulutus` | `/v2-koulutus` | `replace-in-place` | Ei | Ensimmäinen aalto. |
| `/tekoalyn-mestarikurssi` | `/v2-tekoalyn-mestarikurssi` | `keep-and-normalize` | Ei | Säilytetään oma landing. |
| `/tekoalyn-perjantaipulssi` | `/v2-tekoalyn-perjantaipulssi` | `keep-and-normalize` | Ei | Toistuva koulutus. |
| `/zero-click-ajan-digimarkkinointi` | `/v2-zero-click-ajan-digimarkkinointi` | `keep-and-normalize` | Ei | Strateginen ankkurisivu. |
| `/tekoaly-markkinoinnin-ja-myynnin-tukena` | `/v2-tekoaly-markkinoinnin-ja-myynnin-tukena` | `keep-and-normalize` | Ei | AI-koulutuksen tärkeä sivu. |
| `/projektinhallinta-tekoalylla-perjantaipulssi-17.4.2026-kuulu` | `/v2-projektinhallinta-tekoalylla-perjantaipulssi` | `keep-separate-for-now` | Ei | Kampanjasivu, voidaan myöhemmin arkistoida. |

### Palvelusivut

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/digimarkkinointi` | `/v2-digimarkkinointi` | `replace-in-place` | Ei | Ensimmäinen aalto. |
| `/energia-alan-markkinointi` | `/v2-energia-alan-markkinointi` | `keep-and-normalize` | Ei | Vertikaalisivu säilytetään. |
| `/someagentti-eli-somekanavien-auditointi` | `/v2-someauditointi` | `keep-and-normalize` | Ei | Auditointisivu säilyy. |
| `/google-ads-mainonta` | `/v2-google-ads-mainonta` | `keep-and-normalize` | Ei | Demand capture -sivu säilyy. |

### Videopalvelusivut

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/videotuotanto` | `/v2-videotuotanto` | `replace-in-place` | Ei | Ensimmäinen aalto. |
| `/brandivideo` | `/v2-brandivideo` | `keep-and-normalize` | Ei | Premium captured -kulma. |
| `/tv-mainos-tuotanto` | `/v2-tv-mainos-tuotanto` | `keep-and-normalize` | Ei | Jo lähellä uutta tyyliä. |
| `/videotuotanto_vanha` | `/v2-videotuotanto-vanha` | `decide-later` | Mahdollinen | Selvitetään liikenne ja sisäiset linkit ennen päätöstä. |

### Referenssi-indeksit

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/case-studies` | `/v2-case-studies` | `replace-in-place` | Ei | Ensimmäinen aalto. |
| `/asiakasreferenssit` | `/v2-asiakasreferenssit` | `keep-separate-for-now` | Ei | Voi jäädä omaksi toimitukselliseksi näkymäksi. |

### Yritys- / infosivut

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/yhteystiedot` | `/v2-yhteystiedot` | `replace-in-place` | Ei | Ensimmäinen aalto. |
| `/tietosuojaseloste` | `/v2-tietosuojaseloste` | `keep-and-normalize` | Ei | Ei ylioverdesignia. |

### Henkilösivut

| Nykyinen URL | V2-preview | Päätös | Redirect | Huomio |
| --- | --- | --- | --- | --- |
| `/ihmiset/jonna-muurinen` | `/v2-ihmiset-jonna-muurinen` | `keep-and-normalize` | Ei | Poistetaan blogiriippuvuus. |
| `/ihmiset/ville-pohjonen` | `/v2-ihmiset-ville-pohjonen` | `keep-and-normalize` | Ei | Poistetaan blogiriippuvuus. |

### Referenssidetailit

Kaikille referenssidetail-URL:ille oletus on:

- päätös: `keep-and-normalize`
- redirect: Ei

Perustelu:

- URL-rakenne on jo olemassa
- caseilla voi olla ulkoisia linkkejä ja hakunäkyvyyttä
- rakenteen yhtenäistäminen tehdään `reference-detail-v2`-templateen ilman URL-muutoksia

Poikkeuksista päätetään vasta teema-auditin ja liikennedatan jälkeen.

---

## Redirect-päätöksen säännöt

Redirect harkitaan vasta jos kaikki nämä täyttyvät:

1. uusi rakenne ratkaisee selkeän sisällöllisen tai rakenteellisen ongelman
2. vanha URL ei ole kriittinen nykyiselle sisäiselle linkitykselle
3. redirect voidaan dokumentoida ja testata
4. redirect ei lisää etusivun tai navigaation regressioriskiä

Muussa tapauksessa slug säilytetään.

---

## Päätösten tarkistuspisteet

Seuraavissa kohdissa rekisteri tarkistetaan uudelleen:

1. kun HubSpot-teema on auditoitu
2. kun sisäiset linkit on kartoitettu tarkemmin
3. kun ensimmäisen aallon preview-sivut ovat valmiit
4. juuri ennen cutoveria

---

## Yhteenveto

Nykyisten URL:ien oletuskohtelu on:

- **säilytä**
- **normalisoi rakenne**
- **älä redirectaa ilman vahvaa syytä**

Tämä tukee käyttäjän tärkeintä vaatimusta:

> linkityksiä ei rikota eikä tuotannossa tehdä turhia riskejä.
