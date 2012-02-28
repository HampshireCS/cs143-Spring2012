#!/usr/bin/env python

import pygame
from pygame import Rect
from pygame.font import Font
from pygame.locals import *

pygame.init()

### Constants
SCREEN_SIZE = 800, 600

BACKGROUND = 0,0,0,255
FOREGROUND = 255,255,255,255
BLURRED = 100,100,100,255
MSG_BG = 30,30,30,255

CENTER_WIDTH = 4
DIST_FROM_EDGE = 25
PADDLE_SIZE = 10, 80

FPS = 30
FLASH_RATE = FPS

### Text
FONT_LARGE = Font(None, 80)
FONT_MSG = Font(None, 32)

title_text = FONT_LARGE.render("GAME", True, FOREGROUND, MSG_BG)
title_size = title_text.get_rect().inflate(40,20).size

TITLE = pygame.Surface(title_size)
TITLE.fill(FOREGROUND)
TITLE.fill(MSG_BG, TITLE.get_rect().inflate(-10, -10))
TITLE.blit(title_text, (20,13))


### General
def msg_render(text):
    return FONT_MSG.render(text, True, FOREGROUND, MSG_BG)

def draw_board(surf, color, state):
    bounds = surf.get_rect()

    cx = bounds.centerx - CENTER_WIDTH/2
    pygame.draw.rect(surf, color, (cx, 0, CENTER_WIDTH, bounds.height))

    pygame.draw.rect(surf, color, state["p1"])
    pygame.draw.rect(surf, color, state["p2"])
    

def draw_score(surf, color, s1, s2):
    pass

def serve(state):
    state["toserve"] = None
    

def move_ball(state):
    pass

### Game
def game_init(state):
    state["inmenu"] = False
    state["gameover"] = False

    state["score"] = [0,0]

    state["p1"] = Rect((0,0),  PADDLE_SIZE)
    state["p2"] = Rect((0,0),  PADDLE_SIZE)

    state["p1"].midleft = DIST_FROM_EDGE, state["bounds"].centery 
    state["p2"].midright = state["bounds"].width - DIST_FROM_EDGE, state["bounds"].centery

    if not state["paused"]:
        state["toserve"] = 0
        pass


def game_input(state, event):
    pass

def game_update(state):
    _, my = pygame.mouse.get_pos()

    state["p1"].centery = my
    state["p1"].clamp_ip(state["bounds"])


def game_draw(state, surf):
    surf.fill(BACKGROUND)

    draw_board(surf, FOREGROUND, state)

### Main Menu
def menu_init(state, text=None):
    state["paused"] = text is not None

    if not state["paused"]:
        game_init(state)
        state["text"] = msg_render("Click to Start")
        state["step"] = 0
        state["text_off"] = TITLE.get_rect().height * 1.25
    else:
        pass

    state["inmenu"] = True


def menu_input(state, event):
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        if state["paused"]:
            game_init(state)
        else:
            state["quit"] = True

    elif event.type == MOUSEBUTTONDOWN:
        game_init(state)


def menu_update(state):
    if state["paused"]:
        return

    state["step"] += 1

    flash = state["step"] % (FLASH_RATE * 2)
    state["show_text"] = flash < FLASH_RATE


def menu_draw(state, surf):
    surf.fill(BACKGROUND)

    bounds = surf.get_rect()

    draw_board(surf, BLURRED, state)
    
    if state["paused"]:
        pass

    else:
        pos = TITLE.get_rect()
        pos.center = bounds.center
        pos.centery -=  TITLE.get_height() * 1.25
        surf.blit(TITLE, pos)

    if state["show_text"]:
        pos = state["text"].get_rect()
        pos.center = bounds.center
        pos.centery += state["text_off"]
        surf.blit(state["text"], pos)


def main():
    screen = pygame.display.set_mode(SCREEN_SIZE)

    state = {}
    state["quit"] = False
    state["bounds"] = screen.get_rect()
    menu_init(state)

    clock = pygame.time.Clock()
    while not state["quit"]:
        for event in pygame.event.get():
            if event.type == QUIT:
                state["quit"] = True

            if state["inmenu"]:
                menu_input(state, event)
            else:
                game_input(state, event)

        if state["quit"]:
            continue

        if state["inmenu"]:
            menu_update(state)
            menu_draw(state, screen)
        else:
            game_update(state)
            game_draw(state, screen)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    print "ByeBye"
