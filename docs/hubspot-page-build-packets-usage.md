# Kuulu v2: page build packet -käyttöohje

## Tarkoitus

Page build packetit ovat käytännön työpaketteja ensimmäisen aallon sivuille.

Ne kokoavat yhteen samaan JSON-tiedostoon:

- sivun päätavoitteen
- hero-suunnan
- mandatory signaalit
- moduuli-instanssikohtaisen sisältösuunnitelman
- nykyisen live-sivun source extractin
- sisäisen linkkikartan
- HubSpot-buildin page settings -linjaukset

Tämä tekee varsinaisesta toteutuksesta huomattavasti suoraviivaisemman, koska yhtä sivua rakentaessa ei tarvitse avata neljää eri generated-tiedostoa rinnalle.

---

## 1. Missä build packetit ovat

Generoitu hakemisto:

- `docs/generated/first-wave-page-build-packets/`

Indeksi:

- `docs/generated/first-wave-page-build-packets/index.json`

Generoiva skripti:

- `scripts/generate_first_wave_page_build_packets.py`

---

## 2. Mitä yhdessä packetissa on

Jokainen sivukohtainen tiedosto sisältää:

- `page_id`
- `template`
- `preview_slug`
- `url`
- `primary_goal`
- `core_message`
- `hero_direction`
- `mandatory_signals`
- `page_settings`
- `module_plan`
- `source_extract`
- `link_map`

Tämä on käytännössä yhden sivun koko toteutusbriefi koneellisesti luettavassa muodossa.

---

## 3. Käyttö oikeassa HubSpot-buildissä

Kun oikea v2-teema on authin jälkeen käytössä:

1. valitse rakennettava sivu
2. avaa sen packet JSON
3. rakenna sivun moduuli-instanssit packetin `module_plan`-järjestyksen mukaan
4. täytä kunkin moduulin sisältö packetin:
   - `content_job`
   - `source_priority`
   - `editor_notes`
   perusteella
5. tarkista lopuksi:
   - `mandatory_signals`
   - `source_extract.cta_candidates`
   - `link_map.internal_links`

---

## 4. Miksi tämä on hyödyllistä

Ilman packet-rakennetta toteuttajan pitää yhdistellä tietoa useista lähteistä:

- content packs
- hs data
- source extracts
- link map

Packet tekee saman valmiiksi.

Tämä vähentää riskiä:

- unohtaa tärkeä CTA
- kadottaa nykyinen sisäinen linkki
- rikkoa sisällön flow
- tulkita moduulin rooli väärin

---

## 5. Käyttöjärjestys ensimmäisessä aallossa

Suositeltu build-järjestys packetien tasolla:

1. `video-service-v2.json`
2. `training-v2.json`
3. `digimarkkinointi-v2.json`
4. `case-studies-v2.json`
5. `yhteystiedot-v2.json`
6. `homepage-v2.json`

Etusivu viimeisenä.

---

## 6. Yhteenveto

Page build packetit ovat se taso, jossa:

> strateginen suunnittelu muuttuu yhden sivun toteutusbriefiksi.

Niiden tarkoitus on nopeuttaa toteutusta ja samalla vähentää regressioriskiä.
