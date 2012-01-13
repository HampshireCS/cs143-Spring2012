#!/usr/bin/env python
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((565,353))
img = pygame.image.load("img.png").convert()

def greyscale(img):
    pix = pygame.surfarray.array3d(img)
    print pix.size
    return img

done = False
while not done:
    # input
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
    # draw
    screen.blit(greyscale(img), (0,0))
    
    # refresh
    pygame.display.flip()
            
print "Quit"
        
