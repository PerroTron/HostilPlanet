import pygame

import dracoshoot
import player
import sprite


def init(g, r, n, facing='left', *params):
    s = sprite.Sprite3(g, r, 'draco/draco-%s' % (facing), (0, 0, 10, 16))
    s.rect.bottom = r.bottom
    s.rect.centerx = r.centerx
    s.groups.add('solid')
    s.groups.add('enemy')
    s.hit_groups.add('player')
    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.facing = facing

    s.shoot = 250
    s.shooting = 0

    if s.facing == 'left':
        s.vx = 0
    else:
        s.vx = 0
    s.vy = 0

    s._prev = pygame.Rect(-1, -1, 0, 0)
    s.strength = 6
    s.damage = 1

    s.standing = None
    return s


def loop(g, s):
    # sprite.apply_gravity(g,s)
    sprite.apply_standing(g, s)

    # if s.rect.x == s._prev.x: # or sprite.get_code(g,s,sign(s.vx),0) == CODE_DRACO_TURN:
    #	s.vx = -s.vx

    s._prev = pygame.Rect(s.rect)

    if g.player.rect.centerx > s.rect.centerx:
        s.vx += 0
    elif g.player.rect.centerx < s.rect.centerx:
        s.vx -= 0

    if s.vx > 0.0:
        s.facing = 'right'
    elif s.vx < 0.0:
        s.facing = 'left'
    if s.shooting == 0:
        s.image = 'draco/draco-%s' % (s.facing)

    # if sprite.get_code(g,s,sign(s.vx),0) == CODE_DRACO_TURN:
    #	s.vx = 0.0

    s.vx = min(1.0, s.vx)
    s.vx = max(-1.0, s.vx)

    if s.shoot == 0:
        # g.sprites.append(shot)
        s.shoot = 200
        s.shooting = 18

    if s.shooting > 0:
        if s.shooting == 18:
            s.image = 'draco/draco-%s-shoot-0' % (s.facing)  # , (g.frame / 50) % 2)
            shot = dracoshoot.init(g, s.rect, s)
        if s.shooting == 9:
            s.image = 'draco/draco-%s-shoot-1' % (s.facing)  # , (g.frame / 50) % 2)

        s.shooting -= 1

    s.shoot -= 1

    s.rect.x += sprite.myinc(g.frame, s.vx)
    s.rect.y += sprite.myinc(g.frame, s.vy)


def hit(g, a, b):
    player.damage(g, b, a)

# print 'youve been spikeys!'
