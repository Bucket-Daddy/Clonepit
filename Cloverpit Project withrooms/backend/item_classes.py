#item classes
import math

class item:
    pass

class passive(item):
    pass

class lastRound(item):
    pass

class intervention(item):
    pass

class preRoll(item):
    pass

class postRoll(item):
    pass

class randomTrigger(item):
    pass

class button(item):
    pass

class roundEnd(item):
    pass

class deadlineEnd(item):
    pass

class AABatteries(passive):
    weight = 5
    cost = 3

    def trigger(self):
        global affBattChance
        affBattChance += 6
    
    def sold(self):
        global affBattChance
        affBattChance -= 6


class rotatedHamsa(lastRound):
    weight = 10
    cost = 3

    def trigger(self):
        global luck
        luck += 6
    
    def solds(self):
        pass

class painKillers(postRoll):
    weight = 6.5
    cost = 3

    def trigger(self):
        if len(result) == 1:
            pass #temporary pass
            #"If only 1 Pattern shows during a spin, transform its Symbols into the most valued Symbol."

    def sold(self):
        pass


class steamLocomotive(postRoll):
    weight = 6.5
    cost = 2

    def trigger(self):
        if pityCounter >= 3:
            for i in range(7):
                global symbolValues
                symbolValues[i] += baseSymbolValues[i]
    
    def sold(self):
        pass

class horseshoe(passive):
    weight = 10
    cost = 3

    def trigger(self):
        randomTriggerMult *= 2

    def sold(self):
       randomTriggerMult *= 0.5

class luckyCat(postRoll):
    weight = 10
    cost = 1

    def trigger(self):
        if len(result) > 2:
            global coins
            coins += (interest - 1) * depositedAmount
    
    def sold(self):
        pass

class grandmasPurse(roundEnd):
    weight = 10
    cost = 2
    def __init__(self):
        self.startRound = roundNum

    def trigger(self):
        if roundNum - self.startRound < 5:
            global interest
            interest -= 0.15 - 0.03 * (roundNum - self.startRound - 1)
            interest += 0.15 - 0.03 * (roundNum - self.startRound)
        else:
            pass #temporary pass
            #something to kill itself

    def sold(self):
        global interest
        interest -= 0.15 - 0.03 * (roundNum - self.startRound)

