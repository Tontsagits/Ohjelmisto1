# Tietokanta testausta - ihmiset - lisää random hakuja

# ladattavat kirjastot

import mysql.connector

# omat funktiot

def hae_lentoketta_maa_koodilla(maa):
    sql = f"SELECT id, ident, name, municipality FROM airport WHERE iso_country = %s;"
    print(sql)
    kursori = db_lentopeli.cursor()
    kursori.execute(sql, (maa,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
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

code = input('Syötä lentokentän maatunnus: ')
lentokentta = hae_lentoketta_maa_koodilla(code)
if lentokentta is not None:
    for rivi in lentokentta:
        print(f"{rivi[1]} on {rivi[2]} ja sijaitsee paikkakunnalla {rivi[4]}.")
else:
    print('Lentokenttiä ei löytynyt')
