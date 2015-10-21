import pygame
from pygame.locals import *

from cnst import *

import tiles_basic
from tile import *

# NOTE: If you add new tiles, use t_init for regular tiles.
#       tl_init and tr_init are for tiles that take up only half of the
#       16x16 tile, on the left or right side respectively.

TILES = {
#general purpose tiles
0x00    :[t_init,[],None,],
0x01    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x02    :[t_init,['solid'],tiles_basic.hit_breakable,1,1,1,1,],
0x03    :[t_init,['player'],tiles_basic.hit_fire,],
0x04    :[t_init,[],None,], #black background tile
0x05    :[t_init,[],None,], #exit sign
0x10    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x11    :[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x12    :[t_init,['solid'],tiles_basic.hit_fally,1,1,1,1,],
#0x14    :[t_init,['bubble'],tiles_basic.hit_replace,0x15,],
0x15    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x21    :[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],

#powerups and bonus items ...
0x08    :[t_init,['player'],tiles_basic.hit_power,'cannon'], #cannon
0x0C    :[t_init,['player'],tiles_basic.hit_life,], #extra-life
0x18    :[t_init,['player'],tiles_basic.hit_item,100], #points
#0x1A    :[t_init,['player'],tiles_basic.hit_item,250], #points
#0x1C    :[t_init,['player'],tiles_basic.hit_item,500], #points
#0x1E    :[t_init,['player'],tiles_basic.hit_item,1000], #points
0x1C    :[t_init,['player'],tiles_basic.hit_def,], #extra-def
0x28    :[t_init,['player'],tiles_basic.hit_power, 'shootgun'], #shootgun

#mine tiles (0x40...)
0x40	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x41	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x42	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x43	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x44	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x45	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0x51	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0x52	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x54	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x55	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0x61	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0x62	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x64	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x65	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x70	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x71	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x72	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x73	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x74	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x75	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],

#dirt floor set
0x47    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x48    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x49    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x57    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x58    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x59    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x67    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x68    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x69    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x77    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x78    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x79    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],

#dirt floor set #2
0x4A    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x4B    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x4C    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x5A    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x5B    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x5C    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x6A    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x6B    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x6C    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x7A    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x7B    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x7C    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],

#volcano tiles (0x80...)
0x80	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x81	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x82	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x83	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0x84	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x85	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0x91	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0x92	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0x94	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0x95	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0xa1	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0xa2	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xa4	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xa5	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xb0	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xb1	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xb2	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xb3	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xb4	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xb5	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],

# volcano cave set
0x87    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x88    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x89    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x97    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x98    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0x99    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xA7    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xA8    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0xA9    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xB7    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xB8    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xB9    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],

#moon tiles (0xC0...)
0xc0	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xc1	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xc2	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xc3	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xc4	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xc5	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0xd1	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0xd2	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xd4	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xd5	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
#0xe1	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
#0xe2	:[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xe5	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xf0	:[tr_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xf1	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xf2	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xf3	:[tl_init,['solid'],tiles_basic.hit_block,1,0,0,0,],
0xf5	:[t_init,['solid'],tiles_basic.hit_block,1,0,0,0,],

# moon cave set
0xC7    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xC8    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xC9    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xD7    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xD8    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xD9    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xE7    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xE8    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xE9    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xF7    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xF8    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],
0xF9    :[t_init,['solid'],tiles_basic.hit_block,1,1,1,1,],

# tile animations

0x4D    :[t_init,[],None,], # torch
0x4E    :[t_init,[],None,], # torch
0x4F    :[t_init,[],None,], # torch

0x9D    :[t_init,[],None,], # red light
0x9E    :[t_init,[],None,], # red light

0xAD    :[t_init,[],None,], # cable
0xAE    :[t_init,[],None,], # cable
0xAF    :[t_init,[],None,], # cable
0xBD    :[t_init,[],None,], # cable
0xBE    :[t_init,[],None,], # cable
0xBF    :[t_init,[],None,], # cable

0x7D    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # radial
0x7E    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # radial
0x7F    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # radial

0x5D    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # lava
0x5E    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # lava
0x5F    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # lava

0xCD    :[t_init,[],None,], # acid
0xCE    :[t_init,[],None,], # acid
0xCF    :[t_init,[],None,], # acid
0xDD    :[t_init,[],None,], # acid
0xDE    :[t_init,[],None,], # acid
0xDF    :[t_init,[],None,], # acid

0x6D    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # electron
0x6E    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # electron
0x6F    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # electron

0x4A    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # pinchos
0x4B    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # pinchos
0x4C    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # pinchos

0x5A    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # draco
0x5B    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # draco
0x5C    :[t_init,['player'],tiles_basic.hit_dmg,1,1,1,1,], # draco

}


TANIMATE = [
#(starting_tile,animated list of frames incs),
(0x08,[int(v) for v in '00000000000000000000000111222333']), # cannon
(0x0C,[int(v) for v in '00000001112223330000000000000000']), # extra life
(0x18,[int(v) for v in '1100000000000000000000000000000000000000000000000000000000000000']), # veggies
(0x1A,[int(v) for v in '0000000000000000110000000000000000000000000000000000000000000000']),
(0x1C,[int(v) for v in '00000001112223330000000000000000']), # def
(0x1E,[int(v) for v in '0000000000000000000000000000000000000000000000001100000000000000']),
(0x28,[int(v) for v in '00000000000000000000000111222333']), # cannon
(0x30,[int(v) for v in '1111111111111111111111111111111111111111111111111111111111111111']), # door
(0x4D,[int(v) for v in '0000000000000000111111111111111122222222222222221111111111111111']), #torch
(0x9D,[int(v) for v in '1111111111111111111111111111111111111111111111111100000000000000']), #torch
(0xAD,[int(v) for v in '0000000000000000000000000000000000000000000000000112211001100220']), #torch
(0xBD,[int(v) for v in '0000000000000000000000000000000000000000000000000112211001100220']), #torch
(0x7D,[int(v) for v in '00112211001122110011221100112211']), # radial
(0x5D,[int(v) for v in '00000000000111111111112222222222']), # lava
(0xCD,[int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']), #acid
(0xDD,[int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']), #acid
(0x6D,[int(v) for v in '00000000000111111111112222222222']), # electron
(0x4A,[int(v) for v in '0000000000000000000001111111111111111111112222222222222222222222']), #pinchos
(0x5A,[int(v) for v in '00000000000111111111112222222222']), #draco


]

TREPLACE = [
#(tile_to_replace,replace_with)
(0x10,0x00),
(0x11,0x00),
(0x14,0x00),
(0x20,0x00),
]

def t_put(g,pos,n):
	x,y = pos
	if n not in TILES:
		#print 'undefined tile:',x,y,'0x%02x'%n
		t_init(g,pygame.Rect(x*TW,y*TH,TW,TH),n,[],None)
		return
	v = TILES[n]
	v[0](g,pygame.Rect(x*TW,y*TH,TW,TH),n,*v[1:])

