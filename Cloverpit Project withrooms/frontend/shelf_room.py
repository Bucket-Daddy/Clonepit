#Shelf room
import pygame
from frontend.mouseCheck import isSelected
import config.game_config as config
from frontend.text_rendering import renderText

class shelfRoom:

    def __init__(self, resolution, xScaling, yScaling):
        #Opretter fonts
        self.font = pygame.font.Font(None, size = round(32 * xScaling))
        self.titleFont = pygame.font.Font(None, size = round(64 * xScaling))

        #Opretter shelf surface og danner baggrunden
        self.shelf_room = pygame.Surface(resolution, pygame.SRCALPHA)
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, resolution)
        self.shelfPedestal = pygame.image.load('assets/StorePedestal.png')
        self.shelfPedestal = pygame.transform.scale(self.shelfPedestal, (round(self.shelfPedestal.get_width()  * xScaling), round(self.shelfPedestal.get_height() * yScaling)))
        self.priceTag = pygame.image.load('assets/PedestalPrice.png')
        self.priceTag = pygame.transform.scale(self.priceTag, (round(self.priceTag.get_width()  * xScaling), round(self.priceTag.get_height() * yScaling)))
        
    def draw(self, screen, resolution, xScaling, yScaling):
        #Indsætter baggrunden
        self.shelf_room.blit(self.background, (-3, -3))

        for item in config.shelfItems:
            item.sprite = pygame.transform.scale(item.sprite, (100 * xScaling, 100 * yScaling))
            item.sprite.set_colorkey((51,46,46))

        #Pedestals i shelf
        for i in range(12):
            self.shelf_room.blit(self.shelfPedestal, ((200 + i % 6 * 133) * xScaling, (200 + ((i) // 6) * 200) * yScaling))
            self.shelf_room.blit(self.priceTag, ((202 + i % 6 * 133) * xScaling, (300 + ((i) // 6) * 200) * yScaling))

        #Selve items i shelf
        for i in range(len(config.shelfItems)):
            self.shelf_room.blit(config.shelfItems[i].sprite, ((200 + i * 133) * xScaling, 200 * yScaling))
            self.shelf_room.blit(self.font.render(str(config.shelfItems[i].cost), True, (240, 170, 41)), ((240 + i * 133) * xScaling, 310 * yScaling))

        for i in range(len(config.shelfItems)):
            if i < len(config.shelfItems):
                if isSelected(config.shelfItems[i].sprite, ((200 + i * 133) * xScaling, 200 * yScaling), self.shelf_room):
                    tooltip = pygame.Surface((self.shelf_room.get_width() // 2, self.shelf_room.get_height() // 4))
                    #Viser navn og beskrivelse når musen føres over en item
                    tooltip.fill((0,0,0))
                    name = self.titleFont.render(config.shelfItems[i].name, True, (240, 170, 41))
                    tooltip.blit(name, name.get_rect(center=(tooltip.get_width() / 2, 40 * yScaling)))
                    renderText(config.shelfItems[i].description, self.font, tooltip, (8 * xScaling, 70 * yScaling), tooltip.get_width() - 8 * xScaling)
                    self.shelf_room.blit(tooltip, (self.shelf_room.get_width() // 4, 0))
                    if config.shelfItems[i].type == 'button':
                        self.shelf_room.blit(self.font.render('Charges: ' + str(config.shelfItems[i].charges) + '/' + str(config.shelfItems[i].chargeSlots), True, (250, 246, 15)), ((240 + i * 133) * xScaling - self.font.size('Charges: 4/4')[0] / 2, 168 * yScaling))
                    if pygame.mouse.get_just_pressed()[0]:
                        config.tickets += config.shelfItems[i].cost
                        config.shelfRoom -= config.shelfItems[i].space
                        config.shelfItems[i].sold()
                        config.shelfItems.pop(i)

        self.shelf_room.blit(self.font.render(str(len(config.shelfItems) - config.shelfItems.count(0)) + '/' + str(config.shelfSpace), True, (240, 170, 41)), ((600 * xScaling, 700 * yScaling)))
        
        screen.blit(self.shelf_room, (0, 0))
