import os
import pygame

from pgu import engine
import data
from cnst import *
import levels


class Menu(engine.State):
    def __init__(self, game):
        self.game = game

    def init(self):
        self.font = self.game.font
        self.bkgr = pygame.image.load(data.filepath(os.path.join('bkgr', '2.png')))

        self.cur = 0
        self.game.lcur = 0
        self.levels = levels.LEVELS

        self.items = [
            ('play the game!', 'start'),
            ('select <L>', 'play'),
            ('help', 'help'),
            ('credits', 'credits'),
            ('quit', 'quit'),
        ]
        self.rects = []

        self.frame = 0

        self.logo = pygame.image.load(data.filepath(os.path.join('title.png')))

    def debug_mode(self):
        self.levels = []
        for fname in os.listdir(data.filepath('levels')):
            if fname[0] == '.': continue
            self.levels.append((fname, fname.replace('.tga', ''), 1))
        self.levels.sort()
        levels.LEVELS = self.levels

    # print levels.LEVELS


    def paint(self, screen):
        x = self.frame % (self.bkgr.get_width())
        screen.blit(self.bkgr, (-x, 0))
        screen.blit(self.bkgr, (-x + self.bkgr.get_width(), 0))

        # x,y = 0,4
        x, y = 0, 0

        # fnt = self.game.fonts['title']
        # c =(0,0,0)
        # text = TITLE
        # img = fnt.render(text,1,c)
        # screen.blit(img,((SW-img.get_width())/2,y))

        screen.blit(self.logo, ((SW - self.logo.get_width()) / 2, y))
        # y += 48
        y = 140

        fnt = self.font

        """
		text = 'high: %05d'%self.game.high
		c = (0x00,0x00,0x00)
		img = fnt.render(text,0,c)
		x = (SW-img.get_width())/2
		screen.blit(img,(x+1,y+1))
		c = (0xff,0xff,0xff)
		img = fnt.render(text,0,c)
		screen.blit(img,(x,y))
		"""

        # y += 36
        y += 24

        x = 90
        for n in xrange(0, len(self.items)):
            text, value = self.items[n]
            text = text.replace('L', self.levels[self.game.lcur][1])
            c = (0x00, 0x00, 0x00)
            img = fnt.render(text, 0, c)
            x = (SW - img.get_width()) / 2
            screen.blit(img, (x + 1, y + 1))
            c = (0xff, 0xff, 0xff)
            if n == self.cur: c = (0xaa, 0xaa, 0xaa)
            img = fnt.render(text, 0, c)
            screen.blit(img, (x, y))
            # y += 24
            y += 12

        text = 'JAURIA STUDIOS'
        c = (0x00, 0x00, 0x00)
        img = fnt.render(text, 0, c)
        x = (SW - img.get_width()) / 2
        y = SH - (img.get_height() + 4)
        screen.blit(img, (x + 1, y + 1))
        c = (0xff, 0xff, 0xff)
        img = fnt.render(text, 0, c)
        screen.blit(img, (x, y))

        self.game.flip()

    def update(self, screen):
        return self.paint(screen)

    def loop(self):
        self.game.music_play('intro')
        self.frame += 1

    def event(self, e):
        if e.type is USEREVENT and e.action == 'down':
            self.cur = (self.cur + 1) % len(self.items)
            self.repaint()
        elif e.type is USEREVENT and e.action == 'up':
            self.cur = (self.cur - 1 + len(self.items)) % len(self.items)
            self.repaint()
        elif e.type is USEREVENT and e.action == 'left':
            self.game.lcur = (self.game.lcur - 1 + len(self.levels)) % len(self.levels)
            self.cur = 1
            self.repaint()
        elif e.type is USEREVENT and e.action == 'right':
            self.game.lcur = (self.game.lcur + 1) % len(self.levels)
            self.cur = 1
            self.repaint()
        elif e.type is USEREVENT and e.action == 'exit':
            return engine.Quit(self.game)
        elif e.type is USEREVENT and (e.action == 'menu' or e.action == 'jump'):
            text, value = self.items[self.cur]
            if value == 'start':
                self.game.init_play()
                self.game.lcur = 0
                import level
                l = level.Level(self.game, None, self)
                return Transition(self.game, l)
            elif value == 'play':
                self.game.init_play()
                import level
                l = level.Level(self.game, None, self)
                return Transition(self.game, l)
            elif value == 'quit':
                return engine.Quit(self.game)
            elif value == 'credits':
                return Transition(self.game, Credits(self.game, self))
            elif value == 'help':
                return Transition(self.game, Help(self.game, self))
        elif e.type is KEYDOWN and e.key == K_d:
            self.debug_mode()


