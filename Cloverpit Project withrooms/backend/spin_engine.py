# backend/spin_engine.py

import random
import math
import config.game_config as config

from backend.shelf_backend import (preRollTrigger, postRollTrigger, randomTrigger, buttonTrigger, interventionTrigger)

class GameState:
    def __init__(self):

        self.debtNum = config.DEBT_NUM_DEFAULT
        self.spinNum = config.SPIN_NUM_START
        self.OLSSpin = config.OLS_SPIN_START
        self.pityCounter = config.PITY_COUNTER_START
        self.ILSOffset = config.random_ils_offset()


def spin(state: GameState):

    res = []
    modifiers = []
    result = []

    eye = False
    retrigger = 0
    baseLuck = config.luck
    luck = config.luck + config.tempLuck
    debtNum = state.debtNum
    spinNum = state.spinNum
    OLSSpin = state.OLSSpin
    pityCounter = state.pityCounter
    ILSOffset = state.ILSOffset

    preRollTrigger()

    if debtNum == 1 and spinNum != 1 and (spinNum + ILSOffset + 1) % (4 + math.floor(spinNum / 6)) == 0:
        luck += random.choice((4, 5, 6, 6, 7, 8))

    if spinNum == OLSSpin:
        OLSSpin = spinNum + 3 + debtNum + random.getrandbits(1)
        if spinNum % 7 == 0:
            luck += random.randint(7, 9)
        if spinNum % 3 == 0:
            luck += random.randint(5, 7)
        else:
            luck += random.randint(3, 5)

    if pityCounter >= 4:
        luck += pityCounter + 1

    if baseLuck < 5:
        if random.getrandbits(1) == 1:
            luck += 1 + random.getrandbits(1)
    elif baseLuck < 7:
        if random.getrandbits(2) == 1:
            luck += 1
    elif baseLuck == 7:
        if random.randint(0, 6) == 6:
            luck += 1

    luckSymbol = random.choices(config.symbols, weights = config.symbolWeights)
    for _ in range(luck):
        res += luckSymbol

    if len(res) < 15:
        for _ in range(15 - len(res)):
            res += random.choices(config.symbols, weights = config.symbolWeights)

    random.shuffle(res)

    for slot in res:
        r = 100 * random.random()

        if slot == 0 and r <= config.lemonGoldChance:
            modifiers.append(1)
        elif slot == 1 and r <= config.cherryGoldChance:
            modifiers.append(1)
        elif slot == 2 and r <= config.cloverGoldChance:
            modifiers.append(1)
        elif slot == 3 and r <= config.bellGoldChance:
            modifiers.append(1)
        elif slot == 4 and r <= config.diamondGoldChance:
            modifiers.append(1)
        elif slot == 5 and r <= config.treasureGoldChance:
            modifiers.append(1)
        elif slot == 6 and r <= config.sevenGoldChance:
            modifiers.append(1)

        elif slot == 0 and r <= config.lemonTokenChance:
            modifiers.append(2)
        elif slot == 1 and r <= config.cherryTokenChance:
            modifiers.append(2)
        elif slot == 2 and r <= config.cloverTokenChance:
            modifiers.append(2)
        elif slot == 3 and r <= config.bellTokenChance:
            modifiers.append(2)
        elif slot == 4 and r <= config.diamondTokenChance:
            modifiers.append(2)
        elif slot == 5 and r <= config.treasureTokenChance:
            modifiers.append(2)
        elif slot == 6 and r <= config.sevenTokenChance:
            modifiers.append(2)


        elif slot == 0 and r <= config.lemonTicketChance:
            modifiers.append(3)
        elif slot == 1 and r <= config.cherryTicketChance:
            modifiers.append(3)
        elif slot == 2 and r <= config.cloverTicketChance:
            modifiers.append(3)
        elif slot == 3 and r <= config.bellTicketChance:
            modifiers.append(3)
        elif slot == 4 and r <= config.diamondTicketChance:
            modifiers.append(3)
        elif slot == 5 and r <= config.treasureTicketChance:
            modifiers.append(3)
        elif slot == 6 and r <= config.sevenTicketChance:
            modifiers.append(3)


        elif r <= config.repChance:
            modifiers.append(4)
        elif slot > 3 and r <= config.affRepChance:
            modifiers.append(4)
        elif r <= config.battChance:
            modifiers.append(5)
        elif (slot == 2 or slot == 3) and r <= config.affBattChance:
            modifiers.append(5)
        elif r <= config.chainChance:
            modifiers.append(6)
        elif slot > 3 and r <= config.affChainChance:
            modifiers.append(6)
        else:
            modifiers.append(0)

    if 100 * random.random() <= config.chance666:
        res[6] = 7
        res[7] = 7
        res[8] = 7
        config.is666 = True
    else:
        if 100 * random.random() <= 6:
            res[6] = 7
            res[7] = 7
        elif 100 * random.random() <= 7.5:
            res[6] = 7

        interventionTrigger()

        vertList = [0, 0, 0]
        horXLList = [0, 0, 0, 0, 0]
        horLList = [0, 0, 0, 0]
        horList = [0, 0, 0]
        diagList = []
        modTrigs = []

        eyeList = []
        for i in config.eyeShape:
            eyeList.append(res[i])

        if eyeList.count(eyeList[0]) == 10:
            payout = config.symbolValues[eyeList[0]] * config.symbolMult * config.patternValues['eye'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in config.eyeShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[eyeList[0]] += config.baseSymbolValues[eyeList[0]]
                result.append(('eye', payout, modTrigs))
            eye = True
        else:
            for i in range(2):
                for j in range(3):
                    vertList[j] = res[1 + 5 * j + 2 * i]
                if vertList.count(vertList[0]) == 3:
                    payout = config.symbolValues[vertList[0]] * config.symbolMult * config.patternValues['vert'] * config.patternMult
                    modTrigs = tuple([modifiers[slot] for slot in (1 + 2 * i, 6 + 2 * i, 11 + 2 * i) if modifiers[slot] != 0])
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        for gold in range(modTrigs.count(1)):
                            config.symbolValues[vertList[0]] += config.baseSymbolValues[vertList[0]]
                        result.append(('vert' + str((i + 1) * 2), payout, modTrigs))

        for i in range(3):
            for j in range(3):
                vertList[j] = res[5 * j + 2 * i]
            if vertList.count(vertList[0]) == 3:
                payout = config.symbolValues[vertList[0]] * config.symbolMult * config.patternValues['vert'] * config.patternMult
                modTrigs = tuple(modifiers[slot] for slot in (2 * i, 5 + 2 * i, 10 + 2 * i) if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    for gold in range(modTrigs.count(1)):
                        config.symbolValues[vertList[0]] += config.baseSymbolValues[vertList[0]]
                    result.append(('vert' + str(1 + i * 2), payout, modTrigs))

        aboveList = []
        for i in config.aboveShape:
            aboveList.append(res[i])

        if aboveList.count(aboveList[0]) == 8:
            payout = config.symbolValues[aboveList[0]] * config.symbolMult * config.patternValues['above'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in config.aboveShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[aboveList[0]] += config.baseSymbolValues[aboveList[0]]
                result.append(('above', payout, modTrigs))
        else:
            for i in range(5):
                horXLList[i] = res[i]
            if horXLList.count(horXLList[0]) == 5:
                payout = config.symbolValues[horXLList[0]] * config.symbolMult * config.patternValues['horXL'] * config.patternMult
                modTrigs = tuple(modifiers[slot] for slot in range(5) if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    for gold in range(modTrigs.count(1)):
                        config.symbolValues[horXLList[0]] += config.baseSymbolValues[horXLList[0]]
                    result.append(('horXL1', payout, modTrigs))
            else:
                for i in range(4):
                    horLList[i] = res[i]
                if horLList.count(horLList[0]) == 4:
                    payout = config.symbolValues[horLList[0]] * config.symbolMult * config.patternValues['horL'] * config.patternMult
                    modTrigs = tuple(modifiers[slot] for slot in range(4) if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        for gold in range(modTrigs.count(1)):
                            config.symbolValues[horLList[0]] += config.baseSymbolValues[horLList[0]]
                        result.append(('horL1.1', payout, modTrigs))
                else:
                    for i in range(4):
                        horLList[i] = res[i + 1]
                    if horLList.count(horLList[0]) == 4:
                        payout = config.symbolValues[horLList[0]] * config.symbolMult * config.patternValues['horL'] * config.patternMult
                        modTrigs = tuple(modifiers[slot] for slot in (1, 2, 3, 4) if modifiers[slot] != 0)
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            for gold in range(modTrigs.count(1)):
                                config.symbolValues[horLList[0]] += config.baseSymbolValues[horLList[0]]
                            result.append(('horL1.2', payout, modTrigs))
                    else:
                        for i in range(2):
                            for j in range(3):
                                horList[j] = res[2 * i + j]
                            if horList.count(horList[0]) == 3:
                                payout = config.symbolValues[horList[0]] * config.symbolMult * config.patternValues['hor'] * config.patternMult
                                modTrigs = tuple(modifiers[slot] for slot in (2 * i, 2 * i + 1, 2 * i + 2) if modifiers[slot] != 0)
                                for _ in range(1 + retrigger + modTrigs.count(4)):
                                    for gold in range(modTrigs.count(1)):
                                        config.symbolValues[horList[0]] += config.baseSymbolValues[horList[0]]
                                    result.append(('hor1.' + str(1 + 2 * i), payout))
                                break

                        for i in range(3):
                            horList[i] = res[i + 1]
                        if horList.count(horList[0]) == 3 and not eye:
                            payout = config.symbolValues[horList[0]] * config.symbolMult * config.patternValues['hor'] * config.patternMult
                            modTrigs = tuple(modifiers[slot] for slot in (1, 2, 3) if modifiers[slot] != 0)
                            for _ in range(1 + retrigger + modTrigs.count(4)):
                                for gold in range(modTrigs.count(1)):
                                    config.symbolValues[horList[0]] += config.baseSymbolValues[horList[0]]
                                result.append(('hor1.2', payout, modTrigs))

            zigList = []
            for i in config.zigShape:
                zigList.append(i)
            if zigList.count(zigList[0]) == 5:
                payout = config.symbolValues[zigList[0]] * config.symbolMult * config.patternValues['zig'] * config.patternMult
                modTrigs = tuple(modifiers[slot] for slot in config.zigShape if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    for gold in range(modTrigs.count(1)):
                        config.symbolValues[zigList[0]] += config.baseSymbolValues[zigList[0]]
                    result.append(('zig', payout, modTrigs))
            else:
                diagShape = [2, 6, 10]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if diagList.count(diagList[0]) == 3:
                    payout = config.symbolValues[diagList[0]] * config.symbolMult * config.patternValues['diag'] * config.patternMult
                    modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('fwdDiag1', payout, modTrigs))
                else:
                    diagShape = [2, 8, 14]
                    diagList.clear()
                    for i in diagShape:
                        diagList.append(res[i])
                    if diagList.count(diagList[0]) == 3:
                        payout = config.symbolValues[diagList[0]] * config.symbolMult * config.patternValues['diag'] * config.patternMult
                        modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            for gold in range(modTrigs.count(1)):
                                config.symbolValues[diagList[0]] += config.baseSymbolValues[diagList[0]]
                            result.append(('bckDiag3', payout, modTrigs))

        belowList = []
        for i in config.belowShape:
            belowList.append(res[i])

        if belowList.count(belowList[0]) == 8:
            payout = config.symbolValues[belowList[0]] * config.symbolMult * config.patternValues['below'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in config.belowShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[belowList[0]] += config.baseSymbolValues[belowList[0]]
                result.append(('below', payout, modTrigs))
        else:
            for i in range(5):
                horXLList[i] = res[i + 10]
            if horXLList.count(horXLList[0]) == 5:
                payout = config.symbolValues[horXLList[0]] * config.symbolMult * config.patternValues['horXL'] * config.patternMult
                modTrigs = tuple(modifiers[slot] for slot in (10, 11, 12, 13, 14) if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    for gold in range(modTrigs.count(1)):
                        config.symbolValues[horXLList[0]] += config.baseSymbolValues[horXLList[0]]
                    result.append(('horXL3', payout, modTrigs))
            else:
                for i in range(4):
                    horLList[i] = res[i + 10]
                if horLList.count(horLList[0]) == 4:
                    payout = config.symbolValues[horLList[0]] * config.symbolMult * config.patternValues['horL'] * config.patternMult
                    modTrigs = tuple(modifiers[slot] for slot in (10, 11, 12, 13) if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        for gold in range(modTrigs.count(1)):
                            config.symbolValues[horLList[0]] += config.baseSymbolValues[horLList[0]]
                        result.append(('horL3.1', payout, modTrigs))
                else:
                    for i in range(4):
                        horLList[i] = res[i + 11]
                    if horLList.count(horLList[0]) == 4:
                        payout = config.symbolValues[horLList[0]] * config.symbolMult * config.patternValues['horL'] * config.patternMult
                        modTrigs = tuple(modifiers[slot] for slot in (11, 12, 13, 14) if modifiers[slot] != 0)
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            for gold in range(modTrigs.count(1)):
                                config.symbolValues[horLList[0]] += config.baseSymbolValues[horLList[0]]
                            result.append(('horL3.2', payout, modTrigs))
                    else:
                        for i in range(2):
                            for j in range(3):
                                horList[j] = res[2 * i + j + 10]
                            if horList.count(horList[0]) == 3:
                                payout = config.symbolValues[horList[0]] * config.symbolMult * config.patternValues['hor'] * config.patternMult
                                modTrigs = tuple(modifiers[slot] for slot in (2 * i + 10, 2 * i + 11, 2 * i + 12) if modifiers[slot] != 0)
                                for _ in range(1 + retrigger + modTrigs.count(4)):
                                    for gold in range(modTrigs.count(1)):
                                        config.symbolValues[horList[0]] += config.baseSymbolValues[horList[0]]
                                    result.append(('hor3.' + str(1 + 2 * i), payout, modTrigs))
                                break

                        for i in range(3):
                            horList[i] = res[i + 11]
                        if horList.count(horList[0]) == 3 and not eye:
                            payout = config.symbolValues[horList[0]] * config.symbolMult * config.patternValues['hor'] * config.patternMult
                            modTrigs = tuple(modifiers[slot] for slot in (11, 12, 13) if modifiers[slot] != 0)
                            for _ in range(1 + retrigger + modTrigs.count(4)):
                                for gold in range(modTrigs.count(1)):
                                    config.symbolValues[horList[0]] += config.baseSymbolValues[horList[0]]
                                result.append(('hor3.2', payout, modTrigs))

            zagList = []
            for i in config.zagShape:
                zagList.append(i)
            if zagList.count(zagList[0]) == 5:
                payout = config.symbolValues[zagList[0]] * config.symbolMult * config.patternValues['zag'] * config.patternMult
                modTrigs = tuple(modifiers[slot] for slot in config.zagShape if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    for gold in range(modTrigs.count(1)):
                        config.symbolValues[zagList[0]] += config.baseSymbolValues[zagList[0]]
                    result.append(('zag', payout, modTrigs))
            else:
                diagShape = [0, 6, 12]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if diagList.count(diagList[0]) == 3:
                    payout = config.symbolValues[diagList[0]] * config.symbolMult * config.patternValues['diag'] * config.patternMult
                    modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        for gold in range(modTrigs.count(1)):
                            config.symbolValues[diagList[0]] += config.baseSymbolValues[diagList[0]]
                        result.append(('bckDiag1', payout))
                else:
                    diagShape = [4, 8, 12]
                    diagList.clear()
                    for i in diagShape:
                        diagList.append(res[i])
                    if diagList.count(diagList[0]) == 3:
                        payout = config.symbolValues[diagList[0]] * config.symbolMult * config.patternValues['diag'] * config.patternMult
                        modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            for gold in range(modTrigs.count(1)):
                                config.symbolValues[diagList[0]] += config.baseSymbolValues[diagList[0]]
                            result.append(('fwdDiag3', payout, modTrigs))

        for i in range(5):
            horXLList[i] = res[i + 5]
        if horXLList.count(horXLList[0]) == 5:
            payout = config.symbolValues[horXLList[0]] * config.symbolMult * config.patternValues['horXL'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in (5, 6, 7, 8, 9) if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[horXLList[0]] += config.baseSymbolValues[horXLList[0]]
                result.append(('horXL2', payout, modTrigs))
        else:
            for i in range(4):
                horLList[i] = res[i + 5]
            if horLList.count(horLList[0]) == 4:
                payout = config.symbolValues[horLList[0]] * config.symbolMult * config.patternValues['horL'] * config.patternMult
                modTrigs = tuple(modifiers[slot] for slot in (5, 6, 7, 8) if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    for gold in range(modTrigs.count(1)):
                        config.symbolValues[horLList[0]] += config.baseSymbolValues[horLList[0]]
                    result.append(('horL2.1', payout, modTrigs))
            else:
                for i in range(4):
                    horLList[i] = res[i + 6]
                if horLList.count(horLList[0]) == 4:
                    payout = config.symbolValues[horLList[0]] * config.symbolMult * config.patternValues['horL'] * config.patternMult
                    modTrigs = tuple(modifiers[slot] for slot in (6, 7, 8, 9) if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        for gold in range(modTrigs.count(1)):
                            config.symbolValues[horLList[0]] += config.baseSymbolValues[horLList[0]]
                        result.append(('horL2.2', payout, modTrigs))
                else:
                    for i in range(3):
                        for j in range(3):
                            horList[j] = res[i + j + 5]
                        if horList.count(horList[0]) == 3:
                            payout = config.symbolValues[horList[0]] * config.symbolMult * config.patternValues['hor'] * config.patternMult
                            modTrigs = tuple(modifiers[slot] for slot in (i + 5, i + 6, i + 7) if modifiers[slot] != 0)
                            for _ in range(1 + retrigger + modTrigs.count(4)):
                                for gold in range(modTrigs.count(1)):
                                    config.symbolValues[horList[0]] += config.baseSymbolValues[horList[0]]
                                result.append(('hor2.' + str(1 + i), payout, modTrigs))
                            break

        diagShape = [3, 7, 11]
        diagList.clear()
        for i in diagShape:
            diagList.append(res[i])
        if diagList.count(diagList[0]) == 3:
            payout = config.symbolValues[diagList[0]] * config.symbolMult * config.patternValues['diag'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[diagList[0]] += config.baseSymbolValues[diagList[0]]
                result.append(('fwdDiag2', payout, modTrigs))

        diagShape = [1, 7, 13]
        diagList.clear()
        for i in diagShape:
            diagList.append(res[i])
        if diagList.count(diagList[0]) == 3:
            payout = config.symbolValues[diagList[0]] * config.symbolMult * config.patternValues['diag'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[diagList[0]] += config.baseSymbolValues[diagList[0]]
                result.append(('bckDiag2', payout, modTrigs))

        if res.count(res[0]) == 15:
            payout = config.symbolValues[res[0]] * config.symbolMult * config.patternValues['jackpot'] * config.patternMult
            modTrigs = tuple(modifiers[slot] for slot in range(15) if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                for gold in range(modTrigs.count(1)):
                    config.symbolValues[res[0]] += config.baseSymbolValues[res[0]]
                result.append(('jackpot', payout, modTrigs))

    if result == []:
        pityCounter += 1

    config.tempLuck = 0

    postRollTrigger(result, pityCounter)
    randomTrigger(result, pityCounter)

    def patternOrdering(e):
        return config.patternOrder[e[0]]

    result.sort(key=patternOrdering)

    state.luck = luck
    state.pityCounter = pityCounter
    state.spinNum = spinNum + 1
    state.OLSSpin = OLSSpin

    print(result)
    print(config.lemonGoldChance)

    return res, modifiers, result
