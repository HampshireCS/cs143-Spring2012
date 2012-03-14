#!/usr/bin/env python

from random import randint, randrange, choice

N = 1
E = 2
S = 4
W = 8

import pygame

class Cell:
    _north = None
    _east = None
    _south = None
    _west = None
    _ready = False
    _seen = False

    @property
    def north(self):
        result = self._north
        if result is not None and self._ready:
            result._seen = True
        return result

    @property
    def east(self):
        result = self._east
        if result is not None and self._ready:
            result._seen = True
        return result
    
    @property
    def west(self):
        result = self._west
        if result is not None and self._ready:
            result._seen = True
        return result
    
    @property
    def south(self):
        result = self._south
        if result is not None and self._ready:
            result._seen = True
        return result

class Maze:
    def __init__(self, shape):
        self.shape = self.width, self.height = shape
        self.build()

    def _unvisited(self,locs):
        for d,x,y in locs:
            result = self._maze[x][y]._north is None
            result = result and self._maze[x][y]._south is None
            result = result and self._maze[x][y]._east is None
            result = result and self._maze[x][y]._west is None
            
            if result:
                yield [d,x,y]


    def _get_neighbors(self, pos):
        x,y = pos
        w,h = self.shape
        
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
        if d == N:
            self._maze[x0][y0]._north = self._maze[x1][y1]
            self._maze[x1][y1]._south = self._maze[x0][y0]
        elif d == S:
            self._maze[x0][y0]._south = self._maze[x1][y1]
            self._maze[x1][y1]._north = self._maze[x0][y0]
        elif d == E:
            self._maze[x0][y0]._east = self._maze[x1][y1]
            self._maze[x1][y1]._west = self._maze[x0][y0]
        elif d == W:
            self._maze[x0][y0]._west = self._maze[x1][y1]
            self._maze[x1][y1]._east = self._maze[x0][y0]

    def build(self):
        self._init_maze()
        self._make_path()

        x0,y0 = self.start
        x1,y1 = self.end
        self.start = self._maze[x0][y0]
        self.end = self._maze[x1][y1]

        self.start._seen = True
        self.end._seen = True
        for x in range(self.width):
            for y in range(self.height):
                self._maze[x][y]._ready = True
                self._maze[x][y]._x = x
                self._maze[x][y]._y = y


    def _init_maze(self):
        self._maze = [ [ Cell() for y in range(self.height) ] for x in range(self.width) ]
        self.start = 0,0
        self.end = self.width-1, self.height-1

    def _make_path(self):
        # build depthfirst maze
        visited = [self.end]
        while visited:
            current = visited[-1]

            # grab random neighbor
            unvisited = list(self._unvisited(self._get_neighbors(current)))

            # if no unvisited, go out one
            if len(unvisited) == 0:
                visited.pop()
                continue

            cell = choice(unvisited)
            d = cell[0]
            nxt = cell[1:]

            self._destroy_wall(d, current, nxt)
            visited.append(nxt)


class MazeGraphics(object):
    def __init__(self, maze, tile, border):
        self._maze = maze
        self.tile = tile
        self.border = border

    def maze(self, fg, bg, start, end):
        border, tile, maze = self.border, self.tile, self._maze
        width = (tile + border) * maze.width + border
        height = (tile + border) * maze.height + border

        cellw = tile + border

        image = pygame.Surface((width, height))
        image.fill(bg)

        for x in range(maze.width):
            for y in range(maze.height):
                cell = maze._maze[x][y]
                if cell is maze.start:
                    image.fill(start, (x*cellw, y*cellw, cellw, cellw))
                if cell is maze.end:
                    image.fill(end, (x*cellw, y*cellw, cellw, cellw))
                if cell.north is None:
                    image.fill(fg, (x*cellw, y*cellw, cellw+border, border))
                if cell.west is None:
                    image.fill(fg, (x*cellw, y*cellw, border, cellw+border))

        image.fill(fg, (width-border, 0, border, height))
        image.fill(fg, (0, height-border, width, border))

        return image

    def walker(self, walker, path, visited):
        for cell in walker._visited:
            


class MazeWalker(object):
    def __init__(self, maze):
        self._location = maze.start
        self._end = maze.end
        self._won = False
        self._facing = E
        self._visited = [maze.start]
        self._path = [maze.start]


    @property
    def location(self):
        return self._location

    @property
    def forward(self):
        if self._facing == N:
            return self._location.north
        elif self._facing == S:
            return self._location.south
        elif self._facing == E:
            return self._location.east
        elif self._facing == W:
            return self._location.west

    @property
    def left(self):
        if self._facing == N:
            return self._location.west
        elif self._facing == S:
            return self._location.east
        elif self._facing == E:
            return self._location.north
        elif self._facing == W:
            return self._location.south

    @property
    def right(self):
        if self._facing == N:
            return self._location.east
        elif self._facing == S:
            return self._location.west
        elif self._facing == E:
            return self._location.south
        elif self._facing == W:
            return self._location.north

    def go_forward(self):
        if self._facing == N:
            self._location = self._location.north
        elif self._facing == S:
            self._location = self._location.south
        elif self._facing == E:
            self._location = self._location.east
        elif self._facing == W:
            self._location = self._location.west
        self._visited.append(self._location)
        self._path.append(self._location)

    def go_left(self):
        if self._facing == N:
            self._location = self._location.west
            self._facing = W
        elif self._facing == S:
            self._location = self._location.east
            self._facing = E
        elif self._facing == E:
            self._location = self._location.north
            self._facing = N
        elif self._facing == W:
            self._location = self._location.south
            self._facing = S
        self._visited.append(self._location)
        self._path.append(self._location)

    def go_right(self):
        if self._facing == N:
            self._location = self._location.east
            self._facing = E
        elif self._facing == S:
            self._location = self._location.west
            self._facing = W
        elif self._facing == E:
            self._location = self._location.south
            self._facing = S
        elif self._facing == W:
            self._location = self._location.north
            self._facing = N
        self._visited.append(self._location)
        self._path.append(self._location)

    def turn_around(self):
        self._path.pop()
        self._location = self._path[-1]
        self._visited.append(self._location)

        if self._facing == N:
            self._facing = S
        elif self._facing == S:
            self._facing = N
        elif self._facing == W:
            self._facing = E
        elif self._facing == E:
            self._facing = W

    def update(self):
        if self._location is self._end:
            self._won = True
            return

        self.step()