class Transition(engine.State):
    def __init__(self, game, next):
        self.game, self.next = game, next

    def init(self):
        self.s1 = self.game.screen.convert()
        self.init2()
        self.frame = 0
        self.total = FPS
        self.inc = 0

    def init2(self):
        if hasattr(self.next, 'init') and not hasattr(self.next, '_init'):
            self.next._init = 0
            self.next.init()
        self.s2 = self.game.screen.convert()
        self.next.paint(self.s2)

    def loop(self):
        # self.frame += 1
        self.inc += 1
        # if (self.inc%2) == 0: self.frame += 1
        self.frame += 1
        if self.frame == self.total:
            self.game.screen.blit(self.s2, (0, 0))
            self.game.flip()
            return self.next

    def update(self, screen):
        return self.paint(screen)

    def paint(self, screen):
        f = self.frame
        t = self.total
        t2 = t / 2

        if f < t2:
            i = self.s1
            w = max(2, SW * (t2 - f) / t2)
            i = pygame.transform.scale(i, (w, SH * w / SW))
        else:
            f = t2 - (f - t2)
            i = self.s2
            w = max(2, SW * (t2 - f) / t2)
            i = pygame.transform.scale(i, (w, SH * w / SW))

        i = pygame.transform.scale(i, (SW, SH))

        screen.blit(i, (0, 0))
        self.game.flip()


class Intro(engine.State):
    def __init__(self, game, next):
        self.game = game
        self.next = next

    def init(self):
        self.frame = FPS

        self.moon = pygame.image.load(data.filepath(os.path.join('intro', 'intro.png'))).convert()
        img = pygame.image.load(data.filepath(os.path.join('images', 'logo.png')))
        w = 120
        self.logo = pygame.transform.scale(img, (w, img.get_height() * w / img.get_width()))
        self.black = self.moon.convert()
        self.black.fill((0, 0, 0))

    def update(self, screen):
        return self.paint(screen)

    def loop(self):
        self.frame += 1
        if self.frame == FPS * 7:
            return Transition(self.game, Intro2(self.game, self.next))

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('jump', 'bubble', 'menu', 'exit')):
            return Transition(self.game, self.next)

    def paint(self, screen):
        screen.fill((0, 0, 0))
        f = self.frame

        inc = FPS
        if 0 < f < inc:
            pass
        f -= inc

        inc = FPS * 7
        if 0 < f < inc:

            a = 255
            if f > FPS * 2:
                screen.blit(self.moon, (0, 0))
                a = 255 - ((f - FPS * 2) * 255 / (FPS * 2))
                self.black.set_alpha(a)
                screen.blit(self.black, (0, 0))

            fnt = self.game.fonts['intro']
            x, y = 8, 16
            for text in ['Jauria Studios', 'presents']:
                c = (255, 255, 255)
                img = fnt.render(text, 1, (0, 0, 0))
                screen.blit(img, (x + 2, y + 2))
                img = fnt.render(text, 1, c)
                screen.blit(img, (x, y))
                y += 36
            if f < FPS:
                a = 255 - (f * 255 / FPS)
                self.black.set_alpha(a)
                screen.blit(self.black, (0, 0))

            screen.blit(self.logo, (180, 0))

        self.game.flip()


