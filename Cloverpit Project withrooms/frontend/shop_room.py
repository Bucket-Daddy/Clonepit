#Shop script
import pygame

from backend.shop_restock import shopItems
from frontend.mouseCheck import isSelected
from frontend.text_rendering import renderText
from backend.shelf_backend import (shelfRoom, shelfItems, passiveTrigger)
from config.game_config import (tickets, coins)
from frontend.atm_room import debtAmount

class ShopRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 16 * overallScale)
        self.titleFont = pygame.font.Font(None, size = 32 * overallScale)

    def draw(self, screen):
        global tickets, coins, shelfRoom, shelfItems
        # danner baggrunden
        self.shop_room = pygame.Surface((1200, 750), pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (1200, 750))
        self.shop_room.blit(background, (-3, -3))

        #Loader billeder
        storePedestal = pygame.image.load('assets/StorePedestal.png')
        priceTag = pygame.image.load('assets/PedestalPrice.png')
        refresh = pygame.image.load('assets/RefreshPedestal.png')
        storeSign = pygame.image.load('assets/StoreSign.png')
        glass = pygame.image.load('assets/GlassPane.png')

        #Skalerer billeder
        storePedestal = pygame.transform.scale(storePedestal, (storePedestal.get_width(), storePedestal.get_height()))
        priceTag = pygame.transform.scale(priceTag, (priceTag.get_width(), priceTag.get_height()))
        refresh = pygame.transform.scale(refresh, (refresh.get_width(), refresh.get_height()))
        storeSign = pygame.transform.scale(storeSign, (storeSign.get_width() * 0.5, storeSign.get_height() * 0.5))
        glass = pygame.transform.scale(glass, (glass.get_width(), glass.get_height()))

        for item in shopItems:
            if item != 0:
                item.sprite = pygame.transform.scale(item.sprite, (glass.get_width(), glass.get_height()))
                item.sprite.set_colorkey((51,46,46))

        # butikkens skilt
        self.shop_room.blit(storeSign, (self.shop_room.get_width() // 2 - storeSign.get_width() // 2, self.shop_room.get_height() // 30 - storePedestal.get_height() // 230))

        # butikkens 5 standere
        self.shop_room.blit(storePedestal, (self.shop_room.get_width() // 2 - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2))
        self.shop_room.blit(priceTag, (self.shop_room.get_width() // 2 - storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 8 - 2.8))

        self.shop_room.blit(storePedestal, (self.shop_room.get_width() // 2 + storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2))
        self.shop_room.blit(priceTag, (self.shop_room.get_width() // 2 + storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 8 - 2.8))
        
        self.shop_room.blit(storePedestal, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2))
        self.shop_room.blit(priceTag, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 8 - 2.8))
        
        self.shop_room.blit(storePedestal, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2))
        self.shop_room.blit(priceTag, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() - storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 8 - 2.8))

        # refresh standeren
        self.shop_room.blit(refresh, (self.shop_room.get_width() // 2 + storePedestal.get_width() + storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2))
        self.shop_room.blit(priceTag, (self.shop_room.get_width() // 2 + storePedestal.get_width() + storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 8 - 2.8))

        #Selve items i shop
        for i in range(4):
            if shopItems[i] != 0:
                self.shop_room.blit(shopItems[i].sprite, (200 + i * 100, 200))
                self.shop_room.blit(self.font.render(str(shopItems[i].cost), True, (240, 170, 41)), ((240 + i * 100, 300)))
                if isSelected(shopItems[i].sprite, (200 + i * 100, 200), self.shop_room):
                    tooltip = pygame.Surface((self.shop_room.get_width() // 2, self.shop_room.get_height() // 4))
                    #Viser navn og beskrivelse når musen føres over en item
                    tooltip.fill((0,0,0))
                    name = self.titleFont.render(shopItems[i].name, True, (240, 170, 41))
                    tooltip.blit(name, name.get_rect(center=(tooltip.get_width() / 2, 40)))
                    renderText(shopItems[i].description, self.font, tooltip, (8, 70), tooltip.get_width() - 8)
                    #Køber item hvis spilleren clicker på den, spilleren har råd til den og spilleren har plads til den
                    self.shop_room.blit(tooltip, (self.shop_room.get_width() // 4, 0))
                    if pygame.mouse.get_just_pressed()[0] and tickets >= shopItems[i].cost and shelfRoom >= shopItems[i].space:
                        tickets -= shopItems[i].cost
                        shelfRoom -= shopItems[i].space
                        shelfItems.append(shopItems[i])
                        shopItems[i] = 0
                        passiveTrigger(shelfItems[-1])
    

        # glas oven på holderne
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 + storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))

        screen.blit(self.shop_room, (0, 0))
