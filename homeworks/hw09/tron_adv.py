#!/usr/bin/env python
import math

import pygame
from pygame.locals import *
import numpy

# SCREEN
SCREEN_SIZE = 660, 360

# GRID
TILE = 30
OUTLINE = 2
WIDTH = 660/30
HEIGHT = 360/30

# COLORS
BACKGROUND = 0x505050
OUTLINE_COLOR = 0
P1_COLOR = 0xff0000
P2_COLOR = 0x0000ff

# TERMS
P1_NAME = "Red"
P2_NAME = "Blue"

# DIRECTIONS
N = 1
E = 2
S = 3
W = 4

# STATES
RESET = 0
READY = 1
PLAYING = 2
GAMEOVER = 3
PAUSE = 4
RESUME = 5

def next_pos(trail, direction):
    x,y = trail[-1]
    if direction == N:
        return x, y-1
    elif direction == E:
        return x+1, y
    elif direction == S:
        return x, y+1
    else:
        return x-1, y

def has_crashed(pos, *trails):
    x,y = pos

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
       return True
    elif any( (x,y) in trail for trail in trails ):
        return True
    else:
        return False

def draw_cell(surf, trail, direction, color):
    x,y = trail[-1]
    surf.fill(OUTLINE_COLOR, (x*TILE, y*TILE, TILE, TILE))
    surf.fill(color, (x*TILE + OUTLINE, y*TILE + OUTLINE, TILE - OUTLINE*2, TILE - OUTLINE*2))
    
    if direction == N:
        surf.fill(color, (x*TILE + OUTLINE, (y+1)*TILE - OUTLINE, TILE - 2*OUTLINE, 2*OUTLINE))
    if direction == E:
        surf.fill(color, (x*TILE - OUTLINE, y*TILE + OUTLINE, 2*OUTLINE, TILE - 2*OUTLINE))
    if direction == S:
        surf.fill(color, (x*TILE + OUTLINE, y*TILE - OUTLINE, TILE - 2*OUTLINE, 2*OUTLINE))
    if direction == W:
        surf.fill(color, ((x+1)*TILE - OUTLINE, y*TILE + OUTLINE, 2*OUTLINE, TILE - 2*OUTLINE))

def draw_explosion(surf, pos, dir, color):
    x,y = pos

    if dir == E:
        x += 1
    elif dir == S:
        y += 1

    x *= TILE
    y *= TILE

    if dir == N or dir == S:
        x += TILE/2
    if dir == E or dir == W:
        y += TILE/2

    angs = [ 2 * math.pi * i / 16.0 for i in range(16) ]
    radius1 = [ TILE * (i%2 + 0.5) for i in range(16) ]
    radius2 = [ TILE * (i%2 + 0.5) + 5 for i in range(16) ]

    pts1 = [ (x + r*math.cos(t), y + r*math.sin(t)) for r,t in zip(radius1, angs) ]
    pts2 = [ (x + r*math.cos(t), y + r*math.sin(t)) for r,t in zip(radius2, angs) ]

    pygame.draw.polygon(surf, 0xffffff, pts2)
    pygame.draw.polygon(surf, color, pts1)


