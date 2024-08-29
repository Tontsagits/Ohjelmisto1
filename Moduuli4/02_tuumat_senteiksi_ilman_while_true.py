# Ohjelmisto 1 - Moduuli 4 - Tehtävä 2 - Tuumat senteiksi, ilman while true boolean

tuumat = 0
while tuumat >= 0:
    tuumat = float(input('Anna luku tuumina (negatiivinen luku lopettaa): '))
    if tuumat < 0: # jos käyttäjä syöttää negatiivisen lopetetaan heti, ei tulosteta negatiivista
        continue # tämän voi jättää pois jos haluaa että yksi negatiivinen tulostuu
    print(f'{tuumat} tuumaa on {tuumat/2.54:.2f} cm.')
print('Heippa!')
