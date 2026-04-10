# Kuulu v2: linkkikartan käyttö v2-cutoverissa

## Tarkoitus

Tämä dokumentti kertoo, miten ensimmäisen aallon linkkikarttaa käytetään, jotta nykyisistä live-sivuista tuttu sisäinen navigaatio, CTA-virta ja referenssipolut eivät rikkoudu v2-cutoverissa.

Käytettävät tiedostot:

- `docs/generated/kuulu-first-wave-link-map.json`
- `docs/generated/kuulu-first-wave-link-map.md`

Generoiva skripti:

- `scripts/generate_first_wave_link_map.py`

---

## 1. Mitä linkkikartta sisältää

Jokaisesta ensimmäisen aallon sivusta kerätään:

- source URL
- kaikki sisäiset kuuluvat linkit
- linkkien luokiteltu tyyppi
- linkkitekstit / CTA-labelit

Tämä auttaa tunnistamaan:

- mitä sivuja käyttäjäpoluissa pitää säilyä
- mihin nykyinen etusivu ja ensimmäisen aallon alasivut ohjaavat
- mitkä CTA-tekstit eivät saa kadota muutoksen aikana

---

## 2. Käyttö build-vaiheessa

Kun v2-sivua rakennetaan:

1. avaa sivun `section stack`
2. avaa `first-wave HS data`
3. avaa `source extract`
4. avaa `first-wave link map`

Näin näet yhtä aikaa:

- mitä moduuleja sivulla pitää olla
- mitä niissä pitää sanoa
- mitä nykyisessä live-sivussa jo on
- minne nykyiset CTA:t ja sisäiset linkit johtavat

---

## 3. Mitä linkkikartasta pitää erityisesti säilyttää

### 3.1 Kriittiset sisäiset linkit

Erityisen tarkasti säilytettäviä ovat:

- etusivu → koulutus
- etusivu → digimarkkinointi
- etusivu → videotuotanto
- etusivu → referenssit
- etusivu → yhteystiedot
- videotuotanto → referenssit / sparraus
- koulutus → tarjous / yhteys
- digimarkkinointi → referenssit / sparraus

### 3.2 CTA-labelit

Jos nykyinen CTA on käyttäjän näkökulmasta tunnistettava ja toimiva, sen labelia ei vaihdeta kevyesti.

Esim:

- `VARAA SPARRAUS`
- `PYYDÄ TARJOUS`
- `ILMOITTAUDU`

Niitä saa kehittää, mutta ei hajottaa ilman syytä.

---

## 4. Linkkikartan käyttö cutoverissa

Juuri ennen cutoveria:

1. vertaile v2-sivun CTA:t nykyiseen linkkikarttaan
2. varmista, että kaikki kriittiset sisäiset polut ovat edelleen olemassa
3. tarkista, ettei yksikään linkki osoita preview-slugiin
4. tarkista, ettei uusi rakenne kadota tärkeitä polkuja vain siksi, että layout muuttui

---

## 5. Milloin linkki saa muuttua

Sisäinen linkki saa muuttua vain jos:

1. se ohjataan selvästi parempaan v2-kohteeseen
2. muutos on tietoinen eikä vahinko
3. uusi kohde tukee paremmin käyttäjäpolkua
4. muutos on dokumentoitu redirect-/slug-rekisterissä tai cutover-päätöksissä

---

## 6. Yhteenveto

Linkkikartan tehtävä on varmistaa tämä perusasia:

> vaikka sivujen rakenne, tyyli ja moduulit muuttuvat, käyttäjän kannalta tärkeät sisäiset polut eivät katoa.

Se on yksi tärkeimmistä turvakerroksista tilanteessa, jossa:

- nykyistä etusivua ei saa rikkoa
- linkitykset eivät saa hajota
- v2 rakennetaan rinnalle ennen live-vaihtoa
