def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    # 1. KROK: Je cílová pozice na šachovnici?
    radek, sloupec = cilova_pozice
    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

    # 2. KROK: Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. KROK: Pohyb podle typu figury
    rozdil_radku = abs(cilova_pozice[0] - aktualni_pozice[0])
    rozdil_sloupcu = abs(cilova_pozice[1] - aktualni_pozice[1])

    if typ == "král":
        if rozdil_radku <= 1 and rozdil_sloupcu <= 1:
            return True

    elif typ == "jezdec":
        if (rozdil_radku == 2 and rozdil_sloupcu == 1) or \
           (rozdil_radku == 1 and rozdil_sloupcu == 2):
            return True

    return False
