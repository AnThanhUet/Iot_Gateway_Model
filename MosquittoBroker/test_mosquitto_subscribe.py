import paho.mqtt.client as mqtt
import json
import random
from time import sleep
from datetime import datetime

# MQTT setting
MQTT_Broker = "192.168.0.102"
MQTT_Port = 1883
Keep_Alive_Interval = 7200
MQTT_Topic = 'thean'

# Callback server

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(MQTT_Broker))
    mqttc.subscribe(MQTT_Topic, qos = 1)
    print("da subscribe")
# Callback on_message server
def on_message(client, userdata, msg):
    print(str(msg.payload)) # mã bin
    print("=================================================")
    print("Message recieved from mosquitto broker: " + msg.payload.decode())
    print("=================================================")
    t = json.loads(msg.payload)
    print("message nhan duoc: " + str(t))
    print("=================================================")
    #mqttc.publish('hello', json.dumps("da nhan dc message"))
    

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.username_pw_set(username = "thean", password = "qdLpQewK")
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
mqttc.loop_forever()
