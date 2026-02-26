#Slots script
import random
import math

#importerer nødvendig data
prerollItems = []
interventions = []
postrollItems = []
symbols = (0, 1, 2, 3, 4, 5, 6) #lemon, cherry, clover, bell, diamond, treasure, seven.
symbolNames = ['lemon', 'cherry', 'clover', 'bell', 'diamond', 'treasure', 'seven']
symbolWeights = [1.3, 1.3, 1, 1, 0.8, 0.8, 0.5] #lemon, cherry, clover, bell, diamond, treasure, seven.
symbolValues = [2, 2, 3, 3, 5, 5, 7]
symbolMult = 1
patternMult = 1
patternValues = {'hor':1, 'vert':1, 'diag':1, 'horL':2, 'horXL':3, 'zig':4, 'zag':4, 'above':7, 'below':7, 'eye':8, 'jackpot':10}
buttonPressed = False
luck = 15
res = []
chance666 = 1.5
is666 = False
result = []
eyeShape = (1, 2, 3, 5, 6, 8, 9, 11, 12, 13)
aboveShape = (2, 6, 8, 10, 11, 12, 13, 14)
belowShape = (0, 1, 2, 3, 4, 6, 8, 12)
eye = False
zigShape = (2, 6, 8, 10, 14)
zagShape = (0, 4, 6, 8, 12)
retrigger = 0
modifiers = []
patternOrder = {'hor1.1':1, 'hor1.2':2, 'hor1.3':3, 'hor2.1':4, 'hor2.2':5, 'hor2.3':6, 'hor3.1':7, 'hor3.2':8, 'hor3.3':9, 'vert1':10,
                'vert2':11, 'vert3':12, 'vert4':13, 'vert5':14, 'bckDiag1':15, 'bckDiag2':16, 'bckDiag3':17, 'fwdDiag1':18, 'fwdDiag2':19,
                'fwdDiag3':20, 'horL1.1':21, 'horL1.2':22, 'horL2.1':23, 'horL2.2':24, 'horL3.1':25, 'horL3.2':26, 'horXL1':27, 'horXL2':28,
                'horXL3':29, 'zig':30, 'zag':31, 'above':32, 'below':33, 'eye':34, 'jackpot':35}


goldChance = 0
affGoldChance = 0
tokenChance = 0
affTokenChance = 0
ticketChance = 0
affTicketChance = 0
repChance = 0
affRepChance = 0
battChance = 0
affBattChance = 0
chainChance = 0
affChainChance = 0

ILSOffset = random.randint(0,4)
debtNum = 1
spinNum = 1
OLSSpin = 0
pityCounter = 0

baseLuck = luck

#pre-roll items aktiveres
for item in prerollItems:
    item.trigger

#Der tjekkes for ILS (initial luck spins)
if debtNum == 1 and spinNum != 1 and (spinNum + ILSOffset + 1) % (4 + math.floor(spinNum / 6)) == 0:
    luck += random.choice((4, 5, 6, 6, 7, 8))

#Der tjekkes for OLS (occasional luck spins)
if spinNum == OLSSpin:
    OLSSpin = spinNum + 3 + debtNum + random.getrandbits(1)
    if spinNum % 7 == 0:
        luck += random.randint(7, 9)
    if spinNum % 3 == 0:
        luck += random.randint(5, 7)
    else:
        luck += random.randint(3, 5)

#Der tjekkes for pity spins
if pityCounter >= 4:
    luck += pityCounter + 1

#Der tjekkes for base luck bonus
if baseLuck < 5:
    if random.getrandbits(1) == 1:
        luck += 1 + random.getrandbits(1)
elif baseLuck < 7:
    if random.getrandbits(2) == 1:
        luck += 1
elif baseLuck == 7:
    if random.randint(0,6) == 6:
        luck += 1

#Luck symbol vælges og indsættes
luckSymbol = random.choices(symbols, weights = symbolWeights)
for i in range(luck):
    res += luckSymbol

#Resten af symbolerne vælges
if len(res) < 15:
    for i in range(15 - len(res)):
        res += random.choices(symbols, weights = symbolWeights)

#Symbolerne fordeles over skærmen
random.shuffle(res)

