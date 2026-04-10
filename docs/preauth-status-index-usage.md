# Kuulu v2: pre-auth status index -käyttöohje

## Tarkoitus

Tämä dokumentti kertoo, miten koontitiedostoja käytetään, kun halutaan nopeasti ymmärtää koko ennen-auth-vaiheen valmius ilman että avataan kymmeniä erillisiä generated-tiedostoja.

Koontitiedostot:

- `docs/generated/kuulu-preauth-status-index.json`
- `docs/generated/kuulu-preauth-status-index.md`

Generoiva skripti:

- `scripts/generate_preauth_status_index.py`

---

## 1. Mitä kooste tekee

Kooste kokoaa yhteen:

- tärkeimmät generated-tiedostot
- niiden olemassaolon
- keskeiset lukuarvot
- blueprint-rakenteen yhteenvedon
- tämänhetkisen blocker-tilan

Tämä tekee yhdestä tiedostosta nopean tilannekuvan koko pre-auth-paketista.

---

## 2. Milloin kooste kannattaa katsoa

### Ennen authia

Kun halutaan tarkistaa:

- onko kaikki odotettu data generoitu
- puuttuuko jokin tärkeä lähdekerros
- onko blueprint scaffold olemassa

### Authin jälkeen

Koostetta voidaan käyttää lähtötasona ennen fetchiä, jotta nähdään:

- mikä oli pre-auth-tilanne
- mitä tiedostoja on valmiina käytettäväksi source theme -auditin ja v2-buildin tukena

---

## 3. Miten kooste tukee toteutusta

Koosteen tärkein rooli on orientaatio.

Se ei korvaa:

- build packet -tiedostoja
- first wave HS dataa
- source extracteja
- fetched theme -auditointia

Mutta se auttaa näkemään nopeasti:

- kuinka monta sivua inventaario kattaa
- kuinka monta moduulia blueprintissä on
- onko all-page packetit olemassa
- mikä on seuraava blocker

---

## 4. Käyttöjärjestys

Kun haluat nopean tilannekuvan:

1. avaa `docs/generated/kuulu-preauth-status-index.md`
2. varmista että expected generated-lähteet ovat olemassa
3. tarkista blueprint summary
4. tarkista blocker-status
5. siirry sen jälkeen yksityiskohtaisiin dokumentteihin vain tarpeen mukaan

---

## 5. Yhteenveto

Pre-auth status index on projektin “dashboard lite”.

Sen tarkoitus on vastata nopeasti kysymykseen:

> missä kunnossa koko valmistelupaketti on juuri nyt?

