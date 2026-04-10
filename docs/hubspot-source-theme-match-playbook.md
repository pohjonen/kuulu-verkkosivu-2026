# Kuulu v2: source-theme match playbook

## Tarkoitus

Tämä dokumentti kertoo, miten fetched HubSpot source theme verrataan nykyiseen julkiseen kuulu.fi-sivuun niin, että:

- varmistetaan että oikea teema on haettu
- tunnistetaan vastaako fetched teema oikeasti tuotannossa näkyvää kokonaisuutta
- löydetään nopeammin ne assetit, modulit ja templatet jotka liittyvät nykyiseen live-etusivuun ja muihin kriittisiin sivuihin

Tämä on tärkeä vaihe heti fetchin jälkeen ennen varsinaista reuse / fork / replace -päätöstä.

---

## 1. Käytettävät lähteet

### Julkinen referenssi

- `docs/generated/kuulu-public-asset-signature.json`
- `docs/generated/kuulu-public-asset-signature.md`

Nämä kuvaavat mikä juuri nyt näkyy julkisessa sivussa:

- portalId
- sivukohtaiset asset-bundlet
- uniikit asset-nimet
- theme guess -luokitukset

### Paikallinen fetched source

Fetchin jälkeen käytetään:

- `hubspot/source-theme/`

### Vertailuhelper

- `scripts/compare_source_theme_to_public_signature.py`

---

## 2. Tärkein kysymys

Fetchin jälkeen pitää pystyä vastaamaan tähän:

> Onko paikallisesti fetched source theme sama tai erittäin todennäköisesti sama teema, joka renderöi nykyisen julkisen kuulu.fi-kokonaisuuden?

Jos vastaus ei ole riittävän varma, mitään v2-forkkia ei pidä aloittaa vielä.

---

## 3. Ensimmäinen vertailu fetchin jälkeen

Kun `hubspot/source-theme/` on olemassa, aja:

```bash
python3 scripts/compare_source_theme_to_public_signature.py hubspot/source-theme
```

### Mitä skripti tekee

- lukee julkisen asset-signaturen
- käy läpi fetched sourcen tiedostot
- yrittää matchata julkiset asset-filenimet paikallisiin tiedostoihin

### Mitä tuloksesta etsitään

#### Hyvä merkki

- useita täsmääviä asset-filenimiä
- erityisesti:
  - `template_cinematic.min.css`
  - `template_cinematic-responsive.min.css`
  - `template_design-tokens.min.css`
  - `template_module-fixes.min.css`
  - `template_main.min.js`
  - `template_styles.min.css`

#### Varoitusmerkki

- ei yhtään täsmäävää nimeä
- fetched source näyttää täysin eri teemalta
- fetched source sisältää vain osakansion eikä kokonaista themea

---

## 4. Sivukohtainen match-ajattelu

Julkinen asset-signature jakaa viisi tärkeää näkymää:

### Homepage

Odotettu signaali:

- cinematic-uusi
- tokenit + cinematic bundle + main.js

### Video-service

Odotettu signaali:

- cinematic-uusi
- lisäksi mahdollinen rich pricing -bundle

### Training

Odotettu signaali:

- legacy-vaalea
- `template_styles.min.css`
- FAQ-moduulin assetit

### Service

Odotettu signaali:

- legacy-vaalea
- `template_styles.min.css`

### Reference-index

Odotettu signaali:

- sekamuotoinen / epäselvä
- voi vaatia enemmän template- ja moduulirakenteen auditointia

---

## 5. Match-luokat

Fetchin jälkeen luokittele source theme näin:

### `confirmed-match`

Käytä kun:

- asset-nimissä on useita selkeitä osumia
- source theme rakenne tukee julkisen sivun havaintoja
- etusivun ja videotuotannon cinematic-assetit löytyvät järkevästi

### `probable-match`

Käytä kun:

- jotain asset-osumia löytyy
- theme näyttää oikealta mutta build-pipeline saattaa nimetä osan asioista uudelleen

### `weak-match`

Käytä kun:

- osumia on vain vähän
- fetched sisältö vaikuttaa osittaiselta
- ei vielä turvallista aloittaa v2-forkkia

### `wrong-source`

Käytä kun:

- signatuuri ei täsmää käytännössä ollenkaan
- fetched path on todennäköisesti väärä

---

## 6. Mitä tehdään jos match on heikko

Älä aloita forkkausta.

Sen sijaan:

1. varmista että oikea remote path haettiin
2. fetchaa mahdollinen ylempi theme root
3. tarkista onko kyse child theme / parent theme -rakenteesta
4. tarkista onko build-assetit generoituna eri kansiosta
5. toista vertailu

---

## 7. Mitä tehdään jos match on hyvä

Kun match on riittävän hyvä:

1. kirjaa match-luokka
2. kirjaa tärkeimmät osumat
3. kirjaa mitkä assetit näyttävät liittyvän:
   - etusivuun
   - videotuotantoon
   - legacy-palvelusivuihin
4. siirry vasta sitten teema-audit checklistiin
5. tee vasta sen jälkeen `kuulu-theme-v2`-klooni

---

## 8. Yhteenveto

Tämä vaihe estää yhden tärkeän virheen:

> väärän source themen päälle rakennetun v2-haaran

Sääntö:

1. fetch
2. match public signatureen
3. vasta sitten audit
4. vasta sitten clone

