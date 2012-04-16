#!/usr/bin/env python
import os
import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_tie, draw_ywing
from utils import *

class DeathCount(object):
    filename = ".shiphunt"
    def __init__(self):
        self.path = os.path.join(os.path.expanduser("~"), self.filename)
        if not os.path.exists(self.path):
            self.count = 0
        else:
            self.load()
    def load(self):
        f = open(self.path)
        self.count = int(f.read())
        f.close

    def inc(self):
        self.count += 1
    
    def val(self):
        return self.count

    def write(self):
        f = open(self.path, 'w')
        f.write(str(self.count))
        f.close()


###############
# Explosion
###############
class Explosion(Sprite):
    dradius = 60
    duration = 1500
    pad = 5

    def __init__(self, obj):
        Sprite.__init__(self)

        self.pos = obj.rect.center
        
        avg = (obj.rect.width + obj.rect.height) / 2.0
        avg /= 2
        radius = avg * math.sqrt(2) 

        self.radius = int(radius)

        self.life = self.duration

    def color(self):
        return randrange(220, 256), randrange(220, 256), randrange(220, 256)

    def update(self, dt):
        if self.life > 0:
            self.life -= dt
        elif self.radius > 0:
            self.radius -= self.dradius * (dt / 1000.0)
        else:
            self.kill()


class ExplosionGroup(Group):
    def draw(self, surf):
        for obj in self:
            if obj.radius > 0:
                pygame.draw.circle(surf, obj.color(), obj.pos, obj.radius)


    def explode_ships(self, group):
        for xplo in self:
            for ship in group:
                if collide_rect_circle(ship.rect, xplo.pos, xplo.radius-xplo.pad):
                    self.add(ship.kill())
                    break

############
# Ship
############
class Ship(Sprite):
    width = 20
    height = 20

    explosion_type = Explosion

    def __init__(self, x, y, vx, vy, bounds, color):
        Sprite.__init__(self)

        self.vx = vx
        self.vy = vy
        self.color = color
        self.bounds = bounds

        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()

    def draw_image(self):
        self.image.fill(self.color)

    def update(self, dt):
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.x += -2 * dx

        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy = -self.vy
            self.rect.y += -2 * dy

    def kill(self):
        Sprite.kill(self)
        Ship.death_count.inc()
        return self.explosion_type(self)


class ShipSpawner(object):
    ship_type = Ship

    def __init__(self, duration, group, bounds, spawn_area=None):
        if spawn_area is None:
            spawn_area = bounds

        self.group = group
        self.bounds = bounds
        self.area = spawn_area
        self.duration = duration
        self.time = 0

    def get_vel(self):
        vx = randint_neg(1,2)
        vy = randint_neg(1,2)
        return vx,vy

    def get_color(self):
        return 255,255,0

    def spawn(self):
        vx, vy = self.get_vel()
        x = randrange(self.area.width)
        y = randrange(self.area.height)
        color = self.get_color()

        # create ship
        ship = self.ship_type(x, y, vx, vy, self.bounds, color)
        ship.rect.clamp_ip(self.area)
       
        self.group.add(ship)


    def update(self, dt):
        self.time += dt
        if self.time > self.duration:
            self.time = 0
            self.spawn()



class ShipGroup(Group):
    def __init__(self, count):
        Group.__init__(self)
        self.max = count

    def add(self, *sprites):
        for sprite in sprites:
            if len(self) < self.max:
                Group.add(self, sprite)
            

###############
# Tie Fighter
###############
class TieExplosion(Explosion):
    def color(self):
        r = randrange(256)
        return 255, r, 0


class TieFighter(Ship):
    width = 40
    height = 40

    explosion_type = TieExplosion

    def draw_image(self):
        draw_tie(self.image, self.color)

    def update(self, dt):
        vx = self.vx
        vy = self.vy

        Ship.update(self, dt)

        # if we changed direction, split
        if vx != self.vx or vy != self.vy:
            if vx != self.vx:
                vx = self.vx
                vy = -vy
            else:
                vx = -vx
                vy = self.vy

            tie = TieFighter(self.rect.x, self.rect.y, vx, vy, self.bounds, self.color)

            for group in self.groups():
                group.add(tie)


class TieSpawner(ShipSpawner):
    ship_type = TieFighter

    def get_vel(self):
        vx = randint_neg(100,250)
        vy = randint_neg(100,250)
        return vx,vy

    def get_color(self):
        r = randrange(100,256)
        return r,0,0


###############
# Y-Wing
###############
class YWingExplosion(Explosion):
    dradius = 110
    def color(self):
        r = randrange(256)
        return r, 255, 255

class YWing(Ship):
    width = 128
    height = 64

    explosion_type = YWingExplosion

    def draw_image(self):
        draw_ywing(self.image, self.color)
        self.orig_image = self.image
        self.flipped_image = pygame.transform.flip(self.image, True, False)

    def update(self, dt):
        if rand_odds(1,60):
            self.vx = -self.vx
        Ship.update(self, dt)

        if self.vx > 0:
            self.image = self.orig_image
        else:
            self.image = self.flipped_image

