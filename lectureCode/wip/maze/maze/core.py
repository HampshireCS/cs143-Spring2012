#!/usr/bin/env python

from random import randint, randrange, choice
import numpy as npy

from constants import *

class Cell:
    def __init__(self, v):
        self.north = (v & N) == 0
        self.east = (v & E) == 0
        self.south = (v & S) == 0
        self.west = (v & W) == 0

_CELLS = [ Cell(i) for i in range(16) ]

class MazeArray:
    def __init__(self, shape):
        self.shape = self.width, self.height = shape
        self.build()

    def _unvisited(self,locs):
        return [ [d,x,y] for d,x,y in locs if self._maze[y,x] == 0 ]

    def _get_neighbors(self, pos):
        x,y = pos
        w,h = self._maze.shape
        
        neighbors = []
        if y >= 1:  # north
            neighbors.append((N,x,y-1))
        if y < h-1:
            neighbors.append((S,x,y+1))
        if x >= 1:  # west
            neighbors.append((W,x-1,y))
        if x < w-1:
            neighbors.append((E,x+1, y))

        return neighbors

    def _destroy_wall(self, d, cur, nxt):
        x0,y0 = cur
        x1,y1 = nxt
        self._maze[y0,x0] |= d
        self._maze[y1,x1] |= d.back

    def build(self):
        self._dirty = True

        self._maze = npy.zeros(self.shape, dtype=npy.int8)
        self.start = 0,0
        self.end = randint(1, self.width-1), randint(1, self.height-1)

        self._make_path()
        self._remove_deadends()

    def get(self,x,y):
        return _CELLS[ self._maze[y,x] ]

    def _make_path(self):
        # build depthfirst maze
        visited = [self.end]
        while visited:
            current = visited[-1]

            # grab random neighbor
            unvisited = self._unvisited(self._get_neighbors(current))

            # if no unvisited, go out one
            if len(unvisited) == 0:
                visited.pop()
                continue

            cell = choice(unvisited)
            d = cell[0]
            nxt = cell[1:]

            self._destroy_wall(d, current, nxt)
            visited.append(nxt)

    def _remove_deadends(self): 
        # remove deadends
        w,h = self.shape
        deadends = [N,S,E,W]
        for x in range(w):
            for y in range(h):
                loc = x,y
                v = int(self._maze[y,x])
                if loc != self.start and loc != self.end:
                    neighbors = self._get_neighbors(loc)
                    while v in deadends:
                        cell = choice(neighbors)
                        d = cell[0]
                        nxt = cell[1:]
                        self._destroy_wall(d,loc,nxt)
                        v = int(self._maze[y,x])


if __name__ == "__main__":
    # pprint a maze
    size = 5,5
    maze = MazeArray(size)

    maze.build()

    print maze._maze

