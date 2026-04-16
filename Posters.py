import pygame

pygame.init()
posterScale = 0.80
symbolScale = 1
overallScale = 2
font = pygame.font.Font(None, size = 15 * overallScale)
symbolMult = 1
patternMult = 1
symbolValues = [2, 2, 3, 3, 5, 5, 7] #lemon, cherry, clover, bell, diamond, treasure, seven.
symbolWeights = [1.3, 1.3, 1, 1, 0.8, 0.8, 0.5] #lemon, cherry, clover, bell, diamond, treasure, seven.
patternValues = {'hor':1, 'vert':1, 'diag':1, 'horL':2, 'horXL':3, 'zig':4, 'zag':4, 'above':7, 'below':7, 'eye':8, 'jackpot':10}
pygame.display.set_caption('Clonepit Slots - Posters')
screen = pygame.display.set_mode((800, 600))

#Loader billeder
lemon = pygame.image.load('assets/SymbolLemon.webp')
cherry = pygame.image.load('assets/SymbolCherry.webp')
clover = pygame.image.load('assets/SymbolClover.webp')
bell = pygame.image.load('assets/SymbolBell.webp')
diamond = pygame.image.load('assets/SymbolDiamond.webp')
treasure = pygame.image.load('assets/SymbolTreasureChest.webp')
seven = pygame.image.load('assets/SymbolSeven.webp')
patternAbove = pygame.image.load('assets/PatternAbove.webp')
patternBelow = pygame.image.load('assets/PatternBelow.webp')
patternDiag = pygame.image.load('assets/PatternDiag.webp')
patternEye = pygame.image.load('assets/PatternEye.webp')
patternHor = pygame.image.load('assets/PatternHor.webp')
patternHorL = pygame.image.load('assets/PatternHorL.webp')
patternHorXL = pygame.image.load('assets/PatternHorXL.webp')
patternJackpot = pygame.image.load('assets/PatternJackpot.webp')
patternVer = pygame.image.load('assets/PatternVer.webp')
patternZag = pygame.image.load('assets/PatternZag.webp')
patternZig = pygame.image.load('assets/PatternZig.webp')
coin = pygame.image.load('assets/coin.webp')
coin2 = pygame.image.load('assets/coin2.webp')
dice = pygame.image.load('assets/D6.png').convert()
posterBackground = pygame.image.load('assets/PosterBackground.png').convert()

#Skalerer billeder
lemon = pygame.transform.scale(lemon, (36 * symbolScale, 36 * symbolScale))
cherry = pygame.transform.scale(cherry, (36 * symbolScale, 36 * symbolScale))
clover = pygame.transform.scale(clover, (36 * symbolScale, 36 * symbolScale))
bell = pygame.transform.scale(bell, (36 * symbolScale, 36 * symbolScale))
diamond = pygame.transform.scale(diamond, (36 * symbolScale, 36 * symbolScale))
treasure = pygame.transform.scale(treasure, (36 * symbolScale, 36 * symbolScale))
seven = pygame.transform.scale(seven, (36 * symbolScale, 36 * symbolScale))
patternHor = pygame.transform.scale(patternHor, (patternHor.get_width() * 2/7, patternHor.get_height() * 2/7))
patternVer = pygame.transform.scale(patternVer, (patternVer.get_width() * 2/7, patternVer.get_height() * 2/7))
patternDiag = pygame.transform.scale(patternDiag, (patternDiag.get_width() * 2/7, patternDiag.get_height() * 2/7))
patternHorL = pygame.transform.scale(patternHorL, (patternHorL.get_width() * 2/7, patternHorL.get_height() * 2/7))
patternHorXL = pygame.transform.scale(patternHorXL, (patternHorXL.get_width() * 2/7, patternHorXL.get_height() * 2/7))
patternZag = pygame.transform.scale(patternZag, (patternZag.get_width() * 2/7, patternZag.get_height() * 2/7))
patternZig = pygame.transform.scale(patternZig, (patternZig.get_width() * 2/7, patternZig.get_height() * 2/7))
patternAbove = pygame.transform.scale(patternAbove, (patternAbove.get_width() * 2/7, patternAbove.get_height() * 2/7))
patternBelow = pygame.transform.scale(patternBelow, (patternBelow.get_width() * 2/7, patternBelow.get_height() * 2/7))
patternEye = pygame.transform.scale(patternEye, (patternEye.get_width() * 2/7, patternEye.get_height() * 2/7))
patternJackpot = pygame.transform.scale(patternJackpot, (patternJackpot.get_width() * 2/7, patternJackpot.get_height() * 2/7))
coin = pygame.transform.scale(coin, (coin.get_width() * 0.15, coin.get_height() * 0.15))
coin2 = pygame.transform.scale(coin2, (coin2.get_width() * 0.12, coin2.get_height() * 0.12))
dice = pygame.transform.scale(dice, (dice.get_width() * 0.05, dice.get_height() * 0.05)).convert()
dice.set_colorkey((255, 0, 214))
posterBackground = pygame.transform.scale(posterBackground, (posterBackground.get_width() * posterScale, posterBackground.get_height() * posterScale))
posterBackground.set_colorkey((0, 0, 0))

