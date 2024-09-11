# Ohjelmisto 1 - Moduuli 8 - Tehtävä 3 - Lentokenttien väliset etäisyydet


# ladattavat kirjastot

import mysql.connector
import geopy

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

icaot1 = input('Syötä ensimmäisen lentokentän ICAO tunnus: ')
icaot2 = input('Syötä ensimmäisen lentokentän ICAO tunnus: ')
etaisyys = laske_kenttien_etaisyys(icaot1, icaot2)
if etaisyys is not None:
    print(f"{rivi[1]} on {rivi[2]} ja sijaitsee paikkakunnalla {rivi[3]}.")
else:
    print('Lentokenttiä ei löytynyt.')
