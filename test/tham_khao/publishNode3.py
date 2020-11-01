import paho.mqtt.client as mqtt
import json
import random
from datetime import datetime
from time import sleep

#MQTT settings
THINGSBOARD_HOST = 'localhost'
THINGSBOARD_PORT = 1883
THINGSBOARD_TOPIC = 'v1/devices/me/telemetry'
ACCESS_TOKEN = 'hR5aYLkhasr5PYq9tiaZ'

Keep_Alive_Interval = 7200


def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker..." + str(rc) )
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client,userdata,mid):
	pass

def on_disconnect(client, userdata, rc):
	if rc != 0:
		pass

mqttc = mqtt.Client()
mqttc.username_pw_set(ACCESS_TOKEN)
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(THINGSBOARD_HOST,THINGSBOARD_PORT,Keep_Alive_Interval)

def pb3(jsonData):
	mqttc.publish(THINGSBOARD_TOPIC,jsonData)
	print("done")
	