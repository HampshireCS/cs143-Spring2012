#!/usr/bin/env python

import pygame
from pygame.locals import *

from maze import *


class App:
    title = "Maze Solver"
    fps = 10

    size = width,height = 5,5
    tile = 20
    wall = 3

    screen_width = width * (tile + wall) + wall
    screen_height = height * (tile + wall) + wall
    screen_size = screen_width, screen_height

    def __init__(self):
        pygame.init()

    def setup(self):
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)

        self.maze = Maze(self.size)

    def draw(self):
        self.maze.render(self.screen, self.tile, self.wall)

    def update(self):
        pass

    def run(self):
        done = False
        clock = pygame.time.Clock()

        print self.maze._maze._maze
        while not done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

            self.draw()

            pygame.display.flip()
            clock.tick(self.fps)


def main():
    app = App()
    app.setup()
    app.run()
    print "ByeBye"

if __name__ == "__main__":
    main()
