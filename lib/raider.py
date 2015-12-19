import pygame
import sprite
import player
import raidershoot
import random
from cnst import *


def init(g, r, n, facing='left', *params):
    s = sprite.Sprite3(g, r, 'raider/raider-%s-0' % (facing), (0, 0, 16, 14))
    s.rect.bottom = r.bottom
    s.rect.centerx = r.centerx
    s.groups.add('solid')
    s.groups.add('enemy')
    s.hit_groups.add('player')
    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.facing = facing

    s.shoot = 100
    s.shoot_reload = 200
    s.shooting = 0

    s.frame = 0
    s.moving = 0
    s.speed = 2
    s.vx = s.speed
    s.idling = random.randint(20, 40)

    s.frame = 0

    if s.facing == 'left':
        s.vx = -1.0
    else:
        s.vx = 1.0
    s.vy = 0

    s._prev = pygame.Rect(-1, -1, 0, 0)
    s.strength = 5
    s.damage = 1

    s.standing = None
    return s


def loop(g, s):
    # sprite.apply_gravity(g,s)
    sprite.apply_standing(g, s)

    # if s.rect.x == s._prev.x: # or sprite.get_code(g,s,sign(s.vx),0) == CODE_RAIDER_TURN:
    #   s.vx = -s.vx

    s._prev = pygame.Rect(s.rect)

    if g.player.rect.centerx > s.rect.centerx:
        s.vx += 0.02
    elif g.player.rect.centerx < s.rect.centerx:
        s.vx -= 0.02

    if s.vx > 0.0:
        s.facing = 'right'
    elif s.vx < 0.0:
        s.facing = 'left'
    s.image = 'raider/raider-%s-%s' % (s.facing, (g.frame / 10) % 4)

    if sprite.get_code(g, s, sign(s.vx), 0) == CODE_RAIDER_TURN:
        s.vx = 0.0

    s.vx = min(1.0, s.vx)
    s.vx = max(-1.0, s.vx)

    if s.idling > 0:
        if s.idling % 40 > 20:
            s.facing = 'left'
        else:
            s.facing = 'right'
        s.idling -= 1
        if s.idling == 0:
            s.moving = 90
            # if g.game.random % 2 == 0:
            if random.randint(0, 1):
                s.vx = -s.speed
                s.facing = 'left'
            else:
                s.vx = s.speed
                s.facing = 'right'
    elif s.moving > 0:
        s.moving -= 1
        if s.moving == 0:
            s.idling = 80
            s.vx = 0
    else:
        s.idling = 80

    if s.vx < 0:
        s.facing = 'left'
    else:
        s.facing = 'right'

    s.image = 'raider/raider-%s-%s' % (s.facing, (s.frame / 5) % 2)
    s.frame += 1

    if s.shoot == 0:
        shot = raidershoot.init(g, s.rect, s)
        # g.sprites.append(shot)
        s.shoot = s.shoot_reload
        s.shooting = 5

    if s.shooting > 0:
        s.image = 'raider/raider-%s-shoot' % (s.facing)
        s.shooting -= 1

    s.shoot -= 1

    s.rect.x += sprite.myinc(g.frame, s.vx)
    s.rect.y += sprite.myinc(g.frame, s.vy)


def hit(g, a, b):
    player.damage(g, b, a)
