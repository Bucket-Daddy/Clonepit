import pygame

pygame.init()
posterScale = 0.80
overallScale = 2
font = pygame.font.Font(None, size = 15 * overallScale)

pygame.display.set_caption('Clonepit Slots - Posters')
screen = pygame.display.set_mode((1200, 700))

#Loader billeder
slotMachine = pygame.image.load('assets/SlotMachine.png')
button = pygame.image.load('assets/Button.png')
crancker = pygame.image.load('assets/Handle.png')

#Skalerer billeder
smallMachine = pygame.transform.scale(slotMachine, (slotMachine.get_width() * 0.25, slotMachine.get_height() * 0.25))
smallButton = pygame.transform.scale(button, (button.get_width() * 0.25, button.get_height() * 0.25))
smallCrancker = pygame.transform.scale(crancker, (crancker.get_width() * 0.25, crancker.get_height() * 0.25))

bigMachine = pygame.transform.scale(slotMachine, (slotMachine.get_width() * 0.8, slotMachine.get_height() * 0.8))
bigButton = pygame.transform.scale(button, (button.get_width() * 0.8, button.get_height() * 0.8))
bigCrancker = pygame.transform.scale(crancker, (crancker.get_width() * 0.8, crancker.get_height() * 0.8))

# danner baggrunden
background = pygame.image.load('assets/Background.png')
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
slots_room = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
slots_room.blit(background, (-5, -5))

# start text på skærmen
slotsText = font.render('! SPIN 2 WIN !', True, (246, 250, 10))

# lille maskine på baggrunden
slots_room.blit(smallCrancker, (360, 90))
slots_room.blit(smallMachine, (-20, 150))
slots_room.blit(smallButton, (358, 298))
slots_room.blit(slotsText, (182, 240))

# stor maskine på baggrunden
#slots_room.blit(bigCrancker, (800, -250))
#slots_room.blit(bigMachine, (-420, -50))
#slots_room.blit(bigButton, (788, 420))

##############################################################################################################
# the window
running = True
clock = pygame.time.Clock()

deltaTime = 0.1

while running:
    screen.fill((0, 0, 0))
    screen.blit(slots_room, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    deltaTime = max(0.001, min(0.1, deltaTime))


pygame.quit()