class Intro2(engine.State):
    def __init__(self, game, next):
        self.game = game
        self.next = next

    def init(self):
        self.moon = pygame.image.load(data.filepath(os.path.join('intro', 'intro.png'))).convert()
        img = pygame.image.load(data.filepath(os.path.join('images', 'jump', 'player', 'right.png')))
        w = 160
        self.player = pygame.transform.scale(img, (w, img.get_height() * w / img.get_width()))

        self.bkgr = pygame.image.load(data.filepath(os.path.join('bkgr', '2.png')))

        self.frame = 0

    def loop(self):
        self.frame += 1
        if self.frame == FPS * 2:
            return Transition(self.game, self.next)

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('jump', 'bubble', 'menu', 'exit')):
            return Transition(self.game, self.next)

    def paint(self, screen):
        # screen.fill((0,0,0))
        screen.blit(self.bkgr, (0, 0))
        fnt = self.game.fonts['intro']
        x, y = 8, 16
        for text in ['Hostil Planet']:
            c = (255, 255, 255)
            img = fnt.render(text, 1, (0, 0, 0))
            screen.blit(img, (x + 2, y + 2))
            img = fnt.render(text, 1, c)
            screen.blit(img, (x, y))
            y += 36

        screen.blit(self.player, (130, 0))

        self.game.flip()


class Ending(engine.State):
    def __init__(self, game, next):
        self.game = game
        self.next = next

    def init(self):

        self.frame = 0
        self.counter = 0

        self.screen = self.game.screen

        self.background = pygame.image.load(data.filepath(os.path.join('ending', 'bg.png'))).convert()

        w = 32

        # Weapons

        gun = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'gun.png')))
        self.gun = pygame.transform.scale(gun, (w, gun.get_height() * w / gun.get_width()))

        shootgun = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'shootgun.png')))
        self.shootgun = pygame.transform.scale(shootgun, (w, shootgun.get_height() * w / shootgun.get_width()))

        cannon = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'cannon.png')))
        self.cannon = pygame.transform.scale(cannon, (w, cannon.get_height() * w / cannon.get_width()))

        laser = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'laser.png')))
        self.laser = pygame.transform.scale(laser, (w, laser.get_height() * w / laser.get_width()))

        # Items

        life = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'life.png')))
        self.life = pygame.transform.scale(life, (w, life.get_height() * w / life.get_width()))

        shield = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'shield.png')))
        self.shield = pygame.transform.scale(shield, (w, shield.get_height() * w / shield.get_width()))

        # Chips

        green = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'green_chip.png')))
        self.green = pygame.transform.scale(green, (w, green.get_height() * w / green.get_width()))

        red = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'red_chip.png')))
        self.red = pygame.transform.scale(red, (w, red.get_height() * w / red.get_width()))

        yellow = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'yellow_chip.png')))
        self.yellow = pygame.transform.scale(yellow, (w, yellow.get_height() * w / yellow.get_width()))

        blue = pygame.image.load(data.filepath(os.path.join('images', 'utils', 'blue_chip.png')))
        self.blue = pygame.transform.scale(blue, (w, blue.get_height() * w / blue.get_width()))

        # Enemies

        parasit = pygame.image.load(data.filepath(os.path.join('images', 'parasit', 'parasit-left-0.png')))
        self.parasit = pygame.transform.scale(parasit, (w, parasit.get_height() * w / parasit.get_width()))

    def loop(self):
        self.frame += 1

        if (self.frame % 2) == 0:
            self.counter += 1

            self.paint(self.screen)

        # if self.frame == FPS*2:
        #	return Transition(self.game,self.next)

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('jump', 'bubble', 'menu', 'exit')):
            return Transition(self.game, self.next)

    def paint(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.background, (0, 0 - self.frame))

        fnt = self.game.fonts['intro']

        x, y = 160, 72 - self.counter

        for text in ['Weapons', 'Gun', 'Shootgun', 'Cannon', 'Laser', '',
                     'Items', 'Life', 'Shield', '',
                     'Chips', 'Green', 'Red', 'Yellow', 'Blue', '',
                     'Enemies', 'parasit',
                     ]:
            c = (255, 255, 255)
            img = fnt.render(text, 1, (0, 0, 0))
            screen.blit(img, (x + 2, y + 2))
            img = fnt.render(text, 1, c)
            screen.blit(img, (x, y))
            y += 60

        screen.blit(self.gun, (48, 120 - self.counter))
        screen.blit(self.shootgun, (48, 180 - self.counter))
        screen.blit(self.cannon, (48, 240 - self.counter))
        screen.blit(self.laser, (48, 300 - self.counter))

        screen.blit(self.life, (48, 480 - self.counter))
        screen.blit(self.shield, (48, 540 - self.counter))

        screen.blit(self.green, (48, 720 - self.counter))
        screen.blit(self.red, (48, 780 - self.counter))
        screen.blit(self.yellow, (48, 840 - self.counter))
        screen.blit(self.blue, (48, 900 - self.counter))

        self.game.flip()


