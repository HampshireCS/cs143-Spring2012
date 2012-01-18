#!/usr/bin/env python
"""
shmup.py

A simple 2d shoot 'em up game.  Similar to geometry wars
"""

from random import randint

import pygame
from pygame.locals import *



# enemies
class Enemy:
    all = []

    size = 40,40
    color = 255,0,0
    border = 5

    spawn_max = 1000

    def __init__(self, game, pos, vel=None):
        Enemy.all.append(self)
        self.game = game
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
        if self.rect.left < 0 or self.rect.right >= self.game.bounds.right:
            dx = -dx
            self.rect.move_ip(2*dx, 0)
            spawn = dx, -dy/abs(dy) * randint(1,4)
        if self.rect.top < 0 or self.rect.bottom >= self.game.bounds.bottom:
            dy = -dy
            self.rect.move_ip(0, 2*dy)
            spawn = -dx/abs(dx) * randint(1,4), dy

        self.vel = dx,dy
        if spawn and len(Enemy.all) < Enemy.spawn_max:
            Enemy(self.game, self.rect.center, spawn)


# player
class Player:
    size = 25,25
    color = 0,255,110

    def __init__(self, game):
        self.game = game
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.alive = True
        
        # draw
        self.image.fill(self.color)

    def update(self):
        if self.alive:
            self.rect.center = pygame.mouse.get_pos()
            self.rect.clamp_ip(self.game.bounds)


class Game:
    size =  800,600
    background = 40,40,40
    paused = False
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()

        pygame.mouse.set_visible(False)

        self.player = Player(self)

    def pause(self):
        self.paused = not self.paused
        if self.paused:
            overlay = pygame.Surface(self.screen.get_size()).convert_alpha()
            overlay.fill((0,0,0,140))
            self.screen.blit(overlay,(0,0))
        

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.pause()

            if not self.paused:
                self.update()
                self.draw()

            pygame.display.flip()
            clock.tick(30)

    def update(self):
        if len(Enemy.all) == 0:
            pos = self.bounds.width/2, self.bounds.height/2
            Enemy(self, pos)

        self.player.update()

        for enemy in Enemy.all:
            enemy.update()
            if enemy.rect.colliderect(self.player.rect):
                self.player.alive = False

    def draw(self):
        self.screen.fill(self.background)

        for enemy in Enemy.all:
            self.screen.blit(enemy.image, enemy.rect)

        if self.player.alive:
            self.screen.blit(self.player.image, self.player.rect)


Game().run()
print "ByeBye"
