import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
tie_x, tie_y = 400,300
tie_dx, tie_dy = 2,2

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)


def move(x,y,dx,dy):
    x += dx
    y += dy
    return x,y

done = False
clock = pygame.time.Clock() 
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    tie_x, tie_y = move(tie_x, tie_y, tie_dx, tie_dy)

    screen.fill((0,0,0))
    draw_tie(screen, [tie_x, tie_y])
    
    pygame.display.flip()
    clock.tick(15)
    
print "ByeBye"
