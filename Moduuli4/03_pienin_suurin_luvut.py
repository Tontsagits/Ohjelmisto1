# Ohjelmisto 1 - Moduuli 4 - Tehtävä 3 - Pienin ja suurin luku annetuista

pienin = ''
suurin = ''
alku = 0

while True:
    luku = input('Anna luku (tyhjä lopettaa): ')
    if alku == 0:
        pienin = luku
        suurin = luku
        alku += 1
    if len(luku) == 0:
        print('Heippa!')
        break
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
print(f'Suurin luku {suurin} ja pienin luku on {pienin}.')
