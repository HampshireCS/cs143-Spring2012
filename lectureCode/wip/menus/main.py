import pygame

from app import Application
from game import GameState

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Super Coin Get")

    app = Application(screen)
    app.set_state(GameState)

    # create game
    try:
        app.run()
    except KeyboardInterrupt:
        app.quit()

if __name__ == "__main__":
    main()
