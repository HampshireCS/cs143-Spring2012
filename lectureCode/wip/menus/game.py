"""
game.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import spritecollide, GroupSingle

from app import AppState
from level import Level
from resource import play_song

from menustates import PauseState

class GameState(AppState):
    fps = 60

    def setup(self):
        AppState.setup(self)

        self.level = Level(self.screen.get_size())
        self.level.restart()

    def resume(self):
        self.clock = pygame.time.Clock()

    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.app.set_state(PauseState)

    def update(self):
        dt = self.clock.tick(self.fps)
        self.level.update(dt)

    def draw(self):
        self.level.draw(self.screen)
        pygame.display.flip()

