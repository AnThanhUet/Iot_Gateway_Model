import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="anthanh",
  password="25041999",
  database="iotgateway"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)