# Moduuli 2 - 6 Numeroiden arpominen

'''
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
'''

print("Arvotaan kaksi erilaista numerolukon koodia:")

from random import randint

print(f"Kolmenumeroinen koodi (numerot välillä 0..9): {randint(0, 9)}{randint(0, 9)}{randint(0, 9)}")
print(f"Nelinumeroinen koodi (numerot välillä 1..6): {randint(1, 6)}{randint(1, 6)}{randint(1, 6)}{randint(1, 6)}")
