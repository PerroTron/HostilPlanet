import sprite
import explosion

from pid import PID


def init(g, r, p, weapon, enemy, projectile=False):
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

        s = sprite.Sprite3(g, r, 'shoots/%s-cannon-shoot' % p.facing, (0, 0, 15, 3))

        s.player = p
        s.facing = s.player.facing
        s.weapon = weapon
        s.enemy = enemy
        s.cooldown = 50
        s.rect.centerx = r.centerx
        s.rect.centery = r.centery
        s.groups.add('solid')
        s.groups.add('cannon')
        s.hit_groups.add('enemy')
        s.hit = hit
        g.sprites.append(s)
        s.loop = loop
        s.life = 500
        s.deinit = deinit
        s.auto_velocityx = 1.0
        s.auto_velocityy = 1.0
        s.velocityx = 1.0
        s.velocityy = 0.0

        g.game.weaponsound = 'sboom'

        s.strength = 4

        s.x_pid = PID(3.0, 0.4, 1.2)
        s.y_pid = PID(3.0, 0.4, 1.2)

        s.vx = 0
        s.vy = 0
        s.rect.centerx += s.vx * (10 + s.rect.width / 2)
        s.rect.centery -= 2

        g.game.sfx['cannon'].play()

    elif weapon == 'shootgun':

        s = sprite.Sprite3(g, r, 'shoots/%s-shootgun-shoot' % p.facing, (0, 0, 26, 16))

        s.player = p
        s.facing = s.player.facing
        s.weapon = weapon
        s.enemy = enemy
        s.cooldown = 30
        s.rect.centerx = r.centerx
        s.rect.centery = r.centery
        s.groups.add('solid')
        s.groups.add('shoot')
        s.hit_groups.add('enemy')
        s.hit = hit
        g.sprites.append(s)
        s.loop = loop
        s.life = 12
        s.deinit = deinit
        s.velocityx = 3
        s.velocityy = 0

        g.game.weaponsound = 'hit'

        s.strength = 3

        s.vx = 1
        if p.facing == 'left':
            s.vx = -1
        s.vy = 0
        s.rect.centerx += s.vx * (8 + s.rect.width / 2)
        s.rect.centery -= 2

        g.game.sfx['shootgun1'].play()

    elif weapon == 'laser':

        s = sprite.Sprite3(g, r, 'shoots/%s-laser-shoot' % p.facing, (0, 0, 16, 3))

        s.player = p
        s.facing = s.player.facing
        s.weapon = weapon
        s.enemy = enemy
        s.cooldown = 20
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
        s.velocityx = 9
        s.velocityy = 0

        g.game.weaponsound = 'hit'

        s.strength = 2

        s.vx = 1
        if p.facing == 'left':
            s.vx = -1
        s.vy = 0
        s.rect.centerx += s.vx * (4 + s.rect.width / 2)
        s.rect.centery -= 1

        g.game.sfx['laser'].play()

    elif weapon == 'tshoot':

        s = sprite.Sprite3(g, r, 'shoots/%s-tshoot-shoot' % p.facing, (0, 0, 5, 5))

        s.player = p
        s.facing = s.player.facing
        s.weapon = weapon
        s.enemy = enemy
        s.cooldown = 1
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
        s.velocityx = 2
        s.velocityy = 1

        g.game.weaponsound = 'hit'

        s.strength = 2

        if p.facing == 'left':
            s.vx = -1
        else:
            s.vx = 1

        s.vy = 0

        if projectile == "uptop":
            s.vy = -2
        elif projectile == "top":
            s.vy = -1
        elif projectile == "mid":
            s.vy = 0
        elif projectile == "bot":
            s.vy = +1

        s.rect.centerx += s.vx * (4 + s.rect.width / 2)
        s.rect.centery -= 1

        g.game.sfx['laser'].play()

    else:

        s = sprite.Sprite3(g, r, 'shoots/%s-shoot' % p.facing, (0, 0, 6, 3))

        s.player = p
        s.facing = s.player.facing
        s.weapon = weapon
        s.enemy = enemy
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
        s.velocityx = 5
        s.velocityy = 0

        g.game.weaponsound = 'hit'

        s.strength = 1

        s.vx = 1
        if p.facing == 'left':
            s.vx = -1
        s.vy = 0
        s.rect.centerx += s.vx * (6 + s.rect.width / 2)
        s.rect.centery -= 2

        g.game.sfx['shoot'].play()

    g.game.canshoot = False

    return s


def deinit(g, s):
    pass


def loop(g, s):

    if s.weapon == "cannon" and s.enemy:

        s.x_pid.setPoint(s.enemy.rect.centerx)
        s.y_pid.setPoint(s.enemy.rect.centery)

        pid_x = s.x_pid.update(s.rect.centerx)
        pid_y = s.y_pid.update(s.rect.centery)

        s.vx = pid_x
        s.vy = pid_y

        s.vx = min(s.auto_velocityx, s.vx)
        s.vx = max(-s.auto_velocityx, s.vx)

        s.vy = min(s.auto_velocityy, s.vy)
        s.vy = max(-s.auto_velocityy, s.vy)

        s.rect.x += s.vx * s.auto_velocityx
        s.rect.y += s.vy * s.auto_velocityy

        if s.vx > 0:
            s.image = "shoots/right-cannon-shoot"
        elif s.vx < 0:
            s.image = "shoots/left-cannon-shoot"

    elif s.weapon == "cannon" and not s.enemy:

        if s.facing == "right":
            s.vx = s.velocityx
            s.vy = s.velocityy
        elif s.facing == "left":
            s.vx = -s.velocityx
            s.vy = -s.velocityy

        s.rect.x += s.vx * s.velocityx
        s.rect.y += s.vy * s.velocityy

    else:
        s.rect.x += s.vx * s.velocityx
        s.rect.y += s.vy * s.velocityy

    if s.vx == 0 and s.vy == 0:
        s.active = False

    s.life -= 1
    if s.life == 0:
        s.active = False


def hit(g, a, b):
    sound(g)

    a.active = False

    if a.weapon == "cannon":
        explosion.init(g, a.rect, a)

    b.strength -= a.strength
    if b.strength <= 0:
        # b.active = False
        code = None
        if hasattr(b, '_code'):
            code = b._code
            delattr(b, '_code')

        explode(g, b)


def sound(g):
    g.game.sfx[g.game.weaponsound].play()


def explode(level, sprite):
    s = sprite
    s.hit_groups = set()

    def loop(g, s):
        s.exploded += 2
        if s.exploded > 8:
            s.active = False

    s.loop = loop
