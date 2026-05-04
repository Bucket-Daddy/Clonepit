#administrering af shelf items

from config.game_config import (ShelfSpace, shelfRoom, shelfItems)

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

def postRollTrigger():
    for item in shelfItems:
        if item.type == 'postRoll':
            item.trigger()

def randomTrigger():
    for item in shelfItems:
        if item.type == 'random':
            item.trigger()

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