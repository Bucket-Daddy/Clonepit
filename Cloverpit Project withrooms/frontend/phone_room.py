#Phone script
import pygame


class PhoneRoom:

    def __init__(self, resolution, xScaling, yScaling):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)

        # danner baggrunden
        self.phone_room = pygame.Surface(resolution, pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (1200, 750))
        self.phone_room.blit(background, (-3, -3))

        # Loader billeder
        phoneResting = pygame.image.load('assets/Phone (resting).png')
        phoneActive = pygame.image.load('assets/Phone (active).png')

        # Skalerer billeder
        phoneResting = pygame.transform.scale(phoneResting, (phoneResting.get_width() * 0.8, phoneResting.get_height() * 0.8))
        phoneActive = pygame.transform.scale(phoneActive, (phoneActive.get_width() * 1.2, phoneActive.get_height() * 1.2))
        
        # til maskering og hitbox osv.
        phoneInteract = pygame.image.load('assets/Phone (interraction).png')
        phoneInteract = pygame.transform.scale(phoneInteract, (phoneInteract.get_width() * 0.5, phoneInteract.get_height() * 0.5))
        
        # Telefoner
        # self.phone_room.blit(phoneResting, (self.phone_room.get_width() // 6 - phoneResting.get_width() // 2, 200))
        self.phone_room.blit(phoneActive, (self.phone_room.get_width() // 3.2 - phoneActive.get_width() // 2, 30))

        # telefonens teksbokse
        pygame.draw.rect(self.phone_room, (0, 0, 0), (self.phone_room.get_width() // 3.2 + phoneActive.get_width() // 1.75, self.phone_room.get_width() // 50, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 4), 0)
        pygame.draw.rect(self.phone_room, (232, 132, 44), (self.phone_room.get_width() // 3.2 + phoneActive.get_width() // 1.75, self.phone_room.get_width() // 50, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 4), 5)
        
        # valgboks 1, 2 og 3
        pygame.draw.rect(self.phone_room, (0, 0, 0), (self.phone_room.get_width() // 25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 0)
        pygame.draw.rect(self.phone_room, (246, 250, 10), (self.phone_room.get_width() // 25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 4)
        
        pygame.draw.rect(self.phone_room, (0, 0, 0), (self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 0)
        pygame.draw.rect(self.phone_room, (246, 250, 10), (self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 4)
        
        pygame.draw.rect(self.phone_room, (0, 0, 0), (self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 0)
        pygame.draw.rect(self.phone_room, (246, 250, 10), (self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 4)

        # telefonens tekst
        textPhone = self.font.render('--- UNKNOWN NUMBER ---', True, (232, 132, 44))
        textRandomMessage = self.font.render('randomized message here', True, (232, 132, 44))
        textAnswerOne = self.font.render('Answer 1', True, (246, 250, 10))
        textAnswerTwo = self.font.render('Answer 2', True, (246, 250, 10))
        textAnswerThree = self.font.render('Answer 3', True, (246, 250, 10))
        self.phone_room.blit(textPhone, textPhone.get_rect(center=(self.phone_room.get_width() // 3.2 + phoneActive.get_width() // 1.75 + self.phone_room.get_width() // 5, self.phone_room.get_width() // 25)))
        self.phone_room.blit(textRandomMessage, textRandomMessage.get_rect(center=(self.phone_room.get_width() // 3.2 + phoneActive.get_width() // 1.75 + self.phone_room.get_width() // 5, self.phone_room.get_width() // 15)))        

        
        

    def draw(self, screen, resolution, xScaling, yScaling):
        screen.blit(self.phone_room, (0, 0))