def main():
    
    # init
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("TRON")
    pygame.mouse.set_visible(False)

    # initial graphics
   
    p1_score = 0
    p2_score = 0

    clock = pygame.time.Clock()
    done = False
    state = RESET
    buff = None
    while not done:
        # input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            elif event.type == KEYDOWN and event.key == K_SPACE and state == PLAYING:
                state = PAUSE
            elif event.type == KEYDOWN and event.key == K_SPACE and state == PAUSE:
                state = RESUME
            elif event.type == KEYDOWN and event.key == K_SPACE and state == GAMEOVER:
                state = RESET
            if state == PLAYING or state == READY:
                if event.type == KEYDOWN and event.key == K_w and p1_dir != S:
                    p1_dir = N
                elif event.type == KEYDOWN and event.key == K_a and p1_dir != E:
                    p1_dir = W
                elif event.type == KEYDOWN and event.key == K_s and p1_dir != N:
                    p1_dir = S
                elif event.type == KEYDOWN and event.key == K_d and p1_dir != W:
                    p1_dir = E
                elif event.type == KEYDOWN and event.key == K_UP and p2_dir != S:
                    p2_dir = N
                elif event.type == KEYDOWN and event.key == K_LEFT and p2_dir != E:
                    p2_dir = W
                elif event.type == KEYDOWN and event.key == K_DOWN and p2_dir != N:
                    p2_dir = S
                elif event.type == KEYDOWN and event.key == K_RIGHT and p2_dir != W:
                    p2_dir = E

            if state == READY:
                if event.type == KEYUP and event.key == K_w:
                    p1_dir = None
                elif event.type == KEYUP and event.key == K_a:
                    p1_dir = None
                elif event.type == KEYUP and event.key == K_s:
                    p1_dir = None
                elif event.type == KEYUP and event.key == K_d:
                    p1_dir = None
                elif event.type == KEYUP and event.key == K_UP:
                    p2_dir = None
                elif event.type == KEYUP and event.key == K_LEFT:
                    p2_dir = None
                elif event.type == KEYUP and event.key == K_DOWN:
                    p2_dir = None
                elif event.type == KEYUP and event.key == K_RIGHT:
                    p2_dir = None

        # update
        if state == RESET:
            winner = None
            dirty = True
            p1 = [(2,2)]
            p1_dir = None

            p2 = [(WIDTH - 3, HEIGHT - 3)]
            p2_dir = None
            state = READY

        if state == READY and p1_dir and p2_dir:
            state = PLAYING

        if state == PLAYING:
            dirty = True
            p1_pos = next_pos(p1, p1_dir)
            p2_pos = next_pos(p2, p2_dir)
            if has_crashed(p1_pos, p1, p2):
                winner = p2
                state = GAMEOVER
            else:
                p1.append(p1_pos)
            
            if has_crashed(p2_pos, p1, p2):
                if winner:
                    winner = None
                else:
                    winner = p1
                state = GAMEOVER
            else:
                p2.append(p2_pos)
                pass

        # drawing
        if state == READY:
            if dirty:
                screen.fill(BACKGROUND)
                draw_cell(screen, p1, None, P1_COLOR)
                draw_cell(screen, p2, None, P2_COLOR)
            pygame.display.flip()
            dirty = False
            clock.tick(30)

        elif state == PLAYING:
            draw_cell(screen, p1, p1_dir, P1_COLOR)
            draw_cell(screen, p2, p2_dir, P2_COLOR)
            pygame.display.flip()
            clock.tick(12)

        elif state == PAUSE:
            if dirty:
                buff = screen.convert()
                pixels = pygame.surfarray.pixels2d(screen)
                pixels[:] *= 0.5
                del pixels
                pygame.display.flip()
            dirty = False
            clock.tick(30)

        elif state == RESUME:
            screen.blit(buff, (0,0))
            state = PLAYING

        elif state == GAMEOVER:
            if dirty:
                if winner == p1:
                    p1_score += 1
                    p1_hit = None
                    p2_hit = p2_pos
                    winner_color = P1_COLOR
                elif winner == p2:
                    p2_score += 1
                    p1_hit = p1_pos
                    p2_hit = None
                    winner_color = P2_COLOR
                else:
                    p1_hit = p1_pos
                    p2_hit = p2_pos
                    winner_color = 0x202020

                pixels = pygame.surfarray.pixels2d(screen)
                pixels[ pixels == OUTLINE_COLOR ] = ~OUTLINE_COLOR
                pixels[ pixels == P1_COLOR ] = OUTLINE_COLOR
                pixels[ pixels == P2_COLOR ] = OUTLINE_COLOR
                pixels[ pixels == BACKGROUND ] = winner_color
                del pixels

                # draw explosion
                if p1_hit:
                    draw_explosion(screen, p1[-1], p1_dir, P1_COLOR)
                if p2_hit:
                    draw_explosion(screen, p2[-1], p2_dir, P2_COLOR)

                # print score
                print "%s: %d, %s: %d" % (P1_NAME, p1_score, P2_NAME, p2_score)

                pygame.display.flip()
            dirty = False
            clock.tick(30)

if __name__ == "__main__":
    main()
    print "ByeBye"
