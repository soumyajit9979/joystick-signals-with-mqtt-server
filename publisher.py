import paho.mqtt.client as mqtt
import sys
import msvcrt
client = mqtt.Client()
# client.username_pw_set("soumyajit", password=1234)
# client.connect(mqttBroker,1883,60)
if client.connect("localhost",1883,60)!=0:
    print("couln not connect")
    sys.exit(-1)

# client.publish("topic","hemlo world",0)
x=1
while x!=0:
    x=msvcrt.getch()
    client.publish("topic",x,0)
    if(x==0):
        client.disconnect()




# while True:
#     msg=input("type the message you want to send")
#     client.publish("topic", msg)
#     print("sent the msg: " + str(msg) + " to the Topic named topic")
#     time.sleep(1)
