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
    group = []
    spawn_max = 1000
    spawn_rate = 120
    spawn_step = 0

    size = 40,40
    color = 255,0,0
    border = 5

    def __init__(self, pos):
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()

        Enemy.group.append(self)

        self.vel = randint(-4,4), randint(-4,4)

        self.image.fill((0,0,0))
        filling = self.rect.inflate(-self.border, -self.border)
        self.image.fill(self.color, filling)

        self.rect.center = pos

    def update(self):
        dx,dy = self.vel
        self.rect.move_ip(dx, dy)

        if self.rect.left < 0 or self.rect.right >= SCREEN_WIDTH:
            dx = -dx
            self.rect.move_ip(2*dx, 0)
        if self.rect.top < 0 or self.rect.bottom >= SCREEN_HEIGHT:
            dy = -dy
            self.rect.move_ip(0, 2*dy)

        self.vel = dx,dy

    @classmethod
    def spawn(cls):
        cls.spawn_step += 1
        if (cls.spawn_step % cls.spawn_rate) == 0:
            if len(cls.group) >= cls.spawn_max:
                # do nothing
                pass
            elif len(cls.group) > 0:
                for enemy in [ e for e in cls.group ]:
                    Enemy( enemy.rect.center )
            else:
                pos = randint(100,700), randint(100,500)
                Enemy(pos)



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
    Enemy.spawn()

    player.update()
    for enemy in Enemy.group:
        enemy.update()
        if enemy.rect.colliderect(player.rect):
            player.alive = False


    # draw
    screen.fill(BG_COLOR)

    for enemy in Enemy.group:
        screen.blit(enemy.image, enemy.rect)

    if player.alive:
        screen.blit(player.image, player.rect)

    # refresh
    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
