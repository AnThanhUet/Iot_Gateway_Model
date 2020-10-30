import paho.mqtt.client as mqtt
import json

from sendFromGatewayToMcu import publish_NodeMcu
from InsertOperationLampIntoDatabase import OperationLamp
from datetime import datetime

# MQTT setting
MQTT_Broker = "tntholdings.ddns.net"
MQTT_Topic = "v1/devices/me/rpc/request/+" # topic tu thingsboard
Interval = 7200 
MQTT_Port = 1883 

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
        print ("Unable to connect to MQTT Broker...")
    else:
        print ("Connected with MQTT Broker: " + str(MQTT_Broker))

    client.subscribe(MQTT_Topic,1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

       try:
               json_Dict = json.loads(msg.payload)
               status=""
               data={}
               try:
                    t =json_Dict['method']
                    if t != "checkStatus":
                       t1 = json_Dict['params']
                       print(t)
                       print(t1)
                       data[t] = t1
                       print(msg.payload)
                       if t1 == True:
                          status = "ON"
                       else:
                          status = "OFF"
                       OperationLamp(t,status)
                       client.publish('v1/devices/me/attributes',json.dumps(data))
                       publish_NodeMcu(msg.payload)
                       print(datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                       
               except:
                    print("")
       except:
           print("!")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username = "iot.02@tnt.associates", password = "19001234")
client.connect(MQTT_Broker, 1883, 3600)
client.loop_forever()

