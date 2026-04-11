# HubSpot-moduulien lisääminen ja muokkaaminen – step by step

Kattavat ohjeet moduulien käyttöön Design Managerissa ja sisältöeditorissa.

---

## Uuden moduulin luominen (Design Manager)

1. Siirry **Sisältö** → **Suunnittelun hallinta** (Design Manager).
2. Klikkaa yläreunassa **Tiedosto**-pudotusvalikkoa → **Uusi tiedosto**.
3. Valitse "Mitä haluat rakentaa?" -valikosta **Moduuli**.
4. Valitse moduulin laajuus:
   - **Paikallinen moduuli** – käytössä vain yhdessä mallissa
   - **Globaali moduuli** – muutokset päivittyvät kaikkialle, missä moduulia käytetään
5. Anna moduulille nimi ja tallenna.

---

## Kenttien lisääminen moduuliin

1. Avaa moduuli Design Managerissa klikkaamalla sitä hakemistosta.
2. Klikkaa oikean sivupalkin **Kentät**-osiossa **Lisää kenttä** -pudotusvalikkoa.
3. Valitse kenttätyyppi (esim. teksti, kuva, päivämäärä, rich text, CTA-painike).
4. Määritä kentän nimi, oletussisältö ja mahdolliset näyttöehdot.
5. Kopioi kentän valmistekti (snippet) ja liitä se moduulin `module.html`-osioon.

---

## Moduulin muokkaaminen

1. Siirry **Sisältö** → **Suunnittelun hallinta**.
2. Etsi ja avaa muokattava moduuli hakemistosta.
3. **Kentän muokkaus:** vie kursori kentän päälle oikean sivupalkin Kentät-osiossa → klikkaa **Muokkaa**.
4. **CSS-muokkaus:** klikkaa **Advanced**-välilehteä → **Custom CSS** → kirjoita koodi → tallenna.
5. **Sisältötyypit:** klikkaa moduulin nimen alla olevaa **Sisältötyypit**-kohtaa ja valitse/poista haluamasi tyypit.
6. Klikkaa lopuksi **Julkaise muutokset** oikeasta yläkulmasta.

---

## Moduulin lisääminen sivulle (sisältöeditori)

1. Avaa sivu tai sähköposti sisältöeditorissa.
2. Klikkaa vasemmassa sivupalkissa **+** (Lisää)-kuvaketta.
3. Selaa kategorioita tai käytä hakupalkkia löytääksesi haluamasi moduulin.
4. Klikkaa moduulia lisätäksesi sen sivulle.
5. Muokkaa moduulin sisältöä (teksti, kuvat, linkit) avautuvassa editoripaneelissa.

---

## Moduulin lisääminen malliin (Design Manager)

1. Avaa mallipohja Design Managerissa.
2. **Drag & drop -malli:** klikkaa tarkastajan yläosassa **+ Lisää** -välilehteä → hae moduuli ja vedä haluamaasi kohtaan.
3. **Koodattu mallipohja:** klikkaa hiiren oikealla moduulia hakemistossa → **Kopioi valmistekti** → liitä koodieditoriin.
4. **Julkaise muutokset**.

---

## Moduulin asentaminen Marketplace-palvelusta

1. Siirry **HubSpot Marketplace** → hae haluamasi moduuli.
2. Klikkaa **Asenna** ja valitse, mihin tiliin asennetaan.
3. Moduuli ilmestyy Design Manageriin käyttövalmiiksi.

---

## Kuulu-projektissa

- Moduulit sijaitsevat paikallisesti: `kuulu-theme-2025-dev/modules/*.module/`.
- Teeman upload: `hs cms upload kuulu-theme-2025-dev kuulu-theme-2025-dev` (projektin juuresta).
- Moduulikansioiden nimen pitää päättyä `.module` (HubSpot vaatii).
