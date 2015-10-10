import pygame
from pygame.locals import *

import player
import sprite

def init(g,r,p):
    s = sprite.Sprite3(g,r,'shoots/%s-parasitshoot'%(p.facing),(0,0,13,7))

    s.rect.centerx = r.centerx
    s.rect.centery = r.centery

    s.groups.add('solid')
    s.groups.add('parasitshoot')
    #s.groups.add('enemy')
    s.hit_groups.add('player')

    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.life = 90
    s.strength = 1
    #if big: s.strength = 3
    
    s.vx = 1
    if p.facing == 'left':
        s.vx = -1
    s.vy = 0
    s.rect.centerx += s.vx*(5+s.rect.width/2)
    s.rect.centery -= 3
    
    return s
    
def loop(g,s):
    s.rect.x += s.vx*2
    s.life -= 1
    if s.life == 0:
        s.active = False
        #die(g,s)

def hit(g,a,b): 
    player.damage(g,b)
    #die(g,a)
    #a.act
    

    #b.strength -= a.strength
    #if b.strength <= 0:
        #b.active = False