#modifiers vælges
for slot in res:
    if 100 * random.random() <= goldChance:
        modifiers.append(1)
    elif slot > 3 and 100 * random.random() <= affGoldChance:
        modifiers.append(1)
    elif 100 * random.random() <= tokenChance:
        modifiers.append(2)
    elif slot < 2 and 100 * random.random() <= affTokenChance:
        modifiers.append(2)
    elif 100 * random.random() <= ticketChance:          
        modifiers.append(3)
    elif (slot == 2 or slot == 3) and 100 * random.random() <= affTicketChance:
        modifiers.append(3)
    elif 100 * random.random() <= repChance:
        modifiers.append(4)
    elif slot > 3 and 100 * random.random() <= affRepChance:
        modifiers.append(4)
    elif 100 * random.random() <= battChance:
        modifiers.append(5)
    elif (slot == 2 or slot == 3) and 100 * random.random() <= affBattChance:
        modifiers.append(5)
    elif 100 * random.random() <= chainChance:
        modifiers.append(6)
    elif slot > 3 and 100 * random.random() <= affChainChance:
        modifiers.append(6)
    else:
        modifiers.append(0)

#res = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#modifiers = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]

#666, 66 og 6 chancerne rulles
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
    
#Hvis der ikke er en 666 aktiveres interventions
    for item in interventions:
        item.trigger

#Derefter tjekkes der for patterns
    vertList = [0,0,0]
    horXLList = [0,0,0,0,0]
    horLList = [0,0,0,0]
    horList = [0,0,0]
    diagList = []
    modTrigs = []
    repetition = 0

#Eye listen defineres
    eyeList = []
    for i in eyeShape:
        eyeList.append(res[i])

#Det tjekkes om der er et eye
    if eyeList.count(eyeList[0]) == 10:
        payout = symbolValues[eyeList[0]] * symbolMult * patternValues['eye'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in eyeShape if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('eye', payout, modTrigs))
        eye = True
    else: #Hvis der ikke er et eye tjekkes de 2 verts der indgår i eye
        for i in range(2):
            for j in range(3):
                vertList[j] = res[1 + 5 * j +2 * i]
            if vertList.count(vertList[0]) == 3:
                payout = symbolValues[vertList[0]] * symbolMult * patternValues['vert'] * patternMult
                modTrigs = tuple([modifiers[slot] for slot in (1 + 2 * i, 6 + 2 * i, 11 + 2 * i) if modifiers[slot] != 0])
                for r in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('vert' + str(i * 2), payout, modTrigs))

#De tre andre verts tjekkes lige meget hvad
    for i in range(3):
        for j in range(3):
            vertList[j] = res[5 * j + 2 * i]
        if vertList.count(vertList[0]) == 3:
            payout = symbolValues[vertList[0]] * symbolMult * patternValues['vert'] * patternMult
            modTrigs = tuple([modifiers[slot] for slot in (2 * i, 5 + 2 * i, 10 + 2 * i) if modifiers[slot] != 0])
            for r in range(1 + retrigger + modTrigs.count(4)):
                result.append(('vert' + str(1 + i * 2), payout, modTrigs))
    
#Above listen defineres
    aboveList = []
    for i in aboveShape:
        aboveList.append(res[i])

#Det tjekkes om der er en above
    if aboveList.count(aboveList[0]) == 8:
        payout = symbolValues[aboveList[0]] * symbolMult * patternValues['above'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in aboveShape if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('above', payout, modTrigs))
    else: #Hvis der ikke er et above tjekkes den horXL der indgår i above
        for i in range(5):
            horXLList[i] = res[i]   
        if horXLList.count(horXLList[0]) == 5: # X X X X X
            payout = symbolValues[horXLList[0]] * symbolMult * patternValues['horXL'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in range(5) if modifiers[slot] != 0)
            for r in range(1 + retrigger + modTrigs.count(4)):
                result.append(('horXL1', payout, modTrigs))
        else: #Hvis der ikke er en horXL tjekkes den første af de 2 horL der kan indgå i horXL
            for i in range(4):
                horLList[i] = res[i]
            if horLList.count(horLList[0]) == 4: # X X X X *
                payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in range(4) if modifiers[slot] != 0)
                for r in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('horL1.1', payout, modTrigs))
            else: #Hvis den første horL ikke er der tjekkes der for den anden
                for i in range(4):
                    horLList[i] = res[i + 1]
                if horLList.count(horLList[0]) == 4: # * X X X X
                    payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in (1, 2, 3, 4) if modifiers[slot] != 0)
                    for r in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('horL1.2', payout, modTrigs))  
                else: #hvis der ikke er nogen horL tjekkes der for 2 af de 3 mulige hor
                    for i in range(2):
                        for j in range(3):
                            horList[j] = res[2 * i + j]
                        if horList.count(horList[0]) == 3:
                            payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                            modTrigs = tuple(modifiers[slot] for slot in (2 * i, 2 * i + 1, 2 * i + 2) if modifiers[slot] != 0)
                            for r in range(1 + retrigger + modTrigs.count(4)):
                                result.append(('hor1.' + str(1 + 2 * i), payout))
                            break
