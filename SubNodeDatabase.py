import paho.mqtt.client as mqtt
import json
import random
from time import sleep
from Insert import Sensors
#from GuiThings import pd1
# MQTT setting
MQTT_Broker = "192.168.0.102"
MQTT_Port = 1883
Keep_Alive_Interval = 7200
MQTT_Topic = 'hello'

# Callback server
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
    else:
        print("Connection returned result: " + str(MQTT_Broker))
    mqttc.subscribe(MQTT_Topic, qos = 1)
    print("Subscribe: " + str(MQTT_Topic))

# Callback on_message server
def on_message(client, userdata, msg):
    #pd1(msg.payload.decode()) #publish things
    Sensors(msg.payload) #lua database
    print("Message Recieved from tang 20: "+msg.payload.decode())
    
    
    #mosquitto_pub -d -t thean -m "{\"name\":\"vlxx\",\"id\":4,\"u\":4,\"i\":6,\"w\":45}"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
mqttc.loop_forever()
