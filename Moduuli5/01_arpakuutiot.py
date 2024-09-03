# Ohjelmisto 1 - Moduuli 5 - Tehtävä 1 - Arpakuutiot

from random import randint

maara = int(input('Montaako arpakuutiota heitetään? '))
summa = 0

for _ in range(maara):
    summa += randint(1,6)

print(f'summa: {summa}')
