#!/usr/bin/env python
import pygame
from pygame.locals import *

## consts
SCREEN = W,H = 900,600

SIZE = 10

pygame.init()
screen = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("Terrain")

## tile
tile = pygame.image.load("tile.png").convert()
tile.set_colorkey((255,255,255))

## map
f = open("tile.map")
tilemap = [ [ int(i) for i in line.strip().split(' ') ] for line in f.read().strip().split("\n") ]
f.close()

done = False
width = len(tilemap)
height = len(tilemap[0])
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

        ## draw
        screen.fill((40,40,40))
        for i in range(width):
            for j in reversed(range(height)):
                x = 11 * (i + j)
                y = 6 * (i - j)
                x += 10 
                y += 50 + 6 * height
                y -= tilemap[i][j] * 2
                screen.blit(tile, (x,y))
        pygame.display.flip()

print "ByeBye"
