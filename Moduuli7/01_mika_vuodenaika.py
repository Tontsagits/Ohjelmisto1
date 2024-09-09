# Ohjelmisto 1 - Moduuli 7 - Tehtävä 1 - Mikä vuodenaika

vuodenaika = 9
vuodenajat = "kevat", "kesa", "syys", "talvi"
kuukausi = int(input("Kuinka mones kuukausi on? "))
if 2 < kuukausi < 6:
    vuodenaika = 1
elif 5 < kuukausi < 9:
    vuodenaika = 2
elif 8 < kuukausi < 12:
    vuodenaika = 3
elif 11 < kuukausi < 3:
    vuodenaika = 4
print(f"{kuukausi}. kuukausi on {vuodenajat[vuodenaika-1]}kuukausi.")
