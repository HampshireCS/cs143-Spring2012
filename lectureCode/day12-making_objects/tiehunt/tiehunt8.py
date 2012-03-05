#!/usr/bin/env python

import math

from random import randrange

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
        self.image.set_colorkey(C_BLACK)
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
        

class Explosion(object):
    alive = True

    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius

        self.counter = radius * 2

    def update(self):
        self.counter -= 1
        if self.counter <= 0:
            self.alive = False
        elif self.radius > self.counter:
            self.radius = self.counter

    def draw(self, surf):
        c = randrange(256)
        pygame.draw.circle(surf, (255, c, 0), self.pos, self.radius)


class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    spawn_every = 15
    max_ties = 1000

    def spawn(self):
        size = 40
        x = randrange(self.bounds.width - size)
        y = randrange(self.bounds.height - size)
        vx = randrange(-5, 6)
        vy = randrange(-5, 6)
        color = randrange(128,256), randrange(128,256), randrange(128,256)
        tie = TieFighter(x, y, vx, vy, self.bounds, size, color)
        self.ties.append(tie)


    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)

        self.ties = []
        self.xplos = []
        self.spawn()


    def run(self):
        clock = pygame.time.Clock()
        done = False
        spawn_counter = 0
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.xplos.append( Explosion(pygame.mouse.get_pos(), 40) )

            # update
            if spawn_counter == 0 and len(self.ties) < self.max_ties:
                self.spawn()
            spawn_counter = (spawn_counter + 1) % self.spawn_every

            for tie in self.ties:
                tie.update()

            for xplo in self.xplos:
                if xplo.alive:
                    xplo.update()
                else:
                    self.xplos.remove(xplo)

            # draw
            self.screen.fill(C_BLACK)
            for tie in self.ties:
                tie.draw(self.screen)

            for xplo in self.xplos:
                xplo.draw(self.screen)

            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
