# Ohjelmisto 1 - Moduuli 5 - Tehtävä 1 - Arpakuutiot

from random import randint

maara = int(input('Montaako arpakuutiota heitetään? '))

for i in range(maara):
    noppa = randint(1,6)
    print(f'noppa näyttää luku: {noppa}')
