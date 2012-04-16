from math import ceil, floor

import pygame
from pygame.locals import *

from pygame import Rect

MAX_DEPTH = 10

class QuadTreeNode(object):

    def __init__(self, rect, depth = 0):
        self.rect = rect
        self.data = None
        self.is_split = False

        self.ne = None
        self.nw = None
        self.se = None
        self.sw = None

        self.depth = depth

    def add_point(self, point):
        # if we don't have data, just add it
        if self.data is None and not self.is_split:
            self.data = point
            return
        elif self.depth == MAX_DEPTH:
            self.data = point
            return

        # if already haven't split, do that now
        if not self.is_split:
            prev_point = self.data
            self.is_split = True

            r = self.rect
            w = self.rect.width / 2.0
            h = self.rect.height / 2.0
            d = self.depth + 1

            self.nw = QuadTreeNode( Rect(r.left, r.top, floor(w), floor(h) ), d )
            self.ne = QuadTreeNode( Rect(r.centerx, r.top, ceil(w), floor(h) ), d ) 
            self.sw = QuadTreeNode( Rect(r.left, r.centery, floor(w), ceil(h) ), d )
            self.se = QuadTreeNode( Rect(r.centerx, r.centery, ceil(w), ceil(h) ), d )

            # re add the point
            self.add_point(prev_point)

        # add the point to the split
        if self.nw.rect.collidepoint(point):
            self.nw.add_point(point)
        elif self.ne.rect.collidepoint(point):
            self.ne.add_point(point)
        elif self.sw.rect.collidepoint(point):
            self.sw.add_point(point)
        else:
            self.se.add_point(point)

def get_active(node, point):
    if not node.rect.collidepoint(point):
        return None

    if node.is_split:
        if node.nw.rect.collidepoint(point):
            return get_active(node.nw, point)
        elif node.ne.rect.collidepoint(point):
            return get_active(node.ne, point)
        elif node.sw.rect.collidepoint(point):
            return get_active(node.sw, point)
        elif node.se.rect.collidepoint(point):
            return get_active(node.se, point)
    else:
        return node


def get_points(node=None):
    if node is None:
        node = self.root

    if node.is_split:
        points = get_points(node.nw) 
        points += get_points(node.ne) 
        points += get_points(node.sw) 
        points += get_points(node.se)
        return points

    elif node.data is not None:
        return [ node.data ]

    else:
        return []

def get_bounds(node, bounds=None):
    if bounds is None:
        bounds = []

    bounds.append(node.rect)
    if node.is_split:
        get_bounds(node.nw, bounds)
        get_bounds(node.ne, bounds)
        get_bounds(node.sw, bounds)
        get_bounds(node.se, bounds)

    return bounds


pygame.init()
screen = pygame.display.set_mode((800, 800))
root = QuadTreeNode(screen.get_rect())

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            root.add_point(pygame.mouse.get_pos())

    screen.fill(0)

    # draw quadtree
    active = get_active(root, pygame.mouse.get_pos())
    if active:
        screen.fill((80,80,80), active.rect)


    for rect in get_bounds(root):
        pygame.draw.rect(screen, (170, 170, 170), rect, 1)

    for point in get_points(root):
        pygame.draw.circle(screen, (255,255,255), point, 3)

    pygame.display.flip()
    clock.tick(30)
