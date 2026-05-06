# Telefon abilities

import math

import config.game_config as config
import frontend.shop_room as shop

config.unlockedCalls = []
config.callWeights = []

def callInit():

    class itemSpaceCall():
        name = 'Please don\'t throw my stuff away!'
        description = 'Increase Charm\'s space by 1, permanently.'
        weight = 85

        def trigger():
            config.shelfSpace += 1
            config.unlockedCalls.pop(0)
            config.callWeights.pop(0)

    config.unlockedCalls.append(itemSpaceCall)
    config.callWeights.append(itemSpaceCall.weight)


    class jackpotValueCall():
        name = 'I can\'t quit now!'
        description = 'Double Jackpot\'s value'
        weight = 100

        def trigger():
            config.patternValues['jackpot'] *= 2

    config.unlockedCalls.append(jackpotValueCall)
    config.callWeights.append(jackpotValueCall.weight)

    class ticketCall():
        name = 'Can I borrow some green?'
        description = '+5 Clover Tickets'
        weight = 100

        def trigger():
            config.tickets += 5

    config.unlockedCalls.append(ticketCall)
    config.callWeights.append(ticketCall.weight)    

    class shopDiscountCall():
        name = 'Can I eat something?'
        description = 'Lucky Charms at the store are discounted by 2 until the next Restock of the store.'
        weight = 100
    
        def trigger():
            for item in shop.shopItems:
                item.cost -= 2
            
    config.unlockedCalls.append(shopDiscountCall)
    config.callWeights.append(shopDiscountCall.weight)

    class itemChargeCall():
        name = 'Can you give me some Energy Drinks?'
        description = 'Restore all Charges on all Charms triggered by the Red Button.'
        weight = 100

        def trigger():
            for item in config.shelfItems:
                if item.type == 'button' and item.charges < item.chargeSlots:
                    item.charges = item.chargeSlots
            
    config.unlockedCalls.append(itemChargeCall)
    config.callWeights.append(itemChargeCall.weight)

    class lemonCall():
        name = 'Life gave me lemons'
        description = 'Lemons manifest more often (+1), permanently.'
        weight = 100

        def trigger():
            config.symbolWeights[0] += 1

    config.unlockedCalls.append(lemonCall)
    config.callWeights.append(lemonCall.weight)

    class cherryCall():
        name = 'I used to eat healthy...'
        description = 'Cherries manifest more often (+1), permanently.'
        weight = 100

        def trigger():
            config.symbolWeights[1] += 1

    config.unlockedCalls.append(cherryCall)
    config.callWeights.append(cherryCall.weight)

    class cloverCall():
        name = 'Today\'s my Lucky day!'
        description = 'Clovers manifest more often (+1), permanently.'
        weight = 85

        def trigger():
            config.symbolWeights[2] += 1

    config.unlockedCalls.append(cloverCall)
    config.callWeights.append(cloverCall.weight)

    class bellCall():
        name = 'I need to be there!'
        description = 'Bells manifest more often (+1), permanently.'
        weight = 85

        def trigger():
            config.symbolWeights[3] += 1

    config.unlockedCalls.append(bellCall)
    config.callWeights.append(bellCall.weight)

    class diamondCall():
        name = 'Please! I\'ll give you anything!'
        description = 'Diamonds manifest more often (+1), permanently.'
        weight = 65

        def trigger():
            config.symbolWeights[4] += 1

    config.unlockedCalls.append(diamondCall)
    config.callWeights.append(diamondCall.weight)

    class treasureCall():
        name = 'I need money!'
        description = 'Diamonds manifest more often (+1), permanently.'
        weight = 65
        def trigger():
            config.symbolWeights[5] += 1

    config.unlockedCalls.append(treasureCall)
    config.callWeights.append(treasureCall.weight)

    class sevenCall():
        name = 'I didn\'t hurt anybody...'
        description = 'Sevens manifest more often (+1), permanently.'
        weight = 40

        def trigger():
            config.symbolWeights[6] += 1

    config.unlockedCalls.append(sevenCall)
    config.callWeights.append(sevenCall.weight)

    class lemonCherryValue():
        name = 'I need supplements!'
        description = 'Double the value of Lemons and Cherries.'
        weight = 100

        def trigger(self):
            config.symbolValues[0] *= 2
            config.symbolValues[1] *= 2

    config.unlockedCalls.append(lemonCherryValue)
    config.callWeights.append(lemonCherryValue.weight)

    class cloverBellValue():
        name = 'I\'m feeling lucky!'
        description = 'Double the value of Clovers and Bells.'
        weight = 100

        def trigger():
            config.symbolValues[2] *= 2 
            config.symbolValues[3] *= 2

    config.unlockedCalls.append(cloverBellValue)
    config.callWeights.append(cloverBellValue.weight)

    class diamondTreasureValue():
        name = 'Gold and Diamonds are a good investment!'
        description = 'Double the value of Diamonds and Treasures.'
        weight = 85

        def trigger():
            config.symbolValues[4] *= 2 
            config.symbolValues[5] *= 2

    config.unlockedCalls.append(diamondTreasureValue)
    config.callWeights.append(diamondTreasureValue.weight)

    class sevenValue():
        name = 'I\'m gonna go \"All In\"!'
        description = 'Triple the value of the Seven.'
        weight = 85

        def trigger():
            config.symbolValues[6] *= 3

    config.unlockedCalls.append(sevenValue)
    config.callWeights.append(sevenValue.weight)

    class smallPatternValue():
        name = 'I\'m thinking of some strategies!'
        description = 'Increase the value of Patterns with 3 or less symbols by their base value.'
        weight = 85

        def trigger():
            config.patternValues['hor'] += config.basePatternValues['hor']
            config.patternValues['vert'] += config.basePatternValues['vert']
            config.patternValues['diag'] += config.basePatternValues['diag']

    config.unlockedCalls.append(smallPatternValue)
    config.callWeights.append(smallPatternValue.weight)

    class bigPatternValue():
        name = 'I found a winning strategy!'
        description = 'Increase the value of Patterns with 4+ symbols by their base value.'
        weight = 85

        def trigger():
            config.patternValues['horL'] += config.basePatternValues['horL']
            config.patternValues['horXL'] += config.basePatternValues['horXL']
            config.patternValues['zig'] += config.basePatternValues['zig']
            config.patternValues['zag'] += config.basePatternValues['zag']
            config.patternValues['above'] += config.basePatternValues['above']
            config.patternValues['below'] += config.basePatternValues['below']
            config.patternValues['eye'] += config.basePatternValues['eye']
            config.patternValues['jackpot'] += config.basePatternValues['jackpot']
