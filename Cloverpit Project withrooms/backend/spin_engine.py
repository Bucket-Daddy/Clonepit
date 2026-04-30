# backend/spin_engine.py

import random
import math
import config.game_config

from config.game_config import (
    symbols,
    symbolWeights,
    symbolValues,
    patternValues,
    patternOrder,
    eyeShape,
    aboveShape,
    belowShape,
    zigShape,
    zagShape,
    symbolMult,
    patternMult,
    buttonPressed,
    chance666,
    is666,
    
    lemonGoldChance,
    cherryGoldChance,
    cloverGoldChance,
    bellGoldChance,
    diamondGoldChance,
    treasureGoldChance,
    sevenGoldChance,

    lemonTokenChance,
    cherryTokenChance,
    cloverTokenChance,
    bellTokenChance,
    diamondTokenChance,
    treasureTokenChance,
    sevenTokenChance,

    lemonTicketChance,
    cherryTicketChance,
    cloverTicketChance,
    bellTicketChance,
    diamondTicketChance,
    treasureTicketChance,
    sevenTicketChance,
    
    repChance,
    affRepChance,
    battChance,
    affBattChance,
    chainChance,
    affChainChance,
    BASE_LUCK_DEFAULT,
    DEBT_NUM_DEFAULT,
    SPIN_NUM_START,
    PITY_COUNTER_START,
    OLS_SPIN_START,
    random_ils_offset,
)


class GameState:
    def __init__(self):
        self.prerollItems = []
        self.interventions = []
        self.postrollItems = []

        self.debtNum = DEBT_NUM_DEFAULT
        self.spinNum = SPIN_NUM_START
        self.OLSSpin = OLS_SPIN_START
        self.pityCounter = PITY_COUNTER_START
        self.ILSOffset = random_ils_offset()

        self.baseLuck = BASE_LUCK_DEFAULT
        self.luck = self.baseLuck


