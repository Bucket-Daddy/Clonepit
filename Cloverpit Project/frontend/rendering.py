#rendering
import pygame
pygame.init()

#Opretter vindue
screen = pygame.display.set_mode((1144, 344))

def render(surface, position):
    screen.blit(surface, position)
    pygame.display.flip()
    