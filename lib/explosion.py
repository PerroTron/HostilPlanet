import pygame
from pygame.locals import *

import player
import sprite

def init(g,r,p):
    s = sprite.Sprite3(g,r,'shoots/explosion-0',(0,0,32,32))

    s.rect.centerx = r.centerx
    s.rect.centery = r.centery

    s.groups.add('solid')
    s.groups.add('explosion')
    s.hit_groups.add('player')

    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.life = 180
    s.counter = 0
    s.frame = 0
    s.strength = 1
    s.damage = 1
    
    s.rect.centerx += (s.rect.width/2)-16
    s.rect.centery -= (s.rect.height/2)-16
    
    return s
    
def loop(g,s):
    
    if (s.frame % 2) == 0:
        if s.counter < 3:
            s.image = 'shoots/explosion-%d' % s.counter
            
        else:
            s.active = False
        s.counter += 1
    s.frame += 1
    
def hit(g,a,b):
    player.damage(g,b,a)
    a.active = False
    
    b.strength -= a.strength
    if b.strength <= 0:
        #b.active = False
        code = None
        if hasattr(b,'_code'):
            code = b._code
            delattr(b,'_code')
        
        
        explode(g,b)

def explode(level,sprite):
    s = sprite
    s.hit_groups = set()
    def loop(g,s):
        s.exploded += 2
        if s.exploded > 8:
            s.active = False
    
    s.loop = loop
