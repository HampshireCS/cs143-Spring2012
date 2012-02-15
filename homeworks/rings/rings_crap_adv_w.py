#!/usr/bin/env python

from math import radians

import pygame
from pygame.locals import *
from pygame import Rect

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

BLUE_BOX = Rect(50, 30, 220, 220)
BLACK_BOX = Rect(290, 30, 220, 220) 
RED_BOX = Rect(530, 30, 220, 220) 
YELLOW_BOX = Rect(170, 140, 220, 220)
GREEN_BOX = Rect(410, 140, 220, 220)

pygame.draw.ellipse(screen, BLUE, BLUE_BOX, THICKNESS)
pygame.draw.ellipse(screen, BLACK, BLACK_BOX, THICKNESS)
pygame.draw.ellipse(screen, RED, RED_BOX, THICKNESS)
pygame.draw.ellipse(screen, YELLOW, YELLOW_BOX, THICKNESS)
pygame.draw.ellipse(screen, GREEN, GREEN_BOX, THICKNESS)
c = 255,0,255

pygame.draw.arc(screen, WHITE, BLUE_BOX.inflate(12,12), radians(-20), radians(10), THICKNESS + 12)
pygame.draw.arc(screen, BLUE, BLUE_BOX, radians(-20), radians(10), THICKNESS)


pygame.draw.arc(screen, WHITE, BLACK_BOX.inflate(12,12), radians(240), radians(270), THICKNESS + 12)
pygame.draw.arc(screen, WHITE, BLACK_BOX.inflate(12,12), radians(-20), radians(10), THICKNESS + 12)
pygame.draw.arc(screen, BLACK, BLACK_BOX, radians(240), radians(270), THICKNESS)
pygame.draw.arc(screen, BLACK, BLACK_BOX, radians(-20), radians(10), THICKNESS)

pygame.draw.arc(screen, WHITE, RED_BOX.inflate(12,12), radians(240), radians(270), THICKNESS + 12)
pygame.draw.arc(screen, RED, RED_BOX, radians(240), radians(270), THICKNESS)

pygame.draw.arc(screen, WHITE, YELLOW_BOX.inflate(12,12), radians(60), radians(90), THICKNESS + 12)
pygame.draw.arc(screen, WHITE, YELLOW_BOX.inflate(12,12), radians(150), radians(190), THICKNESS + 12)
pygame.draw.arc(screen, YELLOW, YELLOW_BOX, radians(60), radians(90), THICKNESS)
pygame.draw.arc(screen, YELLOW, YELLOW_BOX, radians(150), radians(190), THICKNESS)


pygame.draw.arc(screen, WHITE, GREEN_BOX.inflate(12,12), radians(60), radians(90), THICKNESS + 12)
pygame.draw.arc(screen, WHITE, GREEN_BOX.inflate(12,12), radians(150), radians(190), THICKNESS + 12)
pygame.draw.arc(screen, GREEN, GREEN_BOX, radians(60), radians(90), THICKNESS)
pygame.draw.arc(screen, GREEN, GREEN_BOX, radians(150), radians(190), THICKNESS)

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