def spin(state: GameState):
    prerollItems = state.prerollItems
    interventions = state.interventions
    postrollItems = state.postrollItems

    res = []
    modifiers = []
    result = []

    eye = False
    retrigger = 0

    baseLuck = state.baseLuck
    luck = state.luck
    debtNum = state.debtNum
    spinNum = state.spinNum
    OLSSpin = state.OLSSpin
    pityCounter = state.pityCounter
    ILSOffset = state.ILSOffset

    for item in prerollItems:
        item.trigger

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

    luckSymbol = random.choices(symbols, weights=symbolWeights)
    for _ in range(luck):
        res += luckSymbol

    if len(res) < 15:
        for _ in range(15 - len(res)):
            res += random.choices(symbols, weights=symbolWeights)

    random.shuffle(res)

    for slot in res:
        r = 100 * random.random()

        if slot == 0 and r <= lemonGoldChance:
            modifiers.append(1)
        elif slot == 1 and r <= cherryGoldChance:
            modifiers.append(1)
        elif slot == 2 and r <= cloverGoldChance:
            modifiers.append(1)
        elif slot == 3 and r <= bellGoldChance:
            modifiers.append(1)
        elif slot == 4 and r <= diamondGoldChance:
            modifiers.append(1)
        elif slot == 5 and r <= treasureGoldChance:
            modifiers.append(1)
        elif slot == 6 and r <= sevenGoldChance:
            modifiers.append(1)

        elif slot == 0 and r <= lemonTokenChance:
            modifiers.append(2)
        elif slot == 1 and r <= cherryTokenChance:
            modifiers.append(2)
        elif slot == 2 and r <= cloverTokenChance:
            modifiers.append(2)
        elif slot == 3 and r <= bellTokenChance:
            modifiers.append(2)
        elif slot == 4 and r <= diamondTokenChance:
            modifiers.append(2)
        elif slot == 5 and r <= treasureTokenChance:
            modifiers.append(2)
        elif slot == 6 and r <= sevenTokenChance:
            modifiers.append(2)


        elif slot == 0 and r <= lemonTicketChance:
            modifiers.append(3)
        elif slot == 1 and r <= cherryTicketChance:
            modifiers.append(3)
        elif slot == 2 and r <= cloverTicketChance:
            modifiers.append(3)
        elif slot == 3 and r <= bellTicketChance:
            modifiers.append(3)
        elif slot == 4 and r <= diamondTicketChance:
            modifiers.append(3)
        elif slot == 5 and r <= treasureTicketChance:
            modifiers.append(3)
        elif slot == 6 and r <= sevenTicketChance:
            modifiers.append(3)


        elif r <= repChance:
            modifiers.append(4)
        elif slot > 3 and r <= affRepChance:
            modifiers.append(4)
        elif r <= battChance:
            modifiers.append(5)
        elif (slot == 2 or slot == 3) and r <= affBattChance:
            modifiers.append(5)
        elif r <= chainChance:
            modifiers.append(6)
        elif slot > 3 and r <= affChainChance:
            modifiers.append(6)
        else:
            modifiers.append(0)

    if 100 * random.random() <= chance666:
        res[6] = 7
        res[7] = 7
        res[8] = 7
        is666 = True
    else:
        if 100 * random.random() <= 6:
            res[6] = 7
            res[7] = 7
        elif 100 * random.random() <= 7.5:
            res[6] = 7

        for item in interventions:
            item.trigger

        vertList = [0, 0, 0]
        horXLList = [0, 0, 0, 0, 0]
        horLList = [0, 0, 0, 0]
        horList = [0, 0, 0]
        diagList = []
        modTrigs = []

        eyeList = []
        for i in eyeShape:
            eyeList.append(res[i])

        if eyeList.count(eyeList[0]) == 10:
            payout = symbolValues[eyeList[0]] * symbolMult * patternValues['eye'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in eyeShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('eye', payout, modTrigs))
            eye = True
        else:
            for i in range(2):
                for j in range(3):
                    vertList[j] = res[1 + 5 * j + 2 * i]
                if vertList.count(vertList[0]) == 3:
                    payout = symbolValues[vertList[0]] * symbolMult * patternValues['vert'] * patternMult
                    modTrigs = tuple(
                        [modifiers[slot] for slot in (1 + 2 * i, 6 + 2 * i, 11 + 2 * i) if modifiers[slot] != 0]
                    )
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('vert' + str(i * 2), payout, modTrigs))

        for i in range(3):
            for j in range(3):
                vertList[j] = res[5 * j + 2 * i]
            if vertList.count(vertList[0]) == 3:
                payout = symbolValues[vertList[0]] * symbolMult * patternValues['vert'] * patternMult
                modTrigs = tuple(
                    [modifiers[slot] for slot in (2 * i, 5 + 2 * i, 10 + 2 * i) if modifiers[slot] != 0]
                )
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('vert' + str(1 + i * 2), payout, modTrigs))

        aboveList = []
        for i in aboveShape:
            aboveList.append(res[i])

        if aboveList.count(aboveList[0]) == 8:
            payout = symbolValues[aboveList[0]] * symbolMult * patternValues['above'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in aboveShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('above', payout, modTrigs))
        else:
            for i in range(5):
                horXLList[i] = res[i]
            if horXLList.count(horXLList[0]) == 5:
                payout = symbolValues[horXLList[0]] * symbolMult * patternValues['horXL'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in range(5) if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('horXL1', payout, modTrigs))
            else:
                for i in range(4):
                    horLList[i] = res[i]
                if horLList.count(horLList[0]) == 4:
                    payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in range(4) if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('horL1.1', payout, modTrigs))
                else:
                    for i in range(4):
                        horLList[i] = res[i + 1]
                    if horLList.count(horLList[0]) == 4:
                        payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                        modTrigs = tuple(
                            modifiers[slot] for slot in (1, 2, 3, 4) if modifiers[slot] != 0
                        )
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('horL1.2', payout, modTrigs))
                    else:
                        for i in range(2):
                            for j in range(3):
                                horList[j] = res[2 * i + j]
                            if horList.count(horList[0]) == 3:
                                payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                                modTrigs = tuple(
                                    modifiers[slot] for slot in (2 * i, 2 * i + 1, 2 * i + 2) if modifiers[slot] != 0
                                )
                                for _ in range(1 + retrigger + modTrigs.count(4)):
                                    result.append(('hor1.' + str(1 + 2 * i), payout))
                                break

                        for i in range(3):
                            horList[i] = res[i + 1]
                        if horList.count(horList[0]) == 3 and not eye:
                            payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                            modTrigs = tuple(
                                modifiers[slot] for slot in (1, 2, 3) if modifiers[slot] != 0
                            )
                            for _ in range(1 + retrigger + modTrigs.count(4)):
                                result.append(('hor1.2', payout, modTrigs))

            zigList = []
            for i in zigShape:
                zigList.append(i)
            if zigList.count(zigList[0]) == 5:
                payout = symbolValues[zigList[0]] * symbolMult * patternValues['zig'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in zigShape if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('zig', payout, modTrigs))
            else:
                diagShape = [2, 6, 10]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if diagList.count(diagList[0]) == 3:
                    payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('fwdDiag1', payout, modTrigs))
                else:
                    diagShape = [2, 8, 14]
                    diagList.clear()
                    for i in diagShape:
                        diagList.append(res[i])
                    if diagList.count(diagList[0]) == 3:
                        payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                        modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('bckDiag3', payout, modTrigs))

        belowList = []
        for i in belowShape:
            belowList.append(res[i])

        if belowList.count(belowList[0]) == 8:
            payout = symbolValues[belowList[0]] * symbolMult * patternValues['below'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in belowShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('below', payout, modTrigs))
        else:
            for i in range(5):
                horXLList[i] = res[i + 10]
            if horXLList.count(horXLList[0]) == 5:
                payout = symbolValues[horXLList[0]] * symbolMult * patternValues['horXL'] * patternMult
                modTrigs = tuple(
                    modifiers[slot] for slot in (10, 11, 12, 13, 14) if modifiers[slot] != 0
                )
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('horXL3', payout, modTrigs))
            else:
                for i in range(4):
                    horLList[i] = res[i + 10]
                if horLList.count(horLList[0]) == 4:
                    payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                    modTrigs = tuple(
                        modifiers[slot] for slot in (10, 11, 12, 13) if modifiers[slot] != 0
                    )
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('horL3.1', payout, modTrigs))
                else:
                    for i in range(4):
                        horLList[i] = res[i + 11]
                    if horLList.count(horLList[0]) == 4:
                        payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                        modTrigs = tuple(
                            modifiers[slot] for slot in (11, 12, 13, 14) if modifiers[slot] != 0
                        )
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('horL3.2', payout, modTrigs))
                    else:
                        for i in range(2):
                            for j in range(3):
                                horList[j] = res[2 * i + j + 10]
                            if horList.count(horList[0]) == 3:
                                payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                                modTrigs = tuple(
                                    modifiers[slot]
                                    for slot in (2 * i + 10, 2 * i + 11, 2 * i + 12)
                                    if modifiers[slot] != 0
                                )
                                for _ in range(1 + retrigger + modTrigs.count(4)):
                                    result.append(('hor3.' + str(1 + 2 * i), payout, modTrigs))
                                break

                        for i in range(3):
                            horList[i] = res[i + 11]
                        if horList.count(horList[0]) == 3 and not eye:
                            payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                            modTrigs = tuple(
                                modifiers[slot] for slot in (11, 12, 13) if modifiers[slot] != 0
                            )
                            for _ in range(1 + retrigger + modTrigs.count(4)):
                                result.append(('hor3.2', payout, modTrigs))

            zagList = []
            for i in zagShape:
                zagList.append(i)
            if zagList.count(zagList[0]) == 5:
                payout = symbolValues[zagList[0]] * symbolMult * patternValues['zag'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in zagShape if modifiers[slot] != 0)
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('zag', payout, modTrigs))
            else:
                diagShape = [0, 6, 12]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if diagList.count(diagList[0]) == 3:
                    payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('bckDiag1', payout))
                else:
                    diagShape = [4, 8, 12]
                    diagList.clear()
                    for i in diagShape:
                        diagList.append(res[i])
                    if diagList.count(diagList[0]) == 3:
                        payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                        modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                        for _ in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('fwdDiag3', payout, modTrigs))

        for i in range(5):
            horXLList[i] = res[i + 5]
        if horXLList.count(horXLList[0]) == 5:
            payout = symbolValues[horXLList[0]] * symbolMult * patternValues['horXL'] * patternMult
            modTrigs = tuple(
                modifiers[slot] for slot in (5, 6, 7, 8, 9) if modifiers[slot] != 0
            )
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('horXL2', payout, modTrigs))
        else:
            for i in range(4):
                horLList[i] = res[i + 5]
            if horLList.count(horLList[0]) == 4:
                payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                modTrigs = tuple(
                    modifiers[slot] for slot in (5, 6, 7, 8) if modifiers[slot] != 0
                )
                for _ in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('horL2.1', payout, modTrigs))
            else:
                for i in range(4):
                    horLList[i] = res[i + 6]
                if horLList.count(horLList[0]) == 4:
                    payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                    modTrigs = tuple(
                        modifiers[slot] for slot in (6, 7, 8, 9) if modifiers[slot] != 0
                    )
                    for _ in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('horL2.2', payout, modTrigs))
                else:
                    for i in range(3):
                        for j in range(3):
                            horList[j] = res[i + j + 5]
                        if horList.count(horList[0]) == 3:
                            payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                            modTrigs = tuple(
                                modifiers[slot] for slot in (i + 5, i + 6, i + 7) if modifiers[slot] != 0
                            )
                            for _ in range(1 + retrigger + modTrigs.count(4)):
                                result.append(('hor2.' + str(1 + i), payout, modTrigs))
                            break

        diagShape = [3, 7, 11]
        diagList.clear()
        for i in diagShape:
            diagList.append(res[i])
        if diagList.count(diagList[0]) == 3:
            payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('fwdDiag2', payout, modTrigs))

        diagShape = [1, 7, 13]
        diagList.clear()
        for i in diagShape:
            diagList.append(res[i])
        if diagList.count(diagList[0]) == 3:
            payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('bckDiag2', payout, modTrigs))

        if res.count(res[0]) == 15:
            payout = symbolValues[res[0]] * symbolMult * patternValues['jackpot'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in range(15) if modifiers[slot] != 0)
            for _ in range(1 + retrigger + modTrigs.count(4)):
                result.append(('jackpot', payout, modTrigs))

    if result == []:
        pityCounter += 1

    luck = baseLuck

    for item in postrollItems:
        item.trigger

    def patternOrdering(e):
        return patternOrder[e[0]]

    result.sort(key=patternOrdering)

    state.luck = luck
    state.pityCounter = pityCounter
    state.spinNum = spinNum + 1
    state.OLSSpin = OLSSpin

    return res, modifiers, result
