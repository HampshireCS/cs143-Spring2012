#!/usr/bin/env python

import pygame
from pygame.locals import *

class KeyListener(object):
    def on_keydown(self, evt):
        pass

    def on_keyup(self, evt):
        pass


class KeydownCounter(KeyListener):
    def __init__(self, name):
        self.name = name
        self.count = 0

    def on_keydown(self, evt):
        self.count += 1
        print "Pressed %s %d times" % (self.name, self.count)


class KeyToggle(KeyListener):
    def __init__(self, name, state=False):
        self.name = name
        self.state = state

    def on_keydown(self, evt):
        self.state = not self.state
        print "%s: %r" % (self.name, self.state)

class RequiresToggle(KeyListener):
    def __init__(self, listener, method, *toggles):
        self.listener = listener
        self.method = method
        self.toggles = toggles

    def on_keydown(self, evt):
        if self.method(toggle.state for toggle in self.toggles):
            self.listener.on_keydown(evt)
    
    def on_keyup(self, evt):
        if self.method(toggle.state for toggle in self.toggles):
            self.listener.on_keyup(evt)


class KeyInputManager(object):
    def __init__(self):
        self._listeners = {}

    def register(self, key, listener):
        if key not in self._listeners:
            self._listeners[key] = []
        self._listeners[key].append(listener)

    def unregister(self, key, listener):
        if key in self._listener:
            try:
                self._listener[key].remove(listener)
            except ValueError:
                pass

    def __contains__(self, key):
        return key in self._listeners

    def handle_event(self, evt):
        if evt.type == KEYDOWN and evt.key in self._listeners:
            for listener in self._listeners[evt.key]:
                listener.on_keydown(evt)
        elif evt.type == KEYUP and evt.key in self._listeners:
            for listener in self._listeners[evt.key]:
                listener.on_keyup(evt)



pygame.init()
screen = pygame.display.set_mode((400,400))

# create input manager
inpt_mgr = KeyInputManager()

# listeners

# basic counter
counter1 = KeydownCounter("Enter")
counter2 = KeydownCounter("comma or period")

inpt_mgr.register(K_RETURN, counter1)
inpt_mgr.register(K_COMMA, counter2)
inpt_mgr.register(K_PERIOD, counter2)

# basic toggle
toggle_a = KeyToggle("A button switch")
toggle_op = KeyToggle("O or P button switch")

inpt_mgr.register(K_a, toggle_a)
inpt_mgr.register(K_o, toggle_op)
inpt_mgr.register(K_p, toggle_op)

# Space requires
toggles = [ KeyToggle("1 switch"), KeyToggle("2 switch"), KeyToggle("3 switch") ]

for i,t in enumerate(toggles):
    inpt_mgr.register(K_1 + i, t)
inpt_mgr.register(K_SPACE, RequiresToggle(KeydownCounter("Space with any of 1,2,3"), any, *toggles))
inpt_mgr.register(K_SPACE, RequiresToggle(KeydownCounter("Space with all of 1,2,3"), all, *toggles))



clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        inpt_mgr.handle_event(event)

    clock.tick(30)
