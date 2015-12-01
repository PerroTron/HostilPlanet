import player
import sprite


def init(g, r, p):
    s = sprite.Sprite3(g, r, 'shoots/tentactulshoot', (0, 0, 8, 4))

    s.rect.centerx = r.centerx
    s.rect.centery = r.centery

    s.groups.add('solid')
    s.groups.add('enemyshoot')
    s.hit_groups.add('player')

    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.life = 90
    s.strength = 1
    s.damage = 1

    s.vx = 1
    if p.facing == 'left':
        s.vx = -2
    s.vy = 0
    s.rect.centerx += s.vx * (1 + s.rect.width / 2)
    s.rect.centery -= -7

    return s


def loop(g, s):
    s.rect.x += s.vx * 2
    s.life -= 1
    if s.life == 0:
        s.active = False


def hit(g, a, b):
    player.damage(g, b, a)
    a.active = False
