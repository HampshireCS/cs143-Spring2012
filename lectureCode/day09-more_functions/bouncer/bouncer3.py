import pygame
from pygame import draw
from pygame.locals import *

SCREEN_SIZE = WIDTH, HEIGHT = 800,600

#from tie9.py
ties = []
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
x,y = 400,300
dx,dy = 2,2

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

def move(x, y, dx, dy,width,height):
    x += dx
    y += dy

    if x < 0 or x >= width:
        dx = -dx
        x += 2*dx
    if y < 0 or y >= height:
        dy = -dy
        y += 2*dy

    return x, y, dx, dy

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    x,y,dx,dy = move(x,y,dx,dy,WIDTH,HEIGHT)

    screen.fill((0,0,0))
    draw_tie(screen, [x, y])
    
    pygame.display.flip()
    pygame.time.wait(20)
    
print "ByeBye"
