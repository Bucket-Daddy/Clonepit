#shop restock
import random
shopItems = []

def shopRestock(unlockedItems, itemWeights):
    shopItemClasses = random.choices(unlockedItems, weights = itemWeights, k = 4)

    for item in range(4):
        shopItems[item] = shopItemClasses[item]()
        
    return shopItems