"""
Vzorové e-maily od hotelov v rôznych formátoch.
Simulujú reálny vstup, ktorý Relaxos dostáva od stoviek hotelov.
"""

SAMPLE_EMAILS = [
    {
        "id": "email_001",
        "from": "recepcia@hoteltatry.sk",
        "subject": "Akciové pobyty LETO 2025",
        "body": """
Dobrý deň,

dovoľujeme si Vám ponúknuť naše letné akciové pobyty:

Hotel Tatry **** - Vysoké Tatry, Tatranská Lomnica

AKCIA 1: Romantický víkend
- Termín: 1.6.2025 - 30.8.2025 (len víkendy)
- Typ izby: Dvojlôžková izba Superior
- Bežná cena: 180 EUR/noc
- Akciová cena: 126 EUR/noc (zľava 30%)
- Zahŕňa: raňajky pre 2 osoby, wellness vstup

AKCIA 2: Rodinný pobyt
- Termín: 15.6.2025 - 31.8.2025
- Typ izby: Apartmán Family (2+2)
- Bežná cena: 260 EUR/noc
- Akciová cena: 195 EUR/noc (zľava 25%)
- Zahŕňa: polpenzia, deti do 12 rokov zadarmo

Kontakt: recepcia@hoteltatry.sk | +421 52 123 456
"""
    },
    {
        "id": "email_002",
        "from": "sales@aquacity-resort.com",
        "subject": "Special offers - AquaCity Resort Poprad",
        "body": """
Dear partners,

We are pleased to present our exclusive deals for summer season 2025:

AquaCity Resort Poprad - 5 star resort

>> EARLY BOOKING DISCOUNT <<
Valid: June 1 - September 30, 2025
Room: Standard Double Room
Regular price: 210 EUR
Special price: 147 EUR (-30% discount)
Includes: breakfast, unlimited AquaCity waterpark access

>> SPA RETREAT PACKAGE <<
Valid: 1.7.2025 - 31.8.2025
Room: Deluxe Room with spa view
Regular: 320 EUR/night
Offer: 224 EUR/night (save 30%)
Includes: HB, 2x 60min massage, private spa

Minimum stay: 2 nights
For reservations: sales@aquacity-resort.com
"""
    },
    {
        "id": "email_003",
        "from": "rezervacie@penzionhorna.sk",
        "subject": "Cenník a akcie - Penzión Horná Lehota",
        "body": """
Zdravím,

posielam aktuálny cenník akcií pre vašu databázu.

Penzión Horná Lehota ** - Nízke Tatry, Chopok

Izba: 2-lôžková štandardná
Platnosť: 01.06.2025 - 30.09.2025
Cena pred zľavou: 75€
Cena po zľave: 60€
Zľava: 20%
Strava: raňajky

Izba: 2-lôžková s balkónom
Platnosť: 01.07.2025 - 31.08.2025
Cena pred zľavou: 90€
Cena po zľave: 67,50€
Zľava: 25%
Strava: polpenzia

Poznámka: Psi povolení za príplatok 10€/noc.
Tel: 0905 123 789
"""
    },
    {
        "id": "email_004",
        "from": "info@grandhotelzilina.sk",
        "subject": "Ponuka pobytov",
        "body": """
Vážení partneri,

Grand Hotel Žilina **** ponúka pre vašich klientov tieto špeciálne ponuky:

Mestský relax balíček
Obdobie platnosti: celý rok 2025 (okrem 24.12-1.1)
Kategória ubytovania: Superior dvojlôžková izba
Pôvodná cena za noc: 155,00 EUR
Zvýhodnená cena: 108,50 EUR
Percentuálna zľava: 30%
Zahrnuté služby: bohaté bufetové raňajky, parkovanie zdarma, neskorý odchod do 14:00

Konferenčný balíček pre 2
Platnosť: pracovné dni, celý rok 2025
Izba: Business Twin Room
Štandardná cena: 175 EUR/noc
Akciová cena: 140 EUR/noc (20% off)
Obsahuje: raňajky, rýchly WiFi, použitie konferenčnej sály 2h zdarma

S pozdravom,
Obchodné oddelenie Grand Hotel Žilina
"""
    }
]
