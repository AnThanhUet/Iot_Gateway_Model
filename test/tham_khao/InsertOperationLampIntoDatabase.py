import pymysql
import json
from datetime import datetime

def OperationLamp(name,status) :
	time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	db = pymysql.connect("localhost","root","admin999999999","Lamp")
	
	cursor = db.cursor()
	
	cursor.execute("INSERT INTO ControlLamp(name,time,status) VALUES(%s, %s, %s)",(str(name),(time),str(status)))
	print("SAVE DATABASE Lamp!")
	db.commit()
	db.close()
