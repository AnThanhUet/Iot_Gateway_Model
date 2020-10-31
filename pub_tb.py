import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'localhost'
THINGSBOARD_PORT = 1883 
THINGSBOARD_TOPIC = 'v1/devices/me/telemetry'
ACCESS_TOKEN = 'abc'
INTERVAL=2

sensor_data = {'temperature': 0, 'humidity': 7}
next_reading = time.time() 
client = mqtt.Client() 					# clinet
client.username_pw_set(ACCESS_TOKEN) 	# set access token
client.connect(THINGSBOARD_HOST, THINGSBOARD_PORT, 60)

def pb1(jsonData):
	client.publish(THINGSBOARD_TOPIC, json.dumps(jsonData))
	print("Gui things")
client.loop_stop()
client.disconnect()
