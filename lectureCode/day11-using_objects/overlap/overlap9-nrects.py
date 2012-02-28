#!/usr/bin/env python

import pygame
from pygame.locals import *

# globals
ROW, COL = 10, 10
TILE_X, TILE_Y = 80, 60
PADDING = 15
BORDER = 5

BACKGROUND = 80, 80, 80
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = ROW * TILE_X, COL * TILE_Y
FPS = 30

# COLORS
C_BLACK = 0,0,0
C_RECT = 255,0,0
C_ACTIVE = 255,255,255
C_TOUCH = 0,255,0

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

bounds = screen.get_rect()

rects = []
for y in range(ROW):
    for x in range(COL):
        rect = pygame.Rect(x * TILE_X, y * TILE_Y, TILE_X, TILE_Y)
        rect.inflate_ip(-PADDING, -PADDING)
        rects.append(rect)

clock = pygame.time.Clock()
done = False
grabbed = None
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        if evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        if evt.type == MOUSEBUTTONDOWN:
            pt = pygame.mouse.get_pos()
            for rect in rects:
                if rect.collidepoint(pt):
                    grabbed = rect
            if grabbed is not None:
                rects.remove(grabbed)
                rects.append(grabbed)
                pygame.mouse.get_rel() # clearing relative before this point
        if evt.type == MOUSEBUTTONUP:
            grabbed = None


    # update
    if grabbed:
        x,y = pygame.mouse.get_rel()
        print x,y
        grabbed.move_ip(x,y)
        grabbed.clamp_ip(bounds)

    # draw
    screen.fill(BACKGROUND)
    for rect in rects:
        # copy so it doesn't collide with itself
        others = rects[:]
        others.remove(rect)

        if rect == grabbed:
            color = C_ACTIVE
        elif rect.collidelist(others) != -1:
            color = C_TOUCH
        else:
            color = C_RECT

        screen.fill(C_BLACK, rect)
        screen.fill(color, rect.inflate(-BORDER, -BORDER))

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 5)

    # refresh
    pygame.display.flip()
    clock.tick(FPS)

print "ByeBye"
