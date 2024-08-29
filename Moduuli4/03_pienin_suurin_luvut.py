# Ohjelmisto 1 - Moduuli 4 - Tehtävä 3 - Pienin ja suurin luku annetuista

pienin = ''
suurin = ''
alku = 0

while True:
    luku = input('Anna luku (tyhjä lopettaa): ')
    if alku == 0 and len(luku) != 0 and luku != ' ': # alustetaan muuttujat ensimmäisellä käyttäjän syöttämällä luvulla
        pienin = luku
        suurin = luku
        alku += 1 # tässä käydään vain yhden kerran ohjelmassa
    if len(luku) == 0: # jos käyttäjä syöttää ei mitään, lopetaan
        break
    if luku == ' ': # jos käyttäjä syöttää välilyönnin, lopetetaan
        break
    if luku < pienin: # jos uusi syötetty luku on pienempi
        pienin = luku
    if luku > suurin: # jos uusi syötetty luku on suurempi
        suurin = luku
# tulostetaan lopputulos vain jos käyttäjä on syöttänyt jotain käypiä arvoja
# jos ei ole niin tulostetaan vain heippa
if len(pienin) != 0 and len(suurin) != 0:
    print(f'Suurin luku {suurin} ja pienin luku on {pienin}.')
else:
    print('Heippa!')