class Prompt(engine.State):
    def __init__(self, game, text, yes, no):
        self.game = game
        self.text = text
        self.yes = yes
        self.no = no

    def init(self):
        self.font = self.game.fonts['pause']
        self.bkgr = self.game.screen.convert()

    def event(self, e):
        if (e.type is KEYDOWN and e.key == K_y) or (e.type is USEREVENT and e.action in ('menu')):
            return self.yes
        if (e.type is KEYDOWN and e.key == K_n) or (e.type is USEREVENT and e.action in ('exit')):
            return self.no

    def paint(self, screen):
        screen.blit(self.bkgr, (0, 0))
        text = self.text
        fnt = self.font
        c = (255, 255, 255)
        img = fnt.render(text, 0, (0, 0, 0))
        x, y = (SW - img.get_width()) / 2, (SH - img.get_height()) / 2
        screen.blit(img, (x + 2, y + 2))
        img = fnt.render(text, 0, c)
        screen.blit(img, (x, y))
        self.game.flip()


class Pause(engine.State):
    def __init__(self, game, text, next):
        self.game = game
        self.text = text
        self.next = next

    def init(self):
        self.font = self.game.fonts['pause']
        self.bkgr = self.game.screen.convert()

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('jump', 'bubble', 'menu', 'exit')):
            return self.next

    def paint(self, screen):
        screen.blit(self.bkgr, (0, 0))
        text = self.text
        fnt = self.font
        c = (255, 255, 255)
        img = fnt.render(text, 0, (0, 0, 0))
        x, y = (SW - img.get_width()) / 2, (SH - img.get_height()) / 2
        screen.blit(img, (x + 2, y + 2))
        img = fnt.render(text, 0, c)
        screen.blit(img, (x, y))
        self.game.flip()


class Credits(engine.State):
    def __init__(self, game, next):
        self.game = game
        self.next = next

    def init(self):
        self.frame = 0

        self.bkgr = pygame.image.load(data.filepath(os.path.join('bkgr', "5.png"))).convert()

    def update(self, screen):
        return self.paint(screen)
        pass

    def loop(self):
        self.frame += 1

    # if self.frame == FPS*7:
    # return Transition(self.game,Intro2(self.game,self.next))

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('jump', 'bubble', 'menu', 'exit')):
            return Transition(self.game, self.next)

    def paint(self, screen):
        x = self.frame % (self.bkgr.get_width())
        screen.blit(self.bkgr, (-x, 0))
        screen.blit(self.bkgr, (-x + self.bkgr.get_width(), 0))

        fnt = self.game.fonts['help']
        x, y = 8, 10
        for text in [
            'Team',
            '',
            'Jauria Studios',
            '',
            '',
            '',
            '',
            'This game is based',
            'in Imitationpickles',
            'Barbie Seahorse Adventures',
        ]:
            c = (255, 255, 255)
            img = fnt.render(text, 0, (0, 0, 0))
            x = (SW - img.get_width()) / 2
            screen.blit(img, (x + 2, y + 2))
            img = fnt.render(text, 0, c)
            screen.blit(img, (x, y))
            y += 20
        self.game.flip()


