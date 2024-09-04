# Ohjelmisto 1 - Moduuli 6 - Tehtävä 1 - Heitä noppaa kunnes kuusi, funktiolla

from random import randint

def noppa():
    return randint(1,6)

tulos = 0

while tulos != 6:
    tulos = noppa()
    print(f"Noppa heitti: {tulos}")
