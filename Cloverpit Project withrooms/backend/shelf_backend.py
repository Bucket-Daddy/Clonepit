#administrering af shelf items
import pygame
import random
import config.game_config as config
pygame.init()

ButtonPressSFX = pygame.mixer.Sound('assets/Redbuttonpress.mp3')
ButtonPressSFXActivations = pygame.mixer.Sound('assets/Redbuttonpresswithactivations.mp3')

def passiveTrigger(item):
    if item.type == 'passive':
        item.trigger()

def lastSpinTrigger():
    for item in config.shelfItems:
        if item.type == 'passive':
            item.trigger()

def preRollTrigger():
    for item in config.shelfItems:
        if item.type == 'preRoll':
            item.trigger()

def postRollTrigger(pityCounter, result):
    for item in config.shelfItems:
        if item.type == 'postRoll':
            item.trigger(pityCounter, result)

def randomTrigger(pityCounter, result):
    for item in config.shelfItems:
        if item.type == 'random' and 100 * random.random() <= item.chance * config.randomTriggerMult:
            item.trigger(pityCounter, result)

def buttonTrigger():
    isTriggered = False
    for item in config.shelfItems:
        if item.type == 'button' and item.charges == item.chargeSlots:
            item.trigger()
            item.charges = 0
            isTriggered = True

    if isTriggered:
        ButtonPressSFXActivations.play()
    else:
        ButtonPressSFX.play()


def roundEndTrigger():
    for item in config.shelfItems:
        if item.type == 'roundEnd':
            item.trigger()

def deadlineEndTrigger():
    for item in config.shelfItems:
        if item.type == 'deadlineEnd':
            item.trigger()

def interventionTrigger():
    for item in config.shelfItems:
        if item.type == 'intervention':
            item.trigger()
