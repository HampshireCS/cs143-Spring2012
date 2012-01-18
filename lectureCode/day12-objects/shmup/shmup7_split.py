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
ENEMY_SPAWN = 120    # every N frames

PLAYER_SIZE = 25,25
PLAYER_COLOR = 0,255,110

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

# player
player = {}
player["image"] = pygame.Surface(PLAYER_SIZE)
player["image"].fill(PLAYER_COLOR)
player["rect"] = player["image"].get_rect()
player["alive"] = True

# main
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
step = 1


done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # update
    if player["alive"]:
        player["rect"].center = pygame.mouse.get_pos()

    if step % ENEMY_SPAWN == 0:
        if enemies:
            new_enemies = []
            for enemy in enemies:
                new_enemies.append( create_enemy( enemy["rect"].center ))
            enemies += new_enemies
        else:
            pos = randint(100,700), randint(100,500)
            enemies.append( create_enemy(pos) )

    for enemy in enemies:
        update_enemy(enemy)
        if enemy["rect"].colliderect(player["rect"]):
            player["alive"] = False

    # draw
    screen.fill(BG_COLOR)

    for enemy in enemies:
        screen.blit(enemy["image"], enemy["rect"])
    if player["alive"]:
        screen.blit(player["image"], player["rect"])

    # refresh
    pygame.display.flip()
    step += 1
    clock.tick(30)

print "ByeBye"
