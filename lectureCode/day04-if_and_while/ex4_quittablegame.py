#!/usr/bin/env python
"ex4_quittablegame"

import pygame
from pygame.locals import *

screen_size = 640,480
background = 255,0,255

# initialize pygame
pygame.init()
pygame.display.set_mode(screen_size)

# loop
done = False
while not done:
    event = pygame.event.poll()

    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse %d,%d" % pygame.mouse.get_pos()

    screen.fill(background)
    pygame.display.flip()

print "ByeBye"
