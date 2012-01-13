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

def draw_tie(surf, pos, color):
    "draw a tie fighter at location"
    x,y = pos
    draw.rect(surf, color, (x, y, 5, 40))
    draw.rect(surf, color, (x+35, y, 5, 40))
    draw.rect(surf, color, (x, y+17, 40, 5))
    draw.circle(surf, color, (x+20, y+20), 10)


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
    draw_tie(screen, (100,300), (255,0,0))
    draw_tie(screen, (400,400), (255,255,0))
    draw_tie(screen, (600,10), (255,0,255))

    ## Refresh
    pygame.display.flip()
        
print "ByeBye"
