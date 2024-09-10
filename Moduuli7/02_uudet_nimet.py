# Ohjelmisto 1 - Moduuli 7 - Tehtävä 2 - Uudet nimet

nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopetta): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
for alkio in nimet:
    print(alkio)
