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

# Callback 
def on_publish(client, userdata, mid):
    #print("onpublish")
    mqttc.publish(MQTT_Topic, json.dumps("da nhan thanh cong"))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
#mqttc.username_pw_set(username = "thean", password = "qdLpQewK")S
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.publish(MQTT_Topic, json.dumps("on")) 

mqttc.loop_forever()

# rc: ket qua cua ket noi thanh cong hay khong
# mid: ID thong bao cho yeu cau xuat ban