import paho.mqtt.client as mqtt
import sys
import time

def on_connect(mqtt_client, obj, flags, rc):
         mqtt_client.subscribe("topic")

def on_message(client, userdata, message):
    print("Received message: ", str(message.topic + ":"+ message.payload.decode("utf-8")))
    
    


# mqttBroker = "172.20.130.33"
client = mqtt.Client()

client.on_message=on_message

if client.connect("localhost",1883,60)!=0:
    print("couln not connect")
    sys.exit(-1)
# client.username_pw_set("soumyajit", password=1234)
# client.connect(mqttBroker,1883,60)
# client.connect("localhost",1883,60)

client.subscribe("topic")

# if(client.on_message==0):
    
# client.on_connect=on_connect
# client.on_message = on_message
client.loop_forever()
client.disconnect()
