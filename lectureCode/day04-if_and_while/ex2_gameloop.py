#!/usr/bin/env python
"ex2_gameloop"

import pygame

screen_size = 640,480
background = 255,0,255

# initialize pygame
pygame.init()
pygame.display.set_mode(screen_size)

while True:
    screen.fill(background)
    pygame.display.flip()
