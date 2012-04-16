#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group


class Player(Sprite):
    def __init__(self, color):
        Sprite.__init__(self)
        self.vx, self.vy = 0, 0

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy


class PlayerManager(Group):
    def create(self, color):
        player = Player(color)
        self.add(player)
        return player


class PlayerController(object):
    
