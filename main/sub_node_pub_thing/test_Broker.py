import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
# Seting broker
BROKER_HOST = '192.168.0.101'
BROKER_TOPIC = 'hello'
# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2
#mosquitto_pub -d -t hello -m "{\"Area\":\"xuanthuy\",\"ID\":1,\"Temperature\":4,\"Humidity\":45}"

sensor_data = {'Area': 'XuanThuy', 'ID': 1, 'Temperature': 0, 'Humidity': 0}
next_reading = time.time() 
client = mqtt.Client()
# Set access token
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(BROKER_HOST, 1883, 60)
client.loop_start()

try:
    while True:
        humidity = random.randrange(10, 70)
        temperature = random.randrange(10, 70)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        sensor_data['Temperature'] = temperature
        sensor_data['Humidity'] = humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish(BROKER_TOPIC, json.dumps(sensor_data), 1)
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()