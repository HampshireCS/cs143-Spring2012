#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Player(Sprite):
    bullets = Group()
    pass

class Bullet(Sprite):
    def __init__(self):
        pass

class Baddie(Sprite):
    bullets = Group()
    pass


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400,800))

    def quit(self):
        self.done = True

    def run(self):
        self.done = False
        while not self.done:
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    self.quit()
                elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                    self.quit()

  

if __name__ == "__main__":
    Game().run()
