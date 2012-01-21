from pygame import draw
from pygame import Surface

from core import MazeArray
from constants import *

class MazeWalker:
    class Path:
        pass

class Maze:
    class colors:
        background = 50,50,50
        wall = 255,255,255
        start = 255,255,0
        end = 0,255,0

    def __init__(self, shape):
        self.colors = Maze.colors()
        self._maze = MazeArray(shape)

    def render(self, image, tile, wall):
        w,h = self._maze.shape
        cell = tile + wall

        north = wall,cell
        west = cell,wall
        corner = wall,wall

        image.fill(self.colors.background)

        # render start and end locations
        start = [ i*tile+wall for i in self._maze.start ]
        end = [ i*tile+wall for i in self._maze.end ]

        draw.rect(image, self.colors.start, (start, (tile,tile)))
        draw.rect(image, self.colors.end, (end, (tile,tile)))

        # draw upper corner

        # loop through maze and draw north and east side
        for x in range(w):
            for y in range(h):
                pos = x*cell, y*cell

                draw.rect(image, self.colors.wall, (pos, corner))

                v = self._maze.get(x,y)
                if v.north:
                    draw.rect(image, self.colors.wall, (pos, north))
                if v.west:
                    draw.rect(image, self.colors.wall, (pos, west))

        


        return image