class YWingSpawner(ShipSpawner):
    ship_type = YWing

    def get_vel(self):
        vx = randint_neg(300,500)
        return vx,0

    def get_color(self):
        r = randrange(128,256)
        return r,r,r

###############
# Bomb
###############
class Bomb(Sprite):
    width = 10
    height = 10
    color = 0,200,255
    fuse = 3000

    def __init__(self, pos):
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = Rect(0,0,self.width, self.height)
        self.rect.center = pos

        self.time = fuse

    def update(self, dt):
        self.time -= dt
        step = self.time / 500

        if step % 2 == 0:
            color = 255,255,0
        else:
            color = 255,0,0

        self.image.fill(color, self.rect.inflate(-self.width/2, self.height/2))


###############
# Weapons
###############
class Weapon(object):
    def __init__(self, game):
        self.game = game

    def primarydown(self, pos):
        pass

    def primaryup(self, pos):
        pass

    def secondarydown(self, pos):
        pass

    def secondaryup(self, pos):
        pass

    def name(self):
        return self.__class__.__name__.replace("Weapon", "")

class MiniExplosion(Explosion):
    duration = 500
    dradius = 150
    def __init__(self, pos, radius):
        Sprite.__init__(self)
        self.pos = pos
        self.radius = radius
        self.life = self.duration

    def color(self):
        r = randrange(128,256)
        return r,255,r

class MiniExplosionsWeapon(Weapon):
    def primarydown(self,pos):
        self.game.xplos.add( MiniExplosion(pos, 20) )
    def secondarydown(self,pos):
        self.game.xplos.add( MiniExplosion(pos, 50) )


class MineLayerWeapon(Weapon):
    def primarydown(self,pos):
        pass

    def secondarydown(self,pos):
        pass

class LaserWeapon(Weapon):
    pass

class WarWeapon(Weapon):
    pass

class PlagueWeapon(Weapon):
    pass

class NukeWeapon(Weapon):
    pass

class Detonator(object):
    duration = 50

    def __init__(self, bounds, group):
        self.time = 0
        self.bounds = bounds
        self.xplos = group

    def update(self, dt):
        self.time += dt
        if self.time > self.duration:
            x = randrange(self.bounds.width)
            y = randrange(self.bounds.height)
            self.time = 0

            # check for power
            f = open("/proc/acpi/ac_adapter/AC/state")
            d = f.read().split()[1]
            f.close()
            if d.startswith("on"):
                self.xplos.add( MiniExplosion((x,y), 20) )

###############
# Game
###############
class Game(Application):
    title = "Splodey Fun Times"
    max_ships = 400

    

    def __init__(self):
        pygame.init()
        #self.screen_size = pygame.display.list_modes()[0]

        Application.__init__(self)
        #pygame.display.toggle_fullscreen()    


        self.ships = ShipGroup(self.max_ships)
        self.xplos = ExplosionGroup()

        self.screen_bounds = bounds = self.screen.get_rect()

        dc_height = 40
        self.dc_font = pygame.font.Font(None, 30)
        self.dc_bounds = Rect(0, bounds.height - dc_height, bounds.width, dc_height)

        self.game_bounds = Rect(0, 0, bounds.width, bounds.height - dc_height)

        spawn_area = self.game_bounds.inflate(-self.game_bounds.width/4, -self.game_bounds.height/4)
        self.spawners = [
            TieSpawner(1000, self.ships, self.game_bounds, spawn_area),
            YWingSpawner(2000, self.ships, self.game_bounds)
        ]
        self.detonator = Detonator(self.game_bounds, self.xplos)

        for spawner in self.spawners:
            spawner.spawn()


        Ship.death_count = DeathCount()
        self.current_weapon = MiniExplosionsWeapon(self)

    def on_quit(self):
        Ship.death_count.write()

    def handle_event(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.current_weapon.primarydown(pos)
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            self.current_weapon.secondarydown(pos)
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            self.current_weapon.primaryup(pos)
        elif event.type == MOUSEBUTTONUP and event.button == 3:
            self.current_weapon.secondaryup(pos)


    def update(self):
        dt = min(200, self.clock.get_time()) # cap dt

        # update all the spawners
        for spawner in self.spawners:
            spawner.update(dt)

        # update ships
        self.ships.update(dt)
        self.xplos.update(dt)

        self.xplos.explode_ships(self.ships)

        self.detonator.update(dt)

        if len(self.xplos) == 0:
            Ship.death_count.write()

    def draw(self, screen):
        screen.fill((0,0,0))
        self.ships.draw(screen)
        self.xplos.draw(screen)

        # hud
        screen.fill((40,40,40), self.dc_bounds)

        # death count
        msg = format_int(Ship.death_count.val()) + " dead"
        text = self.dc_font.render(msg, True, (255,255,255), (40,40,40))
        loc = text.get_rect()
        loc.centery = self.dc_bounds.centery
        loc.right = self.dc_bounds.right - 10
        screen.blit(text, loc)


if __name__ == "__main__":
    Game().run()
    print "ByeBye"
