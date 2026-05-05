#administrering af shelf items
import random
import config.game_config as game_config

def passiveTrigger(item):
    if item.type == 'passive':
        item.trigger()

def lastSpinTrigger():
    for item in game_config.shelfItems:
        if item.type == 'passive':
            item.trigger()

def preRollTrigger():
    for item in game_config.shelfItems:
        if item.type == 'preRoll':
            item.trigger()

def postRollTrigger(pityCounter, result):
    for item in game_config.shelfItems:
        if item.type == 'postRoll':
            item.trigger(pityCounter, result)

def randomTrigger(pityCounter, result):
    for item in game_config.shelfItems:
        if item.type == 'random' and 100 * random.random() <= item.chance * game_config.randomTriggerMult:
            item.trigger(pityCounter, result)

def buttonTrigger():
    for item in game_config.shelfItems:
        if item.type == 'button' and item.charges > 0:
            item.trigger()
            item.charges -= 1

def roundEndTrigger():
    for item in game_config.shelfItems:
        if item.type == 'roundEnd':
            item.trigger()

def deadlineEndTrigger():
    for item in game_config.shelfItems:
        if item.type == 'deadlineEnd':
            item.trigger()

def interventionTrigger():
    for item in game_config.shelfItems:
        if item.type == 'intervention':
            item.trigger()
