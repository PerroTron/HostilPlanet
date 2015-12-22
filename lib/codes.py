import pygame

import init
import sprites
from cnst import *


def _pass(*params): pass


INIT_CODES = {
    0x00: [_pass, ],
    0x10: [sprites.player.init, ],
    0xA0: [sprites.boss.init, ],
}

CODES = {
    # numerical codes for magic uses?
    0x00: [_pass, ],
    0x01: [_pass, ],
    0x02: [_pass, ],
    0x03: [_pass, ],
    0x04: [_pass, ],
    0x05: [_pass, ],
    0x06: [_pass, ],
    0x07: [_pass, ],
    0x08: [_pass, ],
    0x09: [_pass, ],
    0x0A: [_pass, ],
    0x0B: [_pass, ],
    0x0C: [_pass, ],
    0x0D: [_pass, ],
    0x0E: [_pass, ],
    0x0F: [_pass, ],

    # player related (16 codes)
    # 0x10 ...
    # 0x13 ...

    # spiner related (8 codes)
    0x20: [sprites.spiner.init, 1],
    0x21: [sprites.spiner.init, -1],
    0x22: [_pass, ],  # CODE_SPINER_TURN

    # spikey related (8 codes)
    0x28: [sprites.spikey.init, ],

    # platform related (8 codes)
    0x30: [sprites.platform.init, 1, 0],
    0x31: [sprites.platform.init, 0, -1],
    0x32: [sprites.platform.init, -1, 0],
    0x33: [sprites.platform.init, 0, 1],
    0x34: [_pass, ],  # CODE_PLATFORM_TURN

    # sentinel related (8 codes)

    0x38: [sprites.sentinel.init, ],
    0x39: [_pass, ],  # CODE_SENTINEL_TURN

    # frog related (8 codes)
    0x40: [sprites.frog.init, 1],
    0x41: [sprites.frog.init, -1],
    0x42: [_pass, ],  # CODE_FROG_TURN
    0x43: [_pass, ],  # CODE_FROG_JUMP

    # parasit related (8 codes)
    0x48: [sprites.parasit.init, ],
    0x49: [_pass, ],  # CODE_PARASIT_TURN

    # fally related (8 codes)
    0x50: [sprites.tiles_basic.fally_init, ],

    # tentactul related (8 codes)
    0x58: [sprites.tentactul.init, ],
    0x59: [_pass, ],  # CODE_TENTACTUL_TURN

    # door related
    0x60: [sprites.door.init, ],  # CODE_DOOR (press shoot/up to be transported)
    0x61: [_pass, ],  # CODE_DOOR_AUTO (you are instantly transported)
    0x62: [sprites.door.init, True],  # CODE_DOOR_HIDDEN (hidden regular door)

    # brobo related
    0x68: [sprites.brobo.init, 'left'],
    0x69: [sprites.brobo.init, 'right'],
    0x6A: [_pass, ],  # CODE_BROBO_TURN

    # level related
    0x70: [_pass, ],  # CODE_BOUNDS
    0x78: [init.init_bkgr, ],  # bkgr initializer
    0x79: [init.init_bkgr_scroll, 0, 6],  # bkgr scrolly magic stuff
    0x80: [init.init_music, ],  # music ..
    0x88: [_pass, ],  # CODE_EXIT

    # blob related (8 codes)
    0x90: [sprites.blob.init, ],

    # guardian (8 codes)
    0x98: [sprites.guardian.init, ],
    0x99: [_pass, ],  # CODE_GUARDIAN_TURN

    # boss related
    0xA1: [_pass, ],
    0xA2: [_pass, ],

    # zombie related

    0xA8: [sprites.zombie.init, 'left'],
    0xA9: [sprites.zombie.init, 'right'],
    0xAA: [_pass, ],  # CODE_ZOMBIE_TURN
    0xAB: [_pass, ],  # CODE_ZOMBIE_JUMP

    # draco related
    0xB8: [sprites.draco.init, 'left'],
    0xB9: [sprites.draco.init, 'right'],

    # bat related

    0xC8: [sprites.bat.init, 'left'],
    0xC9: [sprites.bat.init, 'right'],
    0xCA: [_pass, ],  # CODE_BAT_TURN
    0xCB: [_pass, ],  # CODE_BAT_ATTACK

    # tower related
    0xD8: [sprites.tower.init, 'left'],
    0xD9: [sprites.tower.init, 'right'],

    # wibert (8 codes)
    0xE8: [sprites.wibert.init, ],
    0xE9: [_pass, ],  # CODE_WIBERT_TURN

    # rock related (8 codes)
    0x91: [sprites.rock.init, 'left'],
    0x92: [sprites.rock.init, 'right'],
    0x93: [_pass, ],  # CODE_ROCK_TURN

    # raider ralated
    0xF8: [sprites.raider.init, ],
    0xF9: [_pass, ],  # CODE_RAIDER_TURN

    # ship related
    0xB0: [sprites.ship.init, ],

}


def c_init(g, pos, n):
    x, y = pos
    if n not in INIT_CODES and n not in CODES:
        print 'undefined code:', x, y, '0x%2x' % n
        return
    if n not in INIT_CODES: return
    v = INIT_CODES[n]
    return v[0](g, pygame.Rect(x * TW, y * TH, TW, TH), n, *v[1:])


def c_run(g, pos, n):
    x, y = pos
    if n not in INIT_CODES and n not in CODES:
        print 'undefined code:', x, y, '0x%2x' % n
        return
    if n not in CODES: return
    v = CODES[n]
    return v[0](g, pygame.Rect(x * TW, y * TH, TW, TH), n, *v[1:])
