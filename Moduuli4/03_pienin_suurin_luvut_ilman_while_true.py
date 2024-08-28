# Ohjelmisto 1 - Moduuli 4 - Tehtävä 3 - Pienin ja suurin luku annetuista, ilman while true

# MITEN TÄMÄN TEKISI ILMAN WHILE TRUE BREAK YHDISTELMÄÄ

pienin = ''
suurin = ''
alku = 0
lopetus = 0
luku = '0'

while luku != '':
    luku = input('Anna luku (tyhjä lopettaa): ')
    if alku == 0:
        pienin = luku
        suurin = luku
        alku += 1
    if len(luku) == 0:
        break
    if luku == ' ':
        break
    elif luku < pienin:
        pienin = luku
    elif luku > suurin:
        suurin = luku
print(f'Suurin luku {suurin} ja pienin luku on {pienin}.')



