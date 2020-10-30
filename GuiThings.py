#import os
#import time
#import sys
#import paho.mqtt.client as mqtt
#import json
#THINGSBOARD_HOST = 'tntholdings.ddns.net'
#ACCESS_TOKEN = 'EUt3c7UQDYqlTy4cunVT'
#INTERVAL=2
#sensor_data = {'temperature': 1, 'humidity': 7}
#next_reading = time.time() 
#client = mqtt.Client()
#client.username_pw_set(ACCESS_TOKEN)
#client.connect(THINGSBOARD_HOST, 1883, 60)
#client.loop_start()
#try:
#	client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
#	next_reading += INTERVAL
#	#sleep_time = next_reading-time.time()
#	if sleep_time > 0:
##		time.sleep(sleep_time)
#	except KeyboardInterrupt:
#		pass

#client.loop_stop()
#client.disconnect()