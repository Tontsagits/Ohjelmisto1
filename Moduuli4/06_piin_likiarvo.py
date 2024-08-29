# Ohjelmisto 1 - Moduuli 4 - Tehtävä 6 - Piin likiarvo

'''
Toteutetaan algoritmi piin (π) likiarvon laskemiseksi.
Oletetaan, että A on yksikköympyrä eli ympyrä, jonka
keskipiste on origossa ja jonka säde on yksi (1).
Sen ympärille piirretään pienin mahdollinen neliö B
siten, että ympyrä A jää kokonaan neliön sisäpuolelle.
'''

from random import uniform

while True:
    # arvottavien koordinaattien lukumäärä
    N = int(input('Anna arvottavien pisteiden määrä (0 lopettaa): '))
    if N == 0:
        break
    # arvontakerrat alussa
    kerrat = 0
    # ympyrän sisälle osuneet alussa
    n = 0
    # toteutetaan laskenta
    while kerrat < N:
        # arvotaan pisteiden x ja y koordinaatteja
        x = uniform(0,1)
        y = uniform(0,1)
        # selvitetään osuuko piste ympyrän A sisälle
        if x ** 2 + y ** 2 < 1:
            # jos osuu kasvatetaan osumien määrää yhdellä
            n += 1
        # muistetaan kasvattaa tehtyjen arvontojen määrää aina yhdellä per kerta
        kerrat += 1
    # lasketaan pii:n likiarvo
    pii = (4 * n) / N
    print(f'Pii:n likiarvo on noin {pii:.5f}')
