# 🏨 Hotel Deal Extractor

> **Mini projekt pre Relaxos** — automatická extrakcia akciových pobytov z e-mailov hotelov

---

## 🎯 Problém, ktorý rieši

Relaxos dostáva podklady o akciových pobytoch od **stoviek hotelov v rôznych formátoch** — plaintext, HTML, rôzne jazyky, rôzna štruktúra. Manuálne spracovanie je časovo náročné a náchylné na chyby.

**Toto riešenie automaticky:**
1. Prijme e-mail od hotela (akýkoľvek formát, SK aj EN)
2. Pomocou pattern matching engine vytiahne všetky štruktúrované dáta
3. Každej ponuke priradí **confidence score** (istota extrakcie)
4. Exportuje výsledky do **prehľadného Excel súboru**
5. Záznamy s nízkou istotou označí na manuálnu kontrolu

---

## ⚙️ Technológie

| Technológia | Účel |
|---|---|
| **Python 3.10+** | Hlavný skript |
| **Regex / Pattern matching** | Extrakcia dát z neštruktúrovaného textu |
| **openpyxl** | Generovanie formátovaného Excel súboru |
| **JSON export** | Výstup pre API / ďalšie spracovanie |

> **Poznámka:** Projekt je navrhnutý tak, aby pattern matching modul šlo jednoducho nahradiť volaním AI API (Claude / Gemini) — bez zmeny zvyšku pipeline.

---

## 🚀 Spustenie

### 1. Požiadavky
```bash
pip install openpyxl
```

### 2. Spustenie
```bash
python extractor.py
```

Žiadny API kľúč, žiadna registrácia — funguje 100% offline.

---

## 📊 Ukážka výstupu

```
🏨 Hotel Deal Extractor — Relaxos demo projekt
   (offline režim — pattern matching engine)
============================================================

📧 Akciové pobyty LETO 2025 (recepcia@hoteltatry.sk)
   ✅ Nájdených 2 ponúk
   🟢 Romantický víkend    | 126€ (30% zľava) | istota: 100%
   🟢 Rodinný pobyt        | 195€ (25% zľava) | istota: 100%

📧 Special offers AquaCity (sales@aquacity-resort.com)
   ✅ Nájdených 2 ponúk
   🟢 Standard Double Room | 147€ (30% zľava) | istota: 86%
   🟢 Deluxe Room spa view | 224€ (30% zľava) | istota: 86%

📧 Ponuka pobytov (info@grandhotelzilina.sk)
   ✅ Nájdených 2 ponúk
   🟢 Mestský relax balíček | 108.50€ (30% zľava) | istota: 86%
   🟢 Business Twin Room    | 140€   (20% zľava) | istota: 86%

💾 Excel uložený: output/deals_20250601_102311.xlsx
============================================================
Celkový počet ponúk:     6
🟢 Vysoká istota (≥85%): 6
Priemerná zľava:         27.5%
```

### Výstupný Excel

Súbor obsahuje dva sheety:

**Sheet 1 — Akciové pobyty** (farebne formátovaný)

| Hotel | Hviezdy | Lokalita | Názov akcie | Cena pred | Cena po | Zľava | Istota |
|---|---|---|---|---|---|---|---|
| Hotel Tatry | ⭐⭐⭐⭐ | Vysoké Tatry | Romantický víkend | 180€ | 126€ | 30% | 🟢 100% |
| AquaCity Resort | ⭐⭐⭐⭐⭐ | Poprad | Early Booking | 210€ | 147€ | 30% | 🟢 86% |

**Sheet 2 — Súhrn** (štatistiky extrakcie)

---

## 🔄 Confidence score — ako funguje

Každá extrahovaná ponuka dostane skóre podľa počtu úspešne vyplnených polí:

| Polia nájdené | Istota | Akcia |
|---|---|---|
| 7 / 7 | 🟢 100% | Auto-import do katalógu |
| 6 / 7 | 🟢 86% | Auto-import do katalógu |
| 4 / 7 | 🔴 57% | Notifikácia na manuálnu kontrolu |

---

## 🔄 Produkčná architektúra (n8n workflow)

```
Gmail trigger (nový e-mail od hotela)
    ↓
n8n: Extract email body
    ↓
AI node (Claude / Gemini API) alebo pattern matching
    ↓
Confidence score validácia
    ↓
    ├── score ≥ 85% → Auto-import do Google Sheets / katalógu
    └── score < 60% → Slack notifikácia na manuálnu kontrolu
```

---

## 📁 Štruktúra projektu

```
hotel-deal-extractor/
├── extractor.py        # Hlavný skript — extrakcia + Excel export
├── sample_emails.py    # Vzorové e-maily (4 hotely, SK + EN)
├── output/
│   ├── deals_*.xlsx   # Výstupný Excel súbor
│   └── deals_*.json   # JSON pre API integráciu
└── README.md
```

---

*Demo projekt vytvorený ako ukážka pre pozíciu AI konzultant @ Netmarketer / Relaxos*
