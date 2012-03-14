#!/usr/bin/env python

import pygame
from pygame.locals import *

from core import *


C_BG = 80, 80, 80
C_WALLS = 255, 255, 255
C_START = 0,255,0
C_END = 255,0,0
C_FOG = 40, 40, 40

TILE = 10
BORDER = 2
WIDTH, HEIGHT = 50, 50
FPS = 10


class Solver(MazeWalker):
    def __init__(self, maze):
        MazeWalker.__init__(self, maze)
        self.visited = []

    def step(self):
        if self.right and self.right not in self.visited:
            self.go_right()
        elif self.forward and self.forward not in self.visited:
            self.go_forward()
        elif self.left and self.left not in self.visited:
            self.go_left()
        else:
            self.turn_around()
        self.visited.append(self.location)




pygame.init()
maze = Maze((WIDTH, HEIGHT))
maze_g = MazeGraphics(maze, TILE, BORDER)
maze_image = maze_g.maze(C_WALLS, C_BG, C_START, C_END)
solver = Solver(maze)

screen = pygame.display.set_mode(maze_image.get_size())

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # update
    solver.update()
    print solver.location._x, solver.location._y, solver._won

    # draw
    screen.blit(maze_image, (0,0))

    pygame.display.flip()
    clock.tick(FPS)


