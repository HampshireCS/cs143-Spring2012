#!/usr/bin/env python

from random import randint

import numpy as npy

class Maze:
    def __init__(self, shape):
        self.shape = self.width, self.height = shape

        self._maze = npy.zeros(shape, dtype=npy.int8)

        self.build()


    def build(self):
        self.end = randint(1, self.width-1), randint(1, self.height-1)
        print self.end
        visited = [self.end]

        while visited:
            # pick a randomly available cell based on location
            pass


if __name__ == "__main__":
    # pprint a maze
    maze = Maze((5,5))

    print " * " * maze.width

