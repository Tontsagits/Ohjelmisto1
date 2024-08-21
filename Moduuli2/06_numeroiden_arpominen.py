# Moduuli 2 - 6 Numeroiden arpominen

'''
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
'''

print("Arvotaan kaksi erilaista numerolukon koodia:")

from random import randint

print("Noppa antaa:", randint(1, 6))

for i in range(7):
    print(randint(1, 40))

rivi = []
while len(rivi) < 7:
    uusi = randint(1, 40)
    if uusi not in rivi:
        rivi.append(uusi)
print(rivi)

