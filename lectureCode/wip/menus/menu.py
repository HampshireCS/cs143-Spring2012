import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group


class MenuItem(Sprite):
    def __init__(self, menu, text, action):
        Sprite.__init__(self)

        self.menu = menu
        self.text = text
        self.action = action


    def draw_normal(self):
        self.image.fill((0,0,0,0))

        text = self.menu.font.render(self.text, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = self.image.get_rect().center

        self.image.blit(text, rect)

    def draw_hover(self):
        pass

    def draw_active(self):
        pass


class Menu(object):
    item_type = MenuItem
    font_size = 40
    padding = 20
    margin = 3
    
    def __init__(self):
        self.active = None
        self.mousedown = False
        self.font = pygame.font.Font(None, self.font_size)
        self.items = []


    def add(self, text, action):
        item = self.item_type(self, text, action)
        self.items.append(item)


    def build(self):
        # calculate the max dimensions
        max_w, max_h = 0, 0
        for item in self.items:
            width, height = self.font.size(item.text)
            max_w = max(width, max_w)
            max_h = max(height, max_h)

        rect = Rect(0,0,max_w,max_h).inflate(self.padding, self.padding)

        # place and initialize each menu item
        bounds = Rect(0, 0, 0, 0)
        top = 0
        for item in self.items:
            item.image = Surface(rect.size, SRCALPHA)
            item.rect = rect.copy()
            item.rect.top = top

            top = item.rect.bottom + self.margin
            
            bounds.union_ip(item.rect)

        # tmp, render each sprite initially
        for item in self.items:
            item.draw_normal()

    def draw(self, surf):
        subsurf = surf
        for item in self.items:
            subsurf.blit(item.image, item.rect)



