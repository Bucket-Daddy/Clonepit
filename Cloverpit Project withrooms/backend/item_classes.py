#item classes
import math
import pygame
import random as rand
import config.game_config as config
from backend.shop_restock import shopRestock
import backend.shop_restock as shopBackend

config.unlockedItems = []
itemWeights = []


def itemInit():    

    class item:
        pass

    class passive(item):
        pass

    class lastSpin(item):
        pass

    class intervention(item):
        pass

    class preRoll(item):
        pass

    class postRoll(item):
        pass

    class random(item):
        pass

    class button(item):
        pass

    class roundEnd(item):
        pass

    class deadlineEnd(item):
        pass

    class AABatteries(passive):
        name = 'AA Batteries'
        description = '+6% Chance for the Symbols Clover and Bell to have the Battery Modifier.'
        sprite = pygame.image.load('assets/AA_Batteries.png')
        weight = 50
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.affBattChance += 6
    
        def sold(self):
            config.affBattChance -= 6

    config.unlockedItems.append(AABatteries)
    itemWeights.append(AABatteries.weight)

    class rotatedHamsa(lastSpin):
        name = 'Rotated Hamsa'
        description = 'Grants \033[92mLuck\033[0m+7 for the last spin of a Round.'
        sprite = pygame.image.load('assets/Rotated_Hamsa.png')
        weight = 100
        cost = 3
        space = 1
        type = 'lastSpin'

        def trigger(self):
            config.luck += 6
    
        def sold(self):
            pass

    config.unlockedItems.append(rotatedHamsa)
    itemWeights.append(rotatedHamsa.weight)

    #class painKillers(postRoll):
        #name = ''
        #description = ''
        #sprite = pygame.image.load('assets/.png')
        #weight = 65
        #cost = 3
        #space = 1
        #type = 'postRoll'

        #def trigger(self):
            #if len(result) == 1:
                #pass #temporary pass
                #"If only 1 Pattern shows during a spin, transform its Symbols into the most valued Symbol."

        #def sold(self):
            #pass

    class steamLocomotive(postRoll):
        name = 'Steam Locomotive'
        description = 'Increase all Symbols by their base value permanently if the previous 3 spins had no reward.'
        sprite = pygame.image.load('assets/Steam_Locomotive.png')
        weight = 65
        cost = 2
        space = 1
        type = 'postRoll'

        def trigger(self, result, pityCounter):
            if pityCounter >= 3:
                for i in range(7):
                    config.symbolValues[i] += config.baseSymbolValues[i]
    
        def sold(self):
            pass

    config.unlockedItems.append(steamLocomotive)
    itemWeights.append(steamLocomotive.weight)

    class horseshoe(passive):
        name = 'Horseshoe'
        description = 'Charms with \"\033[93mTriggers Randomly\033[0m\" activate double more often.'
        sprite = pygame.image.load('assets/Horseshoe.png')
        weight = 100
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.randomTriggerMult *= 2

        def sold(self):
            config.randomTriggerMult *= 0.5

    config.unlockedItems.append(horseshoe)
    itemWeights.append(horseshoe.weight)

    class luckyCat(postRoll):
        name = 'Lucky Cat'
        description = 'Whenever 3+ Patterns trigger during a spin, you earn money equal to your current Interest.'
        sprite = pygame.image.load('assets/Lucky_Cat.png')
        weight = 100
        cost = 1
        space = 1
        type = 'postRoll'

        def trigger(self, result, pityCounter):
            if len(result) > 2:
                config.coins += (config.interest - 1) * config.depositedAmount
    
        def sold(self):
            pass

    config.unlockedItems.append(luckyCat)
    itemWeights.append(luckyCat.weight)

    class grandmasPurse(roundEnd):
        name = ' Grandma\'s Purse'
        description = 'Interest increases by +15%, but decreases by 3% after every Round. Discard this Charm when its bonus is 0.'
        sprite = pygame.image.load('assets/Grandmas_Purse.png')
        weight = 100
        cost = 2
        space = 1
        type = 'roundEnd'

        def __init__(self):
            self.startRound = config.roundNum

        def trigger(self):
            if config.roundNum - self.startRound < 5:
                config.interest -= 0.15 - 0.03 * (config.roundNum - self.startRound - 1)
                config.interest += 0.15 - 0.03 * (config.roundNum - self.startRound)
            else:
                config.shelfItems.pop(-1)
                

        def sold(self):
            config.interest -= 0.15 - 0.03 * (config.roundNum - self.startRound)

    config.unlockedItems.append(grandmasPurse)
    itemWeights.append(grandmasPurse.weight)

    class stonks(passive):
        name = 'Stonks'
        description = '+5% to your Interest.'
        sprite = pygame.image.load('assets/Stonks.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.interest += 0.05
    
        def sold(self):
            config.interest -= 0.05

    config.unlockedItems.append(stonks)
    itemWeights.append(stonks.weight)

    class megaphone(passive):
        name = 'Megaphone'
        description = 'All abilities that you pick at the telephone trigger one more time. -1 to Charms\' space.'
        sprite = pygame.image.load('assets/Megaphone.png')
        weight = 20
        cost = 7
        space = 2
        type = 'passive'

        def trigger(self):
            config.phonecallRep += 1
            config.shelfSpace -= 1
    
        def sold(self):
            config.phonecallRep -= 1
            config.shelfSpace += 1

    config.unlockedItems.append(megaphone)
    itemWeights.append(megaphone.weight)

    class lostBriefcase(passive):
        name = 'Lost Briefcase'
        description = '\033[93mDoesn\'t take space\033[0m. Immediately earn 30% of the debt amount.'
        sprite = pygame.image.load('assets/Lost_Briefcase.png')
        weight = 100
        cost = 2
        space = 0
        type = 'passive'
    
        def trigger(self):
            config.coins += round(0.3 * config.debtAmount)
            config.shelfItems.pop(-1)
    
        def sold(self): #this should never be triggered
            pass

    config.unlockedItems.append(lostBriefcase)
    itemWeights.append(lostBriefcase.weight)

    class fakeCoin(random):
        name = 'Fake Coin'
        description = '\033[93mTriggers Randomly\033[0m (10%): +1 extra spin, then \033[92mLuck+4\033[0m for that spin.'
        sprite = pygame.image.load('assets/Fake_coin.png')
        weight = 100
        cost = 1
        chance = 10
        space = 1
        type = 'random'

        def trigger(self, result, pityCounter):
            config.fakeCoinSpins += 1
    
        def sold(self):
            pass

    config.unlockedItems.append(fakeCoin)
    itemWeights.append(fakeCoin.weight)

    class catFood(passive):
        name = 'Cat Food'
        description = '+2 spins per Round.'
        sprite = pygame.image.load('assets/Cat_Food.png')
        weight = 100
        cost = 4
        space = 1
        type = 'passive'

        def trigger(self):
            config.bonusSpins += 2
    
        def sold(self):
            config.bonusSpins -= 2

    config.unlockedItems.append(catFood)
    itemWeights.append(catFood.weight)

    class toyTrain(postRoll):
        name = 'Toy Train'
        description = '\033[92mLuck\033[0m+5 on next spin if the previous 2 had no reward. +2 extra \033[92mLuck\033[0m for every in sequence activation after the first one.'
        sprite = pygame.image.load('assets/Toy_Train.png')
        weight = 100
        cost = 1
        space = 1
        type = 'postRoll'

        def __init__(self):
            self.init = False
            self.extraLuck = 0

        def trigger(self, result, pityCounter):
            if pityCounter >= 2:
                if self.init:
                    config.luck += 5
                    self.extraLuck += 5
                else:
                    config.luck += 2
                    self.extraLuck += 2
            else:
                config.luck -= self.extraLuck
                self.extraLuck = 0
                
        def sold(self):
            config.luck -= self.extraLuck

    config.unlockedItems.append(toyTrain)
    itemWeights.append(toyTrain.weight)

    class goldenLemon(passive):
        name = 'Golden Lemon'
        description = '+20% Chance for Lemons to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Lemon.png')
        weight = 65
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.lemonGoldChance += 20

        def sold(self):
            config.lemonGoldChance -= 20

    config.unlockedItems.append(goldenLemon)
    itemWeights.append(goldenLemon.weight)

    class goldenCherry(passive):
        name = 'Golden Cherry'
        description = '+20% Chance for Cherries to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Cherry.png')
        weight = 65
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.cherryGoldChance += 20

        def sold(self):
            config.cherryGoldChance -= 20

    config.unlockedItems.append(goldenCherry)
    itemWeights.append(goldenCherry.weight)

    class goldenClover(passive):
        name = 'Golden Clover'
        description = '+20% Chance for Clovers to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Clover.png')
        weight = 80
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.cloverGoldChance += 20

        def sold(self):
            config.cloverGoldChance -= 20

    config.unlockedItems.append(goldenClover)
    itemWeights.append(goldenClover.weight)

    class goldenBell(passive):
        name = 'Golden Bell'
        description = '+20% Chance for Bells to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Bell.png')
        weight = 80
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.bellGoldChance += 20

        def sold(self):
            config.bellGoldChance -= 20

    config.unlockedItems.append(goldenBell)
    itemWeights.append(goldenBell.weight)

    class goldenDiamond(passive):
        name = 'Golden Diamond'
        description = '+25% Chance for Diamonds to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Diamond.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.diamondGoldChance += 25

        def sold(self):
            config.diamondGoldChance -= 25

    config.unlockedItems.append(goldenDiamond)
    itemWeights.append(goldenDiamond.weight)

    class goldenTreasure(passive):
        name = 'Golden Treasure'
        description = '+25% Chance for Treasures to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Treasure.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.treasureGoldChance += 25

        def sold(self):
            config.treasureGoldChance -= 25

    config.unlockedItems.append(goldenTreasure)
    itemWeights.append(goldenTreasure.weight)

    class goldenSeven(passive):
        name = 'Golden Seven'
        description = '+30% Chance for Sevens to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Seven.png')
        weight = 100
        cost = 1
        space = 1
        type = 'passive'

        def trigger(self):
            config.sevenGoldChance += 30

        def sold(self):
            config.sevenGoldChance -= 30

    config.unlockedItems.append(goldenSeven)
    itemWeights.append(goldenSeven.weight)

    class bricks(passive):
        name = 'Bricks'
        description = '+20% Chance for any Lemon to have the Token Modifier.'
        sprite = pygame.image.load('assets/Bricks.png')
        weight = 100
        cost = 1
        space = 1
        type = 'passive'

        def trigger(self):
            config.lemonTokenChance += 20

        def sold(self):
            config.lemonTokenChance -= 20

    config.unlockedItems.append(bricks)
    itemWeights.append(bricks.weight)

    class wood(passive):
        name = 'Wood'
        description = '+20% Chance for any Cherry to have the Token Modifier.'
        sprite = pygame.image.load('assets/Wood.png')
        weight = 100
        cost = 1
        space = 1
        type = 'passive'

        def trigger(self):
            config.cherryTokenChance += 20

        def sold(self):
            config.cherryTokenChance -= 20

    config.unlockedItems.append(wood)
    itemWeights.append(wood.weight)

    class sheep(passive):
        name = 'Sheep'
        description = '+15% Chance for any Clover to have the Token Modifier.'
        sprite = pygame.image.load('assets/Sheep.png')
        weight = 90
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.cloverTokenChance += 15

        def sold(self):
            config.cloverTokenChance -= 15

    config.unlockedItems.append(sheep)
    itemWeights.append(sheep.weight)

    class wheat(passive):
        name = 'Wheat'
        description = '+15% Chance for any Bell to have the Token Modifier.'
        sprite = pygame.image.load('assets/Wheat.png')
        weight = 90
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.bellTokenChance += 15

        def sold(self):
            config.bellTokenChance -= 15

    config.unlockedItems.append(wheat)
    itemWeights.append(wheat.weight)

    class stone(passive):
        name = 'Stone'
        description = '+10% Chance for any Diamond to have the Token Modifier.'
        sprite = pygame.image.load('assets/Stone.png')
        weight = 80
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.diamondTokenChance += 10

        def sold(self):
            config.diamondTokenChance -= 10

    config.unlockedItems.append(stone)
    itemWeights.append(stone.weight)

    class harbor(passive):
        name = 'Harbor'
        description = '+10% Chance for any Treasure to have the Token Modifier.'
        sprite = pygame.image.load('assets/Harbor.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.treasureTokenChance += 10

        def sold(self):
            config.treasureTokenChance -= 10

    config.unlockedItems.append(harbor)
    itemWeights.append(harbor.weight)

    class thief(passive):
        name = 'Thief'
        description = '+10% Chance for any Seven to have the Token Modifier.'
        sprite = pygame.image.load('assets/Thief.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.sevenTokenChance += 10

        def sold(self):
            config.sevenTokenChance -= 10

    config.unlockedItems.append(thief)
    itemWeights.append(thief.weight)

    class wheelbarrow(passive):
        name = 'Wheelbarrow'
        description = '+20% Chance for any Lemon to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Wheelbarrow.png')
        weight = 65
        cost = 4
        space = 1
        type = 'passive'

        def trigger(self):
            config.lemonTicketChance += 20
    
        def sold(self):
            config.lemonTicketChance -= 20

    config.unlockedItems.append(wheelbarrow)
    itemWeights.append(wheelbarrow.weight)

    class shoe(passive):
        name = 'Shoe'
        description = '+20% Chance for any Cherry to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Shoe.png')
        weight = 65
        cost = 4
        space = 1
        type = 'passive'

        def trigger(self):
            config.cherryTicketChance += 20
    
        def sold(self):
            config.cherryTicketChance -= 20

    config.unlockedItems.append(shoe)
    itemWeights.append(shoe.weight)

    class thimble(passive):
        name = 'Thimble'
        description = '+20% Chance for any Clover to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Thimble.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.cloverTicketChance += 20
    
        def sold(self):
            config.cloverTicketChance -= 20

    config.unlockedItems.append(thimble)
    itemWeights.append(thimble.weight)

    class iron(passive):
        name = 'Iron'
        description = '+20% Chance for any Bell to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Iron.png')
        weight = 100
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.bellTicketChance += 20
    
        def sold(self):
            config.bellTicketChance -= 20

    config.unlockedItems.append(iron)
    itemWeights.append(iron.weight)

    class car(passive):
        name = 'Car'
        description = '+20% Chance for any Diamond to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Car.png')
        weight = 65
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.diamondTicketChance += 20
    
        def sold(self):
            config.diamondTicketChance -= 20

    config.unlockedItems.append(car)
    itemWeights.append(car.weight)

    class ship(passive):
        name = 'Ship'
        description = '+20% Chance for Treasures to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Ship.png')
        weight = 65
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.treasureTicketChance += 20
    
        def sold(self):
            config.treasureTicketChance -= 20

    config.unlockedItems.append(ship)
    itemWeights.append(ship.weight)

    class tubaHat(passive):
        name = 'Tuba Hat'
        description = '+20% Chance for any Seven to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Tuba_Hat.png')
        weight = 65
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.sevenTicketChance += 20
    
        def sold(self):
            config.sevenTicketChance -= 20

    config.unlockedItems.append(tubaHat)
    itemWeights.append(tubaHat.weight)

    class aceOfHearts(postRoll):
        name = 'Ace of Hearts'
        description = 'Whenever 3+ Patterns trigger during a spin, raise all fruits by their base value permanently.'
        sprite = pygame.image.load('assets/Ace_of_Hearts.png')
        weight = 100
        cost = 3
        space = 1
        type = 'postRoll'

        def trigger(self, result, pityCounter):
            if len(result) >= 3:
                config.symbolValues[0] += config.baseSymbolValues[0]
                config.symbolValues[1] += config.baseSymbolValues[1]
    
        def sold(self):
            pass

    config.unlockedItems.append(aceOfHearts)
    itemWeights.append(aceOfHearts.weight)

    class aceOfDiamonds(postRoll):
        name = 'Ace of Diamonds'
        description = 'Every time you score at least 1 Pattern of 4+ Symbols, raise Diamonds and Treasures by their base value permanently.'
        sprite = pygame.image.load('assets/Ace_of_Diamonds.png')
        weight = 100
        cost = 3
        space = 1
        type = 'postRoll'

        def trigger(self, result, pityCounter):
            for i in result:
                if len(config.patterns[i[0]]) > 3:
                    config.symbolValues[4] += config.baseSymbolValues[4]
                    config.symbolValues[5] += config.baseSymbolValues[5]
                    break
    
        def sold(self):
            pass

    config.unlockedItems.append(aceOfDiamonds)
    itemWeights.append(aceOfDiamonds.weight)

    class d6(roundEnd):
        name = 'D6'
        description = 'Restock the store for free at the end of every Round.'
        sprite = pygame.image.load('assets/D6.png')
        weight = 65
        cost = 2
        space = 1
        type = 'roundEnd'

        def trigger(self):
            shopRestock(config.unlockedItems, itemWeights)
    
        def sold(self):
            pass

    config.unlockedItems.append(d6)
    itemWeights.append(d6.weight)

    class d20(roundEnd):
        name = 'D20'
        description = 'At the end of each Round, replace all lucky Charms inside all drawers with new random ones.'
        sprite = pygame.image.load('assets/D20.png')
        weight = 65
        cost = 5
        space = 1
        type = 'roundEnd'

        def trigger(self):
            pass #temporary pass
            #something to randomise the shelves, maybe reusing the shop restock function

        def sold(self):
            pass

    config.unlockedItems.append(d20)
    itemWeights.append(d20.weight)

    class crystalSphere(passive):
        name = 'Crystal Sphere'
        description = '+12% Chance for the Symbols Diamond, Treasure, and Seven to have the Chain Modifier.'
        sprite = pygame.image.load('assets/Crystal_Sphere.png')
        weight = 80
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.affChainChance += 12
    
        def sold(self):
            config.affChainChance -= 12

    config.unlockedItems.append(crystalSphere)
    itemWeights.append(crystalSphere.weight)

    class clicker(passive):
        name = 'Clicker'
        description = '+15% chance for every fruit to have the Repetition Modifier.'
        sprite = pygame.image.load('assets/Clicker.png')
        weight = 80
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.affRepChance += 15
    
        def sold(self):
            config.affRepChance -= 15

    config.unlockedItems.append(clicker)
    itemWeights.append(clicker.weight)

    class ritualBell(postRoll):
        name = 'Ritual Bell'
        description = 'Whenever you see a 666, gain 3 \033[32mFree Restocks\033[0m.'
        sprite = pygame.image.load('assets/Ritual_Bell.png')
        weight = 100
        cost = 1
        space = 1
        type = 'postRoll'

        def trigger(self, result, pityCounter):
            if config.is666:
                config.freeRestocks += 3
    
        def sold(self):
            pass

    config.unlockedItems.append(ritualBell)
    itemWeights.append(ritualBell.weight)

    class necronomicon(passive):
        name = 'Necronomicon'
        description = '\033[33mPatterns Multiplier\033[0m +2. +3% chance of seeing a 666.'
        sprite = pygame.image.load('assets/Necronomicon.png')
        weight = 90
        cost = 3
        space = 1
        type = 'passive'

        def trigger(self):
            config.patternMult += 2
            config.chance666 += 3
    
        def sold(self):
            config.patternMult -= 2
            config.chance666 -= 3

    config.unlockedItems.append(necronomicon)
    itemWeights.append(necronomicon.weight)

    class redPepper(random):
        name = 'Red Pepper'
        description = '\033[93mTriggers Randomly\033[0m (20%): \033[92mLuck\033[0m+5 for the next spin. Discard after 12 activations.'
        sprite = pygame.image.load('assets/Red_Pepper.png')
        weight = 100
        cost = 1
        chance = 20
        space = 1
        type = 'random'

        def __init__(self):
            self.activations = 0

        def trigger(self, result, pityCounter):
            config.tempLuck += 5
            self.activations += 1
            if self.activations == 12:
                config.shelfItems.pop(-1)

        def sold(self):
            pass

    config.unlockedItems.append(redPepper)
    itemWeights.append(redPepper.weight)

    class cloverPot(deadlineEnd):
        name = 'CloverPot'
        description = 'At the end of every Deadline, earn 1 Ticket for every X Ticket you own, where X is the current Deadline.'
        sprite = pygame.image.load('assets/CloverPot.png')
        weight = 80
        cost = 2
        space = 1
        type = 'deadlineEnd'

        def trigger(self):
            config.tickets += math.floor(config.tickets/config.debtNum)
    
        def sold(self):
            pass

    config.unlockedItems.append(cloverPot)
    itemWeights.append(cloverPot.weight)

    class cloverPet(preRoll):
        name = 'CloverPet'
        description = '\033[93mSymbols Multiplier\033[0m +1 for every 5 Ticket you own.'
        sprite = pygame.image.load('assets/CloverPet.png')
        weight = 65
        cost = 1
        space = 1
        type = 'preRoll'

        def __init__(self):
            self.extraMult = 0

        def trigger(self):
            config.symbolMult -= self.extraMult
            self.extraMult = math.floor(config.tickets/5)
            config.symbolMult += self.extraMult
    
        def sold(self):
            config.symbolMult -= self.extraMult

    config.unlockedItems.append(cloverPet)
    itemWeights.append(cloverPet.weight)        

    class cigarettes(passive):
        name = 'Cigarettes'
        description = '\033[93mDoesn\'t take space\033[0m. Increase all Symbols by their base value, permanently. Then immediately restock the store together with this charm. The price of this charm increases by 1 ticket every time until Deadline end.'
        sprite = pygame.image.load('assets/Cigarettes.png')
        weight = 100
        cost = 1
        space = 0
        type = 'passive'

        def trigger(self):
            config.unlockedItems[44].cost += 1
            for i in range(7):
                config.symbolValues[i] += config.baseSymbolValues[i]
                shopRestock(config.unlockedItems, itemWeights)
            config.shelfItems.pop(-1)
            shopBackend.shopItems[rand.randint(0, 3)] = cigarettes()

        def sold(self): #this should never be triggered
            pass

    config.unlockedItems.append(cigarettes)
    itemWeights.append(cigarettes.weight)

    class cardboardHouse(passive):
        name = 'Cardboard House'
        description = '\033[93mDoesn\'t take space\033[0m. Makes space for 1 more Lucky Charm! This Charm will not show up again after usage.'
        sprite = pygame.image.load('assets/Cardboard_House.png')
        weight = 100
        cost = 2
        space = 0
        type = 'passive'

        def trigger(self):
            config.cardboardInit = False
            config.shelfSpace += 1
            config.shelfItems.pop(-1)
    
        def sold(self): #this should never be triggered
            pass

    config.unlockedItems.append(cardboardHouse)
    itemWeights.append(cardboardHouse.weight)

    class propertyCertificate(passive):
        name = 'Property Certificate'
        description = 'Makes space for 2 more Lucky Charms.'
        sprite = pygame.image.load('assets/Property_Certificate.png')
        weight = 80
        cost = 2
        space = 1
        type = 'passive'

        def trigger(self):
            config.shelfSpace += 2
    
        def sold(self):
            config.shelfSpace -= 2

    config.unlockedItems.append(propertyCertificate)
    itemWeights.append(propertyCertificate.weight)

    class crowbar(passive):
        name = 'Crowbar'
        description = '\033[93mDoesn\'t take space\033[0m. +3 \033[32mFree Restocks\033[0m.'
        sprite = pygame.image.load('assets/Crowbar.png')
        weight = 80
        cost = 2
        space = 0
        type = 'passive'

        def trigger(self):
            config.freeRestocks += 3
            config.shelfItems.pop(-1)

        def sold(self): #this should never be triggered
            pass

    config.unlockedItems.append(crowbar)
    itemWeights.append(crowbar.weight)

    class consolationPrize(random):
        name = 'Consolation Prize'
        description = '\033[93mTriggers Randomly\033[0m (25%): This Charm triggers only if the current spin has no Patterns. Increase all Symbols by their base value, permanently.'
        sprite = pygame.image.load('assets/Consolation_Prize.png')
        weight = 100
        cost = 2
        chance = 25
        space = 1
        type = 'random'

        def trigger(self, result, pityCounter):
            if pityCounter > 0:
                for i in range(7):
                    config.symbolValues[i] += config.baseSymbolValues[i]
    
        def sold(self):
            pass

    config.unlockedItems.append(consolationPrize)
    itemWeights.append(consolationPrize.weight)

    class lemonPicture(button):
        name = 'Lemon Picture'
        description = 'Triggered by the red button. Lemons manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Lemon_Picture.png')
        weight = 100
        cost = 2
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[0] += 2
            config.tempSymbolWeights[0] += 2
        
        def sold(self):
            config.symbolWeights[0] -= 2
            config.tempSymbolWeights[0] -= 2

    config.unlockedItems.append(lemonPicture)
    itemWeights.append(lemonPicture.weight)

    class cherryPicture(button):
        name = 'Cherry Picture'
        description = 'Triggered by the red button. Cherries manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Cherry_Picture.png')
        weight = 100
        cost = 2
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[1] += 2
            config.tempSymbolWeights[1] += 2
        
        def sold(self):
            config.symbolWeights[1] -= 2
            config.tempSymbolWeights[1] -= 2

    config.unlockedItems.append(cherryPicture)
    itemWeights.append(cherryPicture.weight)

    class cloverPicture(button):
        name = 'Clover Picture'
        description = 'Triggered by the red button. Clovers manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Clover_Picture.png')
        weight = 90
        cost = 3
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[2] += 2
            config.tempSymbolWeights[2] += 2
        
        def sold(self):
            config.symbolWeights[2] -= 2
            config.tempSymbolWeights[2] -= 2

    config.unlockedItems.append(cloverPicture)
    itemWeights.append(cloverPicture.weight)

    class bellPicture(button):
        name = 'Bell Picture'
        description = 'Triggered by the red button. Bells manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Bell_Picture.png')
        weight = 90
        cost = 3
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[3] += 2
            config.tempSymbolWeights[3] += 2
        
        def sold(self):
            config.symbolWeights[3] -= 2
            config.tempSymbolWeights[3] -= 2

    config.unlockedItems.append(bellPicture)
    itemWeights.append(bellPicture.weight)

    class diamondPicture(button):
        name = 'Diamond Picture'
        description = 'Triggered by the red button. Diamonds manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Diamond_Picture.png')
        weight = 80
        cost = 4
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[4] += 2
            config.tempSymbolWeights[4] += 2
        
        def sold(self):
            config.symbolWeights[4] -= 2
            config.tempSymbolWeights[4] -= 2

    config.unlockedItems.append(diamondPicture)
    itemWeights.append(diamondPicture.weight)

    class treasurePicture(button):
        name = 'Treasure Picture'
        description = 'Triggered by the red button. Treasures manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Treasure_Picture.png')
        weight = 80
        cost = 4
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[5] += 2
            config.tempSymbolWeights[5] += 2
        
        def sold(self):
            config.symbolWeights[5] -= 2
            config.tempSymbolWeights[5] -= 2

    config.unlockedItems.append(treasurePicture)
    itemWeights.append(treasurePicture.weight)

    class sevenPicture(button):
        name = 'Seven Picture'
        description = 'Triggered by the red button. Sevens manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Seven_Picture.png')
        weight = 65
        cost = 4
        charges = 4
        chargeSlots = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            config.symbolWeights[6] += 2
            config.tempSymbolWeights[6] += 2
        
        def sold(self):
            config.symbolWeights[6] -= 2
            config.tempSymbolWeights[6] -= 2
    
    config.unlockedItems.append(sevenPicture)
    itemWeights.append(sevenPicture.weight)    

    class carBattery(passive):
        name = 'Car Battery'
        description = '\033[93mDoesn\'t take space\033[0m. Immediately restore all charges on all equipped lucky charms triggerable by the red button.'
        sprite = pygame.image.load('assets/Car_Battery.png')
        weight = 10
        cost = 2
        space = 0
        type = 'passive'

        def trigger(self):
            for item in config.shelfItems:
                if item.type == 'button' and item.charges < item.chargeSlots:
                    item.charges = item.chargeSlots
            config.shelfItems.pop(-1)
            
        def sold(self): #Burde aldrig blive aktiveret
            pass   
    
    config.unlockedItems.append(carBattery)
    itemWeights.append(sevenPicture.weight)

    return config.unlockedItems, itemWeights
