import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

from collections import namedtuple

pygame.init()
screen = pygame.display.set_mode((800,600))


def draw_tie(surf, tie):
    "Draws a tie fighter"
    color = 255,0,0
    x,y,dx,dy,size = tie
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)


def move(tie, bounds):
    x, y, dx, dy, size = tie

    x += dx
    y += dy

    if x < bounds.left or x + size > bounds.right:
        dx = -dx
        x += 2 * dx
        split(tie)

    if y < bounds.top or y + size > bounds.bottom:
        dy = -dy
        y += 2 * dy
        split(tie)

    return x,y,dx,dy,size


def split(tie):
    global ties
    x,y,dx,dy,size = tie
    size /= 2
    if size != 0:
        ties.append([x,y,-dx,-dy,size])

ties = [
  [400, 300, 2, 2, 40],
  [200, 200, -1, 3, 50]
]
bounds = screen.get_rect()

done = False
clock = pygame.time.Clock() 
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    for i in range(len(ties)):
        ties[i] = move(ties[i], bounds)
    

    screen.fill((0,0,0))
    for tie in ties:
        draw_tie(screen, tie)
    
    pygame.display.flip()
    clock.tick(30)
    
print "ByeBye"
