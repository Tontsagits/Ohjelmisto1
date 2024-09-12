# Ohjelmisto 1 - Moduuli 8 - Tehtävä 2 - Laske kenttien lukumäärät

# ladattavat kirjastot

import mysql.connector

# omat funktiot

def laske_lentokenttatyypit_koodilla(tunnus):
    kysely = f"SELECT count(*), type FROM airport WHERE iso_country = %s GROUP BY type order by type;"
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

maatunnus = input('Syötä laskettavien lentokenttien maatunnus: ')
lentokenttatyypit = laske_lentokenttatyypit_koodilla(maatunnus)
if lentokenttatyypit is not None:
    print(f"Maassa {maatunnus} olevat lentokenttätyypit:")
    for rivi in lentokenttatyypit:
        print(f"{rivi[1]} {rivi[0]} kpl.")
else:
    print('Lentokenttiä ei löytynyt.')
