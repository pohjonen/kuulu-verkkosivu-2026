# Kuulu v2: cutover-checklist ilman staging-featurea

## Tarkoitus

Tämä checklist on tarkoitettu viimeiseen julkaisuhetkeen, kun v2-rakenne on jo rakennettu rinnalle HubSpotiin preview-sivuina ja versionoituina moduleina/templateina.

Tavoite:

- siirtää v2 turvallisesti liveksi
- estää rikkinäiset linkit, formit ja navigaatiot
- pitää rollback-polku valmiina
- varmistaa, ettei keskeneräistä rakennetta näy tuotannossa

---

## 1. Cutoverin esiehdot

Seuraavien täytyy olla totta ennen kuin yksikään live-sivu vaihdetaan:

- [ ] oikea HubSpot account / portal varmistettu
- [ ] nykyinen live-teema auditoitu
- [ ] v2-teema tai versionoidut v2-rakenteet valmiina
- [ ] kaikki preview-sivut rakennettu
- [ ] kaikki preview-sivut testattu desktopilla
- [ ] kaikki preview-sivut testattu mobiilissa
- [ ] kaikki CTA:t tarkistettu
- [ ] kaikki formit tarkistettu
- [ ] kaikki meeting-linkit tarkistettu
- [ ] kaikki sisäiset linkit tarkistettu
- [ ] navigaatiomuutokset testattu
- [ ] footer-linkit testattu
- [ ] noindex on aktiivinen preview-sivuilla
- [ ] rollback-polku dokumentoitu

---

## 2. Cutover-järjestyksen valinta

Valitaan yksi kahdesta mallista:

### Vaihtoehto A — vaiheittainen julkaisu

Suositus, jos halutaan pienin riski.

Etenemisjärjestys:

1. videopalvelusivut
2. koulutussivut
3. palvelusivut
4. referenssi-indeksit
5. referenssidetailit
6. yhteystiedot / infosivut
7. henkilöprofiilit
8. etusivu viimeisenä

### Vaihtoehto B — koko paketti yhdellä kertaa

Sopii vain jos:

- kaikki riippuvuudet on täysin kartoitettu
- navigaatio muuttuu laajasti kerralla
- rollback on harjoiteltu tai hyvin dokumentoitu

Kuulun tapauksessa ensisijainen suositus on:

> vaiheittainen julkaisu, etusivu viimeisenä

---

## 3. Ennen yksittäisen sivun live-vaihtoa

Tee nämä jokaiselle sivulle:

- [ ] varmista vanhan live-sivun nykyinen template
- [ ] varmista uuden v2-sivun template
- [ ] varmista vanha slug
- [ ] varmista uusi slug
- [ ] varmista että preview-sivun sisältö vastaa hyväksyttyä versiota
- [ ] varmista että canonical on oikein
- [ ] varmista että form/meeting CTA toimii
- [ ] varmista ettei preview-sivulla ole enää testitekstejä
- [ ] varmista ettei preview-sivu ole riippuvainen liveen kytketystä shared-riskirakenteesta

---

## 4. Slug- ja URL-vaihto

### Jos URL pysyy samana

Suositus:

- pidä tuotanto-URL samana
- vaihda taustalla vain sivun/template-rakenne

Esim:

- vanha live: `/digimarkkinointi`
- uusi v2 ottaa saman URL:n käyttöön vasta cutoverissa

### Jos URL muuttuu pakosta

- [ ] tee 301-redirect
- [ ] kirjaa redirect päätösrekisteriin
- [ ] tarkista canonical
- [ ] tarkista sisäiset linkit

Poikkeuspolut ja legacy-URL:t käsitellään aina yksittäin, ei summittaisesti.

---

## 5. Navigaation cutover

### Jos navigaatio ei muutu

- [ ] varmista että kaikki vanhat valikkolinkit osoittavat uusiin live-sivuihin

### Jos navigaatio muuttuu

- [ ] aktivoi vain hyväksytty v2-navigation
- [ ] tarkista kaikki ylävalikon linkit
- [ ] tarkista megamenu / dropdownit
- [ ] tarkista CTA-painike headerissä
- [ ] tarkista mobile navigation

Erityissääntö:

> Header-muutosta ei tehdä ensimmäisten sivujen mukana, ellei sen käyttäytyminen ole 100 % validoitu.

---

## 6. Footerin cutover

- [ ] tarkista kaikki footer-linkit
- [ ] tarkista yhteystiedot
- [ ] tarkista tietosuojaselosteen linkki
- [ ] tarkista mahdolliset some-linkit
- [ ] tarkista ettei footer-v2 vuoda keskeneräisenä muihin sivuihin

---

## 7. Formit ja konversiopisteet

Jokaiselle v2-liveen siirtyvälle sivulle:

- [ ] form ID oikein
- [ ] form renderöityy
- [ ] required-kentät toimivat
- [ ] success state toimii
- [ ] meeting-linkki avautuu oikeaan paikkaan
- [ ] CTA-linkit eivät osoita preview-slugeihin

---

## 8. Smoke test heti julkaisun jälkeen

Tämä tehdään välittömästi jokaisen cutoverin jälkeen.

### Sivukohtainen smoke test

- [ ] sivu avautuu 200-statuksella
- [ ] title ja H1 oikein
- [ ] hero näkyy oikein
- [ ] CTA:t toimivat
- [ ] media näkyy oikein
- [ ] mobiilin tärkeimmät kohdat toimivat

### Sivustotason smoke test

- [ ] etusivu toimii
- [ ] navigaatio toimii
- [ ] footer toimii
- [ ] tärkeimmät service-sivut aukeavat
- [ ] tärkeimmät training-sivut aukeavat
- [ ] case-index toimii
- [ ] yhteystiedot toimii

---

## 9. Rollback-checklist

Jos jokin menee pieleen:

- [ ] palauta vanha template käyttöön
- [ ] palauta vanha global group / header / footer jos muutos liittyi niihin
- [ ] palauta vanha slug-järjestely
- [ ] poista uusi rikkoutunut navigaatiomuutos
- [ ] varmista että etusivu toimii
- [ ] varmista että tärkeimmät konversiosivut toimivat

Rollback onnistuu vain jos nämä on kirjattu etukäteen:

- edellinen template
- edellinen moduuliversio
- edellinen navigation/footer-tila

---

## 10. Cutoverin jälkeinen 24h tarkistus

Julkaisun jälkeen tarkistetaan vielä:

- [ ] sivut latautuvat oikein edelleen
- [ ] ei rikkinäisiä sisäisiä linkkejä
- [ ] formit toimivat edelleen
- [ ] ei väärään sivuun osoittavia CTA:ita
- [ ] ei preview-sivuja indeksoitavina
- [ ] redirectit toimivat kuten pitää

---

## 11. Erityissääntö etusivulle

Etusivu vaihdetaan vasta kun:

- kaikki tärkeimmät alasivut ovat jo vakaat
- v2-moduulit on testattu käytännössä
- navigation-v2 ja footer-v2 on testattu
- rollback vanhaan etusivuun on dokumentoitu yksityiskohtaisesti

Etusivu on viimeinen iso cutover.

---

## Yhteenveto

Ilman staging-featurea turvallinen julkaisu syntyy kurinalaisuudesta:

1. versionoitu rakenne
2. preview-sivut
3. tarkka slug/redirect-rekisteri
4. vaiheittainen cutover
5. nopea rollback

Tärkein sääntö:

> Jos jokin näyttää epävarmalta juuri ennen live-vaihtoa, sitä ei julkaista vielä.
