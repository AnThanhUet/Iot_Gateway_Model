import pymysql

db = pymysql.connect("localhost", "anthanh", "25041999")
cursor = db.cursor()

cursor.execute("CREATE DATABASE Lamp") 
