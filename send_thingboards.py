import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = 'localhost'
THINGSBOARD_PORT = 1883 
THINGSBOARD_TOPIC = 'v1/devices/me/telemetry'
ACCESS_TOKEN = 'VeYjm5FnygELIcDovOXS'
INTERVAL=2

sensor_data = {'temperature': 0, 'humidity': 7}

next_reading = time.time() 

client = mqtt.Client() 					# clinet
client.username_pw_set(ACCESS_TOKEN) 	# set access token
client.connect(THINGSBOARD_HOST, THINGSBOARD_PORT, 60)

client.loop_start()

try:
	while True:
		temperature = random.randrange(10, 70)
		humidity = random.randrange(10, 70)
		
		print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
		sensor_data['temperature'] = temperature
		sensor_data['humidity'] = humidity

		# Send things
		client.publish(THINGSBOARD_TOPIC, json.dumps(sensor_data), 1)

		next_reading += INTERVAL
		sleep_time = next_reading - time.time()
		if sleep_time > 0:
			time.sleep(sleep_time)
except KeyboardInterrupt:
	pass

"""
def pd1(jsonData):
	try:
    	client.publish('v1/devices/me/telemetry', json.dumps(jsonData), 1)
    	next_reading += INTERVAL
    	sleep_time = next_reading-time.time()
    	if sleep_time > 0:
        	time.sleep(sleep_time)
	except KeyboardInterrupt:
    	pass
"""
client.loop_stop()
client.disconnect()