# danner baggrunden
background = pygame.image.load('assets/Background.png')
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
posters = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
posters.blit(background, (-5, -5))

##############################################################################################################
# placering af plakaten
symbolPosterX = 30
symbolPosterY = 45
posters.blit(posterBackground, (symbolPosterX, symbolPosterY - 15))

# texten på plakaten defineres
textSymbols = font.render('---     SYMBOLS     ---', True, (0, 0, 0))
textSymbolsMult = font.render('  SYMBOLS     MULTIPLIER ', True, (0, 0, 0))
SymbolsMult = font.render(' X ' + str(symbolMult), True, (0, 0, 0))

# værdien for hver symbol, hvis værdien er >= 7 cifre, vil den blive vist i videnskabelig notation
# Lemon - placering af værdi
if len(str(symbolValues[0])) >= 7:
    symbolValue = round(symbolValues[0] * 10**(-1 * (len(str(symbolValues[0])) - 1)), 2)
    textLemonValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[0])) - 1), True, (0, 0, 0))
else:
    textLemonValue = font.render(': ' + str(symbolValues[0]), True, (0, 0, 0))

# Cherry - placering af værdi
if len(str(symbolValues[1])) >= 7:
    symbolValue = round(symbolValues[1] * 10**(-1 * (len(str(symbolValues[1])) - 1)), 2)
    textCherryValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[1])) - 1), True, (0, 0, 0))
else:
    textCherryValue = font.render(': ' + str(symbolValues[1]), True, (0, 0, 0))

# Clover - placering af værdi
if len(str(symbolValues[2])) >= 7:
    symbolValue = round(symbolValues[2] * 10**(-1 * (len(str(symbolValues[2])) - 1)), 2)
    textCloverValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[2])) - 1), True, (0, 0, 0))
else:
    textCloverValue = font.render(': ' + str(symbolValues[2]), True, (0, 0, 0))

# Bell - placering af værdi
if len(str(symbolValues[3])) >= 7:
    symbolValue = round(symbolValues[3] * 10**(-1 * (len(str(symbolValues[3])) - 1)), 2)
    textBellValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[3])) - 1), True, (0, 0, 0))
else:
    textBellValue = font.render(': ' + str(symbolValues[3]), True, (0, 0, 0))

# Diamond - placering af værdi
if len(str(symbolValues[4])) >= 7:
    symbolValue = round(symbolValues[4] * 10**(-1 * (len(str(symbolValues[4])) - 1)), 2)
    textDiamondValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[4])) - 1), True, (0, 0, 0))
else:
    textDiamondValue = font.render(': ' + str(symbolValues[4]), True, (0, 0, 0))

# Treasure - placering af værdi
if len(str(symbolValues[5])) >= 7:
    symbolValue = round(symbolValues[5] * 10**(-1 * (len(str(symbolValues[5])) - 1)), 2)
    textTreasureValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[5])) - 1), True, (0, 0, 0))
else:
    textTreasureValue = font.render(': ' + str(symbolValues[5]), True, (0, 0, 0))

# Seven - placering af værdi
if len(str(symbolValues[6])) >= 7:
    symbolValue = round(symbolValues[6] * 10**(-1 * (len(str(symbolValues[6])) - 1)), 2)
    textSevenValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[6])) - 1), True, (0, 0, 0))
else:
    textSevenValue = font.render(': ' + str(symbolValues[6]), True, (0, 0, 0))

