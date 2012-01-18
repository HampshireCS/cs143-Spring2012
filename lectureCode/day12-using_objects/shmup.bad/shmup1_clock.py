#/usr/bin/env python
"""
shmup.py

A simple 2d shoot 'em up game.  Similar to geometry wars
"""

import pygame
from pygame.locals import *

# globals
SCREEN_SIZE = 800,600
BG_COLOR = 20,20,20

# main
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # update

    # draw
    screen.fill(BG_COLOR)

    # refresh
    pygame.display.flip()
    clock.tick(30)

            
print "ByeBye"
