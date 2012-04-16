"""
game.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import GroupSingle, groupcollide

from coin import CoinGroup
from images import ImageManager
from level import Level
from player import Player
from tilesheet import TileSheet

from settings import FPS, COIN_N_STARTING


class Game(object):

    def __init__(self, screen):
        self.screen = screen

#        tilesheet = TileSheet(ImageManager().load("tiles"), (32, 32))
#        self.level = Level("test_level", tilesheet)
#        self.player = GroupSingle(Player(self.level.bounds))
        self.coins = CoinGroup(self.level.bounds)

        self.font = pygame.font.Font(None, 36)

        # create initial coins
        for i in range(COIN_N_STARTING):
            self.coins.spawn()


    def quit(self):
        self.done = True


    def update(self):
        dt = self.clock.tick(FPS)

        # basic update
        self.player.update(dt)
        self.coins.update(dt)

        # check if the player is on the path
        onpath = spritecollide(self.player, self.level.path, False)
        self.player.on_path(onpath)

        # collide coins
        for coin in spritecollide(self.player, self.coins, True):
            self.score += 1

        self.cam.update(self.player.rect)


    def draw(self):
        # draw level
        self.cam.draw_background(self.game_area, self.level.background)
        self.cam.draw_sprite(self.game_area, self.player)

        for coin in self.coins:
            self.cam.draw_sprite(self.game_area, coin)


    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()

        while not self.done:
            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.quit()

            self.update()
            self.draw()
            pygame.display.flip()