#Den sidste hor tjekkes, men her skal det også tjekkes om det overskrives af eye
                    for i in range(3):
                        horList[i] = res[i + 1]
                    if horList.count(horList[0]) == 3 and not eye: # * X X X *
                        payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                        modTrigs = tuple(modifiers[slot] for slot in (1, 2, 3) if modifiers[slot] != 0)
                        for r in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('hor1.2', payout, modTrigs)) 

#Hvis der ikke er et above tjekkes der for en zig
        zigList = []    
        for i in zigShape:
            zigList.append(i)
        if zigList.count(zigList[0]) == 5:
            payout = symbolValues[zigList[0]] * symbolMult * patternValues['zig'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in zigShape if modifiers[slot] != 0)
            for r in range(1 + retrigger + modTrigs.count(4)):
                result.append(('zig', payout, modTrigs))
        else: #Hvis der ikke er en zig tjekkes der for den første af de 2 mulige diags
            diagShape = [2, 6, 10]
            diagList.clear()
            for i in diagShape:
                diagList.append(res[i])
            if diagList.count(diagList[0]) == 3:
                payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                for r in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('fwdDiag1', payout, modTrigs))
            else: #Hvis den første diag ikke er der tjekkes der for den anden
                diagShape = [2, 8, 14]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if diagList.count(diagList[0]) == 3:
                    payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                    for r in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('bckDiag3', payout, modTrigs))

#Below listen defineres
    belowList = []
    for i in belowShape:
        belowList.append(res[i])

#Det tjekkes om der er en below
    if belowList.count(belowList[0]) == 8:
        payout = symbolValues[belowList[0]] * symbolMult * patternValues['below'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in belowShape if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('below', payout, modTrigs))
    else: #Hvis der ikke er et below tjekkes den horXL der indgår i below
        for i in range(5):
            horXLList[i] = res[i + 10]
        if horXLList.count(horXLList[0]) == 5: # X X X X X
            payout = symbolValues[horXLList[0]] * symbolMult * patternValues['horXL'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in (10, 11, 12, 13, 14) if modifiers[slot] != 0)
            for r in range(1 + retrigger + modTrigs.count(4)):
                result.append(('horXL3', payout, modTrigs)) 
        else: #Hvis der ikke er en horXL tjekkes den første af de 2 horL der kan indgå i horXL
            for i in range(4):
                horLList[i] = res[i + 10]
            if horLList.count(horLList[0]) == 4: # X X X X *
                payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in (10, 11, 12, 13) if modifiers[slot] != 0)
                for r in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('horL3.1', payout, modTrigs))
            else: #Hvis den første horL ikke er der tjekkes der for den anden
                for i in range(4):
                    horLList[i] = res[i + 11]
                if horLList.count(horLList[0]) == 4: # * X X X X
                    payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in (11, 12, 13, 14) if modifiers[slot] != 0)
                    for r in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('horL3.2', payout, modTrigs))  
                else: #hvis der ikke er nogen horL tjekkes der for 2 af de 3 mulige hor
                    for i in range(2):
                        for j in range(3):
                            horList[j] = res[2 * i + j + 10]
                        if horList.count(horList[0]) == 3: # X X X * *
                            payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                            modTrigs = tuple(modifiers[slot] for slot in (2 * i + 10, 2 * i + 11, 2 * i + 12) if modifiers[slot] != 0)
                            for r in range(1 + retrigger + modTrigs.count(4)):
                                result.append(('hor3.' + str(1 + 2 * i), payout, modTrigs))
                            break
#Den sidste hor tjekkes, men her skal det også tjekkes om det overskrives af eye
                    for i in range(3):
                        horList[i] = res[i + 11]    
                    if horList.count(horList[0]) == 3 and not eye: # * X X X *
                        payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                        modTrigs = tuple(modifiers[slot] for slot in (11, 12, 13) if modifiers[slot] != 0)
                        for r in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('hor3.2', payout, modTrigs))
