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
BACKGROUND = 255, 255, 255
TRANSPARENT = 0,0,0,0

THICKNESS = 20

## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
top = screen.copy().convert_alpha()
bot = screen.copy().convert_alpha()

## Draw
screen.fill(BACKGROUND)
top.fill(TRANSPARENT)
bot.fill(TRANSPARENT)

pygame.draw.circle(top, BACKGROUND, (160, 140), 116)
pygame.draw.circle(top, BLUE, (160, 140), 110)
pygame.draw.circle(top, BACKGROUND, (160, 140), 90)
pygame.draw.circle(top, TRANSPARENT, (160, 140), 84)

pygame.draw.circle(top, BACKGROUND, (400, 140), 116)
pygame.draw.circle(top, BLACK, (400, 140), 110)
pygame.draw.circle(top, BACKGROUND, (400, 140), 90)
pygame.draw.circle(top, TRANSPARENT, (400, 140), 84)

pygame.draw.circle(top, BACKGROUND, (640, 140), 116)
pygame.draw.circle(top, RED, (640, 140), 110)
pygame.draw.circle(top, BACKGROUND, (640, 140), 90)
pygame.draw.circle(top, TRANSPARENT, (640, 140), 84)

pygame.draw.circle(bot, BACKGROUND, (280, 250), 116)
pygame.draw.circle(bot, YELLOW, (280, 250), 110)
pygame.draw.circle(bot, BACKGROUND, (280, 250), 90)
pygame.draw.circle(bot, TRANSPARENT, (280, 250), 84)

pygame.draw.circle(bot, BACKGROUND, (520, 250), 116)
pygame.draw.circle(bot, GREEN, (520, 250), 110)
pygame.draw.circle(bot, BACKGROUND, (520, 250), 90)
pygame.draw.circle(bot, TRANSPARENT, (520, 250), 84)


screen.blit(top, (0,0))
screen.blit(bot, (0,0))

screen.blit(top, (235,130), (235,130,40,60))
screen.blit(top, (475,130), (475,130,40,60))
screen.blit(top, (350,210), (350,210,50,60))
screen.blit(top, (590,210), (590,210,50,60))

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
