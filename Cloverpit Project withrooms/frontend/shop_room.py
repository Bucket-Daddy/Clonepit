#Shop script
import pygame
from backend.shop_restock import shopItems

class ShopRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)

    def draw(self, screen):
        
        # danner baggrunden
        self.shop_room = pygame.Surface((1200, 750), pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (self.shop_room.get_width(), self.shop_room.get_height()))
        self.shop_room.blit(background, (-5, -5))

        #Loader billeder
        storePedestals = pygame.image.load('assets/StorePedestals.png')
        storeSign = pygame.image.load('assets/StoreSign.png')
        glass = pygame.image.load('assets/Glass_panes.png.png')

        #Skalerer billeder
        storePedestals = pygame.transform.scale(storePedestals, (storePedestals.get_width(), storePedestals.get_height()))
        storeSign = pygame.transform.scale(storeSign, (storeSign.get_width() * 0.5, storeSign.get_height() * 0.5))
        glass = pygame.transform.scale(glass, (glass.get_width(), glass.get_height()))

        for item in shopItems:
            item.sprite = pygame.transform.scale(item.sprite, (100, 100))
            item.sprite.set_colorkey((51,46,46))

        #Holdere til items i shop
        self.shop_room.blit(storePedestals, (350, 170))

        #Skilt til shop
        self.shop_room.blit(storeSign, (220, 30))

        #Selve items i shop
        self.shop_room.blit(shopItems[0].sprite, (20, 20))
        self.shop_room.blit(shopItems[1].sprite, (120, 20))
        self.shop_room.blit(shopItems[2].sprite, (220, 20))
        self.shop_room.blit(shopItems[3].sprite, (320, 20))

        #Prisen af items i shop
        self.shop_room.blit(self.font.render(str(shopItems[0].cost), True, (240, 170, 41)), (60, 120))
        self.shop_room.blit(self.font.render(str(shopItems[1].cost), True, (240, 170, 41)), (160, 120))
        self.shop_room.blit(self.font.render(str(shopItems[2].cost), True, (240, 170, 41)), (260, 120))
        self.shop_room.blit(self.font.render(str(shopItems[3].cost), True, (240, 170, 41)), (360, 120))

        #glas oven på holderne
        self.shop_room.blit(glass, (405, 332))

        #Render til skærmen
        screen.blit(self.shop_room, (0, 0))
