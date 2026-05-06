#shop restock
import config.game_config as config
import random
shopItems = [0, 0, 0, 0]

def shopRestock():
    shopItemClasses = []
    itemPool = []
    itemPoolWeights = []
          
    for i in range(len(config.unlockedItems)):
        new = True
        for item in config.shelfItems:
            if config.unlockedItems[i].name == item.name:
                new = False

        if new:
            itemPool.append(config.unlockedItems[i])
            itemPoolWeights.append(config.itemWeights[i])

    for i in range(4):
        item = random.choices(itemPool, weights = itemPoolWeights, k = 1)
        shopItemClasses.append(item[0])
        itemPoolWeights.pop(itemPool.index(item[0]))
        itemPool.remove(item[0])

    for item in range(4):
        global shopItems
        shopItems[item] = shopItemClasses[item]()
