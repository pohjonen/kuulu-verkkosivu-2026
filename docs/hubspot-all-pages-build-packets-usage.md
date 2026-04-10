# Kuulu v2: all-pages build packet -käyttöohje

## Tarkoitus

Tämä dokumentti kuvaa, miten koko ei-blogi-sivuston sivukohtaisia build packeteja käytetään silloin, kun toteutus laajenee ensimmäisestä aallosta koko sivustoon.

Käytettävät tiedostot:

- `docs/generated/all-page-build-packets/`
- `docs/generated/all-page-build-packets/index.json`

Generoiva skripti:

- `scripts/generate_all_page_build_packets.py`

---

## 1. Mitkä lähdetiedostot syöttävät all-pages packetit

All-pages packetit yhdistävät nyt nämä generated-lähteet:

- `docs/generated/kuulu-public-site-inventory.json`
- `docs/generated/kuulu-full-link-graph.json`
- `docs/generated/kuulu-all-source-extracts.json`

Ensimmäisen aallon packetit ovat edelleen tarkempi “golden path”, mutta koko sivuston packetit käyttävät nyt koko inventaarion laajuista source extract -dataa.

## 2. Mikä ero on first wave packetin ja all-pages packetin välillä

### First wave packet

Tarkempi, strategisesti painotettu, kuudelle tärkeimmälle sivulle.

### All-pages packet

Laajentaa saman ajattelun koko ei-blogi-inventaarioon:

- kaikki palvelusivut
- kaikki koulutussivut
- kaikki videopalvelusivut
- kaikki referenssi-indeksit
- kaikki referenssidetailit
- yhteys-/info-sivut
- henkilöprofiilit

All-pages packetit ovat erityisen hyödyllisiä, kun build etenee ensimmäisen aallon jälkeen.

---

## 3. Mitä all-pages packet sisältää

Jokainen sivukohtainen packet kokoaa yhteen:

- page id
- template
- preview slug
- nykyinen URL
- page type
- current theme
- primary goal
- core message
- hero direction
- mandatory signals
- page settings
- module plan
- source extract
- link map

Tämä tekee jokaisesta sivusta itsenäisen toteutusbriefin.

---

## 4. Käyttö authin jälkeen

Kun oikea HubSpot-teema on fetchattu ja `kuulu-theme-v2` on luotu:

1. valitse rakennettava sivu
2. avaa sen packet tiedostosta `docs/generated/all-page-build-packets/`
3. rakenna sivu packetin `module_plan`-järjestyksessä
4. käytä packetin:
   - `primary_goal`
   - `core_message`
   - `hero_direction`
   - `mandatory_signals`
   ohjaamaan sisältöä
5. käytä `source_extract`-osaa live-sivun sisällöllisen arvon säilyttämiseen
6. käytä `link_map`-osaa varmistamaan, että sisäiset polut säilyvät

---

## 5. Mihin tätä kannattaa käyttää erityisesti

### 4.1 Referenssidetailit

Näillä sivuilla on paljon URL:ia ja monesti vähän dokumentoitua käsityötä.

Packet auttaa:

- pitämään rakenteen yhtenäisenä
- säilyttämään tärkeät CTA-polut
- varmistamaan ettei nykyinen case-sisältö katoa

### 4.2 Henkilöprofiilit

Packet muistuttaa:

- profiilin tehtävä on luottamus, ei blogiarkisto
- tärkeät yhteys- ja asiantuntijuussignaalit pitää säilyttää

### 4.3 Legacy service/training -sivut

Packet auttaa muuntamaan vanhan sivun uuteen templateen niin, että:

- slug säilyy
- viesti normalisoituu
- rakenne muuttuu ilman että sivu menettää käyttäjäpolun

---

## 6. Yhteenveto

All-pages packetit ovat koko ei-blogi-sivuston laajuinen toteutuskerros.

Ne tarkoittavat käytännössä tätä:

> kun build laajenee ensimmäisestä aallosta koko sivustoon, jokaiselle sivulle löytyy oma koneellisesti luettava toteutusbriefi valmiina.
