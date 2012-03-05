#!/usr/bin/env python

import pygame
from pygame.locals import *

C_BLACK = 0,0,0
C_RED = 255,0,0


def draw_tie(surf, color, size):
        wall = size/8
        surf.fill(C_BLACK)
        pygame.draw.rect(surf, color, (0, 0, wall, size))
        pygame.draw.rect(surf, color, (size - wall, 0, wall, size))
        pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
        pygame.draw.circle(surf, color, (size/2, size/2), size/4)


class TieFighter(object):
    def __init__(self, x, y, vx, vy, size=40, color=C_RED):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color

        self.image = pygame.Surface((size, size))
        draw_tie(self.image, color, size)

        self.rect = pygame.Rect(x, y, size, size)


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        


class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

        self.ties = []
        self.ties.append( TieFighter(200, 200, 3, 3) )


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
            self.screen.fill(C_BLACK)
            for tie in self.ties:
                tie.draw(self.screen)

            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
