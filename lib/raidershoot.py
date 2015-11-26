import pygame
from pygame.locals import *

import player
import sprite

def init(g,r,p):
    s = sprite.Sprite3(g,r,'shoots/right-raider-shoot',(0,0,2,20))

    s.rect.centerx = r.centerx
    s.rect.centery = r.centery

    s.groups.add('solid')
    s.groups.add('raidershoot')
    #s.groups.add('enemy')
    s.hit_groups.add('player')

    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.life = 180
    s.strength = 1
    #if big: s.strength = 3
    
    s.vx = 0
    s.vy = 2
    s.rect.centerx += s.vx*(s.rect.width/2)
    s.rect.centery += 25
    
    return s
    
def loop(g,s):
    s.rect.y += s.vy
    s.life -= 1
    if s.life == 0:
        s.active = False
        #die(g,s)

def hit(g,a,b): 
    player.damage(g,b)
    a.active = False
    #die(g,a)
    #a.act
    

    #b.strength -= a.strength
    #if b.strength <= 0:
        #b.active = False
