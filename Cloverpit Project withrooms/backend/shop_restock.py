#shop restock
import random
shopItems = [0, 0, 0, 0]

def shopRestock(unlockedItems, itemWeights):
    shopItemClasses = random.choices(unlockedItems, weights = itemWeights, k = 4)

    for item in range(4):
        global shopItems
        shopItems[item] = shopItemClasses[item]()
