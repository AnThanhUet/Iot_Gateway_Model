import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
# Setings Thing
THINGS_HOST = 'localhost'
ACCESS_TOKEN = 'hR5aYLkhasr5PYq9tiaZ'
THINGS_TOPIC = 'v1/devices/me/telemetry'
# Data capture 
INTERVAL=2
sensor_data = {'temperature': 0, 'humidity': 0}
next_reading = time.time() 

client = mqtt.Client()
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGS_HOST, 1883, 60)
client.loop_start()
try:
    while True:
        humidity = random.randrange(10, 70)
        temperature = random.randrange(10, 70)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity
        # Sending humidity and temperature data 
        client.publish(THINGS_TOPIC, json.dumps(sensor_data), 1)
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()