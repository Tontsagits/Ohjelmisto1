# Moduuli 3 - Tehtävä 1 - Kuhan pituus, ehtolause if

hyttiluokka = str.lower(input('Anna hyttiluokka: '))

if hyttiluokka == 'lux':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka == 'a':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == 'b':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == 'c':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')

