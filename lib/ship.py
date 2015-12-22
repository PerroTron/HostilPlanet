import pygame
from cnst import *
import sprite


def init(g, r, n, *params):

    s = sprite.Sprite3(g, r, 'ship/ship-0', (0, 0, 80, 120))
    s.rect.centerx = r.centerx
    s.rect.centery = r.centery - (32 - 16) / 2
    s.loop = loop

    g.sprites.insert(0, s)

    return s


def loop(g, s):
    if g.frame % 30 == 0:
        s.image = "ship/ship-1"
    else:
        s.image = "ship/ship-0"
