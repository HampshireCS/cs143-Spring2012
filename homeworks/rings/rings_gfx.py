#!/usr/bin/env python

import pygame
import pygame.gfxdraw
from pygame.locals import *

## Config
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BACKGROUND = 220, 220, 220
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


pygame.gfxdraw.filled_circle(screen, 160, 140, 111, BLACK)
pygame.gfxdraw.filled_circle(screen, 400, 140, 111, BLACK)
pygame.gfxdraw.filled_circle(screen, 640, 140, 111, BLACK)
pygame.gfxdraw.filled_circle(screen, 280, 250, 111, BLACK)
pygame.gfxdraw.filled_circle(screen, 520, 250, 111, BLACK)
pygame.gfxdraw.filled_circle(screen, 520, 250, 110, BACKGROUND)
pygame.gfxdraw.filled_circle(screen, 280, 250, 110, BACKGROUND)
pygame.gfxdraw.filled_circle(screen, 640, 140, 110, BACKGROUND)
pygame.gfxdraw.filled_circle(screen, 400, 140, 110, BACKGROUND)
pygame.gfxdraw.filled_circle(screen, 160, 140, 110, BACKGROUND)

screen.blit(top, (0,0))
screen.blit(bot, (0,0))

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
