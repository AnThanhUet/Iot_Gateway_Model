import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "anthanh",
    passwd = "25041999")
cursor = db.cursor() 

cursor.execute("CREATE DATABASE iotgateway") 
