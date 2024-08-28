# Moduuli 3 - Tehtävä 3 - Hemoglobiini

sukupuoli = str.lower(input('Anna sukupuoli (mies/nainen): '))
hemogobiiniarvo = 0

if sukupuoli == 'nainen':
    hemoglobiiniarvo = int(input('Anna hemoglobiiniarvo (numero, g/l): '))
    if hemoglobiiniarvo < 117:
        print('Hemoglobiiniarvo on matala')
    elif hemoglobiiniarvo <= 175:
        print('Hemoglobiiniarvo on normaali')
    else:
        print('Hemoglobiiniarvo on korkea')
elif sukupuoli == 'mies':
    hemoglobiiniarvo = int(input('Anna hemoglobiiniarvo (numero, g/l): '))
    if hemoglobiiniarvo < 134:
        print('Hemoglobiiniarvo on matala')
    elif hemoglobiiniarvo <= 195:
        print('Hemoglobiiniarvo on normaali')
    else:
        print('Hemoglobiiniarvo on korkea')
else:
    print('Tarvitaan sukupuoli (mies/nainen)')
