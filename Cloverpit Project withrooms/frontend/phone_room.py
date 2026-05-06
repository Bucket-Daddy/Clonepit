#Phone script
import pygame
import config.game_config as config
from frontend.text_rendering import renderText
from backend.roll_phone import (phoneOptions, rollPhone)

class PhoneRoom:

    def __init__(self, resolution, xScaling, yScaling):

        config.phoneIsActive = True
        self.font = pygame.font.Font(None, size = round(32 * xScaling))

        # danner baggrunden
        self.phone_room = pygame.Surface(resolution, pygame.SRCALPHA)
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, resolution)

        # Loader billeder
        self.phoneResting = pygame.image.load('assets/Phone (resting).png')
        self.phoneActive = pygame.image.load('assets/Phone (active).png')

        # Skalerer billeder
        self.phoneResting = pygame.transform.scale(self.phoneResting, (self.phoneResting.get_width() * 0.8 * xScaling, self.phoneResting.get_height() * 0.8 * yScaling))
        self.phoneActive = pygame.transform.scale(self.phoneActive, (self.phoneActive.get_width() * 1.2 * xScaling, self.phoneActive.get_height() * 1.2 * yScaling))
        
        # til maskering og hitbox osv.
        phoneInteract = pygame.image.load('assets/Phone (interraction).png')
        phoneInteract = pygame.transform.scale(phoneInteract, (phoneInteract.get_width() * 0.5, phoneInteract.get_height() * 0.5))
        

    def draw(self, screen, resolution, xScaling, yScaling):

        #Baggrund
        self.phone_room.blit(self.background, (-3, -3))

        if config.phoneIsActive and config.debtNum > 1:
            #Telefonen
            self.phone_room.blit(self.phoneActive, (self.phone_room.get_width() // 3.2 - self.phoneActive.get_width() // 2, 30))

            #Telefonens tekstbokse
            pygame.draw.rect(self.phone_room, (0, 0, 0), (self.phone_room.get_width() // 3.2 + self.phoneActive.get_width() // 1.75, self.phone_room.get_width() // 50, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 4), 0)
            pygame.draw.rect(self.phone_room, (232, 132, 44), (self.phone_room.get_width() // 3.2 + self.phoneActive.get_width() // 1.75, self.phone_room.get_width() // 50, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 4), 5)
        
            #Valgboks 1
            choiceBox1 = pygame.Rect(self.phone_room.get_width() // 25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8)
            pygame.draw.rect(self.phone_room, (0, 0, 0), choiceBox1, 0)
            pygame.draw.rect(self.phone_room, (246, 250, 10), (self.phone_room.get_width() // 25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 4)
            #Navnet på valgmuligheden
            renderText(phoneOptions[0].name, self.font, self.phone_room, (self.phone_room.get_width() // 20, self.phone_room.get_width() // 2.4), self.phone_room.get_width() // 3.6)
            #Beskrivelsen af valgmuligheden
            renderText(phoneOptions[0].description, self.font, self.phone_room, (self.phone_room.get_width() // 20, self.phone_room.get_width() // 2.4 + 48 * yScaling), self.phone_room.get_width() // 3.6)
            if choiceBox1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                for i in range(config.phonecallRep + 1):
                    phoneOptions[0].trigger()
                config.phoneIsActive = False
                rollPhone()


            #Valgboks 2
            choiceBox2 = pygame.Rect((self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8))
            pygame.draw.rect(self.phone_room, (0, 0, 0), choiceBox2, 0)
            pygame.draw.rect(self.phone_room, (246, 250, 10), (self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 4)
            #Navnet på valgmuligheden
            renderText(phoneOptions[1].name, self.font, self.phone_room, (self.phone_room.get_width() // 20 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.4), self.phone_room.get_width() // 3.6)
            #Beskrivelsen af valgmuligheden
            renderText(phoneOptions[1].description, self.font, self.phone_room, (self.phone_room.get_width() // 20 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.4 + 48 * yScaling), self.phone_room.get_width() // 3.6)
            if choiceBox2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                for i in range(config.phonecallRep + 1):
                    phoneOptions[1].trigger()
                config.phoneIsActive = False
                rollPhone()
                    

            #Valgboks 3
            choiceBox3 = pygame.Rect(self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8)
            pygame.draw.rect(self.phone_room, (0, 0, 0), choiceBox3, 0)
            pygame.draw.rect(self.phone_room, (246, 250, 10), (self.phone_room.get_width() // 25 + self.phone_room.get_width() // 3.25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.5, self.phone_room.get_width() // 3.4, self.phone_room.get_width() // 8), 4)
            #Navnet på valgmuligheden
            renderText(phoneOptions[2].name, self.font, self.phone_room, (self.phone_room.get_width() // 20 + self.phone_room.get_width() // 3.25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.4), self.phone_room.get_width() // 3.6)
            #Beskrivelsen af valgmuligheden
            renderText(phoneOptions[2].description, self.font, self.phone_room, (self.phone_room.get_width() // 20 + self.phone_room.get_width() // 3.25 + self.phone_room.get_width() // 3.25, self.phone_room.get_width() // 2.4 + 48 * yScaling), self.phone_room.get_width() // 3.6)
            if choiceBox3.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                for i in range(config.phonecallRep + 1):
                    phoneOptions[2].trigger()
                config.phoneIsActive = False
                rollPhone()

            
            #Telefonens tekst
            textPhone = self.font.render('--- UNKNOWN NUMBER ---', True, (232, 132, 44))
            textRandomMessage = self.font.render('randomized message here', True, (232, 132, 44))
            self.phone_room.blit(textPhone, textPhone.get_rect(center=(self.phone_room.get_width() // 3.2 + self.phoneActive.get_width() // 1.75 + self.phone_room.get_width() // 5, self.phone_room.get_width() // 25)))
            self.phone_room.blit(textRandomMessage, textRandomMessage.get_rect(center=(self.phone_room.get_width() // 3.2 + self.phoneActive.get_width() // 1.75 + self.phone_room.get_width() // 5, self.phone_room.get_width() // 15)))

        else:
            self.phone_room.blit(self.phoneResting, (self.phone_room.get_width() // 6 - self.phoneResting.get_width() // 2, 200))

        screen.blit(self.phone_room, (0, 0))
