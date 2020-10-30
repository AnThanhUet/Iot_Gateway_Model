import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "anthanh",
    passwd = "25041999"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# alm the nao de runcode lien tuc
# cac nhan data ve luu vao database
