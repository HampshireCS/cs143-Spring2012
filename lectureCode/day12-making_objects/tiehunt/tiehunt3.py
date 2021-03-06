#!/usr/bin/env python

import pygame
from pygame.locals import *

C_BLACK = 0,0,0
C_RED = 255,0,0



class TieFighter(object):
    def __init__(self, x, y, vx, vy, bounds, size=40, color=C_RED):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.bounds = bounds
        self.size = size
        self.color = color

        self.image = pygame.Surface((self.size, self.size))
        self.rect = pygame.Rect(x,y,size,size)
        self.redraw()


    def redraw(self):
        surf = self.image
        size = self.size
        wall = self.size/8
        color = self.color

        surf.fill(C_BLACK)
        pygame.draw.rect(surf, color, (0, 0, wall, size))
        pygame.draw.rect(surf, color, (size - wall, 0, wall, size))
        pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
        pygame.draw.circle(surf, color, (size/2, size/2), size/4)


    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.x += 2 * self.vx

        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy = -self.vy
            self.rect.y += 2 * self.vy

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        


class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)

        self.ties = []
        self.ties.append( TieFighter(0, 0, 3, 3, self.bounds) )


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
            for tie in self.ties:
                tie.update()

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
