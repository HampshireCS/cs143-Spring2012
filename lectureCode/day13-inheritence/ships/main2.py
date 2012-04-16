#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_tie, draw_ywing
from ships import Ship, ShipSpawner
from utils import *


class Game(Application):
    title = "Spaceships"
    screen_size = 800, 600

    def __init__(self):
        Application.__init__(self)

        self.bounds = self.screen.get_rect()
        self.ships = Group()

        self.spawners = [ ShipSpawner(2000, self.ships, self.bounds) ]

    def update(self):
        dt = self.clock.get_time()

        self.ships.update(dt)

        for spawner in self.spawners:
            spawner.update(dt)

    def draw(self, screen):
        screen.fill((0,0,0))
        self.ships.draw(screen)


if __name__ == "__main__":
    Game().run()
    print "ByeBye"
