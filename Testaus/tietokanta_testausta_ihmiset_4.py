# Tietokanta testausta - ihmiset - lisää random hakuja

# ladattavat kirjastot

import mysql.connector

# omat funktiot

def hae_työntekijät_joilla_palkka_yli(raja):
    kysely = f"SELECT * FROM työntekijä where palkka > {raja};"
    print(kysely)
    kursori = db_ihmiset.cursor() # palauttaa listan jonka alkiot monikkoja, myös dict onnistuu: dictionary=True
    kursori.execute(kysely)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for rivi in tulos:
            print(f"{rivi[2]} {rivi[1]}, palkka {rivi[6]} euroa.")

def päivitä_palkkaa(numero, uusi_palkka):
    sql = f"UPDATE Työntekijä SET Palkka={uusi_palkka} WHERE Numero={numero}"
    print(sql)
    kursori = db_ihmiset.cursor()
    kursori.execute(sql)
    if kursori.rowcount == 1:
        print("Palkka päivitetty")

def hae_työntekijät():
    kysely = f"SELECT * FROM työntekijä order by numero;"
    print(kysely)
    kursori = db_ihmiset.cursor() # palauttaa listan, myös dict onnistuu: dictionary=True
    kursori.execute(kysely)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        print(tulos)
        return tulos
    else:
        return None


# main pääohjelma

db_ihmiset = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='ihmiset',
    user='tontsah',
    password='tontsah1234',
    autocommit=True
)

duunarit = hae_työntekijät()
if duunarit is not None:
    for rivi in duunarit:
        print(f"Työntekijä numero {rivi[0]} on nimeltään {rivi[2]} {rivi[1]}.")
else:
    print('Duunareita ei löytynyt')

'''
palkkaraja = input("Anna haettava palkkaraja: ")
hae_työntekijät_joilla_palkka_yli(palkkaraja)

numero = int(input("Anna työntekijän järjestysnumero: "))
uusi_palkka = float(input("Anna uusi palkka: "))
päivitä_palkkaa(numero, uusi_palkka)
'''