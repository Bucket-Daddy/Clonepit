#Shop script
import pygame


class ShopRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)

        # danner baggrunden
        self.shop_room = pygame.Surface((1200, 700), pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (self.shop_room.get_width(), self.shop_room.get_height()))
        self.shop_room.blit(background, (-5, -5))
        self. shop_room.blit(storeSign, (220, 30))

        #Loader billeder
        storePedestals = pygame.image.load('assets/StorePedestals.png')
        storeSign = pygame.image.load('assets/StoreSign.png')
        glass = pygame.image.load('assets/Glass_panes.png.png')

        #Skalerer billeder
        storePedestals = pygame.transform.scale(storePedestals, (storePedestals.get_width(), storePedestals.get_height()))
        storeSign = pygame.transform.scale(storeSign, (storeSign.get_width() * 0.5, storeSign.get_height() * 0.5))
        glass = pygame.transform.scale(glass, (glass.get_width(), glass.get_height()))

        # Holdere til items i shop
        self.shop_room.blit(storePedestals, (350, 170))

        # Selve items i shop

        # glas oven på holderne
        self.shop_room.blit(glass, (405, 332))

    def draw(self, screen):
        screen.blit(self.shop_room, (0, 0))
