#!/usr/bin/env python

import pygame
from pygame.locals import *

## Config
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20

## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))

## Draw
screen.fill(WHITE)

pygame.draw.circle(screen, BLUE, (160, 140), 110, THICKNESS)
pygame.draw.circle(screen, BLACK, (400, 140), 110, THICKNESS)
pygame.draw.circle(screen, RED, (640, 140), 110, THICKNESS)
pygame.draw.circle(screen, YELLOW, (280, 250), 110, THICKNESS)
pygame.draw.circle(screen, GREEN, (520, 250), 110, THICKNESS)


pygame.display.flip()

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    clock.tick(30)
