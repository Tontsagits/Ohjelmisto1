# MySQL Connector plugin testausta

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tontsah",
  password="tontsah1234"
)

print(mydb)

