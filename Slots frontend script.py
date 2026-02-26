#slot machine frontend script
import pygame
import random
import math

pygame.init()

reels = []
reelsY = [-1560, -1560, -1560, -1560, -1560]
patternInit = True


#Opretter vindue
screen = pygame.display.set_mode((640, 640))

#Loader billeder
lemon = pygame.image.load('assets/SymbolLemon.webp')
cherry = pygame.image.load('assets/SymbolCherry.webp')
clover = pygame.image.load('assets/SymbolClover.webp')
bell = pygame.image.load('assets/SymbolBell.webp')
diamond = pygame.image.load('assets/SymbolDiamond.webp')
treasure = pygame.image.load('assets/SymbolTreasureChest.webp')
seven = pygame.image.load('assets/SymbolSeven.webp')

#Skalerer billeder
lemon = pygame.transform.scale(lemon, (36, 36))
cherry = pygame.transform.scale(cherry, (36, 36))
clover = pygame.transform.scale(clover, (36, 36))
bell = pygame.transform.scale(bell, (36, 36))
diamond = pygame.transform.scale(diamond, (36, 36))
treasure = pygame.transform.scale(treasure, (36, 36))
seven = pygame.transform.scale(seven, (36, 36))

#temporary simulation of result from slots script
res = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
result = [('vert1', 2, ()), ('vert3', 2, ()), ('vert5', 2, ()), ('bckDiag2', 2, ()), ('fwdDiag2', 2, ()), ('horXL2', 6, ()), ('above', 14, ()), ('below', 14, ()), ('eye', 16, ()), ('jackpot', 20, ())]

symbols = {0:lemon, 1:cherry, 2:clover, 3:bell, 4:diamond, 5:treasure, 6:seven}
patterns = {'hor1.1':(0, 1, 2), 'hor1.2':(1, 2, 3), 'hor1.3':(2, 3, 4), 'hor2.1':(5, 6, 7), 'hor2.2':(6, 7, 8), 'hor2.3':(7, 8, 9),
            'hor3.1':(10, 11, 12), 'hor3.2':(11, 12, 23), 'hor3.3':(12, 13, 14), 'vert1':(0, 5, 10), 'vert2':(1, 6, 11), 'vert3':(2, 7, 12),
            'vert4':(3, 8, 13), 'vert5':(4, 9, 14), 'bckDiag1':(0, 6, 12), 'bckDiag2':(1, 7, 13), 'bckDiag3':(2, 8, 14), 
            'fwdDiag1':(2, 6, 10), 'fwdDiag2':(3, 7, 11), 'fwdDiag3':(4, 8, 12), 'horL1.1':(0, 1, 2, 3), 'horL1.2':(1, 2, 3, 4), 
            'horL2.1':(5, 6, 7, 8), 'horL2.2':(6, 7, 8, 9), 'horL3.1':(10, 11, 12, 13), 'horL3.2':(11, 12, 13, 14),
            'horXL1':(0, 1, 2, 3, 4), 'horXL2':(5, 6, 7, 8, 9), 'horXL3':(10, 11, 12, 13, 14), 'zig':(2, 6, 8, 10, 14), 
            'zag':(0, 4, 6, 8, 12), 'above':(2, 6, 8, 10, 11, 12, 13, 14), 'below':(0, 1, 2, 3, 4, 6, 8, 12),
            'eye':(1, 2, 3, 5, 6, 8, 9, 11, 12, 13), 'jackpot':(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)}

#Danner reels
for i in range(5):
    #reelName = 'reel' + str(i)
    reel = pygame.Surface((36, 1560), pygame.SRCALPHA)

    for slot in range(3):
        reel.blit(symbols[res[slot * 5 + i]], (0, slot * 52))

    for slot in range(27):
        reel.blit(random.choice((lemon, cherry, clover, bell, diamond, treasure, seven)), (0, 156 + slot * 52))

    reels.append(reel)

    #exec(reelName + ' = reel')

    
running = True

clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))

    for reel in range(5):
        if reelsY[reel] < 16:
            reelsY[reel] += 10 - reel
        else:
            reelsY[reel] = 16

    for reel in range(5):
        screen.blit(reels[reel], (100 + reel * 100, reelsY[reel]))

    if reelsY.count(16) == 5 and patternInit:
        for pat in result:
            for slot in patterns[pat[0]]:
                pygame.draw.rect(screen, (36, 252, 3), pygame.Rect(95 + slot % 5 * 100, 11 + math.floor(slot / 5) * 52, 46, 46), 2, 3)
            pygame.display.flip()
            pygame.time.wait(325)
            for slot in patterns[pat[0]]:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(95 + slot % 5 * 100, 11 + math.floor(slot / 5) * 52, 46, 46), 2, 3)
            pygame.display.flip()
            pygame.time.wait(100)
        patternInit = False
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()