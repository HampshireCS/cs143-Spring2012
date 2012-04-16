#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group

from world import *


class Game(object):
    background = 80,80,80

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))

        self.players = Group()
        p1 = Player((255,0,0), self.players)
        p2 = Player((0,0,255), self.players)

    def draw(self):
        self.screen.fill(self.background)

    def update(self):
        self.players.update()



if __name__ == "__main__":
    Game().run()
