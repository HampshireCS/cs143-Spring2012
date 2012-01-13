#!/usr/bin/env python
"""
tiefighter.py

Draw a tie fighter on the screen
"""
from random import randrange

import pygame
from pygame import draw
from pygame.locals import *

## Settings
BLACK = 0,0,0

size = 800,600

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "draw a tie fighter at location"
    x,y = pos
    w,h = size,size

    x0,x1 = x - (size/2), x + (size/2)
    y0,y1 = y - (size/2), y + (size/2)

    wing = size/8
    radius = size/4

    draw.rect(surf, color, (x0, y0, wing, h))
    draw.rect(surf, color, (x1-wing, y0, wing, h))
    draw.rect(surf, color, (x0, y0+(h-wing)/2, w, wing))
    draw.circle(surf, color, (x, y), radius)


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
        elif event.type == MOUSEBUTTONDOWN:
            color = randrange(50,256), randrange(50,256), randrange(50,256)
            size = randrange(20,80)
            draw_tie(screen, pygame.mouse.get_pos(), color, size)

    ## Draw
    #screen.fill(BLACK)

    ## Refresh
    pygame.display.flip()
        
print "ByeBye"
