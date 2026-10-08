def vynasob_xty_prvek(seznam, x, nasobek):
    """funkce vezme x-ty prvek seznamu (zadano jako 1 pro prvni prvek), 
    vynasobi ho pomoci * nasobkem a ulozi zpet do seznamu na puvodni pozici.
    Pozor, seznam muze mit mene prvku nez x"""

  
    if len(seznam) < x:
        print("V seznamu neni tolik prvku")
        return seznam
    x-= 1
    if x < 0:
        print("Zadany index je zaporny")
        return seznam
      
    seznam[x] *= nasobek
    seznam[x] = seznam[x] * nasobek
    return seznam

def spocitej_prumer(seznam):
    """funkce spocita prumer cisel v seznamu"""
    soucet = sum(seznam)
    delka = len(seznam)
    if delka <= 0:
        print("Prazdny seznam")
        return None
    prumer = soucet / delka
    return prumer

def formatuj_text(student):
    prumer = spocitej_prumer(student["znamky"])
    prumer = round(prumer, 1)
    text = f"Student {student['jmeno']} {student['prijmeni']}, Vek: {student['vek']}, Prumer: {prumer}"
    return text


if __name__ == "__main__":

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]}
    print(formatuj_text(student))
    
    #   #vek = input("zadej svuj vek: ")
    #   vek = int(vek)

    # if vek >= 21:
            #   print("Muzes pit v USA")
    #else:
    #    print("Dej si colu")   

    #   vek += 1
    #   print(f"Za rok ti bude {vek}")

    #   seznam = [1, 2, 3, "ctyri", 5]
    #   print(seznam)
    #   seznam.append("ahoj")
    #   print(seznam[2])

    #   print(f"Seznam ma {len(seznam)} prvku")