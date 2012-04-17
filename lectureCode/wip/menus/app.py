import pygame
from pygame.locals import *

class AppState(object):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self._setup = False

    def setup(self):
        self._setup = True

    def resume(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Application(object):
    def __init__(self, screen):
        self.screen = screen

    def quit(self):
        self.done = True

    def set_state(self, state):
        # if not instantiated, do so
        if not isinstance(state, AppState):
            state = state(self)

        # run setup if it hasn't been run already
        if not state._setup:
            state.setup()
        state.resume()

        # store this state
        self.state = state

    def run(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                else:
                    self.state.handle_event(event)
            self.state.update()
            self.state.draw()
