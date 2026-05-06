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
        self.font      = pygame.font.Font(None, size=round(16 * overallScale * yScaling))
        self.titleFont = pygame.font.Font(None, size=round(32 * overallScale * yScaling))
        self.shop_room = pygame.Surface(resolution, pygame.SRCALPHA)
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, resolution)

        # Loader og skalerer billeder
        self.storePedestal = pygame.image.load('assets/StorePedestal.png')
        self.priceTag      = pygame.image.load('assets/PedestalPrice.png')
        self.refresh       = pygame.image.load('assets/restock button.png')
        self.storeSign     = pygame.image.load('assets/StoreSign.png')
        self.glass         = pygame.image.load('assets/glassPane.png')

        self.storePedestal = pygame.transform.scale(self.storePedestal,
            (round(self.storePedestal.get_width()  * xScaling),
             round(self.storePedestal.get_height() * yScaling)))
        self.priceTag = pygame.transform.scale(self.priceTag,
            (round(self.priceTag.get_width()  * xScaling),
             round(self.priceTag.get_height() * yScaling)))
        self.storeSign = pygame.transform.scale(self.storeSign,
            (round(self.storeSign.get_width()  * 0.5 * xScaling),
             round(self.storeSign.get_height() * 0.5 * yScaling)))
        self.glass = pygame.transform.scale(self.glass,
            (round(self.glass.get_width()  * xScaling),
             round(self.glass.get_height() * yScaling)))
        self.refresh = pygame.transform.scale(self.refresh,
            (self.glass.get_width(), self.glass.get_height()))
        self.refresh.set_colorkey((255, 255, 255))

        # Pedestal bredde bruges som spacing
        # centreres som en gruppe midt på skærmen.
        pw = self.storePedestal.get_width()   # skaleret pedestal bredde
        ph = self.storePedestal.get_height()

        # 5 standere med bredde pw centreret: gruppe bredde = 5 * pw
        # centerX er skærmens midte: gruppe starter ved centerX - 2.5 * pw
        centerX = resolution[0] // 2
        self.groupStartX = centerX - pw * 2 - pw // 2   # venstre kant af stander 0

        # Y: standerne placeres i nedre tredjedel
        self.pedestalY    = round(resolution[1] / 1.7 - ph / 2)
        self.priceTagY    = round(resolution[1] / 1.7 - ph / 8)
        self.glassY       = self.pedestalY   # glas starter samme Y som pedestal

        # Forudberegn X for alle 5 standere (0-3 = items, 4 = restock)
        self.pedestalXs = [self.groupStartX + i * pw for i in range(5)]

    def draw(self, screen, resolution, xScaling, yScaling):
        self.shop_room.blit(self.background, (-3, -3))

        pw = self.storePedestal.get_width()
        ph = self.storePedestal.get_height()

        # Butikkens skilt centreret øverst
        self.shop_room.blit(self.storeSign,
            (resolution[0] // 2 - self.storeSign.get_width() // 2,
             round(resolution[1] * 0.02)))

        # Tegn de 4 item-standere + 1 restock-stander
        for i in range(4):
            self.shop_room.blit(self.storePedestal, (self.pedestalXs[i], self.pedestalY))
            self.shop_room.blit(self.priceTag,      (self.pedestalXs[i], self.priceTagY))

        # Restock stander (index 4)
        self.shop_room.blit(self.refresh,   (self.pedestalXs[4], self.pedestalY))
        self.shop_room.blit(self.priceTag,  (self.pedestalXs[4], self.priceTagY))

        if isSelected(self.refresh, (self.pedestalXs[4], self.pedestalY), self.shop_room) \
                and pygame.mouse.get_just_pressed()[0]:
            shopRestock()

        # Skaler item sprites til glaspanelstørrelse
        for item in shopItems:
            if item != 0:
                item.sprite = pygame.transform.scale(
                    item.sprite, (self.glass.get_width(), self.glass.get_height()))
                item.sprite.set_colorkey((51, 46, 46))

        # Tegn items oven på standerne
        for i in range(4):
            if shopItems[i] != 0:
                self.shop_room.blit(shopItems[i].sprite, (self.pedestalXs[i], self.pedestalY))
                costText = self.font.render(str(shopItems[i].cost), True, (240, 170, 41))
                self.shop_room.blit(costText,
                    costText.get_rect(center=(self.pedestalXs[i] + pw // 2, self.priceTagY + self.priceTag.get_height() // 2)))

        # Hover tooltip og buying logic for items
        for i in range(4):
            if shopItems[i] != 0:
                if isSelected(shopItems[i].sprite, (self.pedestalXs[i], self.pedestalY), self.shop_room):
                    tooltip = pygame.Surface((resolution[0] // 2, resolution[1] // 4))
                    tooltip.fill((0, 0, 0))
                    pygame.draw.rect(tooltip, (120, 95, 26), tooltip.get_rect(), 2, border_radius=6)
                    name = self.titleFont.render(shopItems[i].name, True, (240, 170, 41))
                    tooltip.blit(name, name.get_rect(center=(tooltip.get_width() // 2, round(40 * yScaling))))
                    renderText(shopItems[i].description, self.font, tooltip,
                               (8, round(70 * yScaling)), tooltip.get_width() - 8)
                    self.shop_room.blit(tooltip, (resolution[0] // 4, 0))

                    if (pygame.mouse.get_just_pressed()[0]
                            and config.tickets >= shopItems[i].cost
                            and config.shelfSpace - len(config.shelfItems) >= shopItems[i].space):
                        config.tickets  -= shopItems[i].cost
                        config.shelfRoom -= shopItems[i].space
                        config.shelfItems.append(shopItems[i])
                        shopItems[i] = 0
                        passiveTrigger(config.shelfItems[-1])

        # Glas oven på de 4 item standere
        for i in range(4):
            self.shop_room.blit(self.glass, (self.pedestalXs[i], self.glassY))

        screen.blit(self.shop_room, (0, 0))
