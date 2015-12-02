import player
import sprite


def init(g, r, p):
    s = sprite.Sprite3(g, r, 'shoots/%s-wibertshoot' % p.facing, (0, 0, 5, 5))

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
        s.vx = -1
    s.vy = -1.6
    s.rect.centerx += s.vx * (9 + s.rect.width / 2)
    s.rect.centery -= 11

    return s


def loop(g, s):
    s.rect.x += s.vx * 3
    s.rect.y += s.vy
    s.life -= 1
    if s.life == 0:
        s.active = False


def hit(g, a, b):
    player.damage(g, b, a)
    a.active = False
