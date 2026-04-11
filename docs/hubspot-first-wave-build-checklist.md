# Kuulu v2: ensimmäisen aallon HubSpot build-checklist

## Tarkoitus

Tämä checklist on tarkoitettu siihen hetkeen, kun:

- HubSpot-auth on tehty
- source theme on fetchattu
- v2-klooni on olemassa
- ensimmäisen aallon sivut aletaan rakentaa oikeaan HubSpot v2 -teemaan

Tämä dokumentti sitoo yhteen:

- `docs/generated/kuulu-first-wave-content-packs.json`
- `docs/generated/kuulu-first-wave-hs-data.json`
- `docs/kuulu-first-wave-section-stacks.md`
- `docs/kuulu-module-build-order.md`
- `docs/kuulu-module-field-model.md`

---

## Ensimmäisen aallon sivut

1. etusivu
2. videotuotanto
3. koulutus
4. digimarkkinointi
5. case-studies
6. yhteystiedot

Huomio:

- etusivu rakennetaan ensimmäisen aallon mukana, mutta **vaihdetaan liveksi viimeisenä**
- ensimmäisen aallon tarkoitus on todentaa koko v2-järjestelmän peruslogiikka

---

## 1. Ennen ensimmäistäkään moduulimuutosta

- [ ] `hs account auth` tehty
- [ ] oikea account varmistettu
- [ ] `.hsaccount` override tehty tarvittaessa
- [ ] `source-theme/` fetchattu
- [ ] `source-theme/` auditoitu
- [ ] `kuulu-theme-v2/` kloonattu
- [ ] `kuulu-theme-v2-blueprint/` verrattu oikeaan v2-klooniin
- [ ] reuse / fork / replace / protect päätetty foundation-moduuleille

---

## 2. Foundation-moduulit ensin

Rakennusjärjestys:

1. `hero-cinematic-v2`
2. `final-cta-v2`
3. `problem-grid-v2`
4. `service-pillars-v2`

Jokaisesta moduulista tarkistetaan:

- [ ] oikea fields-rakenne
- [ ] oikea meta-rakenne
- [ ] tokenoitu CSS
- [ ] ei vapaita värejä tai layout-hackeja
- [ ] CTA-kentät rajattu oikein
- [ ] moduuli ei riko current live-teeman shared-osia

---

## 3. System-moduulit

Rakennetaan seuraavaksi:

1. `audience-split-v2`
2. `process-steps-v2`
3. `stats-trust-band-v2`
4. `reference-grid-v2`

Tarkistetaan:

- [ ] 95/5-logiikka toimii
- [ ] repeaterit toimivat editorissa
- [ ] korttirakenteet pysyvät selkeinä
- [ ] reference-linkit voidaan syöttää turvallisesti

---

## 4. Erikoismoduulit

Rakennetaan tämän jälkeen:

1. `video-model-comparison-v2`
2. `training-agenda-v2`
3. `faq-v2`
4. `lead-capture-form-cta-v2`
5. `team-grid-v2`
6. `contact-info-v2`

Tarkistetaan:

- [ ] captured / hybrid / AI-järjestys on lukittu
- [ ] agenda on rakenteinen, ei sekava richtext
- [ ] FAQ toimii mobiilissa
- [ ] form- ja meeting-kentät ovat turvallisia
- [ ] yhteystietorakenne ei nojaa vapaaseen käsinsyöttöön liikaa

---

## 5. Ensimmäiset oikeat sivut HubSpotissa

Suositeltu rakennusjärjestys:

1. `/v2-videotuotanto`
2. `/v2-koulutus`
3. `/v2-digimarkkinointi`
4. `/v2-case-studies`
5. `/v2-yhteystiedot`
6. `/v2-etusivu`

Perustelu:

- etusivu on korkein regressioriski
- alasivut todentavat ensin foundation-moduulit käytännössä

---

## 6. Jokaiselle ensimmäisen aallon sivulle tehtävä tarkistus

- [ ] oikea `template`
- [ ] oikea `preview_slug`
- [ ] oikea `section_stack`
- [ ] oikea `hero_direction`
- [ ] oikeat `mandatory_signals`
- [ ] oikeat CTA:t
- [ ] oikeat media-slotit
- [ ] oikea noindex-asetus previewssa

Lähteet otetaan täältä:

- `docs/generated/kuulu-first-wave-content-packs.json`
- `docs/generated/kuulu-first-wave-hs-data.json`

---

## 7. Editoritestaus ennen mitään cutoveria

Jokaiselle ensimmäisen aallon sivulle:

- [ ] otsikot vaihdettavissa editorissa
- [ ] CTA:t vaihdettavissa editorissa
- [ ] kuvat vaihdettavissa editorissa
- [ ] videot vaihdettavissa editorissa
- [ ] repeater-kortit lisättävissä ilman että layout hajoaa
- [ ] spacing- ja background-variantit toimivat
- [ ] mobiilinäkymä pysyy ehjänä

---

## 8. Preview-QA ennen liveä

Jokaisesta ensimmäisen aallon preview-sivusta tarkistetaan:

- [ ] content flow
- [ ] hierarchy
- [ ] CTA-polku
- [ ] forms / meeting-linkit
- [ ] canonical preview-tilassa
- [ ] noindex preview-tilassa
- [ ] ettei sivu näy live-navigation kautta

---

## 9. Ensimmäisen aallon valmistumisen hyväksymiskriteeri

Ensimmäinen aalto on valmis vasta kun:

- [ ] kaikki foundation-moduulit toimivat
- [ ] kaikki system-moduulit toimivat
- [ ] kaikki erikoismoduulit toimivat
- [ ] ensimmäisen aallon preview-sivut toimivat
- [ ] editorimuokattavuus on testattu
- [ ] etusivu-v2 on valmis mutta ei vielä live
- [ ] yksikään nykyinen live-sivu ei ole muuttunut

---

## 10. Yhteenveto

Ensimmäisen aallon tehtävä ei ole vain rakentaa kuusi sivua.

Sen tehtävä on todistaa, että:

- v2-teemarakenne toimii
- moduulit toimivat
- sisältömalli toimii
- editorikokemus toimii
- live-sivusto ei rikkoudu

Vasta tämän jälkeen siirrytään hallittuun cutover-vaiheeseen.
