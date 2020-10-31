import paho.mqtt.client as mqtt
import json
import random
from time import sleep
from save_database import save
from send_thingboards import pd1

# MQTT setting
MQTT_Broker = "192.168.1.237"
MQTT_Port = 1883
Keep_Alive_Interval = 7200
MQTT_Topic = 'hello'

#ACCESS_TOKEN = 'VeYjm5FnygELIcDovOXS'
#sensor_data = {'temperature': 0, 'humidity': 0}
# Callback server
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
    else:
        print("Connection returned result: " + str(MQTT_Broker))
    client.subscribe(MQTT_Topic, qos = 1)
    print("Subscribe: ")
    #client.publish('v1/devices/me/telemetry',json.dumps(sensor_data))
    #print("publish: " )

# Callback on_message server
def on_message(client, userdata, msg):
    print ('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload)
    # Decode JSON request
    #data = json.loads(msg.payload)
    #pd1(msg.payload.decode()) #publish things
    save(msg.payload) #save database
    #mosquitto_pub -d -t thean -m "{\"name\":\"vlxx\",\"id\":4,\"u\":4,\"i\":6,\"w\":45}"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.username_pw_set(ACCESS_TOKEN)
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
client.loop_forever()
