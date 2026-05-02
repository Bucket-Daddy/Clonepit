#Shop script
import pygame


class ShopRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)

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

        # Selve items i shop

        # glas oven på holderne
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 + storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))
        self.shop_room.blit(glass, (self.shop_room.get_width() // 2 - storePedestal.get_width() - storePedestal.get_width() - storePedestal.get_width() // 2, self.shop_room.get_height() // 1.7 - storePedestal.get_height() // 2 + 2.8))

    def draw(self, screen):
        screen.blit(self.shop_room, (0, 0))
