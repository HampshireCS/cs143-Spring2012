"""
level.py

"""

import os

import pygame
from pygame import Rect, Surface
from pygame.sprite import Group, spritecollide

from resource import load_image, play_song

from player import Player
from coin import CoinGroup

class Level(object):
    initial_coins = 5
    song = "maintheme"

    def __init__(self, size):
        self.bounds = Rect((0,0), size)
        self.bg_tile = load_image("grass")
        self.score_font = pygame.font.Font(None, 48)

    def draw_background(self, surf):
        tw, th = self.bg_tile.get_size()
        sw, sh = surf.get_size()

        for y in range(0, sh, th):
            for x in range(0, sw, tw):
                surf.blit(self.bg_tile, (x,y))

    def restart(self):
        self.score = 0
        self.player = Player()
        self.player.rect.center = self.bounds.center

        self.coins = CoinGroup(self.bounds)

        # create initial coins
        for i in range(self.initial_coins):
            self.coins.spawn()

        # start the background music
        play_song(self.song)
    
    def update(self, dt):
        self.player.update(dt)
        self.coins.update(dt)

        # lock player in bounds
        self.player.rect.clamp_ip(self.bounds)

        # collide player with coins
        if spritecollide(self.player, self.coins, True):
            self.score += 1

    def draw(self, surf):
        self.draw_background(surf)
        self.coins.draw(surf)
        surf.blit(self.player.image, self.player.rect)

        score = self.score_font.render(str(self.score), True, (0,0,0))
        rect = score.get_rect()
        rect.topright = self.bounds.inflate(-5, -5).topright
        surf.blit(score, rect)
