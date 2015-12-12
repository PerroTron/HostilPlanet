import pygame
import sprite


def init(g, r, n):
    s = sprite.Sprite3(g, r, "drone/shield", (0, 0, 7, 8))

    s.player = n
    s.rect.bottom = r.bottom
    s.rect.centerx = r.centerx

    #s.groups.add('solid')
    g.sprites.append(s)

    s.loop = loop

    s.vx = 0
    s.vy = 0

    s._prev = pygame.Rect(-1, -1, 0, 0)

    s.standing = None

    return s


def loop(g, s):

    s.rect.x = s.player.rect.x - 10
    s.rect.y = s.player.rect.y - 2