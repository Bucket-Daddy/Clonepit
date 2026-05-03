#Function to check for mouse collision
import pygame

def isSelected(clickable, location, surface):
    mouseX, mouseY = pygame.mouse.get_pos()
    #Tjekker for rect kollision før der tjekkes for den dyere pixel-perfect kollision
    if clickable.get_rect().move(location).collidepoint((mouseX, mouseY)):
        #Tjekker om den pixel musen er på har baggrundsfarven
        if clickable.get_at((mouseX - location[0], mouseY - location[1])) != clickable.get_colorkey():
            #Tegner en outline
            pygame.draw.lines(surface, (250, 246, 15), False, [(p[0] + location[0], p[1] + location[1]) for p in pygame.mask.from_surface(clickable).outline()], 3)
            return True