# Chancen for hver symbol, vist som en procentdel med 1 decimal.
textLemonChance = font.render(': ' + str(round(symbolWeights[0]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textCherryChance = font.render(': ' + str(round(symbolWeights[1]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textCloverChance = font.render(': ' + str(round(symbolWeights[2]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textBellChance = font.render(': ' + str(round(symbolWeights[3]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textDiamondChance = font.render(': ' + str(round(symbolWeights[4]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textTreasureChance = font.render(': ' + str(round(symbolWeights[5]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textSevenChance = font.render(': ' + str(round(symbolWeights[6]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))

# texten på plakaten
posters.blit(textSymbols, textSymbols.get_rect(center=(posterBackground.get_width()/2 + symbolPosterX, symbolPosterY + 30)))
posters.blit(textSymbolsMult, textSymbolsMult.get_rect(center=(posterBackground.get_width()/2 + symbolPosterX, symbolPosterY + 36 * symbolScale + 305)))
posters.blit(SymbolsMult, SymbolsMult.get_rect(center=(symbolPosterX + 240, symbolPosterY + 370)))
posters.blit(textLemonValue, (symbolPosterX + 100, symbolPosterY + 40))
posters.blit(textCherryValue, (symbolPosterX + 100, symbolPosterY + 80))
posters.blit(textCloverValue, (symbolPosterX + 100, symbolPosterY + 120))
posters.blit(textBellValue, (symbolPosterX + 100, symbolPosterY + 160))
posters.blit(textDiamondValue, (symbolPosterX + 100, symbolPosterY + 200))
posters.blit(textTreasureValue, (symbolPosterX + 100, symbolPosterY + 245))
posters.blit(textSevenValue, (symbolPosterX + 100, symbolPosterY + 288))
posters.blit(textLemonChance, (symbolPosterX + 220, symbolPosterY + 40))
posters.blit(textCherryChance, (symbolPosterX + 220, symbolPosterY + 80))
posters.blit(textCloverChance, (symbolPosterX + 220, symbolPosterY + 120))
posters.blit(textBellChance, (symbolPosterX + 220, symbolPosterY + 160))
posters.blit(textDiamondChance, (symbolPosterX + 220, symbolPosterY + 200))
posters.blit(textTreasureChance, (symbolPosterX + 220, symbolPosterY + 245))
posters.blit(textSevenChance, (symbolPosterX + 220, symbolPosterY + 287.5))

    # Symboler på plakaten
posters.blit(lemon, (symbolPosterX + 25, symbolPosterY + 40))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 40))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 40))
posters.blit(cherry, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 40))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 42))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 43))
posters.blit(clover, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 80))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 82))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 83))
posters.blit(bell, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 120))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 122))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 123))
posters.blit(diamond, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 162.5))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 164.5))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 163))
posters.blit(treasure, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 205))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 207))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 208))
posters.blit(seven, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 247.5))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 249.5))
posters.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 250))
posters.blit(coin, (symbolPosterX + 200, symbolPosterY + 355))

##############################################################################################################
# Plakaten med værdierne for mønstrene
patternPosterX = symbolPosterX + posterBackground.get_width() + 30
patternPosterY = symbolPosterY
posters.blit(posterBackground, (patternPosterX , patternPosterY - 15))

# texten på plakaten
textPatterns = font.render('---     PATTERNS     ---', True, (0, 0, 0))
textPatternsMult = font.render('  PATTERN     MULTIPLIER ', True, (0, 0, 0))
PatternsMult = font.render(' X ' + str(patternMult), True, (0, 0, 0))
textHor = font.render('HOR', True, (0, 0, 0))
textVer = font.render('VER', True, (0, 0, 0))
textDiag = font.render('DIAG', True, (0, 0, 0))
textHorL = font.render('HOR-L', True, (0, 0, 0))
textHorXL = font.render('HOR-XL', True, (0, 0, 0))
textZig = font.render('ZIG', True, (0, 0, 0))
textZag = font.render('ZAG', True, (0, 0, 0))
textAbove = font.render('ABOVE', True, (0, 0, 0))
textBelow = font.render('BELOW', True, (0, 0, 0))
textEye = font.render('EYE', True, (0, 0, 0))
textJackpot = font.render('JACKPOT', True, (0, 0, 0))

