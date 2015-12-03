import pygame

import sprite
import droneshoot

def init(g, r, n):
    s = sprite.Sprite3(g, r, "drone/drone-0", (0, 0, 7, 7))

    s.rect.bottom = r.bottom - 32
    s.rect.centerx = r.centerx

    s.groups.add('solid')
    g.sprites.append(s)

    s.loop = loop

    s.facing = "right"

    s.shoot = 100
    s.shooting = 0

    s.vx = 0
    s.vy = 0

    s._prev = pygame.Rect(-1, -1, 0, 0)

    s.standing = None

    return s


def loop(g, s):

    if g.frame & 30 == 0:
        s.image = "drone/drone-1"
    else:
        s.image = "drone/drone-0"

    sprite.apply_standing(g, s)

    s._prev = pygame.Rect(s.rect)

    if g.player.rect.centerx > s.rect.centerx:
        s.vx += 0.5
    elif g.player.rect.centerx < s.rect.centerx:
        s.vx -= 0.5

    if g.player.rect.centery > s.rect.centery + 16:
        s.vy += 0.5
    elif g.player.rect.centery < s.rect.centery + 16:
        s.vy -= 0.5

    s.vx = min(1.0, s.vx)
    s.vx = max(-1.0, s.vx)

    s.vy = min(1.0, s.vy)
    s.vy = max(-1.0, s.vy)

    s.rect.x += sprite.myinc(g.frame, s.vx)
    s.rect.y += sprite.myinc(g.frame, s.vy)

    if s.vx > 0:
        s.facing = "right"
    else:
        s.facing = "left"

    sprites = g.sprites[:]

    for enemy in sprites:
        if "enemy" in enemy.groups:

            if s.shoot == 0:
                shot = droneshoot.init(g, s.rect, s)
                s.shoot = 100
                s.shooting = 5

            if s.shooting > 0:
                s.shooting -= 1

            s.shoot -= 1