import sys
import paho.mqtt.client as mqtt

import pygame
from pygame.locals import*
client = mqtt.Client()
if client.connect("172.20.139.194",1883,60)!=0:
    print("couln not connect")
    sys.exit(-1)
clock=pygame.time.Clock()
pygame.init()
pygame.joystick.init()
joysticks=[pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())
while True:
    for event in pygame.event.get():

        if event.type==JOYAXISMOTION:
            if event.axis==1:
                
                if event.value<0:
                    g=["FORWARD",event.value]
                    client.publish("topic","FORWARD",0)
                    print(g)
                if event.value>0:
                    g=["BACKWARD",event.value]
                    client.publish("topic","BACKWARD",0)
                    print(g)
                
                if event.value==-3.051850947599719e-05:
                    client.publish("topic","upper_y_stop",0)
                    print("upper_y_stop")
            
            if event.axis==0:
                if event.value<0:
                    g=["LEFT",event.value]
                    client.publish("topic","LEFT",0)
                    print(g)
                if event.value>0:
                    g=["RIGHT",event.value]
                    client.publish("topic","RIGHT",0)
                    print(g)
                elif event.value==0:
                    client.publish("topic","upper_x_stop",0)
                    print("upper_x_stop")
            
            if event.axis==3:
                if event.value<0:
                    g=["LOWER_FORWARD",event.value]
                    client.publish("topic","LOWER_FORWARD",0)
                    print(g)
                if event.value>0:
                    g=["LOWER_BACKWARD",event.value]
                    client.publish("topic","LOWER_BACKWARD",0)
                    print(g)
                if event.value==-3.051850947599719e-05:
                    print("lower_y_stop")
                    client.publish("topic","lower_y_stop",0)
            
            if event.axis==2:
                if event.value<0:
                    g=["LOWER_LEFT",event.value]
                    client.publish("topic","LOWER_LEFT",0)
                    print(g)
                if event.value>0:
                    g=["LOWER_RIGHT",event.value]
                    client.publish("topic","LOWER_RIGHT",0)
                    print(g)
                elif event.value==0:
                    client.publish("topic","lower_x_stop",0)
                    print("lower_x_stop")

            if event.axis==4:
                g=["left_analog",event.value]
                client.publish("topic","left_analog",0)
                print(g)
            
            if event.axis==5:
                g=["right_analog",event.value]
                client.publish("topic","right_analog",0)
                print(g)
            
            
            
        if event.type==JOYBUTTONDOWN:
            if event.button==0:
                client.publish("topic","A",0)
                print("A")
            if event.button==1:
                client.publish("topic","B",0)
                print("B")
            if event.button==2:
                client.publish("topic","B",0)
                print("X")
            if event.button==3:
                client.publish("topic","Y",0)
                print("Y")
            if event.button==4:
                client.publish("topic","right_trigger",0)
                print("right_trigger")
            if event.button==5:
                client.publish("topic","leftt_trigger",0)
                print("left_trigger")
            if event.button==6:
                client.publish("topic","Select",0)
                print("Select")
            if event.button==7:
                client.publish("topic","Start",0)
                print("Start")
        
        if event.type==JOYBUTTONUP:
            if event.button==0:
                client.publish("topic","A_UP",0)
                print("A_UP")
            if event.button==1:
                client.publish("topic","B_UP",0)
                print("B_UP")
            if event.button==2:
                client.publish("topic","X_UP",0)
                print("X_UP")
            if event.button==3:
                client.publish("topic","Y_UP",0)
                print("Y_UP")
            if event.button==4:
                client.publish("topic","right_trigger_UP",0)
                print("right_trigger_UP")
            if event.button==5:
                client.publish("topic","left_trigger_UP",0)
                print("left_trigger_UP")
            if event.button==6:
                client.publish("topic","Select_UP",0)
                print("Select_UP")
            if event.button==7:
                client.publish("topic","Start_UP",0)
                print("Start_UP")
        
        if event.type==JOYHATMOTION:
            if event.value==(0,1):
                client.publish("topic","up",0)
                print("up")
            if event.value==(1,0):
                client.publish("topic","right",0)
                print("right")
            if event.value==(-1,0):
                client.publish("topic","left",0)
                print("left")
            if event.value==(0,-1):
                client.publish("topic","down",0)
                print("down")
            if event.value==(1,1):
                client.publish("topic","up-right",0)
                print("up-right")
            if event.value==(-1,1):
                client.publish("topic","up-left",0)
                print("up-left")
            if event.value==(-1,-1):
                client.publish("topic","down-left",0)
                print("down-left")
            if event.value==(1,-1):
                client.publish("topic","down-right",0)
                print("down-right")
            if event.value==(0,0):
                client.publish("topic","arrow-stopped",0)
                print("arrow_stopped")
    clock.tick(60)