class Help(engine.State):
    def __init__(self, game, next):
        self.game = game
        self.next = next

    def init(self):
        self.frame = 0

        self.bkgr = pygame.image.load(data.filepath(os.path.join('bkgr', "5.png"))).convert()

    def update(self, screen):
        return self.paint(screen)
        pass

    def loop(self):
        self.frame += 1

    # if self.frame == FPS*7:
    # return Transition(self.game,Intro2(self.game,self.next))

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('jump', 'bubble', 'menu', 'exit')):
            return Transition(self.game, self.next)

    def paint(self, screen):
        x = self.frame % (self.bkgr.get_width())
        screen.blit(self.bkgr, (-x, 0))
        screen.blit(self.bkgr, (-x + self.bkgr.get_width(), 0))

        fnt = self.game.fonts['help']
        x, y = 8, 10
        for text in [
            'Help',
            '',
            'Use your arrow keys to',
            'move the Robot.',
            'Button 1 - Jump',
            'Button 2 - Shoot',
        ]:
            c = (255, 255, 255)
            img = fnt.render(text, 0, (0, 0, 0))
            x = (SW - img.get_width()) / 2
            screen.blit(img, (x + 2, y + 2))
            img = fnt.render(text, 0, c)
            screen.blit(img, (x, y))
            y += 20
        self.game.flip()


