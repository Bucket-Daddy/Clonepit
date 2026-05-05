#Shelf room
import pygame
from frontend.mouseCheck import isSelected
import config.game_config as config
from frontend.text_rendering import renderText

class shelfRoom:

    def __init__(self):
        #Opretter fonts
        self.font = pygame.font.Font(None, size = 32)
        self.titleFont = pygame.font.Font(None, size = 64)

        #Opretter shelf surface og danner baggrunden
        self.shelf_room = pygame.Surface((1200, 750), pygame.SRCALPHA)
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, (1200, 750))

    def draw(self, screen):
        #Indsætter baggrunden
        self.shelf_room.blit(self.background, (-3, -3))

        for item in config.shelfItems:
            item.sprite = pygame.transform.scale(item.sprite, (100,100))
            item.sprite.set_colorkey((51,46,46))

            #Selve items i shelf
        for i in range(len(config.shelfItems)):
            self.shelf_room.blit(config.shelfItems[i].sprite, (200 + i * 100, 200))
            self.shelf_room.blit(self.font.render(str(config.shelfItems[i].cost), True, (240, 170, 41)), ((240 + i * 100, 300)))

        for i in range(len(config.shelfItems)):
            if i < len(config.shelfItems):
                if isSelected(config.shelfItems[i].sprite, (200 + i * 100, 200), self.shelf_room):
                    tooltip = pygame.Surface((self.shelf_room.get_width() // 2, self.shelf_room.get_height() // 4))
                    #Viser navn og beskrivelse når musen føres over en item
                    tooltip.fill((0,0,0))
                    name = self.titleFont.render(config.shelfItems[i].name, True, (240, 170, 41))
                    tooltip.blit(name, name.get_rect(center=(tooltip.get_width() / 2, 40)))
                    renderText(config.shelfItems[i].description, self.font, tooltip, (8, 70), tooltip.get_width() - 8)
                    self.shelf_room.blit(tooltip, (self.shelf_room.get_width() // 4, 0))
                    if pygame.mouse.get_just_pressed()[0]:
                        config.tickets += config.shelfItems[i].cost
                        config.shelfRoom -= config.shelfItems[i].space
                        config.shelfItems[i].sold()
                        config.shelfItems.pop(i)

        self.shelf_room.blit(self.font.render(str(len(config.shelfItems) - config.shelfItems.count(0)) + '/' + str(config.shelfSpace), True, (240, 170, 41)), ((600, 700)))
        
        screen.blit(self.shelf_room, (0, 0))
