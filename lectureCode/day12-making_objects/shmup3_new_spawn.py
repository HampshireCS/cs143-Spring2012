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


# enemies
class Enemy:
    all = []

    size = 40,40
    color = 255,0,0
    border = 5

    spawn_max = 1000

    def __init__(self, pos, vel=None):
        Enemy.all.append(self)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()

        if vel is None:
            self.vel = randint(1,4), randint(1,4)
        else:
            self.vel = vel

        self.image.fill((0,0,0))
        filling = self.rect.inflate(-self.border, -self.border)
        self.image.fill(self.color, filling)

        self.rect.center = pos

    def update(self):
        dx,dy = self.vel
        self.rect.move_ip(dx, dy)

        spawn = None
        if self.rect.left < 0 or self.rect.right >= SCREEN_WIDTH:
            dx = -dx
            self.rect.move_ip(2*dx, 0)
            spawn = dx, -dy/abs(dy) * randint(1,4)
        if self.rect.top < 0 or self.rect.bottom >= SCREEN_HEIGHT:
            dy = -dy
            self.rect.move_ip(0, 2*dy)
            spawn = -dx/abs(dx) * randint(1,4), dy

        self.vel = dx,dy
        if spawn and len(Enemy.all) < Enemy.spawn_max:
            Enemy(self.rect.center, spawn)


# player
class Player:
    size = 25,25
    color = 0,255,110

    def __init__(self):
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.alive = True
        
        # draw
        self.image.fill(self.color)

    def update(self):
        if self.alive:
            self.rect.center = pygame.mouse.get_pos()


# main
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
player = Player()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # update
    if len(Enemy.all) == 0:
        pos = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
        Enemy(pos)

    player.update()
    for enemy in Enemy.all:
        enemy.update()
        if enemy.rect.colliderect(player.rect):
            player.alive = False


    # draw
    screen.fill(BG_COLOR)

    for enemy in Enemy.all:
        screen.blit(enemy.image, enemy.rect)

    if player.alive:
        screen.blit(player.image, player.rect)

    # refresh
    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