class stonks(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global interest
        interest += 0.05
    
    def sold(self):
       global interest
       interest -= 0.05

class megaphone(passive):
    weight = 2
    cost = 7

    def trigger(self):
        global phonecallRep
        global itemSpace
        phonecallRep += 1
        itemSpace -= 1
    
    def sold(self):
        global phonecallRep
        global itemSpace
        phonecallRep -= 1
        itemSpace += 1

class lostBriefcase(passive):
    weight = 10
    cost = 2
    
    def trigger(self):
        global coins
        coins += 0.3 * debtAmount
        #Something to kill itself
    
    def sold(self): #this should never be triggered
        pass


class fakeCoin(randomTrigger):
    weight = 10
    cost = 1
    chance = 10

    def trigger(self):
        global fakeCoinSpins
        fakeCoinSpins += 1
    
    def sold(self):
        pass

class catFood(passive):
    weight = 10
    cost = 4

    def trigger(self):
        global bonusSpins
        bonusSpins += 2
    
    def sold(self):
        global bonusSpins
        bonusSpins -= 2

class toyTrain(postRoll):
    weight = 10
    cost = 1
    def __init__(self):
        self.init = False
        self.extraLuck = 0

    def trigger(self):
        if pityCounter >= 2:
            if self.init:
                global luck
                luck += 5
                self.extraLuck += 5
            else:
                luck += 2
                self.extraLuck += 2
        else:
            global luck
            luck -= self.extraLuck
            self.extraLuck = 0
                
    def sold(self):
        global luck
        luck -= self.extraLuck

class goldenLemon(passive):
    weight = 6.5
    cost = 3

    def trigger(self):
        global lemonGoldChance
        lemonGoldChance += 20

    def sold(self):
        global lemonGoldChance
        lemonGoldChance -= 20

class goldenCherry(passive):
    weight = 6.5
    cost = 3

    def trigger(self):
        global cherryGoldChance
        cherryGoldChance += 20

    def sold(self):
        global cherryGoldChance
        cherryGoldChance -= 20

class goldenClover(passive):
    weight = 8
    cost = 3

    def trigger(self):
        global cloverGoldChance
        cloverGoldChance += 20

    def sold(self):
        global cloverGoldChance
        cloverGoldChance -= 20

class goldenBell(passive):
    weight = 8
    cost = 3

    def trigger(self):
        global bellGoldChance
        bellGoldChance += 20

    def sold(self):
        global bellGoldChance
        bellGoldChance -= 20

class goldenDiamond(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global diamondGoldChance
        diamondGoldChance += 25

    def sold(self):
        global diamondGoldChance
        diamondGoldChance -= 25

class goldenTreasure(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global treasureGoldChance
        treasureGoldChance += 25

    def sold(self):
        global treasureGoldChance
        treasureGoldChance -= 25

class goldenSeven(passive):
    weight = 10
    cost = 1

    def trigger(self):
        global sevenGoldChance
        sevenGoldChance += 30

    def sold(self):
        global sevenGoldChance
        sevenGoldChance -= 30

class bricks(passive):
    weight = 10
    cost = 1

    def trigger(self):
        global lemonTokenChance
        lemonTokenChance += 20

    def sold(self):
        global lemonTokenChance
        lemonTokenChance -= 20

class wood(passive):
    weight = 10
    cost = 1

    def trigger(self):
        global cherryTokenChance
        cherryTokenChance += 20

    def sold(self):
        global cherryTokenChance
        cherryTokenChance -= 20

class sheep(passive):
    weight = 9
    cost = 2

    def trigger(self):
        global cloverTokenChance
        cloverTokenChance += 15

    def sold(self):
        global cloverTokenChance
        cloverTokenChance -= 15

class wheat(passive):
    weight = 9
    cost = 2

    def trigger(self):
        global bellTokenChance
        bellTokenChance += 15

    def sold(self):
        global bellTokenChance
        bellTokenChance -= 15

class stone(passive):
    weight = 8
    cost = 2

    def trigger(self):
        global diamondTokenChance
        diamondTokenChance += 10

    def sold(self):
        global diamondTokenChance
        diamondTokenChance -= 10

class harbor(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global treasureTokenChance
        treasureTokenChance += 10

    def sold(self):
        global treasureTokenChance
        treasureTokenChance -= 10

class thief(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global sevenTokenChance
        sevenTokenChance += 10

    def sold(self):
        global sevenTokenChance
        sevenTokenChance -= 10

class wheelbarrow(passive):
    weight = 6.5
    cost = 4

    def trigger(self):
        global lemonTicketChance
        lemonTicketChance += 20
    
    def sold(self):
        global lemonTicketChance
        lemonTicketChance -= 20

class shoe(passive):
    weight = 6.5
    cost = 4

    def trigger(self):
        global cherryTicketChance
        cherryTicketChance += 20
    
    def sold(self):
        global cherryTicketChance
        cherryTicketChance -= 20

class thimble(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global cloverTicketChance
        cloverTicketChance += 20
    
    def sold(self):
        global cloverTicketChance
        cloverTicketChance -= 20

class iron(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global bellTicketChance
        bellTicketChance += 20
    
    def sold(self):
        global bellTicketChance
        bellTicketChance -= 20

class iron(passive):
    weight = 6.5
    cost = 3

    def trigger(self):
        global diamondTicketChance
        diamondTicketChance += 20
    
    def sold(self):
        global diamondTicketChance
        diamondTicketChance -= 20

class ship(passive):
    weight = 6.5
    cost = 3

    def trigger(self):
        global treasureTicketChance
        treasureTicketChance += 20
    
    def sold(self):
        global treasureTicketChance
        treasureTicketChance -= 20

class tubaHat(passive):
    weight = 6.5
    cost = 3

    def trigger(self):
        global sevenTicketChance
        sevenTicketChance += 20
    
    def sold(self):
        global sevenTicketChance
        sevenTicketChance -= 20

class aceOfHearts(postRoll):
    weight = 10
    cost = 3

    def trigger(self):
        if len(result) >= 3:
            global symbolValues
            symbolValues[0] += baseSymbolValues[0]
            symbolValues[1] += baseSymbolValues[1]
    
    def sold(self):
        pass

class aceOfDiamonds(postRoll):
    weight = 10
    cost = 3

    def trigger(self):
        for i in result:
            if len[patterns[i[0]]]:
                global symbolValues
                symbolValues[4] += baseSymbolValues[4]
                symbolValues[5] += baseSymbolValues[5]
                break
    
    def sold(self):
        pass

class d6(roundEnd):
    weight = 6.5
    cost = 2

    def trigger(self):
        pass #temporary pass
        #call the shop restock function
    
    def sold(self):
        pass

class d20(roundEnd):
    weight = 6.5
    cost = 5

    def trigger(self):
        pass #temporary pass
        #something to randomise the shelves, maybe reusing the shop restock function

    def sold(self):
        pass

class crystalSphere(passive):
    weight = 8
    cost = 3

    def trigger(self):
        global affChainChance
        affChainChance += 12
    
    def sold(self):
        global affChainChance
        affChainChance -= 12

class clicker(passive):
    weight = 8
    cost = 3

    def trigger(self):
        global affRepChance
        affRepChance += 15
    
    def sold(self):
        global affRepChance
        affRepChance -= 15

class ritualBell(postRoll):
    weight = 10
    cost = 1

    def trigger(self):
        if is666:
            global freeRestocks
            freeRestocks += 3
    
    def sold(self):
        pass

class necronomicon(passive):
    weight = 9
    cost = 3

    def trigger(self):
        global patternMult
        patternMult += 2
        global chance666
        chance666 += 3
    
    def sold(self):
        global patternMult
        patternMult -= 2
        global chance666
        chance666 -= 3

class redPepper(randomTrigger):
    weight = 10
    cost = 1
    chance = 20

    def __init__(self):
        self.activations = 0

    def trigger(self):
        global tempLuck
        tempLuck += 5
        self.activations += 1
        if self.activation == 12:
            pass #temporary pass
            #something to kill itself

    def sold(self):
        pass

class cloverPot(deadlineEnd):
    weight = 8
    cost = 2

    def trigger(self):
        global tickets
        tickets += math.floor(tickets/debtNum)
    
    def sold(self):
        pass

class cloverPet(preRoll):
    weight = 6.5
    cost = 1

    def __init__(self):
        self.extraMult = 0

    def trigger(self):
        global symbolMult
        symbolmult -= self.extraMult
        self.extraMult = math.floor(tickets/5)
        symbolMult += self.extraMult
    
    def sold(self):
        global symbolMult
        symbolmult -= self.extraMult
        

class cigarettes(passive):
    weight = 10
    cost = cigaretteCost

    def trigger(self):
        global cigaretteCost
        cigaretteCost += 1
        for i in range(7):
            global symbolValues
            symbolValues[i] += baseSymbolValues[i]
            #call the shop restock function
            #something to kill itself

    def sold(self): #this should never be triggered
        pass

class cardboardHouse(passive):
    weight = 10
    cost = 2

    def trigger(self):
        global cardboardInit
        cardboardInit = False
        global itemSpace
        itemSpace += 1
        #something to kill itself
    
    def sold(self): #this should never be triggered
        pass

class propertyCertificate(passive):
    weight = 8
    cost = 2

    def trigger(self):
        global itemSpace
        itemSpace += 2
        #something to kill itself
    
    def sold(self): #this should never be triggered
        pass

class crowbar(passive):
    weight = 8
    cost = 2

    def trigger(self):
        global freeRestocks
        freeRestocks += 3
        #something to kill itself

    def sold(self): #this should never be triggered
        pass

class consolationPrize(randomTrigger):
    weight = 10
    cost = 2
    chance = 25

    def trigger(self):
        if pityCounter > 0:
            for i in range(7):
                global symbolValues
                symbolValues[i] += baseSymbolValues[i]
    
    def sold(self):
        pass

