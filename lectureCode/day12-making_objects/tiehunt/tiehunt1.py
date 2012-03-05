#!/usr/bin/env python

import pygame
from pygame.locals import *

class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)


    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

            # update

            # draw
            self.screen.fill((0, 0, 0))
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
