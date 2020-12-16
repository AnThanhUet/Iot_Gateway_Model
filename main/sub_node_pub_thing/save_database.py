import pymysql
import json
from datetime import datetime

def save(data):
        
	json_Dict = json.loads(data)
	#print(data)
	Area = json_Dict['Area']
	Id = json_Dict['ID']
	Temperature = json_Dict['Temperature']
	Humidity = json_Dict['Humidity']
	db = pymysql.connect("localhost", "root", "admin999999999", "uet")
	cursor = db.cursor()
	# Execute
	cursor.execute("INSERT INTO sensors(Area, ID, Temperature, Humidity) VALUES(%s,%s,%s,%s)",(Area,Id,Temperature,Humidity))
	print(">> save database uet - table sensors!")
	db.commit()
	db.close()


