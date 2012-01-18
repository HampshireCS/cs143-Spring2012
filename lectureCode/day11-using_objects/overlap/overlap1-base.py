#!/usr/bin/env python

import pygame
from pygame.locals import *

# globals
BACKGROUND = 80, 80, 80
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
RECT_SIZE = 250,200
FPS = 30

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()
done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        if evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True


    # draw
    screen.fill(BACKGROUND)

    # refresh
    pygame.display.flip()
    clock.tick(FPS)

print "ByeBye"
