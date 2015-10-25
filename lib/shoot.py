import pygame
from pygame.locals import *
from time import sleep
import sprite
import capsule

def init(g,r,p,weapon):
    
    
    if p.canshoot == False:
        return
    
    """   
    if not hasattr(g,'shoot_count'):
        g.shoot_count = 0
    if g.shoot_count >= 10:
        return None
    g.shoot_count += 1
    #print 'new shoot', g.shoot_count
    """
    
    if weapon == 'cannon':

        s = sprite.Sprite3(g,r,'shoots/%s-cannon-shoot'%(p.facing),(0,0,16,16))
            
        s.weapon = weapon
        s.cooldown = 50
        s.rect.centerx = r.centerx
        s.rect.centery = r.centery
        s.groups.add('solid')
        s.groups.add('shoot')
        s.hit_groups.add('enemy')
        s.hit = hit
        g.sprites.append(s)
        s.loop = loop
        s.life = 100
        s.deinit = deinit
        s.velocityx = 3
        s.velocityy = 0

        s.strength = 1
        
        s.vx = 1
        if p.facing == 'left':
            s.vx = -1
        s.vy = 0
        s.rect.centerx += s.vx*(6+s.rect.width/2)
        s.rect.centery -= 6
        
        g.game.sfx['rocket1'].play()
        
    elif weapon == 'shootgun':

        s = sprite.Sprite3(g,r,'shoots/%s-shootgun-shoot'%(p.facing),(0,0,16,16))

        s.weapon = weapon
        s.cooldown = 25
        s.rect.centerx = r.centerx
        s.rect.centery = r.centery
        s.groups.add('solid')
        s.groups.add('shoot')
        s.hit_groups.add('enemy')
        s.hit = hit
        g.sprites.append(s)
        s.loop = loop
        s.life = 10
        s.deinit = deinit
        s.velocityx = 3
        s.velocityy = 0


        s.strength = 2
        
        s.vx = 1
        if p.facing == 'left':
            s.vx = -1
        s.vy = 0
        s.rect.centerx += s.vx*(10+s.rect.width/2)
        s.rect.centery -= 6
        
        g.game.sfx['shootgun1'].play()
        g.game.canshoot = False
        
    else:

        s = sprite.Sprite3(g,r,'shoots/%s-shoot'%(p.facing),(0,0,7,7))
        
        s.weapon = weapon
        s.cooldown = 10
        s.rect.centerx = r.centerx
        s.rect.centery = r.centery
        s.groups.add('solid')
        s.groups.add('shoot')
        s.hit_groups.add('enemy')
        s.hit = hit
        g.sprites.append(s)
        s.loop = loop
        s.life = 50
        s.deinit = deinit
        s.velocityx = 6
        s.velocityy = 0

        
        s.strength = 1
        
        s.vx = 1
        if p.facing == 'left':
            s.vx = -1
        s.vy = 0
        s.rect.centerx += s.vx*(6+s.rect.width/2)
        s.rect.centery -= 6
        
        g.game.sfx['shoot'].play()
    

    
    
    g.game.canshoot = False
        
    
    return s

def deinit(g,s):
    #print "shoot deinit"
    #g.shoot_count -= 1
    pass
    
    
def loop(g,s):
    s.rect.x += s.vx*s.velocityx
    s.rect.y += s.vy*s.velocityy
    
    
    s.life -= 1
    if s.life == 0:
        s.active = False
    

def hit(g,a,b): 
    a.active = False
    
    b.strength -= a.strength
    if b.strength <= 0:
        b.active = False
        code = None
        if hasattr(b,'_code'):
            code = b._code
            delattr(b,'_code')
        #s = capsule.init(g,b.rect)
        #if code != None:
        #    s._code = code
    else:
        g.game.sfx['hit'].play()
        
    #print 'shoot hit!'
