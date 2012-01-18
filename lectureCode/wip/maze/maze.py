#!/usr/bin/env python

from random import randint, randrange, choice

import numpy as npy

N = 1
E = 2
S = 4
W = 8

_flipped = {
    N: S,
    S: N,
    E: W,
    W: E
}

class Maze:
    def __init__(self, shape):
        self.shape = self.width, self.height = shape
        self.build()

    def _unvisited(self,locs):
        return [ [d,x,y] for d,x,y in locs if self._maze[x,y] == 0 ]

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
        self._maze[x0,y0] |= d
        self._maze[x1,y1] |= _flipped[d]

    def build(self):
        self._maze = npy.zeros(self.shape, dtype=npy.int8)
        self.start = 0,0
        self.end = randint(1, self.width-1), randint(1, self.height-1)

        # build depthfirst maze
        visited = [self.end]
        while visited:
            current = visited[0]

            # grab random neighbor
            unvisited = self._unvisited(self._get_neighbors(current))

            # if no unvisited, go out one
            if len(unvisited) == 0:
                visited.pop(0)
                continue

            cell = choice(unvisited)
            d = cell[0]
            nxt = cell[1:]

            self._destroy_wall(d, current, nxt)
            visited.append(nxt)
        
        # remove deadends
        w,h = self.shape
        deadends = [N,S,E,W]
        for x in range(w):
            for y in range(h):
                loc = x,y
                v = int(self._maze[x,y])
                if loc != self.start and loc != self.end:
                    neighbors = self._get_neighbors(loc)
                    while v in deadends:
                        cell = choice(neighbors)
                        d = cell[0]
                        nxt = cell[1:]
                        self._destroy_wall(d,loc,nxt)
                        v = int(self._maze[x,y])


if __name__ == "__main__":
    # pprint a maze
    maze = Maze((100,100))

    maze.build()

    for row in maze._maze:
        print " ".join(["%04d" % int(bin(i)[2:]) for i in row ])
    print maze._maze

