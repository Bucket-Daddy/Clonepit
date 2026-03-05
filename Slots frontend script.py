#slot machine frontend script
import pygame
import random
import math

#initialiserer pygame
pygame.init()

#Definerer grafik variabler
symbolScale = 2
symbolSpaceVer = 16
spinSpeed = 10
symbolSpaceHor = 100
squareDist = 5
frameRate = 60
font = pygame.font.Font(None, size = 30)
dividerLineWidth = 8

#definerer reel variabler
reels = []
reelsY = [-(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30]
patternTimer = 0
patternDuration = 1

#Opretter vindue
screen = pygame.display.set_mode((symbolSpaceHor * 5  + 2 * 18 * symbolScale, (18 * symbolScale + symbolSpaceVer) * 3 + symbolSpaceVer))

#Opretter slot machine surface
slotMachine = pygame.Surface((symbolSpaceHor * 5  + 2 * 18 * symbolScale, (18 * symbolScale + symbolSpaceVer) * 3 + symbolSpaceVer), pygame.SRCALPHA)


#Loader billeder
lemon = pygame.image.load('assets/SymbolLemon.webp')
cherry = pygame.image.load('assets/SymbolCherry.webp')
clover = pygame.image.load('assets/SymbolClover.webp')
bell = pygame.image.load('assets/SymbolBell.webp')
diamond = pygame.image.load('assets/SymbolDiamond.webp')
treasure = pygame.image.load('assets/SymbolTreasureChest.webp')
seven = pygame.image.load('assets/SymbolSeven.webp')

#Skalerer billeder
lemon = pygame.transform.scale(lemon, (18 * symbolScale, 18 * symbolScale))
cherry = pygame.transform.scale(cherry, (18 * symbolScale, 18 * symbolScale))
clover = pygame.transform.scale(clover, (18 * symbolScale, 18 * symbolScale))
bell = pygame.transform.scale(bell, (18 * symbolScale, 18 * symbolScale))
diamond = pygame.transform.scale(diamond, (18 * symbolScale, 18 * symbolScale))
treasure = pygame.transform.scale(treasure, (18 * symbolScale, 18 * symbolScale))
seven = pygame.transform.scale(seven, (18 * symbolScale, 18 * symbolScale))

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
    reel = pygame.Surface((18 * symbolScale, (18 * symbolScale + symbolSpaceVer) * 30), pygame.SRCALPHA)

    for slot in range(3):
        reel.blit(symbols[res[slot * 5 + i]], (0, slot * (18 * symbolScale + symbolSpaceVer)))

    for slot in range(27):
        reel.blit(random.choice((lemon, cherry, clover, bell, diamond, treasure, seven)), (0, (18 * symbolScale + symbolSpaceVer) * 3 + slot * (18 * symbolScale + symbolSpaceVer)))

    reels.append(reel)

    #exec(reelName + ' = reel')

    
running = True

clock = pygame.time.Clock()

#Spil loopet
while running:
    slotMachine.fill((0, 0, 0))

#Flytter reels ned langs skærmen
    for reel in range(5):
        if reelsY[reel] < symbolSpaceVer:
            reelsY[reel] += spinSpeed - reel * spinSpeed / 10
        else:
            reelsY[reel] = symbolSpaceVer

#Loader reels til slot machien surface
    for reel in range(5):
        slotMachine.blit(reels[reel], (symbolSpaceHor - 18 * symbolScale + reel * symbolSpaceHor, reelsY[reel]))

#Når reelsene har noget bunden af skærmen vises hvert pattern for patternDuration sekunder
    if reelsY.count(16) == 5 and patternTimer < len(result) * frameRate * patternDuration:
#Tegner kasser om hvert symbol i et givent pattern
        for slot in patterns[result[math.floor(patternTimer / (frameRate * patternDuration))][0]]:
            pygame.draw.rect(slotMachine, (36, 252, 3), pygame.Rect(symbolSpaceHor - 18 * symbolScale - squareDist + slot % 5 * symbolSpaceHor, symbolSpaceVer - squareDist + math.floor(slot / 5) * (18 * symbolScale + symbolSpaceVer), 18 * symbolScale + 2 * squareDist, 18 * symbolScale + 2 * squareDist), 2, 3)
#Viser værdien af et givent pattern 
        text = font.render('+' + str(result[math.floor(patternTimer / (frameRate * patternDuration))][1]), True, (245, 179, 66))
        slotMachine.blit(text , text.get_rect(center=(slotMachine.get_width()/2, slotMachine.get_height()/2)))

        patternTimer += 1

#Tegner linjer mellem reels
    for i in range(4):
        pygame.draw.rect(slotMachine, (237, 156, 50), pygame.Rect(1.5 * (symbolSpaceHor - 18 * symbolScale) + i * symbolSpaceHor + 18 * symbolScale - 0.5 * dividerLineWidth, 0, dividerLineWidth, slotMachine.get_height()))

#Lukker spillet når vinduet lukkes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(slotMachine, (0, 0))
    pygame.display.flip()

    clock.tick(frameRate)

pygame.quit()
