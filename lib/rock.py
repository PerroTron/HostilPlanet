import pygame
from pygame.locals import *

from cnst import *

import sprite
import player

def init(g,r,n,facing,*params):
    s = sprite.Sprite3(g,r,'rock/left-0',(0,0,48,12)) 
    #s.rect.bottom = r.bottom
    s.rect.centery = r.centery
    s.rect.centerx = r.centerx
    s.groups.add('solid')
    s.groups.add('enemy')
    s.hit_groups.add('player')
    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    
    s.vx = 1
    s.vy = 0
    
    s.facing = facing
    
    s._prev = None # pygame.Rect(s.rect)
    s.strength = 4

    s.image = 'rock/%s-0' % s.facing

    #s.standing = None
    return s
    
def loop(g,s):
    #sprite.apply_gravity(g,s)
    if s.facing == 'left':
        if s.vx > 0:
            speed = 3
        else:
            speed = 1
    else:
        if s.vx > 0:
            speed = 1
        else:
            speed = 3
    
    if g.frame % speed == 0:
        if s._prev != None:
            if s.rect.x == s._prev.x or sprite.get_code(g,s,sign(s.vx),0) == CODE_ROCK_TURN:
                s.vx = -s.vx
        s._prev = pygame.Rect(s.rect)

    
        s.rect.x += s.vx*1
        s.rect.y += s.vy
        
    
    #sprite.check_standing(g,s)
    

def hit(g,a,b):
    player.damage(g,b)
    #print 'youve been spikeys!'
