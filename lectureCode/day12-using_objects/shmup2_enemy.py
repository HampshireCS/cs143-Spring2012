#!/usr/bin/env python
"""
shmup.py

A simple 2d shoot 'em up game.  Similar to geometry wars
"""

import pygame
from pygame.locals import *

# globals
SCREEN_SIZE = 800,600
BG_COLOR = 20,20,20

ENEMY_SIZE = 40,40
ENEMY_COLOR = 255,0,0

# enemies
enemies = []
def create_enemy(pos):
    image = pygame.Surface(ENEMY_SIZE)
    image.fill(ENEMY_COLOR)

    rect = image.get_rect()
    rect.center = pos

    return {"image": image, "rect": rect}

# main
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# first enemy
enemies.append( create_enemy((40, 40)) )


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
    for enemy in enemies:
        screen.blit(enemy["image"], enemy["rect"])

    # refresh
    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
