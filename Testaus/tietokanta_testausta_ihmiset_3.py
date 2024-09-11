# Tietokanta testausta - ihmiset - lisää random hakuja

# ladattavat kirjastot

import mysql.connector

# omat funktiot

def hae_työntekijät_joilla_palkka_yli(raja):
    kysely = f"SELECT * FROM työntekijä where palkka > {raja};"
    print(kysely)
    kursori = db_ihmiset.cursor() # palauttaa listan, myös dict onnistuu: dictionary=True
    kursori.execute(kysely)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for rivi in tulos:
            print(f"{rivi[2]} {rivi[1]}, palkka {rivi[6]} euroa.")

# main pääohjelma

db_ihmiset = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='ihmiset',
    user='tontsah',
    password='tontsah1234',
    autocommit=True
)

palkkaraja = input("Anna haettava palkkaraja: ")
hae_työntekijät_joilla_palkka_yli(palkkaraja)
