# File created by Tim Doan

import pygame as pg

from pygame.sprite import Sprite

from settings import *

from random import randint

vec = pg.math.Vector2

# create a player 

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        if self.rect.x > 0:
            print("off the right")
        if self.rect.x < 0:
            print("off the left")
        if self.rect.y > 0:
            print("off the top")
        if self.rect.y < 0:
            print("off the bottom")

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def behavior(self):
        self.acc.x = -MOB_ACC
        self.acc.x = MOB_ACC
        self.acc.y = MOB_ACC
        self.acc.y = -MOB_ACC
        if self.rect.x > WIDTH:
            print("mob off the right")
            self.acc.x = MOB_ACC
        if self.rect.x < WIDTH:
            print("mob off the left")
            self.acc.x = -MOB_ACC
        if self.rect.y > HEIGHT:
            print("mob off the top")
            self.acc.y = -MOB_ACC
        if self.rect.y < HEIGHT:
            print("mob off the bottom")
            self.acc.y = MOB_ACC
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.behavior()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        