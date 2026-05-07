# main.py
import pygame
from screeninfo import get_monitors
for screen in get_monitors():
    if screen.is_primary:
        resolution = (screen.width, screen.height)
        break


xScaling = resolution[0] / 1200
yScaling = resolution[1] / 750

from frontend.slot_room import SlotRoom
from frontend.atm_room import ATMRoom
from frontend.posters_room import PostersRoom
from frontend.shop_room import ShopRoom
from frontend.phone_room import PhoneRoom
from frontend.shelf_room import shelfRoom
from backend.item_classes import itemInit
from backend.call_classes import callInit
from backend.shop_restock import shopRestock
from backend.roll_phone import rollPhone
import config.game_config as config


def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('assets/mondamusic-retro-arcade-game-music-512837.mp3')
    pygame.mixer.music.play(loops = -1)

    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    pygame.display.set_caption('Clonepit Slots')
    clock = pygame.time.Clock()

    #HUD assets indlæses
    hudIconSize = 48
    hudCoinIcon = pygame.transform.scale(pygame.image.load('assets/Coin.webp'), (hudIconSize, hudIconSize))
    hudTicketIcon = pygame.transform.scale(pygame.image.load('assets/ModifierTicket.webp'), (hudIconSize, hudIconSize))
    hudFont = pygame.font.Font(None, size = round(40 * xScaling))

    #Initialiserer items
    itemInit()

    #Fylder shoppen
    shopRestock()

    #Initialserer telefonopkald
    callInit()

    #Fylder telefonen med valgmuligheder
    rollPhone()

    # Opretter alle rum en gang ved start
    rooms = [
        ATMRoom(resolution, xScaling, yScaling),
        ShopRoom(resolution, xScaling, yScaling),
        SlotRoom(resolution, xScaling, yScaling),
        PostersRoom(resolution, xScaling, yScaling),
        PhoneRoom(resolution, xScaling, yScaling),
        shelfRoom(resolution, xScaling, yScaling)
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

    # Navigationspile tegnes oven på alle rum som klikbare overlejringer
    arrowW, arrowH = 28 * xScaling, 52 * yScaling
    arrowPad = 6
    arrowY = resolution[1] // 2
    leftArrowPts  = [(arrowPad + arrowW, arrowY - arrowH // 2),
                     (arrowPad,           arrowY),
                     (arrowPad + arrowW, arrowY + arrowH // 2)]
    rightArrowPts = [(resolution[0] - arrowPad - arrowW, arrowY - arrowH // 2),
                     (resolution[0] - arrowPad,            arrowY),
                     (resolution[0] - arrowPad - arrowW, arrowY + arrowH // 2)]
    leftArrowRect  = pygame.Rect(arrowPad,                 arrowY - arrowH // 2, arrowW, arrowH)
    rightArrowRect = pygame.Rect(resolution[0] - arrowPad - arrowW, arrowY - arrowH // 2, arrowW, arrowH)

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
                    rooms[2].spin_reels(resolution, xScaling, yScaling)

            #Museklik sendes til slots rummet (køb-knapper)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if currentRoom == 2:
                    rooms[2].on_click(event.pos, resolution, xScaling, yScaling)
                # Navigationspile
                if leftArrowRect.collidepoint(event.pos):
                    currentRoom = (currentRoom - 1) % len(rooms)
                    pygame.display.set_caption(roomNames[currentRoom])
                if rightArrowRect.collidepoint(event.pos):
                    currentRoom = (currentRoom + 1) % len(rooms)
                    pygame.display.set_caption(roomNames[currentRoom])


        screen.fill((0, 0, 0))
        rooms[currentRoom].draw(screen, resolution, xScaling, yScaling)

        #Tegner HUD med coins og tickets altid øverst i alle rum
        hudPadding = 12
        textGap = 8
        rowGap = 6

        coinText = hudFont.render(str(config.coins), True, (246, 214, 50))
        ticketText = hudFont.render(str(config.tickets), True, (180, 230, 255))

        hudW = max(hudIconSize + textGap + coinText.get_width(),
                   hudIconSize + textGap + ticketText.get_width()) + hudPadding * 2
        hudH = hudIconSize * 2 + rowGap + hudPadding * 2

        hudSurf = pygame.Surface((hudW, hudH), pygame.SRCALPHA)
        pygame.draw.rect(hudSurf, (0, 0, 0, 160), hudSurf.get_rect(), border_radius=8)
        hudSurf.blit(hudCoinIcon, (hudPadding, hudPadding))
        hudSurf.blit(coinText, (hudPadding + hudIconSize + textGap, hudPadding + hudIconSize // 2 - coinText.get_height() // 2))
        hudSurf.blit(hudTicketIcon, (hudPadding, hudPadding + hudIconSize + rowGap))
        hudSurf.blit(ticketText, (hudPadding + hudIconSize + textGap, hudPadding + hudIconSize + rowGap + hudIconSize // 2 - ticketText.get_height() // 2))

        screen.blit(hudSurf, (resolution[0] - hudW - hudPadding, hudPadding))

        # Tegner navigationspile — subtile trekanter langs skærmens kanter
        mousePos = pygame.mouse.get_pos()
        leftHover  = leftArrowRect.collidepoint(mousePos)
        rightHover = rightArrowRect.collidepoint(mousePos)
        leftColor  = (246, 250, 10) if leftHover  else (160, 140, 60)
        rightColor = (246, 250, 10) if rightHover else (160, 140, 60)
        pygame.draw.polygon(screen, leftColor,  leftArrowPts)
        pygame.draw.polygon(screen, rightColor, rightArrowPts)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
