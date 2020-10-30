import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'localhost'
ACCESS_TOKEN = 'VeYjm5FnygELIcDovOXS'
 
sensor_data = {'temperature': 0}
 
minA = 10 
maxA = 70
 
client = mqtt.Client()
 
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect Thing
client.connect(THINGSBOARD_HOST, 1883)
 
client.loop_start()
 
try:
	while True:
		temperature = random.randrange(minA,maxA)
		print("temperature:{:g}".format(temperature))
		sensor_data['temperature'] = temperature
		client.publish('v1/devices/me/telemetry',json.dumps(sensor_data))
		time.sleep(2)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()