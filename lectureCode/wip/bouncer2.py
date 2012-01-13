import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

#from tie9.py
ties = []
pygame.init()
screen = pygame.display.set_mode((800,600))
xloc, yloc = (400,300)
dx = 5
dy = 5

def draw_tie(surf, pos, color=(randrange(100,256), randrange(100,256), randrange(100,256)), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    wall = size/8
    x0,x1 = x - (size/2), x + (size/2)
    y0,y1 = y - (size/2), y + (size/2)

    draw.rect(surf, color, (x0, y0, wall, size))
    draw.rect(surf, color, (x1-wall, y0, wall, size))
    draw.rect(surf, color, (x0, y-(wall/2), size, wall))
    draw.circle(surf, color, (x, y), size/4)

def move(x, y, dx, dy):
    x = x + dx
    y = y + dy
    draw_tie(screen, [x,y])
    return x, y, dx, dy

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
    screen.fill((0,0,0))
    xloc, yloc, dx, dy = move(xloc,yloc, dx, dy)
    
    pygame.display.flip()
    pygame.time.wait(50)
    
print "well isn't that nice."