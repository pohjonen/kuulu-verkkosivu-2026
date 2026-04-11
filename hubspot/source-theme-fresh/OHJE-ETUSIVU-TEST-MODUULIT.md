# Etusivu-test-moduulit – moduulit näkyviin (HubSpotissa muokattavina)

Templatessa **Etusivu - Moduuliversio (DEV)** on `dnd_area`, jonka sisällä on jo 11 kpl `dnd_module`-tagia (Hero, Early Bird, jne.). HubSpot käyttää tätä **oletussisältönä**: kun luot **uuden sivun** tällä templatella, kaikki 11 moduulia tulevat sivulle automaattisesti ja ovat muokattavissa. Vanha sivu (364696278229) on todennäköisesti luotu ennen templaten päivitystä → sen tallennettu sisältö on tyhjä, siksi moduulit eivät näy.

## Vaihtoehto A: Luo uusi sivu (suositus – moduulit tulevat automaattisesti)

1. HubSpot: **Website** → **Website Pages** (tai suoraan https://app-eu1.hubspot.com/website/450584/pages/site ).
2. **Create** → **Website page**.
3. Valitse teema **Kuulu 2026 DEV**.
4. Valitse template **"Etusivu - Moduuliversio (DEV)"** (jos et näe sitä Page 1:llä, vaihda **Page 2** tai **Page 3** – template on listan loppupuolella; voit myös hakea hakukentällä "Moduuliversio" tai "moduuli").
5. Anna sivun nimi (esim. "Etusivu testi moduulit") ja **Page URL**: `etusivu-test-moduulit`.
6. **Create** / **Next** ja sitten **Publish** (tai ensin Save draft, sitten Publish).

→ Uusi sivu saa templaten oletussisällön: kaikki 11 moduulia (Hero, Early Bird, Ongelmalista, Kaksi koneistoa, jne.). Ne ovat muokattavissa **Content**-välilehdellä.

Jos slug `etusivu-test-moduulit` on jo käytössä, poista tai nimeä vanha sivu uudelleen ensin (Settings → Page URL), tai anna uudelle sivulle toinen slug (esim. `etusivu-test-moduulit-v2`).

---

## Vaihtoehto B: Käytä olemassa olevaa sivua (364696278229) – lisää moduulit itse

Jos haluat pitää nykyisen sivun:

1. Avaa editori: https://app-eu1.hubspot.com/pages/450584/editor/364696278229/content
2. Välilehti **Content** (ei Settings).
3. Vasemmalla on "Sivun sisältö" -alue. Jos se on tyhjä, **Add module** (tai +) ja lisää moduulit yksi kerrallaan:
   - Hero (cinematic_hero)
   - Early Bird -lomake (cinematic_early_bird)
   - Ongelmalista (cinematic_problem_list)
   - Kaksi koneistoa (cinematic_two_engines)
   - Brand DNA ja Tekoäly (cinematic_text_image)
   - Miten pääset alkuun (cinematic_steps)
   - Mittaamme suppilon (cinematic_metrics)
   - Miksi Kuulu (cinematic_authority)
   - Koulutukset CTA (cinematic_cta_cards)
   - Referenssit (cinematic_referenssit)
   - Yhteys-CTA (cinematic_contact_cta)
4. **Settings** → Page URL = `etusivu-test-moduulit` (jos haluat juuri tämän URL:n).
5. **Publish**.

---

## Tärkeää

- **Älä kovakoodaa** moduuleja templateen (ei `{% module %}`-lohkoja). Pidetään `dnd_area` + `dnd_module`, jotta sisältö on muokattavissa HubSpotissa.
- Teema täytyy olla ladattu: `hs cms upload kuulu-theme-2025-dev kuulu-theme-2025-dev`.
- Live-URL: https://www.kuulu.fi/etusivu-test-moduulit
