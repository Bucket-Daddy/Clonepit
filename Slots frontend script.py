#slot machine frontend script
import pygame
import random
import math

#initialiserer pygame
pygame.init()

#Definerer grafik variabler
overallScale = 2
symbolScale = 2 * overallScale
symbolSpaceVer = 16 * overallScale
spinSpeed = 20 * overallScale
symbolSpaceHor = 100 * overallScale
squareDist = 5 * overallScale
frameRate = 60
font = pygame.font.Font(None, size = 30 * overallScale)
dividerLineWidth = 8 * overallScale

#definerer reel variabler
reels = []
reelsY = [-(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30, -(18 * symbolScale + symbolSpaceVer) * 30]
patternTimer = 0
patternDuration = 1

#Opretter vindue
screen = pygame.display.set_mode((symbolSpaceHor * 5, (18 * symbolScale + symbolSpaceVer) * 3 + symbolSpaceVer))

#Opretter slot machine surface
slotMachine = pygame.Surface((symbolSpaceHor * 5, (18 * symbolScale + symbolSpaceVer) * 3 + symbolSpaceVer), pygame.SRCALPHA)

pygame.mixer.set_num_channels(32)

#Loader billeder
lemon = pygame.image.load('assets/SymbolLemon.webp')
cherry = pygame.image.load('assets/SymbolCherry.webp')
clover = pygame.image.load('assets/SymbolClover.webp')
bell = pygame.image.load('assets/SymbolBell.webp')
diamond = pygame.image.load('assets/SymbolDiamond.webp')
treasure = pygame.image.load('assets/SymbolTreasureChest.webp')
seven = pygame.image.load('assets/SymbolSeven.webp')
six = pygame.image.load('assets/SymbolSix.webp')

golden = pygame.image.load('assets/modifierGolden.webp')
token = pygame.image.load('assets/modifierToken.webp')
ticket = pygame.image.load('assets/modifierTicket.webp')
repetition = pygame.image.load('assets/modifierRepetition.webp')
battery = pygame.image.load('assets/modifierBattery.webp')
chain = pygame.image.load('assets/modifierChain.webp')

#Loader lydeffekter
scoreSFX = pygame.mixer.Sound('assets/1-18. Slot Machine Scored.mp3')
jackpotSFX = pygame.mixer.Sound('assets/1-17. Slot Machine Jackpot.mp3')
rollingSFX = pygame.mixer.Sound('assets/2-228. Slotmachinerollingtick.mp3')

#Skalerer billeder
lemon = pygame.transform.scale(lemon, (18 * symbolScale, 18 * symbolScale))
cherry = pygame.transform.scale(cherry, (18 * symbolScale, 18 * symbolScale))
clover = pygame.transform.scale(clover, (18 * symbolScale, 18 * symbolScale))
bell = pygame.transform.scale(bell, (18 * symbolScale, 18 * symbolScale))
diamond = pygame.transform.scale(diamond, (18 * symbolScale, 18 * symbolScale))
treasure = pygame.transform.scale(treasure, (18 * symbolScale, 18 * symbolScale))
seven = pygame.transform.scale(seven, (18 * symbolScale, 18 * symbolScale))
six = pygame.transform.scale(six, (18 * symbolScale, 18 * symbolScale))

golden = pygame.transform.scale(golden, (9 * symbolScale, 9 * symbolScale))
token = pygame.transform.scale(token, (9 * symbolScale, 9 * symbolScale))
ticket = pygame.transform.scale(ticket, (9 * symbolScale, 9 * symbolScale))
repetition = pygame.transform.scale(repetition, (9 * symbolScale, 9 * symbolScale))
battery = pygame.transform.scale(battery, (9 * symbolScale, 9 * symbolScale))
chain = pygame.transform.scale(chain, (9 * symbolScale, 9 * symbolScale))

#temporary simulation of result from slots script
res = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
result = [('vert1', 2, ()), ('vert3', 2, ()), ('vert5', 2, ()), ('bckDiag2', 2, ()), ('fwdDiag2', 2, ()), ('horXL2', 6, ()), ('above', 14, ()), ('below', 14, ()), ('eye', 16, ()), ('jackpot', 20, ())]
modifiers = [0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0, 1, 3, 5]
is666 = True

#Tuples og dictionaries til fortolkning af resultat
symbolsTuple = (lemon, cherry, clover, bell, diamond, treasure, seven)
modifiersTuple = (None, golden, token, ticket, repetition, battery, chain)
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
    reel = pygame.Surface((18 * symbolScale, (18 * symbolScale + symbolSpaceVer) * 30), pygame.SRCALPHA)

    if is666:
        reel.blit(random.choice((lemon, cherry, clover, bell, diamond, treasure, seven)), (0, 0))
        if i < 4 and i > 0:
            reel.blit(six, (0, 18 * symbolScale + symbolSpaceVer))
        else:
            reel.blit(random.choice((lemon, cherry, clover, bell, diamond, treasure, seven)), (0, 18 * symbolScale + symbolSpaceVer))
        reel.blit(random.choice((lemon, cherry, clover, bell, diamond, treasure, seven)), (0, 36 * symbolScale + 2 * symbolSpaceVer))  
    else:

        for slot in range(3):
            reel.blit(symbolsTuple[res[slot * 5 + i]], (0, slot * (18 * symbolScale + symbolSpaceVer)))
            if modifiers[slot * 5 + i] > 0:
                reel.blit(modifiersTuple[modifiers[slot * 5 + i]], (symbolScale * 9, slot * (18 * symbolScale + symbolSpaceVer) + 9 * symbolScale))

    for slot in range(27):
        reel.blit(random.choice((lemon, cherry, clover, bell, diamond, treasure, seven)), (0, (18 * symbolScale + symbolSpaceVer) * 3 + slot * (18 * symbolScale + symbolSpaceVer)))

    reels.append(reel)

    
running = True

clock = pygame.time.Clock()

rollingSFX.play()

#Spil loopet
while running:
    slotMachine.fill((0, 0, 0))

#Flytter reels ned langs skærmen
    for reel in range(5):
        if reelsY[reel] < symbolSpaceVer:
            reelsY[reel] += spinSpeed - reel * spinSpeed / 10
        else:
            reelsY[reel] = symbolSpaceVer

#Loader reels til slot machine surface
    for reel in range(5):
        slotMachine.blit(reels[reel], (symbolSpaceHor - 2 * 18 * symbolScale + reel * symbolSpaceHor, reelsY[reel]))

#Tegner linjer mellem reels
    for i in range(4):
        pygame.draw.rect(slotMachine, (120, 95, 26), pygame.Rect(1.5 * (symbolSpaceHor - 18 * symbolScale) + i * symbolSpaceHor - 0.5 * dividerLineWidth, 0, dividerLineWidth, slotMachine.get_height()))

#Når reelsene har noget bunden af skærmen vises hvert pattern i {patternDuration} sekunder
    if reelsY.count(symbolSpaceVer) == 5 and patternTimer < len(result) * frameRate * 1.25 * patternDuration and not is666:

#Spiller lydeffekten for hvert pattern
        if patternTimer == frameRate * 1.25 * patternDuration * math.floor(patternTimer / (frameRate * 1.25 * patternDuration)):
            if result[math.floor(patternTimer / (frameRate * 1.25 * patternDuration))][0] == 'jackpot':
                jackpotSFX.play()
            else:
                scoreSFX.play()

#Tegner kasser om hvert symbol i et givent pattern
        if patternTimer <= frameRate * patternDuration * math.floor(patternTimer / (frameRate * 1.25 * patternDuration) + 1) + frameRate * patternDuration * 0.25 * math.floor(patternTimer / (frameRate * 1.25 * patternDuration)):
            for slot in patterns[result[math.floor(patternTimer / (frameRate * 1.25 * patternDuration))][0]]:
                pygame.draw.rect(slotMachine, (36, 252, 3), pygame.Rect(symbolSpaceHor - 18 * symbolScale - squareDist + slot % 5 * symbolSpaceHor, symbolSpaceVer - squareDist + math.floor(slot / 5) * (18 * symbolScale + symbolSpaceVer), 18 * symbolScale + 2 * squareDist, 18 * symbolScale + 2 * squareDist), 2, 3)
#Viser værdien af et givent pattern
            if len(str(result[math.floor(patternTimer / (frameRate * 1.25 * patternDuration))][1])) > 7:
                patternPayout = round(result[math.floor(patternTimer / (frameRate * 1.25 * patternDuration))][1] * 10**(-1 * (len(str(result[math.floor(patternTimer / (frameRate * patternDuration))][1])) - 1)), 5)
                text = font.render('+' + str(patternPayout) + 'E+' + str(len(str(result[math.floor(patternTimer / (frameRate * patternDuration))][1])) - 1), True, (250, 10, 10))
            else:
                text = font.render('+' + str(result[math.floor(patternTimer / (frameRate * 1.25 * patternDuration))][1]), True, (246, 250, 10))

            slotMachine.blit(text , text.get_rect(center=(slotMachine.get_width()/2, slotMachine.get_height()/2)))

        patternTimer += 1

#Lukker spillet når vinduet lukkes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(slotMachine, (0, 0))
    pygame.display.flip()

    clock.tick(frameRate)

pygame.quit()
