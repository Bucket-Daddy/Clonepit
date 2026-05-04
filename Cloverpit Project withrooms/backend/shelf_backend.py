#administrering af shelf items
import random
from config.game_config import (shelfSpace, shelfRoom, shelfItems, randomTriggerMult)

def passiveTrigger(item):
    if item.type == 'passive':
        item.trigger()

def lastSpinTrigger():
    for item in shelfItems:
        if item.type == 'passive':
            item.trigger()

def preRollTrigger():
    for item in shelfItems:
        if item.type == 'preRoll':
            item.trigger()

def postRollTrigger(pityCounter, result):
    for item in shelfItems:
        if item.type == 'postRoll':
            item.trigger(pityCounter, result)

def randomTrigger(pityCounter, result):
    for item in shelfItems:
        if item.type == 'random' and 100 * random.random() <= item.chance * randomTriggerMult:
            item.trigger(pityCounter, result)

def buttonTrigger():
    for item in shelfItems:
        if item.type == 'button':
            item.trigger()

def roundEndTrigger():
    for item in shelfItems:
        if item.type == 'roundEnd':
            item.trigger()

def deadlineEndTrigger():
    for item in shelfItems:
        if item.type == 'deadlineEnd':
            item.trigger()

def interventionTrigger():
    for item in shelfItems:
        if item.type == 'intervention':
            item.trigger()
