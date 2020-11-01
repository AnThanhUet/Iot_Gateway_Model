import pymysql
import json
from datetime import datetime
def Sensors(jsonData):
        
	json_Dict = json.loads(jsonData)
	print(jsonData)
	SensorID = json_Dict['ID']
	print("SensorID: " + str(SensorID))

	Temperature = json_Dict['Temperature']
	print("Temperature: " + str(Temperature))

	Humidity = json_Dict['Humidity']
	print("Humidity: " + str(Humidity))

	Light = json_Dict['Light']
	print("Light: " + str(Light))

	Move = json_Dict['Move']
	print("Move: " + str(Move))

	date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	print("Date: " + str(date_time))

	db = pymysql.connect("localhost", "root", "admin999999999", "iotgateway")
	cursor = db.cursor()
	
	cursor.execute("INSERT INTO DataGateway (temperature,humidity,light,move,time) VALUES(%s,%s,%s,%s,%s)",(Temperature,Humidity,Light,Move,date_time))
	print("SAVE DATABASE IotGateway!")
	db.commit()
	db.close()


