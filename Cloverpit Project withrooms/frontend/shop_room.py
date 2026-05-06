#Shop script
import pygame

from backend.shop_restock import shopItems
from frontend.mouseCheck import isSelected
from backend.shop_restock import shopRestock
from frontend.text_rendering import renderText
from backend.shelf_backend import passiveTrigger
import config.game_config as config

class ShopRoom:

    def __init__(self, resolution, xScaling, yScaling):

        overallScale = 2
        self.font = pygame.font.Font(None, size = round(16 * overallScale * yScaling))
        self.titleFont = pygame.font.Font(None, size = round(32 * overallScale * yScaling))
        self.shop_room = pygame.Surface(resolution, pygame.SRCALPHA)
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, resolution)

        #Loader billeder
        self.storePedestal = pygame.image.load('assets/StorePedestal.png')
        self.priceTag = pygame.image.load('assets/PedestalPrice.png')
        self.refresh = pygame.image.load('assets/restock button.png')
        self.storeSign = pygame.image.load('assets/StoreSign.png')
        self.glass = pygame.image.load('assets/glassPane.png')

        #Skalerer billeder
        self.storePedestal = pygame.transform.scale(self.storePedestal, (self.storePedestal.get_width() * xScaling, self.storePedestal.get_height() * yScaling))
        self.priceTag = pygame.transform.scale(self.priceTag, (self.priceTag.get_width() * xScaling, self.priceTag.get_height() * yScaling))
        self.storeSign = pygame.transform.scale(self.storeSign, (self.storeSign.get_width() * 0.5 * xScaling, self.storeSign.get_height() * 0.5 * yScaling))
        self.glass = pygame.transform.scale(self.glass, (self.glass.get_width() * xScaling, self.glass.get_height() * yScaling))
        self.refresh = pygame.transform.scale(self.refresh, (self.glass.get_width(), self.glass.get_height()))
        self.refresh.set_colorkey((255, 255, 255))

        self.pedestalX = self.shop_room.get_width() // 2
        self.pedestalY = self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 2

    def draw(self, screen, resolution, xScaling, yScaling):
        # danner baggrunden
        self.shop_room.blit(self.background, (-3, -3))

        # butikkens skilt
        self.shop_room.blit(self.storeSign, (self.shop_room.get_width() // 2 - self.storeSign.get_width() // 2, self.shop_room.get_height() // 30 - self.storePedestal.get_height() // 230))

        # butikkens 5 standere
        self.shop_room.blit(self.storePedestal, (self.pedestalX - self.storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 2))
        self.shop_room.blit(self.priceTag, (self.pedestalX - self.storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 8 - 2.8))

        self.shop_room.blit(self.storePedestal, (self.pedestalX + self.storePedestal.get_width() // 2, self.pedestalY))
        self.shop_room.blit(self.priceTag, (self.pedestalX + self.storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 8 - 2.8))
        
        self.shop_room.blit(self.storePedestal, (self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() // 2, self.pedestalY))
        self.shop_room.blit(self.priceTag, (self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 8 - 2.8))
        
        self.shop_room.blit(self.storePedestal, (self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() - self.storePedestal.get_width() // 2, self.pedestalY))
        self.shop_room.blit(self.priceTag, (self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() - self.storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 8 - 2.8))

        #refresh standeren
        self.shop_room.blit(self.refresh, (self.pedestalX + self.storePedestal.get_width() + self.storePedestal.get_width() // 2, self.pedestalY))
        self.shop_room.blit(self.priceTag, (self.pedestalX + self.storePedestal.get_width() + self.storePedestal.get_width() // 2 + 2.8, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 8 - 2.8))

        if isSelected(self.refresh, (self.pedestalX + self.storePedestal.get_width() + self.storePedestal.get_width() // 2, self.pedestalY), self.shop_room) and pygame.mouse.get_just_pressed()[0]:
            shopRestock()

        for item in shopItems:
            if item != 0:
                item.sprite = pygame.transform.scale(item.sprite, (self.glass.get_width(), self.glass.get_height()))
                item.sprite.set_colorkey((51,46,46))


        #Selve items i shop
        for i in range(4):
            if shopItems[i] != 0:
                self.shop_room.blit(shopItems[i].sprite, ((self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() - self.storePedestal.get_width() // 2) + i * 142 * xScaling, self.pedestalY))
                self.shop_room.blit(self.font.render(str(shopItems[i].cost), True, (240, 170, 41)), (((self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() - self.storePedestal.get_width() // 2 + 40) + i * 142 * xScaling, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 8 + 5)))

        for i in range(4):
            if shopItems[i] != 0:
                if isSelected(shopItems[i].sprite, ((self.pedestalX - self.storePedestal.get_width() - self.storePedestal.get_width() - self.storePedestal.get_width() // 2) + i * 142 * xScaling, self.pedestalY), self.shop_room):
                    tooltip = pygame.Surface((self.shop_room.get_width() // 2, self.shop_room.get_height() // 4))
                    #Viser navn og beskrivelse når musen føres over en item
                    tooltip.fill((0,0,0))
                    name = self.titleFont.render(shopItems[i].name, True, (240, 170, 41))
                    tooltip.blit(name, name.get_rect(center=(tooltip.get_width() / 2, 40 * yScaling)))
                    renderText(shopItems[i].description, self.font, tooltip, (8, 70 * yScaling), tooltip.get_width() - 8)
                    #Køber item hvis spilleren clicker på den, spilleren har råd til den og spilleren har plads til den
                    self.shop_room.blit(tooltip, (self.shop_room.get_width() // 4, 0))
                    if pygame.mouse.get_just_pressed()[0] and config.tickets >= shopItems[i].cost and config.shelfSpace - len(config.shelfItems) >= shopItems[i].space:
                        config.tickets -= shopItems[i].cost
                        config.shelfRoom -= shopItems[i].space
                        config.shelfItems.append(shopItems[i])
                        shopItems[i] = 0
                        passiveTrigger(config.shelfItems[-1])

        # glas oven på holderne
        self.shop_room.blit(self.glass, (self.shop_room.get_width() // 2 - self.storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(self.glass, (self.shop_room.get_width() // 2 + self.storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(self.glass, (self.shop_room.get_width() // 2 - self.storePedestal.get_width() - self.storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(self.glass, (self.shop_room.get_width() // 2 - self.storePedestal.get_width() - self.storePedestal.get_width() - self.storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - self.storePedestal.get_height() // 2 + 2.8))

        screen.blit(self.shop_room, (0, 0))
