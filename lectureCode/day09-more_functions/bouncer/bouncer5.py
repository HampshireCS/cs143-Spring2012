from random import randrange

import pygame
from pygame import draw
from pygame.locals import *

SCREEN_SIZE = WIDTH, HEIGHT = 800,600


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


def create_tie(width, height):
    tie = {
        "color": [randrange(100,256), randrange(100,256), randrange(100,256)],
        "pos": [randrange(width), randrange(height), randrange(-4,5), randrange(-4,5)]
    }
    return tie


def move(pos, width, height):
    x,y,dx,dy = pos
    x += dx
    y += dy

    if x < 0 or x >= width:
        dx = -dx
        x += 2*dx
    if y < 0 or y >= height:
        dy = -dy
        y += 2*dy

    return x, y, dx, dy


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

ties = [ create_tie(WIDTH, HEIGHT) ] 

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            ties.append(create_tie(WIDTH, HEIGHT))

    for tie in ties:
        color = tie["color"]
        tie["pos"] = move(tie["pos"], WIDTH, HEIGHT)


    screen.fill((0,0,0))
    for tie in ties:
        draw_tie(screen, tie["pos"][:2], tie["color"])
    
    pygame.display.flip()
    pygame.time.wait(20)
    
print "ByeBye"
