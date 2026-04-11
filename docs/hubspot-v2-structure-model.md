# HubSpot v2 -rakenne ilman staging-ominaisuutta

## Tavoite

Rakennetaan uusi Kuulu-verkkosivun kokonaisuus **ilman HubSpotin varsinaista staging-featurea** niin, että:

- nykyinen live-sivusto pysyy täysin koskemattomana
- nykyinen etusivu ei voi rikkoutua vahingossa
- kaikki uusi rakennetaan saman teeman sisään mutta **versionoituna**
- koko v2 voidaan testata valmiiksi ennen live-cutoveria

Tämä dokumentti määrittää turvallisen “pseudo-staging” -mallin HubSpotiin.

---

## Pääperiaate

> Jos muutos voi vaikuttaa nykyiseen live-etusivuun tai muihin tuotantosivuihin, sitä ei tehdä shared-rakenteeseen suoraan.

Sen sijaan tehdään:

1. **teemakopio**
2. **versionoidut moduulit**
3. **versionoidut templaatit**
4. **rinnakkaiset draft-/testisivut**
5. **hallittu cutover vasta lopussa**

---

## 1. Mikä kloonataan

### 1.1 Kloonattava kokonaisuus

Lähtökohtaisesti kloonataan nykyisestä teemapohjasta uusi v2-haara:

- nykyinen teema → `kuulu-theme-v2`

Jos täydellinen teemakopio ei ole järkevä tai mahdollista, vähimmäistaso on:

- versionoidut templaatit
- versionoidut moduulit
- versionoidut global partialit

### 1.2 Mitä EI pidä käyttää suoraan, jos se voi osua liveen

Näitä ei pidä muokata suoraan ilman varmaa eristystä:

- nykyinen etusivun template
- nykyiset live-moduulit, joita etusivu käyttää
- nykyinen header
- nykyinen footer
- shared CSS/JS, jos sama asset ladataan liveen
- shared global groupit

Jos jokin näistä pitää muuttaa, tehdään siitä v2-versio.

---

## 2. Versionointimalli

### 2.1 Teema

Suositus:

- `kuulu-theme-v2`

Jos teemanimeä ei voi tai haluta kloonata näin, käytetään muuta selvää nimikonventiota, mutta tärkeintä on erottaa live ja v2 selvästi.

### 2.2 Templaatit

Esimerkkimalli:

- `homepage-v2`
- `service-landing-v2`
- `training-landing-v2`
- `reference-index-v2`
- `reference-detail-v2`
- `company-info-v2`
- `person-profile-v2`
- `legal-v2`

### 2.3 Moduulit

Esimerkkimalli:

- `hero-cinematic-v2`
- `problem-grid-v2`
- `audience-split-v2`
- `service-pillars-v2`
- `video-model-comparison-v2`
- `training-agenda-v2`
- `reference-grid-v2`
- `final-cta-v2`

### 2.4 Globaalit rakenteet

Jos header/footer tai muut globaalit osat tarvitsevat muutoksia:

- `header-v2`
- `footer-v2`
- `navigation-v2`

Tärkeä sääntö:

> V2-headeriä tai V2-footeria ei kytketä liveen ennen cutover-hetkeä.

---

## 3. Testisivujen rakenne ilman stagingiä

Koska varsinaista staging-domainia ei ehkä ole, rakennetaan rinnakkaiset testisivut HubSpotin sisään.

### 3.1 Sivujen nimeäminen

Suositus:

- `v2-etusivu`
- `v2-digimarkkinointi`
- `v2-videotuotanto`
- `v2-koulutus`
- `v2-case-studies`

Tai turvallisempi malli:

- `preview-etusivu-2026`
- `preview-digimarkkinointi-2026`
- `preview-videotuotanto-2026`

### 3.2 Slug-periaate

Rakennusvaiheessa **ei käytetä tuotantoslugeja** kuten:

- `/`
- `/digimarkkinointi`
- `/videotuotanto`

Vaan väliaikaisia rinnakkaisslugeja kuten:

- `/v2-etusivu`
- `/v2-digimarkkinointi`
- `/v2-videotuotanto`

### 3.3 Näkyvyys

Testisivut pidetään pois näkyvästä tuotantokäytöstä:

- ei lisätä päävalikkoon
- ei lisätä footeriin
- ei lisätä sisäisiin tuotantolinkityksiin
- asetetaan `noindex`
- jätetään pois sitemapista, jos mahdollista
- tarvittaessa käytetään sivukohtaista salasanasuojausta

---

## 4. Mitä rakennetaan missä järjestyksessä

### Vaihe A - turvallinen perusta

1. kopioidaan teema tai rakennetaan v2-haara
2. luodaan v2-tokenit, fontit ja brand-säännöt
3. luodaan v2-moduulit
4. luodaan v2-templatet

### Vaihe B - sivut rinnalle

Rakennetaan preview-sivut tällä järjestyksellä:

1. etusivu-v2
2. palvelusivut-v2
3. videopalvelusivut-v2
4. koulutussivut-v2
5. referenssi-indeksi-v2
6. referenssidetailit-v2
7. yhteystiedot / infosivut-v2
8. henkilöprofiilit-v2

### Vaihe C - testaus

Jokaisesta sivusta tarkistetaan:

