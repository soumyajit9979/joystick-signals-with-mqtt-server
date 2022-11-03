import sys

import pygame
from pygame.locals import*
clock=pygame.time.Clock()
pygame.init()
pygame.joystick.init()
joysticks=[pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())]

for joystick in joysticks:
    print(joystick.get_name())
while True:
    for event in pygame.event.get():
            print(event)
    clock.tick(60)