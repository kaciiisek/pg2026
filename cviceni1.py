def add(a, b):
    c = a + b 
    return c

def mul (a, b, c):
    vysledek = a * b * c
    return vysledek

def div(a, b):
    if b == 0:
        deleno = 0
    else:
        deleno = a/b
    return deleno


def je_beze(a,b):
    x = a % b
    if x == 0:
        return "je beze"
    else:

        return "neni beze"

def je_delitelne_3(a):
    
    return je_beze(a,3)

if __name__ == "__main__":
    # x = add(1, 2)
    # x = mul(1,2,3)
    # x = div(30,5)
    # vysledek = je_beze(10,5)
    # vysledek = je_delitelne_3(9)
    print(vysledek)