#!/usr/bin/env python
"""
drawlines.py

Draw a bunch of lines to the screen
"""
import pygame
from pygame.locals import *

## Settings
BLACK = 0,0,0
RED = 255,0,0

size = 400,400

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
    
    for i in range(0,400,8):
        pygame.draw.line(screen, RED, (0,i), (i,399))

    ## Refresh
    pygame.display.flip()
        
print "ByeBye"
