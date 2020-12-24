import paho.mqtt.client as mqtt
import json
import random
from datetime import datetime
from time import sleep
# Thingsboard settings
THINGSBOARD_HOST = '192.168.137.32' #'localhost'
THINGSBOARD_PORT = 1883
THINGSBOARD_TOPIC = 'v1/devices/me/telemetry'
ACCESS_TOKEN = 'hR5aYLkhasr5PYq9tiaZ'

Keep_Alive_Interval = 7200
# Connect Broker
def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker..." + str(rc) )
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))
# func publish 
def on_publish(client,userdata,mid):
	pass
# func disconnect
def on_disconnect(client, userdata, rc):
	if rc != 0:
		pass
# create clint
mqttc = mqtt.Client()
mqttc.username_pw_set(ACCESS_TOKEN)
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(THINGSBOARD_HOST,THINGSBOARD_PORT,Keep_Alive_Interval)

def pub(jsonData):
	mqttc.publish(THINGSBOARD_TOPIC,jsonData)
	print(">> publish server!")
	