# hor mønsteret
if len(str(patternValues['hor'])) >= 11:
    patternValue = round(patternValues['hor'] * 10**(-1 * (len(str(patternValues['hor'])) - 1)), 2)
    textHorMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['hor'])) - 1), True, (0, 0, 0))
    posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 40))
    posters.blit(textHorMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 40))
else:
    textHorMult = font.render('X ' + str(patternValues['hor']), True, (0, 0, 0))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['hor']))**(1.50 - 0.012 * len(str(patternValues['hor']))), patternPosterY + 40))
    posters.blit(textHorMult, (patternPosterX + 270 - 5 * len(str(patternValues['hor']))**(1.50 - 0.012 * len(str(patternValues['hor']))), patternPosterY + 40))

# vert mønsteret
if len(str(patternValues['vert'])) >= 11:
    patternValue = round(patternValues['vert'] * 10**(-1 * (len(str(patternValues['vert'])) - 1)), 2)
    textVerMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['vert'])) - 1), True, (0, 0, 0))
    posters.blit(textVerMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 68.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 65))
else:
    textVerMult = font.render('X ' + str(patternValues['vert']), True, (0, 0, 0))
    posters.blit(textVerMult, (patternPosterX + 270 - 5 * len(str(patternValues['vert']))**(1.50 - 0.012 * len(str(patternValues['vert']))), patternPosterY + 68.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['vert']))**(1.50 - 0.012 * len(str(patternValues['vert']))), patternPosterY + 65))

# diag mønsteret
if len(str(patternValues['diag'])) >= 11:
    patternValue = round(patternValues['diag'] * 10**(-1 * (len(str(patternValues['diag'])) - 1)), 2)
    textDiagMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['diag'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['diag'])) >= 11:
        posters.blit(textDiagMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 96))
        posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 92.5))
    if len(str(patternValues['diag'])) < 11:
        posters.blit(textDiagMult, (patternPosterX + 212, patternPosterY + 96))
        posters.blit(coin2, (patternPosterX + 192, patternPosterY + 92.5))
else:
    textDiagMult = font.render('X ' + str(patternValues['diag']), True, (0, 0, 0))
    posters.blit(textDiagMult, (patternPosterX + 270 - 5 * len(str(patternValues['diag']))**(1.50 - 0.012 * len(str(patternValues['diag']))), patternPosterY + 96))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['diag']))**(1.50 - 0.012 * len(str(patternValues['diag']))), patternPosterY + 92.5))

# horL mønsteret
if len(str(patternValues['horL'])) >= 10:
    patternValue = round(patternValues['horL'] * 10**(-1 * (len(str(patternValues['horL'])) - 1)), 2)
    textHorLMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['horL'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['horL'])) >= 10:
        posters.blit(textHorLMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 123.5))
        posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 119.5))
    if len(str(patternValues['horL'])) < 10:
        posters.blit(textHorLMult, (patternPosterX + 212, patternPosterY + 123.5))
        posters.blit(coin2, (patternPosterX + 192, patternPosterY + 119.5))
else:
    textHorLMult = font.render('X ' + str(patternValues['horL']), True, (0, 0, 0))
    posters.blit(textHorLMult, (patternPosterX + 270 - 5 * len(str(patternValues['horL']))**(1.50 - 0.012 * len(str(patternValues['horL']))), patternPosterY + 123.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['horL']))**(1.50 - 0.012 * len(str(patternValues['horL']))), patternPosterY + 119.5))

# horXL mønsteret
if len(str(patternValues['horXL'])) >= 8:
    patternValue = round(patternValues['horXL'] * 10**(-1 * (len(str(patternValues['horXL'])) - 1)), 2)
    textHorXLMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['horXL'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['horXL'])) >= 10:
        posters.blit(textHorXLMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 151.5))
        posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 148.5))
    if len(str(patternValues['horXL'])) < 10:
        posters.blit(textHorXLMult, (patternPosterX + 212, patternPosterY + 151.5))
        posters.blit(coin2, (patternPosterX + 192, patternPosterY + 148.5))
