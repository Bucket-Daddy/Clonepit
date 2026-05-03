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
        while font.size(text[:i].replace('\033[93m', '').replace('\033[92m', '').replace('\033[32m', '').replace('\033[33m', ''))[0] < width and i < len(text):
            i += 1
                
        if i < len(text):
            i = text.rfind(' ', 0, i) + 1

        frags = text[:i].split('\x1b')
        for frag in frags:
            if frag.startswith('['):
                frag = frag.split('m', 1)
                frag = font.render(frag[1], True, colorCodes[frag[0]], (0, 0, 0))
            else:
                frag = font.render(frag, True, (255, 255, 255), (0, 0, 0))
            
            surface.blit(frag, (x, y))
            x += frag.get_width()
    
        y += 24
        text = text[i:]
