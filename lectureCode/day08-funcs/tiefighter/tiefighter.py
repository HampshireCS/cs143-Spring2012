#!/usr/bin/env python
"""
tiefighter.py

Draw a tie fighter on the screen
"""
import pygame
from pygame import draw
from pygame.locals import *

## Settings
BLACK = 0,0,0
RED = 255,0,0

size = 800,600

## Initialize
pygame.init()
screen = pygame.display.set_mode(size)
done = False

while not done:
    ## Input
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    ## Draw
    screen.fill(BLACK)

    ## Refresh
    pygame.display.flip()
        
print "ByeBye"