else:
    textHorXLMult = font.render('X ' + str(patternValues['horXL']), True, (0, 0, 0))
    posters.blit(textHorXLMult, (patternPosterX + 270 - 5 * len(str(patternValues['horXL']))**(1.50 - 0.012 * len(str(patternValues['horXL']))), patternPosterY + 151.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['horXL']))**(1.50 - 0.012 * len(str(patternValues['horXL']))), patternPosterY + 146.5))

# zig mønsteret
if len(str(patternValues['zig'])) >= 11:
    patternValue = round(patternValues['zig'] * 10**(-1 * (len(str(patternValues['zig'])) - 1)), 2)
    textZigMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['zig'])) - 1), True, (0, 0, 0))
    posters.blit(textZigMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 179.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 176.5))
else:
    textZigMult = font.render('X ' + str(patternValues['zig']), True, (0, 0, 0))
    posters.blit(textZigMult, (patternPosterX + 270 - 5 * len(str(patternValues['zig']))**(1.50 - 0.012 * len(str(patternValues['zig']))), patternPosterY + 179.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['zig']))**(1.50 - 0.012 * len(str(patternValues['zig']))), patternPosterY + 176.5))

# zag mønsteret
if len(str(patternValues['zag'])) >= 11:
    patternValue = round(patternValues['zag'] * 10**(-1 * (len(str(patternValues['zag'])) - 1)), 2)
    textZagMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['zag'])) - 1), True, (0, 0, 0))
    posters.blit(textZagMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 206.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 204.5))
else:
    textZagMult = font.render('X ' + str(patternValues['zag']), True, (0, 0, 0))
    posters.blit(textZagMult, (patternPosterX + 270 - 5 * len(str(patternValues['zag']))**(1.50 - 0.012 * len(str(patternValues['zag']))), patternPosterY + 206.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['zag']))**(1.50 - 0.012 * len(str(patternValues['zag']))), patternPosterY + 204.5))

# above mønsteret
if len(str(patternValues['above'])) >= 8:
    patternValue = round(patternValues['above'] * 10**(-1 * (len(str(patternValues['above'])) - 1)), 2)
    textAboveMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['above'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['above'])) >= 10:
        posters.blit(textAboveMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 233.5))
        posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 230.5))
    if len(str(patternValues['above'])) < 10:
        posters.blit(textAboveMult, (patternPosterX + 212, patternPosterY + 233.5))
        posters.blit(coin2, (patternPosterX + 192, patternPosterY + 230.5))
else:
    textAboveMult = font.render('X ' + str(patternValues['above']), True, (0, 0, 0))
    posters.blit(textAboveMult, (patternPosterX + 270 - 5 * len(str(patternValues['above']))**(1.50 - 0.012 * len(str(patternValues['above']))), patternPosterY + 233.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['above']))**(1.50 - 0.012 * len(str(patternValues['above']))), patternPosterY + 230.5))

# below mønsteret
if len(str(patternValues['below'])) >= 8:
    patternValue = round(patternValues['below'] * 10**(-1 * (len(str(patternValues['below'])) - 1)), 2)
    textBelowMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['below'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['below'])) >= 10:
        posters.blit(textBelowMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 260))
        posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 257.5))
    if len(str(patternValues['below'])) < 10:
        posters.blit(textBelowMult, (patternPosterX + 212, patternPosterY + 260))
        posters.blit(coin2, (patternPosterX + 192, patternPosterY + 257.5))
else:
    textBelowMult = font.render('X ' + str(patternValues['below']), True, (0, 0, 0))  
    posters.blit(textBelowMult, (patternPosterX + 270 - 5 * len(str(patternValues['below']))**(1.50 - 0.012 * len(str(patternValues['below']))), patternPosterY + 260.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['below']))**(1.50 - 0.012 * len(str(patternValues['below']))), patternPosterY + 257.5))

# eye mønsteret
if len(str(patternValues['eye'])) >= 11:
    patternValue = round(patternValues['eye'] * 10**(-1 * (len(str(patternValues['eye'])) - 1)), 2)
    textEyeMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['eye'])) - 1), True, (0, 0, 0))
    posters.blit(textEyeMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 287.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 284.5))
else:
    textEyeMult = font.render('X ' + str(patternValues['eye']), True, (0, 0, 0))  
    posters.blit(textEyeMult, (patternPosterX + 270 - 5 * len(str(patternValues['eye']))**(1.50 - 0.012 * len(str(patternValues['eye']))), patternPosterY + 287.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['eye']))**(1.50 - 0.012 * len(str(patternValues['eye']))), patternPosterY + 284.5))

