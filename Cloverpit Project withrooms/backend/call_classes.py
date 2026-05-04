# Telefon kræfter


# i need a thing where it stops triggerring the effect, kinda like lostBriefcase from item_classes.

import math
import frontend.text_rendering

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

    def trigger(self, origin, width):
        callText = 'Please don\'t throw my stuff away!'
        callDiscription = '\033[93mIncrease Charm\'s space by 1, permanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class I_cant_quit_now (common):
    # Double Jackpot's value.

    def trigger(self, origin, width):
        callText = 'I can\'t quit now!'
        callDiscription = '\033[93mDouble Jackpot\'s value\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class Can_I_borrow_some_green (common):
    # +5 tickets

    def trigger(self, origin, width):
        callText = 'Can I borrow some green?'
        callDiscription = '\033[93m+5 tickets\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class Can_I_eat_something (common):
    # Lucky Charms at the store are discounted by 2 until the next Restock of the store.
    
    # this def needs something to disable the effect after the next restock
    def trigger(self, origin, width):
        callText = 'Can I eat something?'
        callDiscription = '\033[93mLucky Charms\033[0m at the \033[93mstore\033[0m are \033[93mdiscounted by 2\033[0m until the \033[93mnext Restock\033[0m of the store.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class Can_you_give_me_some_Energy_Drinks (common):
    # Restore all Charges on all Charms triggered by the Red Button

    def trigger(self, origin, width):
        callText = 'Can you give me some Energy Drinks?'
        callDiscription = 'Restore \033[93mall Charges\033[0m on all \033[93mCharms triggered\033[0m by the \033[93mRed Button\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class lemonManifest (common):
    # Lemons manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'Life gave me lemons'
        callDiscription = '\033[93mLemons manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class cherryManifest (common):
    # Cherries manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'I used to eat healthy...'
        callDiscription = '\033[93mCherries manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class cloverManifest (uncommon):
    # Clovers manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'Today\'s my Lucky day!'
        callDiscription = '\033[93mClovers manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class bellManifest (uncommon):
    # Bells manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'I need to be there!'
        callDiscription = '\033[93mBells manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class diamondManifest (rare):
    # Diamonds manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'Please! I\'ll give you anything!'
        callDiscription = '\033[93mDiamonds manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class treasureManifest (rare):
    # Treasures manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'I need money!'
        callDiscription = '\033[93mTreasures manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class sevenManifest (ultraRare):
    # Sevens manifest more often (+1), permanently.

    def trigger(self, origin, width):
        callText = 'I didn\'t hurt anybody...'
        callDiscription = '\033[93mSevens manifest\033[0m more often \033[93m(+1)\033[0m, \033[93mpermanently\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass
    
class lemonValue (common):
    # Double the value of the lemon

    def trigger(self, origin, width):
        callText = 'I need supplements!'
        callDiscription = '\033[93mDouble\033[0m the \033[93mvalue\033[0m of the \033[93mlemon\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class cherryValue (common):
    # Double the value of the cherry

    def trigger(self, origin, width):
        callText = 'I need supplements!'
        callDiscription = '\033[93mDouble\033[0m the \033[93mvalue\033[0m of the \033[93mcherry\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class cloverValue (common):
    # Double the value of the clover

    def trigger(self, origin, width):
        callText = 'I\'m feeling lucky!'
        callDiscription = '\033[93mDouble\033[0m the \033[93mvalue\033[0m of the \033[93mclover\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class bellValue (common):
    # Double the value of the bell

    def trigger(self, origin, width):
        callText = 'I\'m feeling lucky!'
        callDiscription = '\033[93mDouble\033[0m the \033[93mvalue\033[0m of the \033[93mbell\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class diamondValue (uncommon):
    # Double the value of the diamond

    def trigger(self, origin, width):
        callText = 'Gold and Diamonds are a good investment!'
        callDiscription = '\033[93mDouble\033[0m the \033[93mvalue\033[0m of the \033[93mdiamond\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class treasureValue (uncommon):
    # Double the value of the treasure

    def trigger(self, origin, width):
        callText = 'Gold and Diamonds are a good investment!'
        callDiscription = '\033[93mDouble\033[0m the \033[93mvalue\033[0m of the \033[93mtreasure\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class sevenValue (uncommon):
    # Triple the value of the Seven

    def trigger(self, origin, width):
        callText = 'I\'m gonna go "\033[93mAll In\033[0m"!'
        callDiscription = '\033[93mTriple\033[0m the \033[93mvalue\033[0m of the \033[93mSeven\033[0m'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass

class patternValue (uncommon):
    # Increase the value of Patterns with 3 or less/4+ symbols by their base value.

    def trigger(self, origin, width):
        patternValueRandom =round(math.random())
        
        if patternValueRandom == 0:
            callText = 'I\'m thinking of some strategies!'
            callDiscription = '\033[93mIncrease\033[0m the \033[93mvalue\033[0m of Patterns with \033[93m3 or less symbols\033[0m by their \033[93mbase value\033[0m.'
        else:
            callText = 'I found a winning strategy!'
            callDiscription = '\033[93mIncrease\033[0m the \033[93mvalue\033[0m of Patterns with \033[93m4+ symbols\033[0m by their \033[93mbase value\033[0m.'
        frontend.text_rendering.renderText(callDiscription, self.font, self.surface, origin, width)
        pass


