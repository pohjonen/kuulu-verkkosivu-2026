# Kuulu v2: foundation seed data -käyttöohje

## Tarkoitus

Tämä dokumentti kertoo, miten ensimmäisten foundation-forkkien seed-dataa käytetään oikeassa v2-toteutuksessa.

Käytettävät tiedostot:

- `docs/generated/foundation-seed-data.json`
- `docs/generated/foundation-seed-data.md`

Generoiva skripti:

- `scripts/generate_foundation_seed_data.py`

---

## 1. Mitä seed-data tekee

Seed-data kokoaa foundation-kandidaateista juuri ne tiedot, joita tarvitaan ensimmäisessä oikeassa v2-forkissa:

- source-moduulin nimi
- target-moduuli
- moduulin meta-signaalit
- tärkeimmät kentät `fields.json`:sta
- polut source-moduulin tiedostoihin

Tämä säästää aikaa, koska fork-vaiheessa ei tarvitse joka kerta lukea koko source-moduulin rakennetta alusta asti.

---

## 2. Mihin tätä käytetään

Ensimmäisessä foundation-vaiheessa erityisesti näille:

- `hero-cinematic-v2`
- `problem-grid-v2`
- `service-pillars-v2`
- `stats-trust-band-v2`
- `lead-capture-form-cta-v2`

Näissä seed-data auttaa tunnistamaan:

- mitkä nykyiset kentät kannattaa säilyttää
- mitä nimiä ja label-logiikkaa pitää normalisoida
- mitä ei kannata kopioida sellaisenaan

---

## 3. Käyttöjärjestys

Kun foundation-forkkia aletaan tehdä `hubspot/kuulu-theme-v2/`-puolella:

1. avaa `docs/generated/foundation-seed-data.json`
2. valitse forkattava target-moduuli
3. tarkista:
   - `source_module`
   - `highlight_fields`
   - `paths`
4. vertaile source-moduulia ja blueprint-moduulia
5. tee vasta sitten uusi v2-versio oikeaan teemaan

---

## 4. Mitä seed-data EI ole

Seed-data ei ole:

- lopullinen fields.json
- lopullinen HubL-malli
- lopullinen UI-päätös

Se on:

> käytännöllinen lähdepaketti ensimmäisen fork-vaiheen nopeuttamiseen ja riskin pienentämiseen.

---

## 5. Yhteenveto

Foundation seed data on ensimmäinen kohta, jossa:

- fetched source theme
- blueprint
- moduulien field-malli

kohtaavat konkreettisella tasolla.

Sen tarkoitus on nopeuttaa ensimmäisiä turvallisia v2-forkkeja ilman, että source-themeen tarvitsee koskea suoraan.
