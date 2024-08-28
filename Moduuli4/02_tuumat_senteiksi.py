# Ohjelmisto 1 - Moduuli 4 - Tehtävä 2 - Tuumat senteiksi

while True:
    tuumat = float(input('Anna luku tuumina (negatiivinen luku lopettaa): '))
    if tuumat < 0:
        print('Heippa!')
        break
    print(f'{tuumat} tuumaa on {tuumat/2.54:.2f} cm.')
