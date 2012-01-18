#!/usr/bin/env python

import pygame
from pygame.locals import *

from player import Player

class Game:
    title = "Splody Shmup"
    size = 800,600
    background = 40,40,40
    mouse = False
    fps = 30

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        pygame.mouse.set_visible(self.mouse)

        self.player = Player()

        return self
    
    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill(self.background)
        self.screen.blit(self.player.image, self.player.rect)

    def run(self):
        self.clock = pygame.time.Clock()

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

            # events
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(self.fps)

def main():
    Game().setup().run()
    print "Bye Bye"

if __name__ == "__main__":
    main()
