import sprite
from pid import PID


def init(g, r, p, enemy):
    s = sprite.Sprite3(g, r, 'shoots/right-drone-shoot', (0, 0, 4, 2))

    s.rect.centerx = r.centerx
    s.rect.centery = r.centery

    s.groups.add('solid')
    s.groups.add('shoot')
    s.hit_groups.add('enemy')

    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.life = 180
    s.strength = 1
    s.damage = 1

    s.x_pid = PID(3.0, 0.4, 1.2)
    s.y_pid = PID(3.0, 0.4, 1.2)

    s.enemy = enemy

    g.game.weaponsound = 'hit'

    s.vx = 0
    s.vy = 0

    s.max_speed_x = 2.0
    s.max_speed_y = 2.0


    s.rect.centerx += s.vx * (s.rect.width / 2) -2
    s.rect.centery -= 0

    return s


def loop(g, s):

    s.x_pid.setPoint(s.enemy.rect.centerx)
    s.y_pid.setPoint(s.enemy.rect.centery)

    pid_x = s.x_pid.update(s.rect.centerx)
    pid_y = s.y_pid.update(s.rect.centery)

    s.vx = pid_x
    s.vy = pid_y

    s.vx = min(s.max_speed_x, s.vx)
    s.vx = max(-s.max_speed_x, s.vx)

    s.vy = min(s.max_speed_y, s.vy)
    s.vy = max(-s.max_speed_y, s.vy)

    s.rect.x += s.vx
    s.rect.y += s.vy

    s.life -= 1
    if s.life == 0:
        s.active = False


def hit(g, a, b):
    a.active = False

    b.strength -= a.strength
    if b.strength <= 0:
        # b.active = False
        code = None
        if hasattr(b, '_code'):
            code = b._code
            delattr(b, '_code')

        explode(g, b)


def explode(level, sprite):
    s = sprite
    s.hit_groups = set()

    def loop(g, s):
        s.exploded += 2
        if s.exploded > 8:
            s.active = False

    s.loop = loop
