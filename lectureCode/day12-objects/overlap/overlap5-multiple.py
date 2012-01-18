#!/usr/bin/env python

import pygame
from pygame.locals import *

# globals
BACKGROUND = 80, 80, 80
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
RECT_SIZE = 120,80
FPS = 30

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

bounds = screen.get_rect()


rects = [ pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE) ]
rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

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
        if evt.type == MOUSEBUTTONUP:
            grabbed = None


    # update
    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds)

    # draw
    screen.fill(BACKGROUND)
    for rect in rects:
        if rect == grabbed:
            color = 255,255,255
        else:
            color = 255,0,0

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 5)

    # refresh
    pygame.display.flip()
    clock.tick(FPS)

print "ByeBye"
