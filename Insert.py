import pymysql
import json
from datetime import datetime

def Sensors(jsonData):
        
	json_Dict = json.loads(jsonData)
	print(jsonData)
	

	name = json_Dict['name']

	id = json_Dict['id']

	u = json_Dict['u']

	i = json_Dict['i']

	w = json_Dict['w']

	db = pymysql.connect("localhost", "anthanh", "25041999", "demo")
	cursor = db.cursor()
	
	cursor.execute("INSERT INTO data(name, id, u, i, w) VALUES(%s,%s,%s,%s,%s)",(name,id,u,i,w))
	print("SAVE DATABASE IotGateway!")
	db.commit()
	db.close()


