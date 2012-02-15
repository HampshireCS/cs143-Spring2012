#!/usr/bin/env python

from random import shuffle

import pygame
from pygame.locals import *

BLACK = 0
BLUE = 1
BROWN = 2
RED = 3
GREEN = 4

colors = [
    (0,0,0),
    (0,0,255),
    (100,40,0),
    (190,0,0),
    (0,0,200)
]

cards = [ (v,c) for c in colors for v in "ABCD" ]
cards = cards + cards
print len(cards)

pygame.init()
pygame.event.set_allowed([QUIT,KEYDOWN,MOUSEBUTTONDOWN])
screen = pygame.display.set_mode((640,480))
done = False
dirty = True
while not done:
    # input
    event = pygame.event.wait()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    # draw
    if dirty:

        screen.fill((0,128,0))

        for i,card in enumerate(cards):
            value, color = card
            x, y = i%8, i/8


        pygame.display.flip()




print "ByeBye"
