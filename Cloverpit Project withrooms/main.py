# main.py
import pygame

from frontend.slot_room import SlotRoom
from frontend.atm_room import ATMRoom
from frontend.posters_room import PostersRoom
from frontend.shop_room import ShopRoom
from frontend.phone_room import PhoneRoom
from frontend.shelf_room import shelfRoom
from backend.item_classes import itemInit
from backend.shop_restock import shopRestock
import config.game_config as game_config

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption('Clonepit Slots')
    clock = pygame.time.Clock()

    #HUD assets indlæses
    hudIconSize = 48
    hudCoinIcon = pygame.transform.scale(pygame.image.load('assets/Coin.webp'), (hudIconSize, hudIconSize))
    hudTicketIcon = pygame.transform.scale(pygame.image.load('assets/ModifierTicket.webp'), (hudIconSize, hudIconSize))
    hudFont = pygame.font.Font(None, size=40)

    #Definerer items og deres weights
    unlockedItems, itemWeights = itemInit()

    #Fylder shoppen
    shopRestock(unlockedItems, itemWeights)

    # Opretter alle rum en gang ved start
    rooms = [
        ATMRoom(),
        ShopRoom(),
        SlotRoom(),
        PostersRoom(),
        PhoneRoom(),
        shelfRoom()
    ]

    # Navne til caption så man kan se hvilket rum man er i
    roomNames = [
        'Clonepit Slots - ATM',
        'Clonepit Slots - Shop',
        'Clonepit Slots - Slots',
        'Clonepit Slots - Posters',
        'Clonepit Slots - Phone',
        'Clonepit Slots - Shelf'
    ]

    # Starter i slots rummet
    currentRoom = 2

    pygame.display.set_caption(roomNames[currentRoom])

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # Skifter rum med piletasterne (loops)
                if event.key == pygame.K_LEFT:
                    currentRoom = (currentRoom - 1) % len(rooms)
                    pygame.display.set_caption(roomNames[currentRoom])

                if event.key == pygame.K_RIGHT:
                    currentRoom = (currentRoom + 1) % len(rooms)
                    pygame.display.set_caption(roomNames[currentRoom])

                # Space spinner kun i slots rummet
                if event.key == pygame.K_SPACE and currentRoom == 2:
                    rooms[2].on_space()

                if event.key == pygame.K_SPACE and currentRoom == 1:
                    shopRestock(unlockedItems, itemWeights)


        screen.fill((0, 0, 0))
        rooms[currentRoom].draw(screen)

        #Tegner HUD med coins og tickets altid øverst i alle rum
        hudPadding = 12
        textGap = 8
        rowGap = 6

        coinText = hudFont.render(str(game_config.coins), True, (246, 214, 50))
        ticketText = hudFont.render(str(game_config.tickets), True, (180, 230, 255))

        hudW = max(hudIconSize + textGap + coinText.get_width(),
                   hudIconSize + textGap + ticketText.get_width()) + hudPadding * 2
        hudH = hudIconSize * 2 + rowGap + hudPadding * 2

        hudSurf = pygame.Surface((hudW, hudH), pygame.SRCALPHA)
        pygame.draw.rect(hudSurf, (0, 0, 0, 160), hudSurf.get_rect(), border_radius=8)
        hudSurf.blit(hudCoinIcon, (hudPadding, hudPadding))
        hudSurf.blit(coinText, (hudPadding + hudIconSize + textGap, hudPadding + hudIconSize // 2 - coinText.get_height() // 2))
        hudSurf.blit(hudTicketIcon, (hudPadding, hudPadding + hudIconSize + rowGap))
        hudSurf.blit(ticketText, (hudPadding + hudIconSize + textGap, hudPadding + hudIconSize + rowGap + hudIconSize // 2 - ticketText.get_height() // 2))

        screen.blit(hudSurf, (1200 - hudW - hudPadding, hudPadding))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
