#!/usr/bin/env python

import pygame
from pygame.locals import *

# globals
BACKGROUND = 80, 80, 80
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
RECT_SIZE = 120,80
FPS = 30

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

bounds = screen.get_rect()
rect = pygame.Rect((0,0), RECT_SIZE)
rect.center = bounds.center

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
    pygame.draw.rect(screen, (255,0,0), rect)
    pygame.draw.rect(screen, (0,0,0), rect, 5)

    # refresh
    pygame.display.flip()
    clock.tick(FPS)

print "ByeBye"
