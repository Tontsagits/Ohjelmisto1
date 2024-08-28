# Ohjelmisto 1 - Moduuli 4 - Tehtävä 4 - Pienin ja suurin luku annetuista

from random import randint

luku = randint(1, 10)
arvaus = -1

while arvaus != luku:
    arvaus = int(input('Arvaa mikä luku (välillä 1-10)?: '))
    if arvaus < luku:
        print('Liian pieni arvaus')
    elif arvaus > luku:
        print('Liian suuri arvaus')
print('Oikein!')
