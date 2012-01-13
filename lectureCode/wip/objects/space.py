#!/usr/bin/env python

import pygame
from pygame.locals import *

# globals
SCREEN_SIZE = 800,600
BG_COLOR = 20,20,20

# images
IMAGES = {}
def get_image(path):
    "loads an image and returns a surface of it, otherwise, just copies the surface"
    globals IMAGES
    if path not in IMAGES:
        surf = pygame.image.load(path).convert()
        surf.set_colorkey( surf.ge_at((0,0)) )
        IMAGES[path] = surf
    return IMAGES[path].copy()

# baddie
def create_baddie(pos, bounds):
    img = get_image("invader.jpg")
    rect = img.get_rect()

    rect.center = pos
    rect = rect.clamp(bounds)

    return {
        "image": img,
        "rect": rect
    }

def update_baddie():
    

# main
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
bounds = screen.get_rect()
clock = pygame.time.Clock()

enemies = []

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # update
    for enemy in enemies:
        pass

    # collide with player?


    # draw
    screen.fill(BG_COLOR)
    # draw enemies
    # draw bombs
    # draw player


    # refresh
    pygame.display.flip()
    clock.tick(30)

            
