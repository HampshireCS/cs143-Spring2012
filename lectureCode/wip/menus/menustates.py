import pygame
from pygame.locals import *

from app import AppState
from menu import Menu

class PauseState(AppState):
    def setup(self):
        AppState.setup(self)

        self.menu = Menu()
        self.menu.add("Resume", None)
        self.menu.add("Restart", None)
        self.menu.add("Main Menu", None)
        self.menu.add("Exit", None)
        self.menu.build()

        # save app state
        self.game = self.app.state

        # render the screen background
        self.background = pygame.display.get_surface().convert()
        overlay = pygame.Surface(self.background.get_size())
        overlay.set_alpha(200)
        overlay.fill((0,0,0))

        self.background.blit(overlay, (0,0))

    def resume(self):
        pygame.mixer.music.pause()

    def resume_game(self):
        pygame.mixer.music.unpause()
        self.app.set_state(self.game)

    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.resume_game()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.menu.draw(self.screen)
        pygame.display.flip()
