from cnst import *


def init_bkgr(g, r, n):
    x, y = r.centerx / TW, r.centery / TH
    n = g.data[2][y][x + 1]
    g.set_bkgr('%x.png' % n)


def init_music(g, r, n):
    x, y = r.centerx / TW, r.centery / TH
    n = g.data[2][y][x + 1]
    # print 'play music',n
    g.game.music_play('%s' % n)
    # g.game.music_play('%d.ogg'%n)


def init_bkgr_scroll(g, r, n, x, y):
    g.bkgr_scroll.x = x
    g.bkgr_scroll.y = y
