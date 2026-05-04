#item classes
import math
import pygame
import config.game_config as game_config
from backend.shop_restock import shopRestock

game_config.unlockedItems = []
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
            game_config.affBattChance += 6
    
        def sold(self):
            game_config.affBattChance -= 6

    game_config.unlockedItems.append(AABatteries)
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
            game_config.luck += 6
    
        def solds(self):
            pass

    game_config.unlockedItems.append(rotatedHamsa)
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
                    game_config.symbolValues[i] += game_config.baseSymbolValues[i]
    
        def sold(self):
            pass

    game_config.unlockedItems.append(steamLocomotive)
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
            game_config.randomTriggerMult *= 2

        def sold(self):
            game_config.randomTriggerMult *= 0.5

    game_config.unlockedItems.append(horseshoe)
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
                game_config.coins += (game_config.interest - 1) * game_config.depositedAmount
    
        def sold(self):
            pass

    game_config.unlockedItems.append(luckyCat)
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
            self.startRound = game_config.roundNum

        def trigger(self):
            if game_config.roundNum - self.startRound < 5:
                game_config.interest -= 0.15 - 0.03 * (game_config.roundNum - self.startRound - 1)
                game_config.interest += 0.15 - 0.03 * (game_config.roundNum - self.startRound)
            else:
                pass #temporary pass
                #something to kill itself

        def sold(self):
            game_config.interest -= 0.15 - 0.03 * (game_config.roundNum - self.startRound)

    game_config.unlockedItems.append(grandmasPurse)
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
            game_config.interest += 0.05
    
        def sold(self):
            game_config.interest -= 0.05

    game_config.unlockedItems.append(stonks)
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
            game_config.phonecallRep += 1
            game_config.itemSpace -= 1
    
        def sold(self):
            game_config.phonecallRep -= 1
            game_config.itemSpace += 1

    game_config.unlockedItems.append(megaphone)
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
            game_config.coins += 0.3 * game_config.debtAmount
            #Something to kill itself
    
        def sold(self): #this should never be triggered
            pass

    game_config.unlockedItems.append(lostBriefcase)
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
            game_config.fakeCoinSpins += 1
    
        def sold(self):
            pass

    game_config.unlockedItems.append(fakeCoin)
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
            game_config.bonusSpins += 2
    
        def sold(self):
            game_config.bonusSpins -= 2

    game_config.unlockedItems.append(catFood)
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
                    game_config.luck += 5
                    self.extraLuck += 5
                else:
                    game_config.luck += 2
                    self.extraLuck += 2
            else:
                game_config.luck -= self.extraLuck
                self.extraLuck = 0
                
        def sold(self):
            game_config.luck -= self.extraLuck

    game_config.unlockedItems.append(toyTrain)
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
            game_config.lemonGoldChance += 20

        def sold(self):
            game_config.lemonGoldChance -= 20

    game_config.unlockedItems.append(goldenLemon)
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
            game_config.cherryGoldChance += 20

        def sold(self):
            game_config.cherryGoldChance -= 20

    game_config.unlockedItems.append(goldenCherry)
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
            game_config.cloverGoldChance += 20

        def sold(self):
            game_config.cloverGoldChance -= 20

    game_config.unlockedItems.append(goldenClover)
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
            game_config.bellGoldChance += 20

        def sold(self):
            game_config.bellGoldChance -= 20

    game_config.unlockedItems.append(goldenBell)
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
            game_config.diamondGoldChance += 25

        def sold(self):
            game_config.diamondGoldChance -= 25

    game_config.unlockedItems.append(goldenDiamond)
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
            game_config.treasureGoldChance += 25

        def sold(self):
            game_config.treasureGoldChance -= 25

    game_config.unlockedItems.append(goldenTreasure)
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
            game_config.sevenGoldChance += 30

        def sold(self):
            game_config.sevenGoldChance -= 30

    game_config.unlockedItems.append(goldenSeven)
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
            game_config.lemonTokenChance += 20

        def sold(self):
            game_config.lemonTokenChance -= 20

    game_config.unlockedItems.append(bricks)
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
            game_config.cherryTokenChance += 20

        def sold(self):
            game_config.cherryTokenChance -= 20

    game_config.unlockedItems.append(wood)
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
            game_config.cloverTokenChance += 15

        def sold(self):
            game_config.cloverTokenChance -= 15

    game_config.unlockedItems.append(sheep)
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
            game_config.bellTokenChance += 15

        def sold(self):
            game_config.bellTokenChance -= 15

    game_config.unlockedItems.append(wheat)
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
            game_config.diamondTokenChance += 10

        def sold(self):
            game_config.diamondTokenChance -= 10

    game_config.unlockedItems.append(stone)
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
            game_config.treasureTokenChance += 10

        def sold(self):
            game_config.treasureTokenChance -= 10

    game_config.unlockedItems.append(harbor)
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
            game_config.sevenTokenChance += 10

        def sold(self):
            game_config.sevenTokenChance -= 10

    game_config.unlockedItems.append(thief)
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
            game_config.lemonTicketChance += 20
    
        def sold(self):
            game_config.lemonTicketChance -= 20

    game_config.unlockedItems.append(wheelbarrow)
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
            game_config.cherryTicketChance += 20
    
        def sold(self):
            game_config.cherryTicketChance -= 20

    game_config.unlockedItems.append(shoe)
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
            game_config.cloverTicketChance += 20
    
        def sold(self):
            game_config.cloverTicketChance -= 20

    game_config.unlockedItems.append(thimble)
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
            game_config.bellTicketChance += 20
    
        def sold(self):
            game_config.bellTicketChance -= 20

    game_config.unlockedItems.append(iron)
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
            game_config.diamondTicketChance += 20
    
        def sold(self):
            game_config.diamondTicketChance -= 20

    game_config.unlockedItems.append(car)
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
            game_config.treasureTicketChance += 20
    
        def sold(self):
            game_config.treasureTicketChance -= 20

    game_config.unlockedItems.append(ship)
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
            game_config.sevenTicketChance += 20
    
        def sold(self):
            game_config.sevenTicketChance -= 20

    game_config.unlockedItems.append(tubaHat)
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
                game_config.symbolValues[0] += game_config.baseSymbolValues[0]
                game_config.symbolValues[1] += game_config.baseSymbolValues[1]
    
        def sold(self):
            pass

    game_config.unlockedItems.append(aceOfHearts)
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
                if len(game_config.patterns[result[i][0]]) > 3:
                    game_config.symbolValues[4] += game_config.baseSymbolValues[4]
                    game_config.symbolValues[5] += game_config.baseSymbolValues[5]
                    break
    
        def sold(self):
            pass

    game_config.unlockedItems.append(aceOfDiamonds)
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
            shopRestock(game_config.unlockedItems, itemWeights)
    
        def sold(self):
            pass

    game_config.unlockedItems.append(d6)
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

    game_config.unlockedItems.append(d20)
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
            game_config.affChainChance += 12
    
        def sold(self):
            game_config.affChainChance -= 12

    game_config.unlockedItems.append(crystalSphere)
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
            game_config.affRepChance += 15
    
        def sold(self):
            game_config.affRepChance -= 15

    game_config.unlockedItems.append(clicker)
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
            if game_config.is666:
                game_config.freeRestocks += 3
    
        def sold(self):
            pass

    game_config.unlockedItems.append(ritualBell)
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
            game_config.patternMult += 2
            game_config.chance666 += 3
    
        def sold(self):
            game_config.patternMult -= 2
            game_config.chance666 -= 3

    game_config.unlockedItems.append(necronomicon)
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
            game_config.tempLuck += 5
            self.activations += 1
            if self.activation == 12:
                pass #temporary pass
                #something to kill itself

        def sold(self):
            pass

    game_config.unlockedItems.append(redPepper)
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
            game_config.tickets += math.floor(game_config.tickets/game_config.debtNum)
    
        def sold(self):
            pass

    game_config.unlockedItems.append(cloverPot)
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
            game_config.symbolmult -= self.extraMult
            self.extraMult = math.floor(game_config.tickets/5)
            game_config.symbolMult += self.extraMult
    
        def sold(self):
            game_config.symbolmult -= self.extraMult

    game_config.unlockedItems.append(cloverPet)
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
            game_config.unlockedItems[44].cost += 1
            for i in range(7):
                game_config.symbolValues[i] += game_config.baseSymbolValues[i]
                shopRestock(game_config.unlockedItems, itemWeights)
                #something to kill itself

        def sold(self): #this should never be triggered
            pass

    game_config.unlockedItems.append(cigarettes)
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
            game_config.cardboardInit = False
            game_config.shelfSpace += 1
            #something to kill itself
    
        def sold(self): #this should never be triggered
            pass

    game_config.unlockedItems.append(cardboardHouse)
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
            game_config.shelfSpace += 2
    
        def sold(self):
            game_config.shelfSpace -= 2

    game_config.unlockedItems.append(propertyCertificate)
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
            game_config.freeRestocks += 3
            #something to kill itself

        def sold(self): #this should never be triggered
            pass

    game_config.unlockedItems.append(crowbar)
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
                    game_config.symbolValues[i] += game_config.baseSymbolValues[i]
    
        def sold(self):
            pass

    game_config.unlockedItems.append(consolationPrize)
    itemWeights.append(consolationPrize.weight)

    class lemonPicture(button):
        name = 'Lemon Picture'
        description = 'Lemons manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Lemon_Picture.png')
        weight = 100
        cost = 2
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[0] += 2
            game_config.tempSymbolWeights[0] += 2
        
        def sold(self):
            game_config.symbolWeights[0] -= 2
            game_config.tempSymbolWeights[0] -= 2

    game_config.unlockedItems.append(lemonPicture)
    itemWeights.append(lemonPicture.weight)

    class cherryPicture(button):
        name = 'Cherry Picture'
        description = 'Cherries manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Cherry_Picture.png')
        weight = 100
        cost = 2
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[1] += 2
            game_config.tempSymbolWeights[1] += 2
        
        def sold(self):
            game_config.symbolWeights[1] -= 2
            game_config.tempSymbolWeights[1] -= 2

    game_config.unlockedItems.append(cherryPicture)
    itemWeights.append(cherryPicture.weight)

    class cloverPicture(button):
        name = 'Clover Picture'
        description = 'Clovers manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Clover_Picture.png')
        weight = 90
        cost = 3
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[2] += 2
            game_config.tempSymbolWeights[2] += 2
        
        def sold(self):
            game_config.symbolWeights[2] -= 2
            game_config.tempSymbolWeights[2] -= 2

    game_config.unlockedItems.append(cloverPicture)
    itemWeights.append(cloverPicture.weight)

    class bellPicture(button):
        name = 'Bell Picture'
        description = 'Bells manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Bell_Picture.png')
        weight = 90
        cost = 3
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[3] += 2
            game_config.tempSymbolWeights[3] += 2
        
        def sold(self):
            game_config.symbolWeights[3] -= 2
            game_config.tempSymbolWeights[3] -= 2

    game_config.unlockedItems.append(bellPicture)
    itemWeights.append(bellPicture.weight)

    class diamondPicture(button):
        name = 'Diamond Picture'
        description = 'Diamonds manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Diamond_Picture.png')
        weight = 80
        cost = 4
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[4] += 2
            game_config.tempSymbolWeights[4] += 2
        
        def sold(self):
            game_config.symbolWeights[4] -= 2
            game_config.tempSymbolWeights[4] -= 2

    game_config.unlockedItems.append(diamondPicture)
    itemWeights.append(diamondPicture.weight)

    class treasurePicture(button):
        name = 'Treasure Picture'
        description = 'Treasures manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Treasure_Picture.png')
        weight = 80
        cost = 4
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[5] += 2
            game_config.tempSymbolWeights[5] += 2
        
        def sold(self):
            game_config.symbolWeights[5] -= 2
            game_config.tempSymbolWeights[5] -= 2

    game_config.unlockedItems.append(treasurePicture)
    itemWeights.append(treasurePicture.weight)

    class sevenPicture(button):
        name = 'Seven Picture'
        description = 'Sevens manifest more often (+2) for the rest of the deadline'
        sprite = pygame.image.load('assets/Seven_Picture.png')
        weight = 65
        cost = 4
        charges = 4
        space = 1
        type = 'button'
        
        def trigger(self):
            game_config.symbolWeights[6] += 2
            game_config.tempSymbolWeights[6] += 2
        
        def sold(self):
            game_config.symbolWeights[6] -= 2
            game_config.tempSymbolWeights[6] -= 2

    game_config.unlockedItems.append(sevenPicture)
    itemWeights.append(sevenPicture.weight)    

    return game_config.unlockedItems, itemWeights
