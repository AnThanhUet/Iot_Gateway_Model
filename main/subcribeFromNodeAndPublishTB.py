import paho.mqtt.client as mqtt
import random
import json 
from datetime import datetime
from publishNode1 import pb1
from publishNode2 import pb2
from publishNode3 import pb3
from InsertDataIntoDatabase import Sensors
from InsertOperationLampIntoDatabase import OperationLamp
from publishStatusLed import pbLed


#MQTT setting
broker_url="192.168.1.244"
broker_port = 1883
Interval = 7200
MQTT_Topic = "sensor_tx"

sw_data={}

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
    else:
        print("Connected with MQTT Broker: "+str(broker_url))
    client.subscribe(MQTT_Topic, qos=1)
    client.subscribe("node2", qos=1)
    client.subscribe("statusLed", qos=1)

def on_message_from_node3(client, userdata, message):
   print("Message Recieved from node3: "+message.payload.decode())

def on_message_from_statusLed(client, userdata, message):
   print("Message Recieved from statusLed: "+message.payload.decode())
   StatusLed ={}
   t = json.loads(message.payload)
   StatusLed['R1'] = t['R1']
   StatusLed['R2'] = t['R2']
   print(json.dumps(StatusLed))
   pbLed(json.dumps(StatusLed))
   
def on_message_from_node2(client, userdata, message):
   print("Message Recieved from Node2: "+message.payload.decode())
   pb2(message.payload) 

def on_message(client, userdata, msg):
    print("Message Recieved from XuanThuy: "+msg.payload.decode())
    pb1(msg.payload) 
    # luu vao database 
    Sensors(msg.payload) 
    t = json.loads(msg.payload)
    print("t = " + str(t))
    pbLed(json.dumps(t))

client = mqtt.Client()
client.on_connect = on_connect

#To Process Every Other Message
client.on_message = on_message
client.connect(broker_url, broker_port,3600)
client.username_pw_set(username="dvioemit",password="WJzmH3j7O6kH")
client.message_callback_add("statusLed", on_message_from_statusLed)
client.message_callback_add("node2", on_message_from_node2)
client.message_callback_add("node3", on_message_from_node3)
client.loop_forever() 