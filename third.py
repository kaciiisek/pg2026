
def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni
    prvocislo a vrati True nebo False.
    """

    if cislo <= 1:
        return False

    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1
    az maximum a vrati je jako seznam.
    """

    prvocisla = []

    for i in range(2, int(maximum) + 1):
        if je_prvocislo(i):
            prvocisla.append(i)

    return prvocisla


if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
