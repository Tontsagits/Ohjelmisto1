# Ohjelmisto 1 - Moduuli 7 - Tehtävä 3 - Lentoasemat

lentoasemat = {}
valinta = "alku"

lentoasemat["EFHK"] = "Helsinki Airport (Helsinki-Vantaa Airport)"
lentoasemat["EFJO"] = "Joensuu Airport"
lentoasemat["EFVA"] = "Vaasa Airport"
lentoasemat["EFJY"] = "Jyvaskyla Airport"
lentoasemat["ESSA"] = "Stockholm Arlanda Airport"
lentoasemat["ESKN"] = "Stockholm Skavsta Airport"
lentoasemat["ESSU"] = "Eskilstuna Airport"
lentoasemat["ESSL"] = "Linkoping City Airport"

while True:
    valinta = str.lower(input("Haluatko syöttää uuden lentoaseman (uusi), hakea jo syötetyn lentoaseman (haku), listata tallennetut lentoasemat (lista), vai lopettaa (lopetus)? "))
    if valinta == "lopetus" or valinta == "" or valinta == " " :
        break
    elif valinta == "uusi":
        icaokoodi = str.upper(input("Anna lentoaseman ICAO koodi: "))
        lentoasema = input("Anna lentoaseman nimi: ")
        lentoasemat[icaokoodi] = lentoasema
    elif valinta == "haku":
        hakukoodi = str.upper(input("Anna lentoaseman ICAO koodi: "))
        if hakukoodi in lentoasemat:
            print(f"ICAO koodi {hakukoodi} on {lentoasemat[hakukoodi]}")
    elif valinta == "lista":
        for avain, arvo in lentoasemat.items():
            print(f"ICAO koodi {avain} on {arvo}")
