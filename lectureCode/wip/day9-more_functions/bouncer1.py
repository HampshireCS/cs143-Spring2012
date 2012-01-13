import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

#from tie9.py
ties = []
pygame.init()
screen = pygame.display.set_mode((800,600))
x,y = 400,300

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    wall = size/8
    x0,x1 = x - (size/2), x + (size/2)
    y0,y1 = y - (size/2), y + (size/2)

    draw.rect(surf, color, (x0, y0, wall, size))
    draw.rect(surf, color, (x1-wall, y0, wall, size))
    draw.rect(surf, color, (x0, y-(wall/2), size, wall))
    draw.circle(surf, color, (x, y), size/4)

def move(x, y):
    return x, y

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    x,y = move(x,y)

    screen.fill((0,0,0))
    draw_tie(screen, [x, y])
    
    pygame.display.flip()
    pygame.time.wait(50)
    
print "ByeBye"
