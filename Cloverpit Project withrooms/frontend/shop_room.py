#Shop script
import pygame


class ShopRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)

        #Opretter shop surface og danner baggrunden
        self.shop = pygame.Surface((1200, 750), pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (1200, 750))
        self.shop.blit(background, (0, 0))

        #Placeholder tekst
        textShop = self.font.render('--- SHOP ---', True, (246, 250, 10))
        textComingSoon = self.font.render('coming soon', True, (246, 250, 10))
        self.shop.blit(textShop, textShop.get_rect(center=(600, 355)))
        self.shop.blit(textComingSoon, textComingSoon.get_rect(center=(600, 385)))

    def draw(self, screen):
        screen.blit(self.shop, (0, 0))
