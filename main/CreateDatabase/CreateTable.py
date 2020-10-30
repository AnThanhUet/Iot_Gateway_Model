import pymysql

db = pymysql.connect("localhost", "anthanh", "25041999", "iotgateway")
cursor = db.cursor() 

cursor.execute("CREATE TABLE DataGateway(id INT(10) PRIMARY KEY AUTO_INCREMENT, temperature INT(3) NOT NULL, humidity INT(3) NOT NULL, light INT(3) NOT NULL, move INT(3) NOT NULL, time VARCHAR(255) NOT NULL)") 

