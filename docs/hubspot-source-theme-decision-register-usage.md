# Kuulu v2: source-theme decision register -käyttöohje

## Tarkoitus

Tämä dokumentti kertoo, miten authin jälkeen johdettua `source-theme-decision-register`-aineistoa käytetään, kun fetched source themestä päätetään:

- mitä voidaan käyttää uudelleen
- mitä pitää forkata v2:een
- mitä pitää suojella eikä koskea
- mitä kannattaa korvata kokonaan

Käytettävät tiedostot:

- `docs/generated/source-theme-decision-register.json`
- `docs/generated/source-theme-decision-register.md`

Generoiva skripti:

- `scripts/generate_source_theme_decision_register.py`

---

## 1. Mitä decision register sisältää

Se yhdistää kolme aiempaa kerrosta:

1. fetched source theme audit
2. public asset signature -vertailu
3. nykyisen v2-rakennuslogiikan

Tämän tuloksena jokaiselle havaitulle kohteelle annetaan jokin näistä päätöksistä:

- `protect`
- `fork-to-v2`
- `reuse-candidate`
- `replace`
- `review-manually`

---

## 2. Päätösten tarkoitus

### `protect`

Kohde on todennäköisesti shared/global/homepage-riskialue.

Siihen ei kosketa suoraan.

### `fork-to-v2`

Kohde näyttää hyödylliseltä, mutta sitä ei saa muuttaa nykyisessä muodossa.

Ratkaisu:
- tee siitä v2-kopio / rinnakkaisversio

### `reuse-candidate`

Kohde näyttää mahdolliselta uudelleenkäytettävältä palalta.

Silti tämä vahvistetaan aina vielä käytännön template-/module-auditissa.

### `replace`

Kohde näyttää legacyltä, testiltä tai muuten sellaiselta, että sen korvaaminen on todennäköisesti parempi kuin reuse.

### `review-manually`

Ei tarpeeksi varmaa automaattista signaalia.

Tämä tarvitsee ihmisen päätöksen.

---

## 3. Miten tätä käytetään oikeassa buildissä

Kun source theme on fetchattu ja v2-klooni on olemassa:

1. avaa `source-theme-decision-register`
2. aloita high-risk / protect -kohteista
3. varmista että niitä ei muokata suoraan
4. tunnista `fork-to-v2` -kohteet
5. tee `reuse-candidate` -kohteille manuaalinen vahvistus
6. jätä `replace`-kohteet pois v2-rakennuksesta, ellei niillä ole erityistä syytä säilyä

---

## 4. Tärkein hyöty

Tämä tiedosto vähentää yhden ison riskin:

> fetched source theme on iso, sekava ja sisältää sekä nykyisiä että historiallisia osia. Ilman päätösrekisteriä on helppo koskea väärään kohtaan.

Decision register tekee tästä hallitumpaa.

---

## 5. Yhteenveto

Decision register on fetched source theme -vaiheen ensimmäinen varsinainen päätöskerros.

Se ei yksinään päätä kaikkea lopullisesti, mutta se kertoo nopeasti:

- mihin ei kosketa
- mitä kannattaa kopioida v2:een
- mitä voidaan ehkä reuse
- mitä ei todennäköisesti kannata ottaa mukaan
