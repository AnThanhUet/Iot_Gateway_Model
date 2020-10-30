import paho.mqtt.client as mqtt
import json
import random
from datetime import datetime
from time import sleep

#MQTT settings
MQTT_Broker = "tntholdings.ddns.net" 
MQTT_Port = 1883
Keep_Alive_Interval = 7200
MQTT_Topic = 'v1/devices/me/telemetry'

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker..." + str(rc) )
	else:
		print("Connected with MQTT Broker: "+ str(MQTT_Broker))

def on_publish(client,userdata,mid):
	pass

def on_disconnect(client, userdata, rc):
	if rc != 0:
		pass

mqttc = mqtt.Client()
mqttc.username_pw_set(username = 'iot.02@tnt.associates', password = "19001234")
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker,MQTT_Port,Keep_Alive_Interval)

def pb2(jsonData):
	mqttc.publish(MQTT_Topic,jsonData)
	print(jsonData)
	