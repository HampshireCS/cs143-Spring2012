#!/usr/bin/env python

import pygame
from pygame.locals import *

# constants
NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

PAUSED = 0
PLAYING = 1
DEAD = 2

# colors
C_BG = 0, 0, 0
C_SNAKE = 0, 255, 0
C_DEAD = 255, 0, 0
C_ITEM = 255, 255, 0

# game
SQUARE = 20
STATE = PAUSED
SCORE = 0

# snake
SPEED = 10
LENGTH = 3
CELLS = []
START = 
DIRECTION = EAST

pygame.init()
screen = pygame.display.set_mode()
