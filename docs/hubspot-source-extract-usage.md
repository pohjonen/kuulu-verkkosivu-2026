# Kuulu v2: source extract -käyttöohje HubSpot-buildissä

## Tarkoitus

Tämä dokumentti kertoo, miten ensimmäisen aallon `source extract` -tiedostoja käytetään oikean HubSpot-buildin aikana.

Source extractit ovat tärkeä välitaso, koska ne kokoavat nykyisestä julkisesta sivusta:

- näkyvät otsikot
- keskeiset kappaleet
- CTA-linkit
- rakenteelliset havainnot

Näin varsinaista v2-sivua ei tarvitse rakentaa sokkona pelkän selaamisen tai irrallisten muistiinpanojen varassa.

---

## 1. Missä extractit ovat

Generoitu data:

- `docs/generated/kuulu-first-wave-source-extracts.json`
- `docs/generated/kuulu-first-wave-source-extracts.md`

Generoiva skripti:

- `scripts/generate_first_wave_source_extracts.py`

---

## 2. Mitä extract sisältää

Jokaisesta ensimmäisen aallon sivusta extract kokoaa:

- URL
- title
- H1
- H2/H3-poiminnat
- ensimmäiset kappaleet
- sisäiset CTA-linkit
- sisäiset media-/lomakesignaalit

Tämä ei ole lopullinen sisältö eikä copy-päätös. Se on **rakennuslähde**.

---

## 3. Käyttöjärjestys buildissä

Kun oikea HubSpot-teema on authin jälkeen käytettävissä, sivun sisältö täytetään näin:

1. tarkista sivun `section stack`
2. tarkista sivun `first-wave HS data`
3. tarkista sama sivu `source extract` -datasta
4. tarkista mahdollinen Notion-lähde
5. tarkista Zero Click -ydinsisältö
6. päätä lopullinen v2-copy moduuli kerrallaan

Eli käytännössä:

- `section stack` kertoo **missä järjestyksessä**
- `hs-data` kertoo **mitä kunkin moduulin pitää tehdä**
- `source extract` kertoo **mitä nykyisessä live-sivussa jo on**

---

## 4. Mitä source extractista otetaan

Source extractista käytetään erityisesti:

- nykyinen H1 / pääväite
- nykyiset tärkeimmät väliotsikot
- nykyiset hyödylliset listaukset
- nykyiset CTA-linkit
- nykyinen rakennevire

### Ei käytetä sokeasti

Source extractia ei kopioida suoraan, jos:

- Notionissa on parempi uusi ehdotus
- Zero Click -ydin antaa paremman strategisen rungon
- nykyinen copy on liian legacy-henkinen
- rakenne sotii uuden module stackin kanssa

---

## 5. Prioriteettisääntö

Kun lähteet ovat ristiriidassa, käytetään tätä tulkintajärjestystä:

1. käyttäjän kovat linjaukset
2. Brand 2026
3. Zero Click -ydinsisältö
4. sivukohtainen Notion-ehdotus
5. nykyinen live-sivu

Source extract siis suojaa meitä siltä, ettei mitään olennaista nykyisestä sivusta huku, mutta se ei ohita uutta strategista suuntaa.

---

## 6. Käytännön esimerkki

### Videotuotanto

- `source extract` antaa nykyisen H1:n, kipupisteitä ja CTA-logiikkaa
- Notion antaa vahvemman uuden copyrungon
- Zero Click -PDF tuo captured / hybrid / AI-logiikan
- lopullinen moduulitäyttö tehdään näiden yhdistelmänä

### Koulutus

- `source extract` näyttää nykyisen kurssi- ja CTA-rakenteen
- Notionissa on vahva uusi sivuehdotus
- Zero Click tuo osaamisvajeen / murroksen rungon
- v2-sivu rakennetaan Notion + PDF -painotteisesti, mutta extract varmistaa ettei tärkeä live-sisältö katoa

---

## 7. Yhteenveto

Source extractien rooli on:

> varmistaa, että nykyisen live-sivun hyödyllinen sisältö ei katoa, samalla kun uusi v2-sivu rakennetaan strategisesti vahvempaan rakenteeseen.

Ne eivät päätä lopullista copya, mutta ne tekevät toteutuksesta huomattavasti turvallisempaa ja nopeampaa.
