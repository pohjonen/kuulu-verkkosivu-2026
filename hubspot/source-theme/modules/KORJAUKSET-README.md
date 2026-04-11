# Kuulu Brändikorjaukset - Pikaohje

Tiedosto: `BRAND-FIXES-2026-02-17.md`

## Mitä korjattiin?

### 1. Värit CSS-muuttujiksi
Kaikki kovakoodatut värikoodit korvattu CSS-muuttujilla:
- `#00ff88` → `var(--cinematic-green)`
- `#ffffff` → `var(--cinematic-text)`
- `#0a0a0a` → `var(--cinematic-bg)`

### 2. Fontit yhtenäisiksi
- Otsikot: `font-family: var(--font-display);` (Bebas Neue)
- Leipäteksti: `font-family: var(--font-body);` (Inter)

### 3. CTA-napit UPPERCASE
- "Varaa sparraus" → "VARAA SPARRAUS"
- "Ota yhteyttä" → "OTA YHTEYTTÄ"

### 4. Äänensävy suoremmaksi
- "Emme ole tavallinen..." → "Vertaa itse"
- "Tulokset puhuvat..." → "Luvut kertovat"

## Tilastot

- **Moduuleja korjattu:** 31 kpl
- **CSS-tiedostoja:** 17 kpl
- **fields.json:** 31 kpl
- **JSON-validointi:** ✅ Kaikki OK

## Seuraavat vaiheet

```bash
# 1. Testaa lokaalisti
hs watch kuulu-theme-2025-dev kuulu-theme-2025-dev

# 2. Upload DEV-ympäristöön
hs upload kuulu-theme-2025-dev kuulu-theme-2025-dev

# 3. Testaa HubSpotissa
- Tarkista kaikki cinematic-moduulit
- Testaa header/footer scroll
- Validoi mobile-näkymät

# 4. Deploy LIVE kun hyväksytty
```

## Tärkeimmät tiedostot

1. `BRAND-FIXES-2026-02-17.md` - Täydellinen dokumentaatio
2. `scripts/fix_brand_consistency.sh` - Pääkorjausskripti
3. `scripts/validate_json.sh` - JSON-validaattori

## Yhteyshenkilö

Ville Pohjonen  
Deadline: 2026-02-18

