# config/game_config.py

import random

#Backend symbol and pattern configuration

SYMBOLS = (0, 1, 2, 3, 4, 5, 6)  # lemon, cherry, clover, bell, diamond, treasure, seven
SYMBOL_NAMES = ['lemon', 'cherry', 'clover', 'bell', 'diamond', 'treasure', 'seven']
SYMBOL_WEIGHTS = [1.3, 1.3, 1, 1, 0.8, 0.8, 0.5]
SYMBOL_VALUES = [2, 2, 3, 3, 5, 5, 7]

SYMBOL_MULT_DEFAULT = 1
PATTERN_MULT_DEFAULT = 1

PATTERN_VALUES = {
    'hor': 1,
    'vert': 1,
    'diag': 1,
    'horL': 2,
    'horXL': 3,
    'zig': 4,
    'zag': 4,
    'above': 7,
    'below': 7,
    'eye': 8,
    'jackpot': 10,
}

PATTERN_ORDER = {
    'hor1.1': 1, 'hor1.2': 2, 'hor1.3': 3,
    'hor2.1': 4, 'hor2.2': 5, 'hor2.3': 6,
    'hor3.1': 7, 'hor3.2': 8, 'hor3.3': 9,
    'vert1': 10, 'vert2': 11, 'vert3': 12, 'vert4': 13, 'vert5': 14,
    'bckDiag1': 15, 'bckDiag2': 16, 'bckDiag3': 17,
    'fwdDiag1': 18, 'fwdDiag2': 19, 'fwdDiag3': 20,
    'horL1.1': 21, 'horL1.2': 22, 'horL2.1': 23, 'horL2.2': 24,
    'horL3.1': 25, 'horL3.2': 26,
    'horXL1': 27, 'horXL2': 28, 'horXL3': 29,
    'zig': 30, 'zag': 31, 'above': 32, 'below': 33, 'eye': 34, 'jackpot': 35,
}

EYE_SHAPE = (1, 2, 3, 5, 6, 8, 9, 11, 12, 13)
ABOVE_SHAPE = (2, 6, 8, 10, 11, 12, 13, 14)
BELOW_SHAPE = (0, 1, 2, 3, 4, 6, 8, 12)
ZIG_SHAPE = (2, 6, 8, 10, 14)
ZAG_SHAPE = (0, 4, 6, 8, 12)

CHANCE_666 = 1.5

#Backend default chances for modifiers (all zero for now)

GOLD_CHANCE = 0
AFF_GOLD_CHANCE = 0
TOKEN_CHANCE = 0
AFF_TOKEN_CHANCE = 0
TICKET_CHANCE = 0
AFF_TICKET_CHANCE = 0
REP_CHANCE = 0
AFF_REP_CHANCE = 0
BATT_CHANCE = 0
AFF_BATT_CHANCE = 0
CHAIN_CHANCE = 0
AFF_CHAIN_CHANCE = 0

#Backend base luck / state defaults

BASE_LUCK_DEFAULT = 15
DEBT_NUM_DEFAULT = 1
SPIN_NUM_START = 1
PITY_COUNTER_START = 0
OLS_SPIN_START = 0

def random_ils_offset():
    return random.randint(0, 4)

#Frontend configuration

OVERALL_SCALE = 2
SYMBOL_SCALE = 2 * OVERALL_SCALE
SYMBOL_SPACE_VER = 16 * OVERALL_SCALE
SPIN_SPEED = 10 * OVERALL_SCALE
SYMBOL_SPACE_HOR = 100 * OVERALL_SCALE
SQUARE_DIST = 5 * OVERALL_SCALE
FRAME_RATE = 60
FONT_SIZE = 30 * OVERALL_SCALE
DIVIDER_LINE_WIDTH = 8 * OVERALL_SCALE

#Asset paths

ASSET_PATHS = {
    "lemon": "assets/SymbolLemon.webp",
    "cherry": "assets/SymbolCherry.webp",
    "clover": "assets/SymbolClover.webp",
    "bell": "assets/SymbolBell.webp",
    "diamond": "assets/SymbolDiamond.webp",
    "treasure": "assets/SymbolTreasureChest.webp",
    "seven": "assets/SymbolSeven.webp",
    "golden": "assets/modifierGolden.webp",
    "token": "assets/modifierToken.webp",
    "ticket": "assets/modifierTicket.webp",
    "repetition": "assets/modifierRepetition.webp",
    "battery": "assets/modifierBattery.webp",
    "chain": "assets/modifierChain.webp",
}
