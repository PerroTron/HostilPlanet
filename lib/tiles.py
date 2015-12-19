import pygame

import tiles_basic
from tile import *

# NOTE: If you add new tiles, use t_init for regular tiles.
#       tl_init and tr_init are for tiles that take up only half of the
#       16x16 tile, on the left or right side respectively.

TILES = {

    # general purpose tiles

    0x00: [t_init, [], None, ],
    0x01: [t_init, ['solid'], tiles_basic.hit_block, 1, 1, 1, 1, ],
    0x02: [t_init, ['solid'], tiles_basic.hit_breakable, 1, 1, 1, 1, ],
    0x03: [t_init, ['player'], tiles_basic.hit_fire, ],
    0x04: [t_init, [], None, ],  # black background tile
    0x05: [t_init, [], None, ],  # exit sign
    0x10: [t_init, ['solid'], tiles_basic.hit_block, 1, 1, 1, 1, ],
    0x11: [t_init, ['solid'], tiles_basic.hit_block, 1, 0, 0, 0, ],
    0x12: [t_init, ['solid'], tiles_basic.hit_fally, 1, 1, 1, 1, ],
    0x15: [t_init, ['solid'], tiles_basic.hit_block, 1, 1, 1, 1, ],
    0x21: [t_init, ['solid'], tiles_basic.hit_block, 1, 0, 0, 0, ],

    # powerups and bonus items ...

    0x17: [t_init, ['player'], tiles_basic.hit_drone, 'guardian'],  # drone guardian
    0x27: [t_init, ['player'], tiles_basic.hit_drone, 'defender'],  # drone defender
    0x37: [t_init, ['player'], tiles_basic.hit_drone, 'killer'],  # drone killer

    0x26: [t_init, ['player'], tiles_basic.hit_jetpack, 'double_jump'],  # double_jump
    0x36: [t_init, ['player'], tiles_basic.hit_jetpack, 'fly'],  # fly

    0x08: [t_init, ['player'], tiles_basic.hit_power, 'cannon'],  # cannon
    0x18: [t_init, ['player'], tiles_basic.hit_power, 'laser'],  # laser
    0x28: [t_init, ['player'], tiles_basic.hit_power, 'shootgun'],  # shootgun
    0x38: [t_init, ['player'], tiles_basic.hit_power, 'granadelauncher'],  # shootgun

    0x0C: [t_init, ['player'], tiles_basic.hit_life, ],  # extra-life
    0x1C: [t_init, ['player'], tiles_basic.hit_def, ],  # extra-def

    0x2C: [t_init, ['player'], tiles_basic.hit_chip, 1, ],  # chip
    0x2D: [t_init, ['player'], tiles_basic.hit_chip, 2, ],  # chip
    0x2E: [t_init, ['player'], tiles_basic.hit_chip, 3, ],  # chip
    0x2F: [t_init, ['player'], tiles_basic.hit_chip, 4, ],  # chip



    # tile animations

    0x4D: [t_init, [], None, ],  # torch
    0x4E: [t_init, [], None, ],  # torch
    0x4F: [t_init, [], None, ],  # torch

    0x9D: [t_init, [], None, ],  # red light
    0x9E: [t_init, [], None, ],  # red light

    0xAD: [t_init, [], None, ],  # cable
    0xAE: [t_init, [], None, ],  # cable
    0xAF: [t_init, [], None, ],  # cable
    0xBD: [t_init, [], None, ],  # cable
    0xBE: [t_init, [], None, ],  # cable
    0xBF: [t_init, [], None, ],  # cable

    0x7D: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # radial
    0x7E: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # radial
    0x7F: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # radial

    0x5D: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # lava
    0x5E: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # lava
    0x5F: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # lava

    0xCD: [t_init, [], None, ],  # acid
    0xCE: [t_init, [], None, ],  # acid
    0xCF: [t_init, [], None, ],  # acid
    0xDD: [t_init, [], None, ],  # acid
    0xDE: [t_init, [], None, ],  # acid
    0xDF: [t_init, [], None, ],  # acid

    0x6D: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # electron
    0x6E: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # electron
    0x6F: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # electron

    0x4A: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # pinchos
    0x4B: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # pinchos
    0x4C: [t_init, ['player'], tiles_basic.hit_dmg, 1, 1, 1, 1, ],  # pinchos

}

TANIMATE = [

    # (starting_tile,animated list of frames incs),

    (0x0C, [int(v) for v in '00000001112223330000000000000000']),  # extra life
    (0x1C, [int(v) for v in '00000001112223330000000000000000']),  # def

    (0x08, [int(v) for v in '00000000000000000000000111222333']),  # cannon
    (0x18, [int(v) for v in '00000000000000000000000111222333']),  # laser
    (0x28, [int(v) for v in '00000000000000000000000111222333']),  # shootgun
    (0x38, [int(v) for v in '00000000000000000000000111222333']),  # granadelauncher



    (0x30, [int(v) for v in '1111111111111111111111111111111111111111111111111111111111111111']),  # door

    (0x4D, [int(v) for v in '0000000000000000111111111111111122222222222222221111111111111111']),  # torch

    (0x9D, [int(v) for v in '1111111111111111111100011111111111111111111111111100000000000000']),  # red led

    (0xAD, [int(v) for v in '0000000000000000000000000000000000000000000000000112211001100220']),  # cable
    (0xBD, [int(v) for v in '0000000000000000000000000000000000000000000000000112211001100220']),  # cable

    (0xCD, [int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']),  # acid
    (0xDD, [int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']),  # acid



    (0x7D, [int(v) for v in '00112211001122110011221100112211']),  # radial

    (0x5D, [int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']),  # lava

    (0x6D, [int(v) for v in '00000000000111111111112222222222']),  # electron

    (0x4A, [int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']),  # pinchos acido

]

TREPLACE = [

    # (tile_to_replace,replace_with)

    (0x10, 0x00),
    (0x11, 0x00),

]


def t_put(g, pos, n):
    x, y = pos
    if n not in TILES:
        # print 'undefined tile:',x,y,'0x%02x'%n
        t_init(g, pygame.Rect(x * TW, y * TH, TW, TH), n, [], None)
        return
    v = TILES[n]
    v[0](g, pygame.Rect(x * TW, y * TH, TW, TH), n, *v[1:])
