import paho.mqtt.client as mqtt
import json
import random
from time import sleep
#from publish_thingsboard import pub
from save_database import save

# MQTT setting
MQTT_Broker = "192.168.137.68"
MQTT_Port = 1883
Keep_Alive_Interval = 7200
MQTT_Topic = 'hello'

# Callback server
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
    else:
        print("Connection returned result: " + str(MQTT_Broker))
    client.subscribe(MQTT_Topic, qos = 1)

# Callback on_message server
def on_message(client, userdata, msg):
    print("Subscribe Message Recieved: "+msg.payload.decode())
   # pub(msg.payload)
    #save(msg.payload.decode()) #save database
    #mosquitto_pub -d -t hello -m "{\"Area\":\"xuanthuy\",\"ID\":1,\"Temperature\":4,\"Humidity\":45}"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
client.loop_forever()
