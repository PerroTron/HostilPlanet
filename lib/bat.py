import pygame
from pygame.locals import *

from cnst import *

import sprite
import tiles
import player

def init(g,r,n,facing = 'left',*params):
	s = sprite.Sprite3(g,r,'bat/fly-%s-0' % facing,(0,0,16,16))
	s.rect.bottom = r.bottom
	s.rect.centerx = r.centerx
	s.groups.add('solid')
	s.groups.add('enemy')
	s.hit_groups.add('player')
	s.hit = hit
	g.sprites.append(s)
	s.loop = loop
	s.next_frame = 12 
	s.frame = 0
	s.facing = facing
	
	s.vx = 1.8
	
	if s.facing == 'left':
		s.vx = -s.vx
	else:
		s.vx = s.vx
	
	s.vy = 0
	s.attacking = False
	s.flying = True
	# make sure this is always different at startup
	s._prev = None
	
	s.strength = 6
	s.damage = 1
	s.vy_attack = 0
	
	s.standing = None
	return s

def loop(g,s):
	sprite.apply_gravity(g,s)
	sprite.apply_standing(g,s)
	
	#if s.standing != None and s.vx != 0:
		#next_tile = g.layer[s.standing.pos[1]][s.standing.pos[0] + s.direction]
		#next2_tile = g.layer[s.standing.pos[1]][s.standing.pos[0] + s.direction*2]
		#if (next_tile.standable == 0) or (next2_tile.standable == 0):
			#s.rect.x = s._prev.x    
			#s.direction = - s.direction
			#s.next_frame = 1
	
	if s.flying:
		if s._prev != None:
			if s.rect.x == s._prev.x or sprite.get_code(g,s,sign(s.vx),0) == CODE_BAT_TURN:
				s.vx = -s.vx
				s.next_frame=1
				if s.vx < 0:
					s.facing = 'left'
				else:
					s.facing = 'right'
				
		if s.standing != None and sprite.get_code(g,s,sign(s.vx),1) == CODE_BAT_ATTACK:
			s.vy_attack = -4
			"""
			if sprite.get_code(g,s,sign(s.vx)*2,1) == CODE_BAT_ATTACK:
				s.vy_attack = -3.0
				if sprite.get_code(g,s,sign(s.vx)*3,1) == CODE_BAT_ATTACK:
					s.vy_attack = -4.1
			"""
			s.attacking = True
			s.flying = False
			s.next_frame = 20
			s.image = 'bat/preattack-%s' % s.facing
			
		s._prev = pygame.Rect(s.rect)
		
		s.rect.x += s.vx
		s.rect.y += s.vy
	else:
		s._prev = pygame.Rect(s.rect)
		if (s.next_frame <= 0): 
			if (s.standing != None):
				s.flying=True
				s.attacking=False
				s.next_frame=1
			#s.vx*1
			vx = s.vx
			s.rect.x += sprite.myinc(g.frame,vx)
			s.rect.y += sprite.myinc(g.frame,s.vy)
			
	s.next_frame -= 1
	if s.next_frame == 0:
		if s.attacking:
			sprite.stop_standing(g,s)
			s.vy = s.vy_attack
			s.image = 'bat/attack-%s' % s.facing
		else: 
			s.next_frame = 6
			s.frame += 1
			if s.frame > 2:
				s.frame = 0
			s.image = 'bat/fly-%s-%s' % (s.facing, s.frame)

def hit(g,a,b):
	player.damage(g,b,a)
