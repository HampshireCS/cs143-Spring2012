#!/usr/bin/env python
"""
shmup.py

A simple 2d shoot 'em up game.  Similar to geometry wars
"""

from random import randint

import pygame
from pygame.locals import *

# globals
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
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

    vel = randint(-4,4), randint(-4,4)

    return {"image": image, 
            "rect": rect,
            "vel": vel}

def update_enemy(enemy):
    dx, dy = enemy["vel"]
    rect = enemy["rect"]
    rect.move_ip(dx, dy)

    if rect.left < 0 or rect.right >= SCREEN_WIDTH:
        dx = -dx
        rect.move_ip(2*dx, 0)
    if rect.top < 0 or rect.bottom >= SCREEN_HEIGHT:
        dy = -dy
        rect.move_ip(0, 2*dy)

    enemy["vel"] = dx,dy
    
# main
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# first enemy
enemies.append( create_enemy((40, 40)) )
enemies.append( create_enemy((400, 400)) )
enemies.append( create_enemy((100, 500)) )


done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # update
    for enemy in enemies:
        update_enemy(enemy)

    # draw
    screen.fill(BG_COLOR)

    for enemy in enemies:
        screen.blit(enemy["image"], enemy["rect"])

    # refresh
    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
