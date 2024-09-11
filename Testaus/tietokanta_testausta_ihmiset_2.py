# Tietokanta testausta - ihmiset - random hakuja

# ladattavat kirjastot

import mysql.connector

# omat funktiot


# main pääohjelma

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='ihmiset',
         user='tontsah',
         password='tontsah1234',
         autocommit=True
         )