# jackpot mønsteret
if len(str(patternValues['jackpot'])) >= 8:
    patternValue = round(patternValues['jackpot'] * 10**(-1 * (len(str(patternValues['jackpot'])) - 1)), 2)
    textJackpotMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['jackpot'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['jackpot'])) >= 10:
        posters.blit(textJackpotMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 314.5))
        posters.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 310.5))
    if len(str(patternValues['jackpot'])) < 10:
        posters.blit(textJackpotMult, (patternPosterX + 212, patternPosterY + 314.5))
        posters.blit(coin2, (patternPosterX + 192, patternPosterY + 310.5))
else:
    textJackpotMult = font.render('X ' + str(patternValues['jackpot']), True, (0, 0, 0)) 
    posters.blit(textJackpotMult, (patternPosterX + 270 - 5 * len(str(patternValues['jackpot']))**(1.50 - 0.012 * len(str(patternValues['jackpot']))), patternPosterY + 314.5))
    posters.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['jackpot']))**(1.50 - 0.012 * len(str(patternValues['jackpot']))), patternPosterY + 310.5))

# text og mønstre på plakaten
posters.blit(patternHor, (patternPosterX + 25, patternPosterY + 40))
posters.blit(textHor, textHor.get_rect(center=(patternPosterX + 95, patternPosterY + 55)))

posters.blit(patternVer, (patternPosterX + 25, patternPosterY + 66))
posters.blit(textVer, textVer.get_rect(center=(patternPosterX + 93, patternPosterY + 81)))

posters.blit(patternDiag, (patternPosterX + 25, patternPosterY + 93.5))
posters.blit(textDiag, textDiag.get_rect(center=(patternPosterX + 98, patternPosterY + 108.5)))

posters.blit(patternHorL, (patternPosterX + 25, patternPosterY + 120.5))
posters.blit(textHorL, textHorL.get_rect(center=(patternPosterX + 105, patternPosterY + 136.5)))

posters.blit(patternHorXL, (patternPosterX + 25, patternPosterY + 146.5))
posters.blit(textHorXL, textHorXL.get_rect(center=(patternPosterX + 110, patternPosterY + 161.5)))

posters.blit(patternZig, (patternPosterX + 25, patternPosterY + 173.5))
posters.blit(textZig, textZig.get_rect(center=(patternPosterX + 90, patternPosterY + 188.5)))

posters.blit(patternZag, (patternPosterX + 25, patternPosterY + 200.5))
posters.blit(textZag, textZag.get_rect(center=(patternPosterX + 95, patternPosterY + 215.5)))

posters.blit(patternAbove, (patternPosterX + 25, patternPosterY + 227.5))
posters.blit(textAbove, textAbove.get_rect(center=(patternPosterX + 108, patternPosterY + 242.5)))

posters.blit(patternBelow, (patternPosterX + 25, patternPosterY + 254.5))
posters.blit(textBelow, textBelow.get_rect(center=(patternPosterX + 110, patternPosterY + 269.5)))

posters.blit(patternEye, (patternPosterX + 25, patternPosterY + 281.5))
posters.blit(textEye, textEye.get_rect(center=(patternPosterX + 92, patternPosterY + 296.5)))

posters.blit(patternJackpot, (patternPosterX + 25, patternPosterY + 308.5))
posters.blit(textJackpot, textJackpot.get_rect(center=(patternPosterX + 120, patternPosterY + 323.5)))

posters.blit(textPatterns, textPatterns.get_rect(center=(posterBackground.get_width()/2+patternPosterX, patternPosterY + 30)))
posters.blit(textPatternsMult, textPatternsMult.get_rect(center=(posterBackground.get_width()/2+patternPosterX, patternPosterY +  355)))
posters.blit(PatternsMult, PatternsMult.get_rect(center=(patternPosterX + 240, patternPosterY + 380)))
posters.blit(coin, (patternPosterX + 200, patternPosterY + 364.5))


##############################################################################################################
# the window
running = True
clock = pygame.time.Clock()

deltaTime = 0.1

while running:
    screen.fill((0, 0, 0))
    screen.blit(posters, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    deltaTime = max(0.001, min(0.1, deltaTime))


pygame.quit()