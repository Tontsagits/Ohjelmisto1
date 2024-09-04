# Ohjelmisto 1 - Moduuli 6 - Tehtävä 2 - Heitä noppaa kunnes kuusi, kaikki tahkot

from random import randint

def noppa(luku):
    return randint(1,luku)

maksimi = int(input("Anna nopan suurin silmäluku: "))

tulos = 0

while tulos < maksimi:
    tulos = noppa(maksimi)
    print(f"Noppa heitti: {tulos}")

