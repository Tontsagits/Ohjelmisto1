# Moduuli 3 - Tehtävä 4 - Karkausvuosi

vuosi = int(input("Anna vuosi: "))
if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 100 == 0 and vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
