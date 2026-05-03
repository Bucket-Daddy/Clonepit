#Tekst rendering funktion
#Tekst wrapping funktionalitet inspireret af https://www.pygame.org/wiki/TextWrap
import pygame

colorCodes = {
    '[0': (255, 255, 255),
    '[93': (252, 240, 3),
    '[92': (7, 242, 15),
    '[32': (66, 191, 44),
    '[33': (247, 167, 5)
}

def renderText(text, font, surface, origin, width):
    y = origin[1]
    while len(text) > 1:
        i = 1
        x = origin[0]
        while font.size(text[:i])[0] < width and i < len(text):
            i += 1
                
        if i < len(text):
            i = text.rfind(' ', 0, i) + 1

        frags = text[:i].split('\x1b')
        for j in range(len(frags)):
            if frags[j].startswith('['):
                frag = frags[j].split('m', 1)
                frags[j] = font.render(frag[1], True, colorCodes[frag[0]], (0, 0, 0))
            else:
                frags[j] = font.render(frags[j], True, (255, 255, 255), (0, 0, 0))
            
            surface.blit(frags[j], (x, y))
            x += frags[j].get_width()
    


        y += 24
        text = text[i:]