#Hvis der ikke er et below tjekkes der for en zag
        zagList = []    
        for i in zagShape:
            zagList.append(i)
        if zagList.count(zagList[0]) == 5:
            payout = symbolValues[zagList[0]] * symbolMult * patternValues['zag'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in zagShape if modifiers[slot] != 0)
            for r in range(1 + retrigger + modTrigs.count(4)):
                result.append(('zag', payout, modTrigs))
        else: #Hvis der ikke er en zag tjekkes der for den første af de 2 mulige diags
            diagShape = [0, 6, 12]
            diagList.clear()
            for i in diagShape:
                diagList.append(res[i])
            if diagList.count(diagList[0]) == 3:
                payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                for r in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('bckDiag1', payout))
            else: #Hvis den første diag ikke er der tjekkes der for den anden
                diagShape = [4, 8, 12]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if diagList.count(diagList[0]) == 3:
                    payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
                    modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
                    for r in range(1 + retrigger + modTrigs.count(4)):
                        result.append(('fwdDiag3', payout, modTrigs))

#Den midterste horXL tjekkes lige meget hvad
    for i in range(5):
        horXLList[i] = res[i + 5]
    if horXLList.count(horXLList[0]) == 5: # X X X X X
        payout = symbolValues[horXLList[0]] * symbolMult * patternValues['horXL'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in (5, 6, 7, 8, 9) if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('horXL2', payout, modTrigs)) 
    else: #Hvis der ikke er en horXL tjekkes den første af de 2 horL der kan indgå i horXL
        for i in range(4):
            horLList[i] = res[i + 5]
        if horLList.count(horLList[0]) == 4: # X X X X *
            payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
            modTrigs = tuple(modifiers[slot] for slot in (5, 6, 7, 8) if modifiers[slot] != 0)
            for r in range(1 + retrigger + modTrigs.count(4)):
                result.append(('horL2.1', payout, modTrigs))
        else: #Hvis den første horL ikke er der tjekkes der for den anden
            for i in range(4):
                horLList[i] = res[i + 6]
            if horLList.count(horLList[0]) == 4: # * X X X X
                payout = symbolValues[horLList[0]] * symbolMult * patternValues['horL'] * patternMult
                modTrigs = tuple(modifiers[slot] for slot in (6, 7, 8, 9) if modifiers[slot] != 0)
                for r in range(1 + retrigger + modTrigs.count(4)):
                    result.append(('horL2.2', payout, modTrigs))  
            else: #hvis der ikke er nogen horL tjekkes der for de 3 mulige hor
                for i in range(3):
                    for j in range(3):
                        horList[j] = res[i + j + 5]
                    if horList.count(horList[0]) == 3:
                        payout = symbolValues[horList[0]] * symbolMult * patternValues['hor'] * patternMult
                        modTrigs = tuple(modifiers[slot] for slot in (i + 5, i + 6, i + 7) if modifiers[slot] != 0)
                        for r in range(1 + retrigger + modTrigs.count(4)):
                            result.append(('hor2.' + str(1 + i), payout, modTrigs))
                        break

#De midterste 2 diags tjekkes lige meget hvad
    diagShape = [3, 7, 11]
    diagList.clear()
    for i in diagShape:
        diagList.append(res[i])
    if diagList.count(diagList[0]) == 3:
        payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('fwdDiag2', payout, modTrigs))

    diagShape = [1, 7, 13]
    diagList.clear()
    for i in diagShape:
        diagList.append(res[i])
    if diagList.count(diagList[0]) == 3:
        payout = symbolValues[diagList[0]] * symbolMult * patternValues['diag'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in diagShape if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('bckDiag2', payout, modTrigs))

#Jackpot tjekkes lige meget hvad
    if res.count(res[0]) == 15:
        payout = symbolValues[res[0]] * symbolMult * patternValues['jackpot'] * patternMult
        modTrigs = tuple(modifiers[slot] for slot in range(15) if modifiers[slot] != 0)
        for r in range(1 + retrigger + modTrigs.count(4)):
            result.append(('jackpot', payout, modTrigs))

for item in postrollItems:
    item.trigger

if result == []:
    pityCounter += 1

luck = baseLuck

def patternOrdering(e):
    return(patternOrder[e[0]])


result.sort(key = patternOrdering)

print(res[:5])
print(res[5:10])
print(res[10:])
print(result)
print(modifiers[:5])
print(modifiers[5:10])
print(modifiers[10:])
