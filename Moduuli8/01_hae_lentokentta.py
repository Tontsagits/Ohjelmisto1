# Ohjelmisto 1 - Moduuli 8 - Tehtävä 3 - Hae lentokenttä

# ladattavat kirjastot

import mysql.connector

# omat funktiot

def hae_lentokentta_koodilla(tunnus):
    kysely = f"SELECT id, ident, name, municipality FROM airport WHERE ident = %s;"
    # print(kysely)
    kursori = db_lentopeli.cursor()
    kursori.execute(kysely, (tunnus,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        # print(tulos)
        return tulos
    else:
        return None


# main pääohjelma

db_lentopeli = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='tontsah',
    password='tontsah1234',
    autocommit=True
)

icaotunnus = input('Syötä lentokentän ICAO tunnus: ')
lentokentta = hae_lentokentta_koodilla(icaotunnus)
if lentokentta is not None:
    for rivi in lentokentta:
        print(f"{rivi[1]} on {rivi[2]} ja sijaitsee paikkakunnalla {rivi[3]}.")
else:
    print('Lentokenttiä ei löytynyt')
