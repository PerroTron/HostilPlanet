import pygame
from pid import PID
import sprite
import droneshoot


def init(g, r, n, drone):
    s = sprite.Sprite3(g, r, "drone/%s-0" % drone, (0, 0, 7, 8))

    s.drone = drone

    s.player = n
    s.rect.bottom = r.bottom - 32
    s.rect.centerx = r.centerx

    s.groups.add('solid')
    g.sprites.append(s)

    s.loop = loop

    s.facing = "right"

    s.shoot = 100
    s.shooting = 0

    s.x_pid = PID(3.0, 0.4, 1.2)
    s.y_pid = PID(3.0, 0.4, 1.2)

    s.vx = 0
    s.vy = 0

    s.max_speed_x = 1.0
    s.max_speed_y = 1.0

    s._prev = pygame.Rect(-1, -1, 0, 0)

    s.standing = None

    return s


def loop(g, s):
    # s.drone = s.player.drone

    if s.drone == "guardian":

        sprites = g.sprites[:]

        for enemy in sprites:
            if "enemy" in enemy.groups:
                if s.shoot == 0:
                    shot = droneshoot.init(g, s.rect, s, enemy)
                    s.shoot = 100
                    s.shooting = 5

                if s.shooting > 0:
                    s.shooting -= 1

                s.shoot -= 1

    elif s.drone == "killer":

        sprites = g.sprites[:]

        for enemy in sprites:
            if "enemy" in enemy.groups:
                if s.shoot == 0:
                    shot = droneshoot.init(g, s.rect, s, enemy)
                    s.shoot = 100
                    s.shooting = 5

                if s.shooting > 0:
                    s.shooting -= 1

                s.shoot -= 1

    if g.frame & 30 == 0:
        s.image = "drone/%s-1" % s.drone
    else:
        s.image = "drone/%s-0" % s.drone

    sprite.apply_standing(g, s)
    s._prev = pygame.Rect(s.rect)

    s.x_pid.setPoint(g.player.rect.centerx)
    s.y_pid.setPoint(g.player.rect.centery)

    pid_x = s.x_pid.update(s.rect.centerx + 16)
    pid_y = s.y_pid.update(s.rect.centery + 16)

    s.vx = pid_x
    s.vy = pid_y

    s.vx = min(s.max_speed_x, s.vx)
    s.vx = max(-s.max_speed_x, s.vx)

    s.vy = min(s.max_speed_y, s.vy)
    s.vy = max(-s.max_speed_y, s.vy)

    s.rect.x += sprite.myinc(g.frame, s.vx)
    s.rect.y += sprite.myinc(g.frame, s.vy)

    if s.vx > 0:
        s.facing = "right"
    else:
        s.facing = "left"
