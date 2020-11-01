import pymysql

db = pymysql.connect("localhost", "anthanh", "25041999", "Lamp")
cursor = db.cursor()

cursor.execute("CREATE TABLE ControlLamp(id INT(10) PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255) NOT NULL,time VARCHAR(255) NOT NULL,status VARCHAR(255) NOT NULL)")
