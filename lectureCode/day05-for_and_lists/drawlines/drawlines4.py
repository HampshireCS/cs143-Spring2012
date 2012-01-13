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
GREEN = 0,255,0
BLUE = 0,255,255
YELLOW = 255,255,0

size = 400,400

## Step
step = 10

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
        elif event.type == KEYDOWN and event.key == K_UP:
            step -= 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            step += 1

    ## Draw
    screen.fill(BLACK)
    
    for i in range(0,400,step):
        pygame.draw.line(screen, RED, (0,i), (i,399))
        pygame.draw.line(screen, GREEN, (0,i), (399-i,0))
        pygame.draw.line(screen, BLUE, (i,0), (399,i))
        pygame.draw.line(screen, YELLOW, (i,399), (399,399-i))

    ## Refresh
    pygame.display.flip()
        
print "ByeBye"
