#Phone script
import pygame


class PhoneRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)

        #Opretter phone surface og danner baggrunden
        self.phone = pygame.Surface((1200, 750), pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (1200, 750))
        self.phone.blit(background, (0, 0))

        #Placeholder tekst
        textPhone = self.font.render('--- PHONE ---', True, (246, 250, 10))
        textComingSoon = self.font.render('coming soon', True, (246, 250, 10))
        self.phone.blit(textPhone, textPhone.get_rect(center=(600, 355)))
        self.phone.blit(textComingSoon, textComingSoon.get_rect(center=(600, 385)))

    def draw(self, screen):
        screen.blit(self.phone, (0, 0))
