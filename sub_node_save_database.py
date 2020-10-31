import paho.mqtt.client as mqtt
import json
import random
from time import sleep
from pub_tb import pb1
#from save_database import save
# MQTT setting
MQTT_Broker = "192.168.1.237"
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
    print("Subscribe: ")

# Callback on_message server
def on_message(client, userdata, msg):
    print("Message Recieved: "+msg.payload.decode())

    pb1(msg.payload.decode()) #publish things

    #save(msg.payload) #save database
    #mosquitto_pub -d -t hello -m "{\"Area\":\"xuanthuy\",\"STT\":1,\"Temperature\":4,\"Humidity\":45}"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
client.loop_forever()
