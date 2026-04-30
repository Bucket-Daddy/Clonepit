# main.py
import pygame

from frontend.slot_room import SlotRoom
from frontend.atm_room import ATMRoom
from frontend.posters_room import PostersRoom
from frontend.shop_room import ShopRoom
from frontend.phone_room import PhoneRoom


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption('Clonepit Slots')
    clock = pygame.time.Clock()

    # Opretter alle rum en gang ved start
    rooms = [
        ATMRoom(),
        ShopRoom(),
        SlotRoom(),
        PostersRoom(),
        PhoneRoom(),
    ]

    # Navne til caption så man kan se hvilket rum man er i
    roomNames = [
        'Clonepit Slots - ATM',
        'Clonepit Slots - Shop',
        'Clonepit Slots - Slots',
        'Clonepit Slots - Posters',
        'Clonepit Slots - Phone',
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

        screen.fill((0, 0, 0))
        rooms[currentRoom].draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
