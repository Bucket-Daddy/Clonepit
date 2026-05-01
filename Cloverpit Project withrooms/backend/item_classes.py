#item classes
import math
import pygame
unlockedItems = []
itemWeights = []

from config.game_config import (cigaretteCost)

def itemInit():    

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
        name = 'AA Batteries'
        description = '+6% Chance for the Symbols Clover and Bell to have the Battery Modifier.'
        sprite = pygame.image.load('assets/AA_Batteries.png')
        weight = 5
        cost = 3

        def trigger(self):
            global affBattChance
            affBattChance += 6
    
        def sold(self):
            global affBattChance
            affBattChance -= 6

    unlockedItems.append(AABatteries)
    itemWeights.append(AABatteries.weight)

    class rotatedHamsa(lastRound):
        name = 'Rotated Hamsa'
        description = 'Grants \033[92mLuck\033[0m+7 for the last spin of a Round.'
        sprite = pygame.image.load('assets/Rotated_Hamsa.png')
        weight = 10
        cost = 3

        def trigger(self):
            global luck
            luck += 6
    
        def solds(self):
            pass

    unlockedItems.append(rotatedHamsa)
    itemWeights.append(rotatedHamsa.weight)

    #class painKillers(postRoll):
        #name = ''
        #description = ''
        #sprite = pygame.image.load('assets/.png')
        #weight = 6.5
        #cost = 3

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
        weight = 6.5
        cost = 2

        def trigger(self):
            if pityCounter >= 3:
                for i in range(7):
                    global symbolValues
                    symbolValues[i] += baseSymbolValues[i]
    
        def sold(self):
            pass

    unlockedItems.append(steamLocomotive)
    itemWeights.append(steamLocomotive.weight)

    class horseshoe(passive):
        name = 'Horseshoe'
        description = 'Charms with \"\033[93mTriggers Randomly\033[0m\" activate double more often.'
        sprite = pygame.image.load('assets/Horseshoe.png')
        weight = 10
        cost = 3

        def trigger(self):
            randomTriggerMult *= 2

        def sold(self):
            randomTriggerMult *= 0.5

    unlockedItems.append(horseshoe)
    itemWeights.append(horseshoe.weight)

    class luckyCat(postRoll):
        name = 'Lucky Cat'
        description = 'Whenever 3+ Patterns trigger during a spin, you earn money equal to your current Interest.'
        sprite = pygame.image.load('assets/Lucky_Cat.png')
        weight = 10
        cost = 1

        def trigger(self):
            if len(result) > 2:
                global coins
                coins += (interest - 1) * depositedAmount
    
        def sold(self):
            pass

    unlockedItems.append(luckyCat)
    itemWeights.append(luckyCat.weight)

    class grandmasPurse(roundEnd):
        name = ' Grandma\'s Purse'
        description = 'Interest increases by +15%, but decreases by 3% after every Round. Discard this Charm when its bonus is 0.'
        sprite = pygame.image.load('assets/Grandmas_Purse.png')
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

    unlockedItems.append(grandmasPurse)
    itemWeights.append(grandmasPurse.weight)

    class stonks(passive):
        name = 'Stonks'
        description = '+5% to your Interest.'
        sprite = pygame.image.load('assets/Stonks.png')
        weight = 10
        cost = 2

        def trigger(self):
            global interest
            interest += 0.05
    
        def sold(self):
            global interest
            interest -= 0.05

    unlockedItems.append(stonks)
    itemWeights.append(stonks.weight)

    class megaphone(passive):
        name = 'Megaphone'
        description = 'All abilities that you pick at the telephone trigger one more time. -1 to Charms\' space.'
        sprite = pygame.image.load('assets/Megaphone.png')
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

    unlockedItems.append(megaphone)
    itemWeights.append(megaphone.weight)

    class lostBriefcase(passive):
        name = 'Lost Briefcase'
        description = '\033[93mDoesn\'t take space\033[0m. Immediately earn 30% of the debt amount.'
        sprite = pygame.image.load('assets/Lost_Briefcase.png')
        weight = 10
        cost = 2
    
        def trigger(self):
            global coins
            coins += 0.3 * debtAmount
            #Something to kill itself
    
        def sold(self): #this should never be triggered
            pass

    unlockedItems.append(lostBriefcase)
    itemWeights.append(lostBriefcase.weight)

    class fakeCoin(randomTrigger):
        name = 'Fake Coin'
        description = '\033[93mTriggers Randomly\033[0m (10%): +1 extra spin, then \033[92mLuck+4\033[0m for that spin.'
        sprite = pygame.image.load('assets/Fake_coin.png')
        weight = 10
        cost = 1
        chance = 10

        def trigger(self):
            global fakeCoinSpins
            fakeCoinSpins += 1
    
        def sold(self):
            pass

    unlockedItems.append(fakeCoin)
    itemWeights.append(fakeCoin.weight)

    class catFood(passive):
        name = 'Cat Food'
        description = '+2 spins per Round.'
        sprite = pygame.image.load('assets/Cat_Food.png')
        weight = 10
        cost = 4

        def trigger(self):
            global bonusSpins
            bonusSpins += 2
    
        def sold(self):
            global bonusSpins
            bonusSpins -= 2

    unlockedItems.append(catFood)
    itemWeights.append(catFood.weight)

    class toyTrain(postRoll):
        name = 'Toy Train'
        description = '\033[92mLuck\033[0m+5 on next spin if the previous 2 had no reward. +2 extra \033[92mLuck\033[0m for every in sequence activation after the first one.'
        sprite = pygame.image.load('assets/Toy_Train.png')
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
                luck -= self.extraLuck
                self.extraLuck = 0
                
        def sold(self):
            global luck
            luck -= self.extraLuck

    unlockedItems.append(toyTrain)
    itemWeights.append(toyTrain.weight)

    class goldenLemon(passive):
        name = 'Golden Lemon'
        description = '+20% Chance for Lemons to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Lemon.png')
        weight = 6.5
        cost = 3

        def trigger(self):
            global lemonGoldChance
            lemonGoldChance += 20

        def sold(self):
            global lemonGoldChance
            lemonGoldChance -= 20

    unlockedItems.append(goldenLemon)
    itemWeights.append(goldenLemon.weight)

    class goldenCherry(passive):
        name = 'Golden Cherry'
        description = '+20% Chance for Cherries to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Cherry.png')
        weight = 6.5
        cost = 3

        def trigger(self):
            global cherryGoldChance
            cherryGoldChance += 20

        def sold(self):
            global cherryGoldChance
            cherryGoldChance -= 20

    unlockedItems.append(goldenCherry)
    itemWeights.append(goldenCherry.weight)

    class goldenClover(passive):
        name = 'Golden Clover'
        description = '+20% Chance for Clovers to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Clover.png')
        weight = 8
        cost = 3

        def trigger(self):
            global cloverGoldChance
            cloverGoldChance += 20

        def sold(self):
            global cloverGoldChance
            cloverGoldChance -= 20

    unlockedItems.append(goldenClover)
    itemWeights.append(goldenClover.weight)

    class goldenBell(passive):
        name = 'Golden Bell'
        description = '+20% Chance for Bells to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Bell.png')
        weight = 8
        cost = 3

        def trigger(self):
            global bellGoldChance
            bellGoldChance += 20

        def sold(self):
            global bellGoldChance
            bellGoldChance -= 20

    unlockedItems.append(goldenBell)
    itemWeights.append(goldenBell.weight)

    class goldenDiamond(passive):
        name = 'Golden Diamond'
        description = '+25% Chance for Diamonds to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Diamond.png')
        weight = 10
        cost = 2

        def trigger(self):
            global diamondGoldChance
            diamondGoldChance += 25

        def sold(self):
            global diamondGoldChance
            diamondGoldChance -= 25

    unlockedItems.append(goldenDiamond)
    itemWeights.append(goldenDiamond.weight)

    class goldenTreasure(passive):
        name = 'Golden Treasure'
        description = '+25% Chance for Treasures to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Treasure.png')
        weight = 10
        cost = 2

        def trigger(self):
            global treasureGoldChance
            treasureGoldChance += 25

        def sold(self):
            global treasureGoldChance
            treasureGoldChance -= 25

    unlockedItems.append(goldenTreasure)
    itemWeights.append(goldenTreasure.weight)

    class goldenSeven(passive):
        name = 'Golden Seven'
        description = '+30% Chance for Sevens to have the Golden Modifier.'
        sprite = pygame.image.load('assets/Golden_Seven.png')
        weight = 10
        cost = 1

        def trigger(self):
            global sevenGoldChance
            sevenGoldChance += 30

        def sold(self):
            global sevenGoldChance
            sevenGoldChance -= 30

    unlockedItems.append(goldenSeven)
    itemWeights.append(goldenSeven.weight)

    class bricks(passive):
        name = 'Bricks'
        description = '+20% Chance for any Lemon to have the Token Modifier.'
        sprite = pygame.image.load('assets/Bricks.png')
        weight = 10
        cost = 1

        def trigger(self):
            global lemonTokenChance
            lemonTokenChance += 20

        def sold(self):
            global lemonTokenChance
            lemonTokenChance -= 20

    unlockedItems.append(bricks)
    itemWeights.append(bricks.weight)

    class wood(passive):
        name = 'Wood'
        description = '+20% Chance for any Cherry to have the Token Modifier.'
        sprite = pygame.image.load('assets/Wood.png')
        weight = 10
        cost = 1

        def trigger(self):
            global cherryTokenChance
            cherryTokenChance += 20

        def sold(self):
            global cherryTokenChance
            cherryTokenChance -= 20

    unlockedItems.append(wood)
    itemWeights.append(wood.weight)

    class sheep(passive):
        name = 'Sheep'
        description = '+15% Chance for any Clover to have the Token Modifier.'
        sprite = pygame.image.load('assets/Sheep.png')
        weight = 9
        cost = 2

        def trigger(self):
            global cloverTokenChance
            cloverTokenChance += 15

        def sold(self):
            global cloverTokenChance
            cloverTokenChance -= 15

    unlockedItems.append(sheep)
    itemWeights.append(sheep.weight)

    class wheat(passive):
        name = 'Wheat'
        description = '+15% Chance for any Bell to have the Token Modifier.'
        sprite = pygame.image.load('assets/Wheat.png')
        weight = 9
        cost = 2

        def trigger(self):
            global bellTokenChance
            bellTokenChance += 15

        def sold(self):
            global bellTokenChance
            bellTokenChance -= 15

    unlockedItems.append(wheat)
    itemWeights.append(wheat.weight)

    class stone(passive):
        name = 'Stone'
        description = '+10% Chance for any Diamond to have the Token Modifier.'
        sprite = pygame.image.load('assets/Stone.png')
        weight = 8
        cost = 2

        def trigger(self):
            global diamondTokenChance
            diamondTokenChance += 10

        def sold(self):
            global diamondTokenChance
            diamondTokenChance -= 10

    unlockedItems.append(stone)
    itemWeights.append(stone.weight)

    class harbor(passive):
        name = 'Harbor'
        description = '+10% Chance for any Treasure to have the Token Modifier.'
        sprite = pygame.image.load('assets/Harbor.png')
        weight = 10
        cost = 2

        def trigger(self):
            global treasureTokenChance
            treasureTokenChance += 10

        def sold(self):
            global treasureTokenChance
            treasureTokenChance -= 10

    unlockedItems.append(harbor)
    itemWeights.append(harbor.weight)

    class thief(passive):
        name = 'Thief'
        description = '+10% Chance for any Seven to have the Token Modifier.'
        sprite = pygame.image.load('assets/Thief.png')
        weight = 10
        cost = 2

        def trigger(self):
            global sevenTokenChance
            sevenTokenChance += 10

        def sold(self):
            global sevenTokenChance
            sevenTokenChance -= 10

    unlockedItems.append(thief)
    itemWeights.append(thief.weight)

    class wheelbarrow(passive):
        name = 'Wheelbarrow'
        description = '+20% Chance for any Lemon to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Wheelbarrow.png')
        weight = 6.5
        cost = 4

        def trigger(self):
            global lemonTicketChance
            lemonTicketChance += 20
    
        def sold(self):
            global lemonTicketChance
            lemonTicketChance -= 20

    unlockedItems.append(wheelbarrow)
    itemWeights.append(wheelbarrow.weight)

    class shoe(passive):
        name = 'Shoe'
        description = '+20% Chance for any Cherry to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Shoe.png')
        weight = 6.5
        cost = 4

        def trigger(self):
            global cherryTicketChance
            cherryTicketChance += 20
    
        def sold(self):
            global cherryTicketChance
            cherryTicketChance -= 20

    unlockedItems.append(shoe)
    itemWeights.append(shoe.weight)

    class thimble(passive):
        name = 'Thimble'
        description = '+20% Chance for any Clover to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Thimble.png')
        weight = 10
        cost = 2

        def trigger(self):
            global cloverTicketChance
            cloverTicketChance += 20
    
        def sold(self):
            global cloverTicketChance
            cloverTicketChance -= 20

    unlockedItems.append(thimble)
    itemWeights.append(thimble.weight)

    class iron(passive):
        name = 'Iron'
        description = '+20% Chance for any Bell to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Iron.png')
        weight = 10
        cost = 2

        def trigger(self):
            global bellTicketChance
            bellTicketChance += 20
    
        def sold(self):
            global bellTicketChance
            bellTicketChance -= 20

    unlockedItems.append(iron)
    itemWeights.append(iron.weight)

    class car(passive):
        name = 'Car'
        description = '+20% Chance for any Diamond to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Car.png')
        weight = 6.5
        cost = 3

        def trigger(self):
            global diamondTicketChance
            diamondTicketChance += 20
    
        def sold(self):
            global diamondTicketChance
            diamondTicketChance -= 20

    unlockedItems.append(car)
    itemWeights.append(car.weight)

    class ship(passive):
        name = 'Ship'
        description = '+20% Chance for Treasures to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Ship.png')
        weight = 6.5
        cost = 3

        def trigger(self):
            global treasureTicketChance
            treasureTicketChance += 20
    
        def sold(self):
            global treasureTicketChance
            treasureTicketChance -= 20

    unlockedItems.append(ship)
    itemWeights.append(ship.weight)

    class tubaHat(passive):
        name = 'Tuba Hat'
        description = '+20% Chance for any Seven to have the Ticket Modifier.'
        sprite = pygame.image.load('assets/Tuba_Hat.png')
        weight = 6.5
        cost = 3

        def trigger(self):
            global sevenTicketChance
            sevenTicketChance += 20
    
        def sold(self):
            global sevenTicketChance
            sevenTicketChance -= 20

    unlockedItems.append(tubaHat)
    itemWeights.append(tubaHat.weight)

    class aceOfHearts(postRoll):
        name = 'Ace of Hearts'
        description = 'Whenever 3+ Patterns trigger during a spin, raise all fruits by their base value permanently.'
        sprite = pygame.image.load('assets/Ace_of_Hearts.png')
        weight = 10
        cost = 3

        def trigger(self):
            if len(result) >= 3:
                global symbolValues
                symbolValues[0] += baseSymbolValues[0]
                symbolValues[1] += baseSymbolValues[1]
    
        def sold(self):
            pass

    unlockedItems.append(aceOfHearts)
    itemWeights.append(aceOfHearts.weight)

    class aceOfDiamonds(postRoll):
        name = 'Ace of Diamonds'
        description = 'Every time you score at least 1 Pattern of 4+ Symbols, raise Diamonds and Treasures by their base value permanently.'
        sprite = pygame.image.load('assets/Ace_of_Diamonds.png')
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

    unlockedItems.append(aceOfDiamonds)
    itemWeights.append(aceOfDiamonds.weight)

    class d6(roundEnd):
        name = 'D6'
        description = 'Restock the store for free at the end of every Round.'
        sprite = pygame.image.load('assets/D6.png')
        weight = 6.5
        cost = 2

        def trigger(self):
            pass #temporary pass
            #call the shop restock function
    
        def sold(self):
            pass

    unlockedItems.append(d6)
    itemWeights.append(d6.weight)

    class d20(roundEnd):
        name = 'D20'
        description = 'At the end of each Round, replace all lucky Charms inside all drawers with new random ones.'
        sprite = pygame.image.load('assets/D20.png')
        weight = 6.5
        cost = 5

        def trigger(self):
            pass #temporary pass
            #something to randomise the shelves, maybe reusing the shop restock function

        def sold(self):
            pass

    unlockedItems.append(d20)
    itemWeights.append(d20.weight)

    class crystalSphere(passive):
        name = 'Crystal Sphere'
        description = '+12% Chance for the Symbols Diamond, Treasure, and Seven to have the Chain Modifier.'
        sprite = pygame.image.load('assets/Crystal_Sphere.png')
        weight = 8
        cost = 3

        def trigger(self):
            global affChainChance
            affChainChance += 12
    
        def sold(self):
            global affChainChance
            affChainChance -= 12

    unlockedItems.append(crystalSphere)
    itemWeights.append(crystalSphere.weight)

    class clicker(passive):
        name = 'Clicker'
        description = '+15% chance for every fruit to have the Repetition Modifier.'
        sprite = pygame.image.load('assets/Clicker.png')
        weight = 8
        cost = 3

        def trigger(self):
            global affRepChance
            affRepChance += 15
    
        def sold(self):
            global affRepChance
            affRepChance -= 15

    unlockedItems.append(clicker)
    itemWeights.append(clicker.weight)

    class ritualBell(postRoll):
        name = 'Ritual Bell'
        description = 'Whenever you see a 666, gain 3 \033[32mFree Restocks\033[0m.'
        sprite = pygame.image.load('assets/Ritual_Bell.png')
        weight = 10
        cost = 1

        def trigger(self):
            if is666:
                global freeRestocks
                freeRestocks += 3
    
        def sold(self):
            pass

    unlockedItems.append(ritualBell)
    itemWeights.append(ritualBell.weight)

    class necronomicon(passive):
        name = 'Necronomicon'
        description = '\033[33mPatterns Multiplier\033[0m +2. +3% chance of seeing a 666.'
        sprite = pygame.image.load('assets/Necronomicon.png')
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

    unlockedItems.append(necronomicon)
    itemWeights.append(necronomicon.weight)

    class redPepper(randomTrigger):
        name = 'Red Pepper'
        description = '\033[93mTriggers Randomly\033[0m (20%): \033[92mLuck\033[0m+5 for the current spin. Discard after 12 activations.'
        sprite = pygame.image.load('assets/Red_Pepper.png')
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

    unlockedItems.append(redPepper)
    itemWeights.append(redPepper.weight)

    class cloverPot(deadlineEnd):
        name = 'CloverPot'
        description = 'At the end of every Deadline, earn 1 Ticket for every X Ticket you own, where X is the current Deadline.'
        sprite = pygame.image.load('assets/CloverPot.png')
        weight = 8
        cost = 2

        def trigger(self):
            global tickets
            tickets += math.floor(tickets/debtNum)
    
        def sold(self):
            pass

    unlockedItems.append(cloverPot)
    itemWeights.append(cloverPot.weight)

    class cloverPet(preRoll):
        name = 'CloverPet'
        description = '\033[93mSymbols Multiplier\033[0m +1 for every 5 Ticket you own.'
        sprite = pygame.image.load('assets/CloverPet.png')
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

    unlockedItems.append(cloverPet)
    itemWeights.append(cloverPet.weight)        

    class cigarettes(passive):
        name = 'Cigarettes'
        description = '\033[93mDoesn\'t take space\033[0m. Increase all Symbols by their base value, permanently. Then immediately restock the store together with this charm. The price of this charm increases by 1 ticket every time until Deadline end.'
        sprite = pygame.image.load('assets/Cigarettes.png')
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

    unlockedItems.append(cigarettes)
    itemWeights.append(cigarettes.weight)

    class cardboardHouse(passive):
        name = 'Cardboard House'
        description = '\033[93mDoesn\'t take space\033[0m. Makes space for 1 more Lucky Charm! This Charm will not show up again after usage.'
        sprite = pygame.image.load('assets/Cardboard_House.png')
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

    unlockedItems.append(cardboardHouse)
    itemWeights.append(cardboardHouse.weight)

    class propertyCertificate(passive):
        name = 'Property Certificate'
        description = 'Makes space for 2 more Lucky Charms.'
        sprite = pygame.image.load('assets/Property_Certificate.png')
        weight = 8
        cost = 2

        def trigger(self):
            global itemSpace
            itemSpace += 2
            #something to kill itself
    
        def sold(self): #this should never be triggered
            pass

    unlockedItems.append(propertyCertificate)
    itemWeights.append(propertyCertificate.weight)

    class crowbar(passive):
        name = 'Crowbar'
        description = '\033[93mDoesn\'t take space\033[0m. +3 \033[32mFree Restocks\033[0m.'
        sprite = pygame.image.load('assets/Crowbar.png')
        weight = 8
        cost = 2

        def trigger(self):
            global freeRestocks
            freeRestocks += 3
            #something to kill itself

        def sold(self): #this should never be triggered
            pass

    unlockedItems.append(crowbar)
    itemWeights.append(crowbar.weight)

    class consolationPrize(randomTrigger):
        name = 'Consolation Prize'
        description = '\033[93mTriggers Randomly\033[0m (25%): This Charm triggers only if the current spin has no Patterns. Increase all Symbols by their base value, permanently.'
        sprite = pygame.image.load('assets/Consolation_Prize.png')
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

    unlockedItems.append(consolationPrize)
    itemWeights.append(consolationPrize.weight)

    return unlockedItems, itemWeights
