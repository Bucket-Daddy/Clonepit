#Bestemmer valgmulighederne ved telefonen
import random
import config.game_config as config
phoneCallClasses = []
phoneOptions = [0, 0, 0, 0]

def rollPhone():
    callPool = config.unlockedCalls
    callPoolWeights = config.callWeights

    for i in range(3):
        call = random.choices(callPool, weights = callPoolWeights, k = 1)
        phoneCallClasses.append(call[0])
        callPoolWeights.pop(callPool.index(call[0]))
        callPool.remove(call[0])

    for i in range(3):
        global phoneOptions
        phoneOptions[i] = phoneCallClasses[i]()
