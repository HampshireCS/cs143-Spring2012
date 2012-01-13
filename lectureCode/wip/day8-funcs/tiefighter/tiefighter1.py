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

    # tie fighter
    draw.rect(screen, RED, (0,0,5,40))
    draw.rect(screen, RED, (35,0,5,40))
    draw.rect(screen, RED, (0,17,40,5))
    draw.circle(screen, RED, (20,20), 10)

    ## Refresh
    pygame.display.flip()
        
print "ByeBye"
