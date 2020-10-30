import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "anthanh",
    passwd = "25041999",
    database = "iotgateway"
)

cursor = db.cursor()
# DATABASE Tang 20
query = "SELECT * FROM DataIotGateway WHERE ID ='floors20'"

cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)

# DATABASE Tang B1
query = "SELECT * FROM DataIotGateway WHERE ID ='floorsB1'"

cursor.execute(query) # thuc thi cau lenh
records1 = cursor.fetchall() 

for record in records1:
    print(record)

# DATABASE tang B2
query = "SELECT * FROM DataIotGateway WHERE ID ='floorsB2'"

cursor.execute(query)
records2 = cursor.fetchall()

for record in records2:
    print(record)