class Weapon(engine.State):
    def __init__(self, game, next, level):
        self.game = game
        self.level = level
        self.next = next

    def init(self):
        self.font = self.game.fonts['pause']
        self.bkgr = self.game.screen.convert()
        self.weapon_cursor = pygame.image.load(data.filepath('weapon_cursor.png'))
        self.drone_cursor = pygame.image.load(data.filepath('drone_cursor.png'))
        self.jetpack_cursor = pygame.image.load(data.filepath('jetpack_cursor.png'))
        self.window = pygame.image.load(data.filepath('menu.png'))

        self.current_menu = "weapon"

        self.weapon = 0

        if self.game.powerup == "gun":
            self.weapon = 0
        elif self.game.powerup == "shootgun":
            self.weapon = 1
        elif self.game.powerup == "cannon":
            self.weapon = 2
        elif self.game.powerup == "granadelauncher":
            self.weapon = 3
        elif self.game.powerup == "laser":
            self.weapon = 4
        
        self.drone = 0

        if self.game.drone == "guardian":
            self.drone = 0
        elif self.game.drone == "defender":
            self.drone = 1
        elif self.game.drone == "killer":
            self.drone = 2

        self.jetpack = 0

    def update(self, screen):
        return self.paint(screen)
        pass

    def event(self, e):
        if e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('menu')):

            self.game.powerup = self.game.weapons[self.weapon]
            if self.game.drone is not None:
                self.game.drone = self.game.drones[self.drone]
            self.game.jetpack = self.game.jetpacks[self.jetpack]
            return self.level

        elif e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('exit')):
            return self.level

        elif e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('down')):
            if self.current_menu == "weapon":
                if self.game.drone is not None:
                    self.current_menu = "drone"
                else:
                    self.current_menu = "jetpack"

            elif self.current_menu == "drone":
                self.current_menu = "jetpack"

            elif self.current_menu == "jetpack":
                self.current_menu = "weapon"

        elif e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('up')):

            if self.current_menu == "weapon":
                self.current_menu = "jetpack"

            elif self.current_menu == "drone":
                self.current_menu = "weapon"

            elif self.current_menu == "jetpack":
                if self.game.drone is not None:
                    self.current_menu = "drone"
                else:
                    self.current_menu = "weapon"

        elif e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('left')):
            if self.current_menu == "weapon":
                if self.weapon == 0:
                    self.weapon = len(self.game.weapons) -1
                    for weapon in reversed(self.game.weapons):
                        if self.game.weapons[self.weapon] == '':
                            self.weapon -= 1

                elif self.weapon > 0:
                    self.weapon -= 1
                    for weapon in self.game.weapons:
                        if self.game.weapons[self.weapon] == '':
                            self.weapon -= 1

            elif self.current_menu == "drone":
                if self.drone == 0:
                    self.drone = len(self.game.drones)
                    for drone in reversed(self.game.drones):
                        if self.game.drones[self.drone -1] == '':
                            self.drone -= 1

                if self.drone > 0:
                    self.drone -= 1
                    for drone in self.game.drones:
                        if self.game.drones[self.drone] == '':
                            self.drone -= 1

            elif self.current_menu == "jetpack":
                if self.jetpack == 0:
                    self.jetpack = len(self.game.jetpacks)

                if self.jetpack > 0:
                    self.jetpack -= 1

        elif e.type is KEYDOWN or (e.type is USEREVENT and e.action in ('right')):
            if self.current_menu == "weapon":
                if self.weapon == len(self.game.weapons) - 1:
                    self.weapon = 0
                    for weapon in self.game.weapons:
                        if self.game.weapons[self.weapon - 1] == '':
                            self.weapon += 1

                elif self.weapon < len(self.game.weapons) - 1:
                    self.weapon += 1
                    for weapon in reversed(self.game.weapons):
                        if self.weapon > len(self.game.weapons) - 1:
                            self.weapon = 0
                        if self.game.weapons[self.weapon] == '':
                            self.weapon += 1

            elif self.current_menu == "drone":
                if self.drone == len(self.game.drones) - 1:
                    self.drone = 0
                    for drone in self.game.drones:
                        if self.game.drones[self.drone - 1] == '':
                            self.drone += 1

                elif self.drone < len(self.game.drones) - 1:
                    self.drone += 1
                    for drone in reversed(self.game.drones):
                        if self.drone > len(self.game.drones) - 1:
                            self.drone = 0
                        if self.game.drones[self.drone] == '':
                            self.drone += 1

            elif self.current_menu == "jetpack":
                if self.jetpack == len(self.game.jetpacks) - 1:
                    self.jetpack = 0

                elif self.jetpack < len(self.game.jetpacks) - 1:
                    self.jetpack += 1

    def paint(self, screen):

        screen.blit(self.bkgr, (0, 0))
        screen.blit(self.window, ((SW - self.window.get_width()) / 2, (SH - self.window.get_height()) / 2))

        fnt = self.game.fonts['help']

        if self.current_menu == "weapon":
            cursor_x, cursor_y = ((SW - self.weapon_cursor.get_width()) / 2) - 46 + self.weapon * 23, ((SH - self.weapon_cursor.get_height()) / 2) + 56
            screen.blit(self.weapon_cursor, (cursor_x, cursor_y))

        elif self.current_menu == "drone":
            cursor_x, cursor_y = ((SW - self.drone_cursor.get_width()) / 2) + 6 + self.drone * 13, ((SH - self.drone_cursor.get_height()) / 2) - 58
            screen.blit(self.drone_cursor, (cursor_x, cursor_y))

        elif self.current_menu == "jetpack":
            cursor_x, cursor_y = ((SW - self.jetpack_cursor.get_width()) / 2) - 52 + self.jetpack * 11, ((SH - self.jetpack_cursor.get_height()) / 2) - 24
            screen.blit(self.jetpack_cursor, (cursor_x, cursor_y))

        # Weapons

        pics_x, pics_y = (SW / 2) - 55, (SH / 2) + 47

        if self.game.weapons[0] == "gun":
            img = self.level.images[0x07]
            screen.blit(img, (pics_x + 23 * 0, pics_y))

        if self.game.weapons[1] == "shootgun":
            img = self.level.images[0x28]
            screen.blit(img, (pics_x + 23 * 1, pics_y))

        if self.game.weapons[2] == "cannon":
            img = self.level.images[0x08]
            screen.blit(img, (pics_x + 23 * 2, pics_y))

        if self.game.weapons[3] == "granadelauncher":
            img = self.level.images[0x38]
            screen.blit(img, (pics_x + 23 * 3, pics_y))

        if self.game.weapons[4] == "laser":
            img = self.level.images[0x18]
            screen.blit(img, (pics_x + 23 * 4, pics_y))


        player_img = None

        if self.weapon == 0:
            player_img = pygame.image.load(data.filepath(os.path.join('images', 'jump', 'player', 'right.png')))
        elif self.weapon == 1:
            player_img = pygame.image.load(data.filepath(os.path.join('images', 'jump',  'shootgun', 'right.png')))
        elif self.weapon == 2:
            player_img = pygame.image.load(data.filepath(os.path.join('images', 'jump',  'cannon', 'right.png')))
        elif self.weapon == 3:
            player_img = pygame.image.load(data.filepath(os.path.join('images', 'jump',  'granadelauncher', 'right.png')))
        elif self.weapon == 4:
            player_img = pygame.image.load(data.filepath(os.path.join('images', 'jump',  'laser', 'right.png')))

        w = 40

        player_img = pygame.transform.scale(player_img, (w, player_img.get_height() * w / player_img.get_width()))
        player_x, player_y = ((SW - player_img.get_width()) / 2) + 5 , ((SH - player_img.get_height()) / 2) - 10

        screen.blit(player_img, (player_x, player_y))


        # Drones

        if self.game.drone:
            pics_x, pics_y = (SW / 2) - 2, (SH / 2) - 67

            img = None

            if self.game.drones[0] == 'guardian':
                img = self.level.images[0x17]
                screen.blit(img, (pics_x + 13 *0, pics_y))
            if self.game.drones[1] == 'defender':
                img = self.level.images[0x27]
                screen.blit(img, (pics_x + 13 *1, pics_y))
            if self.game.drones[2] == 'killer':
                img = self.level.images[0x37]
                screen.blit(img, (pics_x + 13 *2, pics_y))

            current_drone = None

            if self.drone == 0:
                current_drone = self.level.images[0x17]
            elif self.drone == 1:
                current_drone = self.level.images[0x27]
            elif self.drone == 2:
                current_drone = self.level.images[0x37]

            w = 28

            drone_img = pygame.transform.scale(current_drone, (w, current_drone.get_height() * w / current_drone.get_width()))
            drone_x, drone_y = ((SW - drone_img.get_width()) / 2 + 19) , ((SH - drone_img.get_height()) / 2) - 33
            screen.blit(drone_img, (drone_x, drone_y))

        # Jetpacks

        pics_x, pics_y = (SW / 2) - 58, (SH / 2) - 30

        for text in self.game.jetpacks:

            img = None

            if text == 'jump':
                img = self.level.images[0x16]
            elif text == 'double_jump':
                img = self.level.images[0x26]
            elif text == 'fly':
                img = self.level.images[0x36]

            screen.blit(img, (pics_x, pics_y))
            pics_x += 10

        x,y = 5,10
        w = 40

        if self.jetpack == 1:
            jetpack_img = pygame.image.load(data.filepath(os.path.join('images', 'jetpack', 'double_jump.png')))
            jetpack_img = pygame.transform.scale(jetpack_img, (w, jetpack_img.get_height() * w / jetpack_img.get_width()))
            jetpack_x, jetpack_y = ((SW - jetpack_img.get_width()) / 2 + x) , ((SH - jetpack_img.get_height()) / 2) - y
            screen.blit(jetpack_img, (jetpack_x, jetpack_y))
        elif self.jetpack == 2:
            jetpack_img = pygame.image.load(data.filepath(os.path.join('images', 'jetpack', 'fly.png')))
            jetpack_img = pygame.transform.scale(jetpack_img, (w, jetpack_img.get_height() * w / jetpack_img.get_width()))
            jetpack_x, jetpack_y = ((SW - jetpack_img.get_width()) / 2 + x) , ((SH - jetpack_img.get_height()) / 2) - y
            screen.blit(jetpack_img, (jetpack_x, jetpack_y))

        self.game.flip()