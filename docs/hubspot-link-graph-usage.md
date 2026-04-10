# Kuulu v2: full link graph -käyttöohje

## Tarkoitus

Tämä dokumentti kertoo, miten koko ei-blogi-sivuston sisäistä linkkigraafia käytetään:

- ensimmäisen aallon buildissä
- linkki-QA:ssa
- cutover-suunnittelussa
- redirect-päätösten varmistuksessa

Käytettävät tiedostot:

- `docs/generated/kuulu-full-link-graph.json`
- `docs/generated/kuulu-full-link-graph.md`

Generoiva skripti:

- `scripts/generate_full_link_graph.py`

---

## 1. Mitä full link graph sisältää

Linkkigraafi kuvaa koko inventoidun ei-blogi-sivuston:

- outgoing links per page
- inbound links per target page
- linkkityypin karkeasti:
  - `cta`
  - `navigational`
  - `contextual`

Tämä on tärkeä lisä ensimmäisen aallon linkkikarttaan, koska nyt nähdään myös:

- mitkä sivut ovat koko verkoston solmukohtia
- mihin useat sivut viittaavat
- mitä URL:eja ei saa muuttaa huolimattomasti

---

## 2. Mihin tätä käytetään

### 2.1 Linkki-QA

Kun v2-sivu valmistuu:

1. tarkista sivun packet
2. tarkista first-wave link map
3. tarkista full link graph

Näin näet:

- mitä sivu itse linkittää
- mihin muut sivut linkittävät tätä sivua

### 2.2 Redirect-päätökset

Jos jokin URL halutaan muuttaa tai yhdistää:

- tarkista ensin sen inbound-linkkien määrä
- tarkista millaisilla label-teksteillä siihen tullaan

Jos URL:lla on paljon inbound-polkuja, oletus on:

> älä muuta slugia ilman erittäin hyvää syytä.

### 2.3 Cutover-järjestys

Linkkigraafi auttaa vahvistamaan cutover-järjestystä:

- sivut joihin moni muu sivu linkittää, julkaistaan mieluummin vakaasti ennen niitä jotka vain harvaan polkuun vaikuttavat
- etusivu pidetään edelleen viimeisenä, koska se on sekä korkein näkyvyys- että linkkiriski

---

## 3. Tärkeimmät tulkinnat

### Inbound > outbound

Jos sivulla on paljon inbound-linkkejä:

- se on kriittinen solmu
- sen slugia ei muuteta kevyesti
- sen CTA-polut tarkistetaan erityisen tarkkaan

### CTA-linkit

Jos tiettyyn URL:iin tulee paljon `cta`-luokan linkkejä:

- konversiopolku pitää säilyttää
- uusi v2-sivu ei saa menettää samaa seuraavaa askelta

### Navigational-linkit

Jos linkki näkyy monella sivulla navigational-luokassa:

- kyse on usein header/footer/menu- tai vakiorakenteesta
- siihen liittyvät muutokset ovat korkean riskin muutoksia

---

## 4. Käyttö yhdessä muiden tiedostojen kanssa

Käytä full link graphia yhdessä näiden kanssa:

- `docs/generated/kuulu-first-wave-link-map.json`
- `docs/generated/kuulu-redirect-register.json`
- `docs/generated/kuulu-cutover-checklist.json`
- `docs/generated/first-wave-page-build-packets/`

Roolit:

- first-wave link map = ensimmäisen aallon tarkka sivukohtainen kartta
- full link graph = koko sivuston verkostokuva
- redirect register = päätökset
- cutover checklist = julkaisuoperaatio
- page packets = moduuli-instanssien build-briefit

---

## 5. Yhteenveto

Full link graphin tarkoitus on vastata tähän kysymykseen:

> jos muutamme yhtä sivua, mitä muita sivuja ja polkuja se voi epäsuorasti koskea?

Tämä tekee v2-cutoverista turvallisemman, koska muutoksia ei arvioida vain yksittäisen sivun näkökulmasta vaan koko sisäisen linkkiverkon näkökulmasta.
