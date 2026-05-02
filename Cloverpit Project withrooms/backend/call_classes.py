# Telefon kræfter


# i need a thing where it stops triggerring the effect, kinda like lostBriefcase from item_classes.

import math

class phoneAbility:
    maxPicks = math.inf
    pass

# COMMON appears the most. arbitraty number is 100
# UNCOMMON appears 15% less often than COMMON. arbitraty number is 85
# RARE appears 35% less often than COMMON. arbitraty number is 65
# ULTRA RARE appears 60% less often than COMMON. arbitraty number is 40
# LEGENDARY appears 75% less often than COMMON. arbitraty number is 25

# Sum of all the arbitrary numbers is 315
# chance of getting a COMMON is 100/315
# UNCOMMON is 85/315, RARE is 65/315
# ULTRA RARE is 40/315 and LEGENDARY is 25/315

# COMMON is approximately 31.75%
# UNCOMMON is approximately 26.98%
# RARE is approximately 20.63%
# ULTRA RARE is approximately 12.70%
# LEGENDARY is approximately 7.94%

class common (phoneAbility):
    rarity = 'COMMON'
    pass

class uncommon (phoneAbility):
    rarity = 'UNCOMMON'
    pass

class rare (phoneAbility):
    rarity = 'RARE'
    pass

class ultraRare (phoneAbility):
    rarity = 'ULTRA RARE'
    pass

class legendary (phoneAbility):
    rarity = 'LEGENDARY'
    pass

class Please_dont_throw_my_stuff_away (uncommon):
    # Increase Charm's space by 1, permanently.
    maxPicks = 1

    def trigger(self):
        callText = 'Please don\'t throw my stuff away!'
        pass
    

class I_cant_quit_now (common):
    # Double Jackpot's value.

    def trigger(self):
        callText = 'I can\'t quit now!'
        pass

class Can_I_borrow_some_green (common):
    # +5 tickets

    def trigger(self):
        callText = 'Can I borrow some green?'
        pass

class Can_I_eat_something (common):
    # Lucky Charms at the store are discounted by 2 until the next Restock of the store.
    
    # this def needs something to disable the effect after the next restock
    def trigger(self):
        callText = 'Can I eat something?'
        pass

class Can_you_give_me_some_Energy_Drinks (common):
    # Restore all Charges on all Charms triggered by the Red Button

    def trigger(self):
        callText = 'Can you give me some Energy Drinks?'
        pass

class lemonManifest (common):
    # Lemons manifest more often (+1), permanently.

    def trigger(self):
        callText = 'Life gave me lemons'
        pass

class cherryManifest (common):
    # Cherries manifest more often (+1), permanently.

    def trigger(self):
        callText = 'I used to eat healthy...'
        pass

class cloverManifest (uncommon):
    # Clovers manifest more often (+1), permanently.

    def trigger(self):
        callText = 'Today\'s my Lucky day!'
        pass

class bellManifest (uncommon):
    # Bells manifest more often (+1), permanently.

    def trigger(self):
        callText = 'I need to be there!'
        pass

class diamondManifest (rare):
    # Diamonds manifest more often (+1), permanently.

    def trigger(self):
        callText = 'Please! I\'ll give you anything!'
        pass

class treasureManifest (rare):
    # Treasures manifest more often (+1), permanently.

    def trigger(self):
        callText = 'I need money!'
        pass

class sevenManifest (ultraRare):
    # Sevens manifest more often (+1), permanently.

    def trigger(self):
        callText = 'I didn\'t hurt anybody...'
        pass

class lemonValue (common):
    # Double the value of the lemon

    def trigger(self):
        callText = 'I need supplements!'
        pass

class cherryValue (common):
    # Double the value of the cherry

    def trigger(self):
        callText = 'I need supplements!'
        pass

class cloverValue (common):
    # Double the value of the clover

    def trigger(self):
        callText = 'I\'m feeling lucky!'
        pass

class bellValue (common):
    # Double the value of the bell

    def trigger(self):
        callText = 'I\'m feeling lucky!'
        pass

class diamondValue (uncommon):
    # Double the value of the diamond

    def trigger(self):
        callText = 'Gold and Diamonds are a good investment!'
        pass

class treasureValue (uncommon):
    # Double the value of the treasure

    def trigger(self):
        callText = 'Gold and Diamonds are a good investment!'
        pass

class sevenValue (uncommon):
    # Triple the value of the Seven

    def trigger(self):
        callText = 'I\'m gonna go "All In"!'
        pass

class patternValue (uncommon):
    # Increase the value of Patterns with 3 or less/4+ symbols by their base value.

    def trigger(self):
        patternValueRandom =round(math.random())
        
        if patternValueRandom == 0:
            callText = 'I\'m thinking of some strategies!'
        else:
            callText = 'I found a winning strategy!'
        
        pass





















