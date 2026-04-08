#item classes

class item:
    pass

class passive(item):
    pass

class lastRound(item):
    pass

class intervention(item):
    pass

class postRoll(item):
    pass

class randomTrigger(item):
    pass

class button(item):
    pass

class roundStart(item):
    pass

class AABatteries(passive):
    weight = 5
    cost = 3

    def trigger():
        affBattChance += 6
    
    def sold():
        affBattChance -= 6


class rotatedHamsa(lastRound):
    weight = 10
    cost = 3

    def trigger():
        luck += 6   

#class painKillers(postRoll):
#    weight = 6.5
#    cost = 3
#
#    def trigger():
#        if len(result) == 1:

class steamLocomotive(postRoll):
    weight = 6.5
    cost = 2

    def trigger():
        if pityCounter >= 3:
            for i in range(7):
                symbolValues[i] += baseSymbolValues[i]

class horseshoe(passive):
    weight = 10
    cost = 3

    def trigger():
        randomTriggerMult *= 2

    def sold():
       randomTriggerMult *= 0.5

class luckyCat(postRoll):
    weight = 10
    cost = 1

    def trigger():
        if len(result) > 2:
            coins += (interest - 1) * depositedAmount

class grandmasPurse(roundStart):
    weight = 10
    cost = 2
    self.startRound = roundNum

    def trigger():
        if roundNum - self.startRound < 5:
            interest -= 0.15 - 0.03 * (roundNum - self.startRound - 1)
            interest += 0.15 - 0.03 * (roundNum - self.startRound)

    def sold():
        interest -= 0.15 - 0.03 * (roundNum - self.startRound)

class stonks(passive):
    weight = 10
    cost = 2

    def trigger():
        interest += 0.05
    
    def sold():
       interest -= 0.05

class megaphone(passive):
    weight = 2
    cost = 7

    def trigger():
        phonecallRep += 1
        itemSpace -= 1
    
    def sold():
        phonecallRep -= 1
        itemSpace += 1

class lostBriefcase(passive):
    weight = 10
    cost = 2
    
    def trigger():
        coins += 0.3 * debtAmount
        #Something to kill itself

class fakeCoin(randomTrigger):
    weight = 10
    cost = 1
    chance = 0.1

    def trigger():
        fakeCoinSpins += 1

class catFood(passive):
    weight = 10
    cost = 4

    def trigger():
        bonusSpins += 2

class toyTrain(postRoll):
    weight = 10
    cost = 1
    self.init = True

    def trigger():
        if pityCounter >= 2:
            if self.init:
                luck += 5
            else:
                luck += 2

class goldenLemon(passive):
    weight = 6.5
    cost = 3

    def trigger():
        lemonGoldChance += 20

    def sold():
        lemonGoldChance -= 20

class goldenCherry(passive):
    weight = 6.5
    cost = 3

    def trigger():
        cherryGoldChance += 20

    def sold():
        cherryGoldChance -= 20

class goldenClover(passive):
    weight = 8
    cost = 3

    def trigger():
        cloverGoldChance += 20

    def sold():
        cloverGoldChance -= 20

class goldenBell(passive):
    weight = 8
    cost = 3

    def trigger():
        bellGoldChance += 20

    def sold():
        bellGoldChance -= 20

class goldenDiamond(passive):
    weight = 10
    cost = 2

    def trigger():
        diamondGoldChance += 25

    def sold():
        diamondGoldChance -= 25

class goldenTreasure(passive):
    weight = 10
    cost = 2

    def trigger():
        treasureGoldChance += 25

    def sold():
        treasureGoldChance -= 25

class goldenSeven(passive):
    weight = 10
    cost = 1

    def trigger():
        sevenGoldChance += 30

    def sold():
        sevenGoldChance -= 30

class bricks(passive):
    weight = 10
    cost = 1

    def trigger():
        lemonTokenChance += 20

    def sold():
        lemonTokenChance -= 20

class wood(passive):
    weight = 10
    cost = 1

    def trigger():
        cherryTokenChance += 20

    def sold():
        cherryTokenChance -= 20

class sheep(passive):
    weight = 9
    cost = 2

    def trigger():
        cloverTokenChance += 15

    def sold():
        cloverTokenChance -= 15

class wheat(passive):
    weight = 9
    cost = 2

    def trigger():
        bellTokenChance += 15

    def sold():
        bellTokenChance -= 15

class stone(passive):
    weight = 8
    cost = 2

    def trigger():
        diamondTokenChance += 10

    def sold():
        diamondTokenChance -= 10

class harbor(passive):
    weight = 10
    cost = 2

    def trigger():
        treasureTokenChance += 10

    def sold():
        treasureTokenChance -= 10

class thief(passive):
    weight = 10
    cost = 2

    def trigger():
        sevenTokenChance += 10

    def sold():
        sevenTokenChance -= 10