- sisältö
- flow
- CTA:t
- linkit
- forms
- navigaatio
- mobiili
- editorimuokattavuus
- ettei mikään live-sivu ole muuttunut

---

## 5. Etusivun erityissuojaus

Koska nykyinen etusivu on korkein riskikohde, sille pitää noudattaa erillistä suojausmallia.

### 5.1 Mitä EI tehdä

Ei:

- muokata nykyistä etusivun templatea suoraan
- muokata nykyisen etusivun käyttämiä moduuleja suoraan
- muuttaa nykyisen etusivun headeria/footeria shared-tasolla
- päivittää etusivun assetteja “varovasti” samaan tiedostoon

### 5.2 Mitä tehdään sen sijaan

Tehdään:

- uusi homepage-v2 template
- uudet etusivun moduulit tai versionoidut moduulit
- erillinen preview-etusivu
- tarvittaessa erillinen header-v2 ja footer-v2

### 5.3 Julkaisusääntö

Nykyinen etusivu saa vaihtua vasta kun:

- kaikki muut v2-rakenteet on testattu
- etusivun kaikki CTA:t, navigation-linkit ja forms on validoitu
- on olemassa rollback-polku takaisin vanhaan etusivuun

---

## 6. Globaalien osien turvallinen käsittely

### 6.1 Header

Jos uusi sivusto tarvitsee eri navigaation tai uuden CTA-logiikan:

- tehdään `header-v2`
- käytetään sitä vain v2-sivuilla

### 6.2 Footer

Jos footer muuttuu:

- tehdään `footer-v2`
- käytetään sitä vain v2-sivuilla

### 6.3 Shared CSS / JS

Suositus:

- v2:lle omat assetit
- ei päivitetä live-assetteja päälle

Esim:

- `theme-v2.css`
- `modules-v2.css`
- `theme-v2.js`

---

## 7. Navigaatio ilman live-riskiä

### Rakennusvaiheessa

V2-sivuja ei linkitetä live-navigaation kautta.

Niitä voidaan testata:

- suorilla linkeillä
- testilistauksella
- väliaikaisella sisäisellä preview-sivulla

### Juuri ennen cutoveria

Vasta viimeisessä vaiheessa päätetään:

- vaihtuuko koko päävalikko samalla
- vai pidetäänkö vanha valikko kunnes kaikki uudet sivut ovat live

---

## 8. Cutover-malli

### Vaihtoehto A - koko paketti kerralla

Sopii, jos:

- paljon yhteisiä riippuvuuksia
- koko sivusto halutaan yhtenäisenä kerralla

Vaiheet:

1. final QA
2. live-slugeihin siirto
3. navigation/footer/live-linkitykset käyttöön
4. smoke test heti

### Vaihtoehto B - sivutyyppi kerrallaan

Sopii, jos:

- halutaan minimoida julkaisuhetken riskiä
- sivutyypit ovat riittävän irrallisia

Mahdollinen järjestys:

1. videopalvelusivut
2. koulutussivut
3. palvelusivut
4. referenssit
5. yhteystiedot
6. etusivu viimeisenä

### Suositus Kuululle

Koska etusivu on korkein riskikohde, turvallisin malli on yleensä:

- ensin alasivut valmiiksi
- etusivu viimeisenä

---

## 9. Rollback-malli

Jokaiselle liveen vietävälle sivulle pitää tietää:

- mikä oli vanha template
- mikä oli vanha sivu
- mikä oli vanha slug
- mitä globaaleja osia se käytti

Rollbackin pitää onnistua nopeasti:

1. vanha template takaisin käyttöön
2. vanhat linkit / navigaatio takaisin
3. uudet globaalit osat pois käytöstä

### Erityissääntö

Etusivulle pitää olla oma rollback-polku dokumentoituna ennen cutoveria.

---

## 10. Checklist ennen kuin yksikään tuotantosivu vaihtuu

- [ ] v2-teema tai selkeästi versionoidut rakenteet olemassa
- [ ] etusivu-v2 rakennettu ilman että live-etusivu muuttui
- [ ] kaikki uudet moduulit editoritestattu
- [ ] kaikki preview-sivut tarkistettu mobiilissa
- [ ] kaikki CTA:t tarkistettu
- [ ] kaikki forms tarkistettu
- [ ] kaikki sisäiset linkit tarkistettu
- [ ] noindex / näkyvyyden hallinta kunnossa preview-sivuilla
- [ ] rollback-polku dokumentoitu
- [ ] päätetty julkaistaanko kaikki kerralla vai vaiheittain

---

## 11. Yhteenveto

HubSpotin varsinaisen staging-featuren puuttuminen ei ole este turvalliselle toteutukselle.

Turvallinen malli on:

1. **erillinen v2-teema tai versionoitu rakenne**
2. **erilliset v2-moduulit**
3. **erilliset v2-templatet**
4. **rinnakkaiset preview-sivut väliaikaisilla slugeilla**
5. **ei linkitystä liveen ennen hyväksyntää**
6. **hallittu cutover vasta lopussa**

Tällä mallilla uusi kokonaisuus voidaan rakentaa valmiiksi ilman, että nykyinen pääsivusto tai etusivu on vaarassa rikkoutua.
