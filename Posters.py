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

# posters
symbolsPoster = pygame.Surface((posterBackground.get_width(), posterBackground.get_height()), pygame.SRCALPHA)
patternPoster = pygame.Surface((posterBackground.get_width(), posterBackground.get_height()), pygame.SRCALPHA)
##############################################################################################################
# Poster for symbol value
symbolPosterX = 0
symbolPosterY = 15
symbolsPoster.blit(posterBackground, (symbolPosterX, symbolPosterY - 15))
# text on poster
textSymbols = font.render('---     SYMBOLS     ---', True, (0, 0, 0))
textSymbolsMult = font.render('  SYMBOLS     MULTIPLIER ', True, (0, 0, 0))
SymbolsMult = font.render(' X ' + str(symbolMult), True, (0, 0, 0))
# Value for each symbol, if value is >= 7 digits, it will be displayed in scientific notation
# Lemon
if len(str(symbolValues[0])) >= 7:
    symbolValue = round(symbolValues[0] * 10**(-1 * (len(str(symbolValues[0])) - 1)), 2)
    textLemonValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[0])) - 1), True, (0, 0, 0))
else:
    textLemonValue = font.render(': ' + str(symbolValues[0]), True, (0, 0, 0))
# Cherry
if len(str(symbolValues[1])) >= 7:
    symbolValue = round(symbolValues[1] * 10**(-1 * (len(str(symbolValues[1])) - 1)), 2)
    textCherryValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[1])) - 1), True, (0, 0, 0))
else:
    textCherryValue = font.render(': ' + str(symbolValues[1]), True, (0, 0, 0))
# Clover
if len(str(symbolValues[2])) >= 7:
    symbolValue = round(symbolValues[2] * 10**(-1 * (len(str(symbolValues[2])) - 1)), 2)
    textCloverValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[2])) - 1), True, (0, 0, 0))
else:
    textCloverValue = font.render(': ' + str(symbolValues[2]), True, (0, 0, 0))
# Bell
if len(str(symbolValues[3])) >= 7:
    symbolValue = round(symbolValues[3] * 10**(-1 * (len(str(symbolValues[3])) - 1)), 2)
    textBellValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[3])) - 1), True, (0, 0, 0))
else:
    textBellValue = font.render(': ' + str(symbolValues[3]), True, (0, 0, 0))
# Diamond
if len(str(symbolValues[4])) >= 7:
    symbolValue = round(symbolValues[4] * 10**(-1 * (len(str(symbolValues[4])) - 1)), 2)
    textDiamondValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[4])) - 1), True, (0, 0, 0))
else:
    textDiamondValue = font.render(': ' + str(symbolValues[4]), True, (0, 0, 0))
# Treasure
if len(str(symbolValues[5])) >= 7:
    symbolValue = round(symbolValues[5] * 10**(-1 * (len(str(symbolValues[5])) - 1)), 2)
    textTreasureValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[5])) - 1), True, (0, 0, 0))
else:
    textTreasureValue = font.render(': ' + str(symbolValues[5]), True, (0, 0, 0))
# Seven
if len(str(symbolValues[6])) >= 7:
    symbolValue = round(symbolValues[6] * 10**(-1 * (len(str(symbolValues[6])) - 1)), 2)
    textSevenValue = font.render(': ' + str(symbolValue) + 'E+' + str(len(str(symbolValues[6])) - 1), True, (0, 0, 0))
else:
    textSevenValue = font.render(': ' + str(symbolValues[6]), True, (0, 0, 0))

# Chance for each symbol is displayed as a percentage with 1 decimal.
textLemonChance = font.render(': ' + str(round(symbolWeights[0]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textCherryChance = font.render(': ' + str(round(symbolWeights[1]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textCloverChance = font.render(': ' + str(round(symbolWeights[2]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textBellChance = font.render(': ' + str(round(symbolWeights[3]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textDiamondChance = font.render(': ' + str(round(symbolWeights[4]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textTreasureChance = font.render(': ' + str(round(symbolWeights[5]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
textSevenChance = font.render(': ' + str(round(symbolWeights[6]/sum(symbolWeights)*100, 1)) + '%', True, (0, 0, 0))

# text on poster
symbolsPoster.blit(textSymbols, textSymbols.get_rect(center=(posterBackground.get_width()/2, symbolPosterY + 30)))
symbolsPoster.blit(textSymbolsMult, textSymbolsMult.get_rect(center=(posterBackground.get_width()/2, symbolPosterY + 36 * symbolScale + 305)))
symbolsPoster.blit(SymbolsMult, SymbolsMult.get_rect(center=(symbolPosterX + 240, symbolPosterY + 370)))
symbolsPoster.blit(textLemonValue, (symbolPosterX + 100, symbolPosterY + 40))
symbolsPoster.blit(textCherryValue, (symbolPosterX + 100, symbolPosterY + 80))
symbolsPoster.blit(textCloverValue, (symbolPosterX + 100, symbolPosterY + 120))
symbolsPoster.blit(textBellValue, (symbolPosterX + 100, symbolPosterY + 160))
symbolsPoster.blit(textDiamondValue, (symbolPosterX + 100, symbolPosterY + 200))
symbolsPoster.blit(textTreasureValue, (symbolPosterX + 100, symbolPosterY + 245))
symbolsPoster.blit(textSevenValue, (symbolPosterX + 100, symbolPosterY + 288))
symbolsPoster.blit(textLemonChance, (symbolPosterX + 220, symbolPosterY + 40))
symbolsPoster.blit(textCherryChance, (symbolPosterX + 220, symbolPosterY + 80))
symbolsPoster.blit(textCloverChance, (symbolPosterX + 220, symbolPosterY + 120))
symbolsPoster.blit(textBellChance, (symbolPosterX + 220, symbolPosterY + 160))
symbolsPoster.blit(textDiamondChance, (symbolPosterX + 220, symbolPosterY + 200))
symbolsPoster.blit(textTreasureChance, (symbolPosterX + 220, symbolPosterY + 245))
symbolsPoster.blit(textSevenChance, (symbolPosterX + 220, symbolPosterY + 287.5))

    # Symbols on poster
symbolsPoster.blit(lemon, (symbolPosterX + 25, symbolPosterY + 40))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 40))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 40))
symbolsPoster.blit(cherry, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 40))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 42))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 43))
symbolsPoster.blit(clover, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 80))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 82))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 83))
symbolsPoster.blit(bell, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 120))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 122))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 123))
symbolsPoster.blit(diamond, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 162.5))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 164.5))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 163))
symbolsPoster.blit(treasure, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 205))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 207))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 208))
symbolsPoster.blit(seven, (symbolPosterX + 25, symbolPosterY + 36 * symbolScale + 247.5))
symbolsPoster.blit(coin, (symbolPosterX + 75, symbolPosterY + 36 * symbolScale + 249.5))
symbolsPoster.blit(dice, (symbolPosterX + 190, symbolPosterY + 36 * symbolScale + 250))
symbolsPoster.blit(coin, (symbolPosterX + 200, symbolPosterY + 355))

##############################################################################################################
# Poster for pattern value
patternPosterX = 0
patternPosterY = 15
patternPoster.blit(posterBackground, (patternPosterX, patternPosterY - 15))

# text for the poster
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
# hor
if len(str(patternValues['hor'])) >= 11:
    patternValue = round(patternValues['hor'] * 10**(-1 * (len(str(patternValues['hor'])) - 1)), 2)
    textHorMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['hor'])) - 1), True, (0, 0, 0))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 40))
    patternPoster.blit(textHorMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 40))
else:
    textHorMult = font.render('X ' + str(patternValues['hor']), True, (0, 0, 0))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['hor']))**(1.50 - 0.012 * len(str(patternValues['hor']))), patternPosterY + 40))
    patternPoster.blit(textHorMult, (patternPosterX + 270 - 5 * len(str(patternValues['hor']))**(1.50 - 0.012 * len(str(patternValues['hor']))), patternPosterY + 40))
# vert
if len(str(patternValues['vert'])) >= 11:
    patternValue = round(patternValues['vert'] * 10**(-1 * (len(str(patternValues['vert'])) - 1)), 2)
    textVerMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['vert'])) - 1), True, (0, 0, 0))
    patternPoster.blit(textVerMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 68.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 80))
else:
    textVerMult = font.render('X ' + str(patternValues['vert']), True, (0, 0, 0))
    patternPoster.blit(textVerMult, (patternPosterX + 270 - 5 * len(str(patternValues['vert']))**(1.50 - 0.012 * len(str(patternValues['vert']))), patternPosterY + 68.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['vert']))**(1.50 - 0.012 * len(str(patternValues['vert']))), symbolScale + 80))
# diag
if len(str(patternValues['diag'])) >= 11:
    patternValue = round(patternValues['diag'] * 10**(-1 * (len(str(patternValues['diag'])) - 1)), 2)
    textDiagMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['diag'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['diag'])) >= 11:
        patternPoster.blit(textDiagMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 96))
        patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 107.5))
    if len(str(patternValues['diag'])) < 11:
        patternPoster.blit(textDiagMult, (patternPosterX + 212, patternPosterY + 96))
        patternPoster.blit(coin2, (patternPosterX + 192, symbolScale + 107.5))
else:
    textDiagMult = font.render('X ' + str(patternValues['diag']), True, (0, 0, 0))
    patternPoster.blit(textDiagMult, (patternPosterX + 270 - 5 * len(str(patternValues['diag']))**(1.50 - 0.012 * len(str(patternValues['diag']))), patternPosterY + 96))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['diag']))**(1.50 - 0.012 * len(str(patternValues['diag']))), symbolScale + 107.5))
# horL
if len(str(patternValues['horL'])) >= 10:
    patternValue = round(patternValues['horL'] * 10**(-1 * (len(str(patternValues['horL'])) - 1)), 2)
    textHorLMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['horL'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['horL'])) >= 10:
        patternPoster.blit(textHorLMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 123.5))
        patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 134.5))
    if len(str(patternValues['horL'])) < 10:
        patternPoster.blit(textHorLMult, (patternPosterX + 212, patternPosterY + 123.5))
        patternPoster.blit(coin2, (patternPosterX + 192, symbolScale + 134.5))
else:
    textHorLMult = font.render('X ' + str(patternValues['horL']), True, (0, 0, 0))
    patternPoster.blit(textHorLMult, (patternPosterX + 270 - 5 * len(str(patternValues['horL']))**(1.50 - 0.012 * len(str(patternValues['horL']))), patternPosterY + 123.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['horL']))**(1.50 - 0.012 * len(str(patternValues['horL']))), symbolScale + 134.5))
# horXL
if len(str(patternValues['horXL'])) >= 8:
    patternValue = round(patternValues['horXL'] * 10**(-1 * (len(str(patternValues['horXL'])) - 1)), 2)
    textHorXLMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['horXL'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['horXL'])) >= 10:
        patternPoster.blit(textHorXLMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 151.5))
        patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 161.5))
    if len(str(patternValues['horXL'])) < 10:
        patternPoster.blit(textHorXLMult, (patternPosterX + 212, patternPosterY + 151.5))
        patternPoster.blit(coin2, (patternPosterX + 192, symbolScale + 161.5))
else:
    textHorXLMult = font.render('X ' + str(patternValues['horXL']), True, (0, 0, 0))
    patternPoster.blit(textHorXLMult, (patternPosterX + 270 - 5 * len(str(patternValues['horXL']))**(1.50 - 0.012 * len(str(patternValues['horXL']))), patternPosterY + 151.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['horXL']))**(1.50 - 0.012 * len(str(patternValues['horXL']))), symbolScale + 161.5))
# zig
if len(str(patternValues['zig'])) >= 11:
    patternValue = round(patternValues['zig'] * 10**(-1 * (len(str(patternValues['zig'])) - 1)), 2)
    textZigMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['zig'])) - 1), True, (0, 0, 0))
    patternPoster.blit(textZigMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 179.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 188.5))
else:
    textZigMult = font.render('X ' + str(patternValues['zig']), True, (0, 0, 0))
    patternPoster.blit(textZigMult, (patternPosterX + 270 - 5 * len(str(patternValues['zig']))**(1.50 - 0.012 * len(str(patternValues['zig']))), patternPosterY + 179.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['zig']))**(1.50 - 0.012 * len(str(patternValues['zig']))), symbolScale + 188.5))
# zag
if len(str(patternValues['zag'])) >= 11:
    patternValue = round(patternValues['zag'] * 10**(-1 * (len(str(patternValues['zag'])) - 1)), 2)
    textZagMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['zag'])) - 1), True, (0, 0, 0))
    patternPoster.blit(textZagMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 206.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 215.5))
else:
    textZagMult = font.render('X ' + str(patternValues['zag']), True, (0, 0, 0))
    patternPoster.blit(textZagMult, (patternPosterX + 270 - 5 * len(str(patternValues['zag']))**(1.50 - 0.012 * len(str(patternValues['zag']))), patternPosterY + 206.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['zag']))**(1.50 - 0.012 * len(str(patternValues['zag']))), symbolScale + 215.5))
# above
if len(str(patternValues['above'])) >= 8:
    patternValue = round(patternValues['above'] * 10**(-1 * (len(str(patternValues['above'])) - 1)), 2)
    textAboveMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['above'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['above'])) >= 10:
        patternPoster.blit(textAboveMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 233.5))
        patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 242.5))
    if len(str(patternValues['above'])) < 10:
        patternPoster.blit(textAboveMult, (patternPosterX + 212, patternPosterY + 233.5))
        patternPoster.blit(coin2, (patternPosterX + 192, symbolScale + 242.5))
else:
    textAboveMult = font.render('X ' + str(patternValues['above']), True, (0, 0, 0))
    patternPoster.blit(textAboveMult, (patternPosterX + 270 - 5 * len(str(patternValues['above']))**(1.50 - 0.012 * len(str(patternValues['above']))), patternPosterY + 233.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['above']))**(1.50 - 0.012 * len(str(patternValues['above']))), symbolScale + 242.5))
# below
if len(str(patternValues['below'])) >= 8:
    patternValue = round(patternValues['below'] * 10**(-1 * (len(str(patternValues['below'])) - 1)), 2)
    textBelowMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['below'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['below'])) >= 10:
        patternPoster.blit(textBelowMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 260))
        patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 273.5))
    if len(str(patternValues['below'])) < 10:
        patternPoster.blit(textBelowMult, (patternPosterX + 212, patternPosterY + 260))
        patternPoster.blit(coin2, (patternPosterX + 192, symbolScale + 273.5))
else:
    textBelowMult = font.render('X ' + str(patternValues['below']), True, (0, 0, 0))  
    patternPoster.blit(textBelowMult, (patternPosterX + 270 - 5 * len(str(patternValues['below']))**(1.50 - 0.012 * len(str(patternValues['below']))), patternPosterY + 260.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['below']))**(1.50 - 0.012 * len(str(patternValues['below']))), symbolScale + 269.5))
# eye
if len(str(patternValues['eye'])) >= 11:
    patternValue = round(patternValues['eye'] * 10**(-1 * (len(str(patternValues['eye'])) - 1)), 2)
    textEyeMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['eye'])) - 1), True, (0, 0, 0))
    patternPoster.blit(textEyeMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 287.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 296.5))
else:
    textEyeMult = font.render('X ' + str(patternValues['eye']), True, (0, 0, 0))  
    patternPoster.blit(textEyeMult, (patternPosterX + 270 - 5 * len(str(patternValues['eye']))**(1.50 - 0.012 * len(str(patternValues['eye']))), patternPosterY + 287.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['eye']))**(1.50 - 0.012 * len(str(patternValues['eye']))), symbolScale + 296.5))
# jackpot
if len(str(patternValues['jackpot'])) >= 8:
    patternValue = round(patternValues['jackpot'] * 10**(-1 * (len(str(patternValues['jackpot'])) - 1)), 2)
    textJackpotMult = font.render('X ' + str(patternValue) + 'E+' + str(len(str(patternValues['jackpot'])) - 1), True, (0, 0, 0))
    if len(str(patternValues['jackpot'])) >= 10:
        patternPoster.blit(textJackpotMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 314.5))
        patternPoster.blit(coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), symbolScale + 323.5))
    if len(str(patternValues['jackpot'])) < 10:
        patternPoster.blit(textJackpotMult, (patternPosterX + 212, patternPosterY + 314.5))
        patternPoster.blit(coin2, (patternPosterX + 192, symbolScale + 323.5))
else:
    textJackpotMult = font.render('X ' + str(patternValues['jackpot']), True, (0, 0, 0)) 
    patternPoster.blit(textJackpotMult, (patternPosterX + 270 - 5 * len(str(patternValues['jackpot']))**(1.50 - 0.012 * len(str(patternValues['jackpot']))), patternPosterY + 314.5))
    patternPoster.blit(coin2, (patternPosterX + 250 - 5 * len(str(patternValues['jackpot']))**(1.50 - 0.012 * len(str(patternValues['jackpot']))), symbolScale + 323.5))

# text and patterns on poster
patternPoster.blit(textPatterns, textPatterns.get_rect(center=(posterBackground.get_width()/2+patternPosterX, patternPosterY + 30)))
patternPoster.blit(textPatternsMult, textPatternsMult.get_rect(center=(posterBackground.get_width()/2+patternPosterX, patternPosterY +  355)))
patternPoster.blit(PatternsMult, PatternsMult.get_rect(center=(patternPosterX + 240, patternPosterY + 380)))
patternPoster.blit(patternHor, (patternPosterX + 25, patternPosterY + 40))
patternPoster.blit(textHor, textHor.get_rect(center=(patternPosterX + 95, patternPosterY + 55)))
patternPoster.blit(patternVer, (patternPosterX + 25, symbolScale + 80))
patternPoster.blit(textVer, textVer.get_rect(center=(patternPosterX + 93, symbolScale + 95)))
patternPoster.blit(patternDiag, (patternPosterX + 25, symbolScale + 107.5))
patternPoster.blit(textDiag, textDiag.get_rect(center=(patternPosterX + 98, symbolScale + 107.5 + 15)))
patternPoster.blit(patternHorL, (patternPosterX + 25, symbolScale + 134.5))
patternPoster.blit(textHorL, textHorL.get_rect(center=(patternPosterX + 105, symbolScale + 134.5 + 15)))
patternPoster.blit(patternHorXL, (patternPosterX + 25, symbolScale + 161.5))
patternPoster.blit(textHorXL, textHorXL.get_rect(center=(patternPosterX + 110, symbolScale + 161.5 + 15)))
patternPoster.blit(patternZig, (patternPosterX + 25, symbolScale + 188.5))
patternPoster.blit(textZig, textZig.get_rect(center=(patternPosterX + 90, symbolScale + 188.5 + 15)))
patternPoster.blit(patternZag, (patternPosterX + 25, symbolScale + 215.5))
patternPoster.blit(textZag, textZag.get_rect(center=(patternPosterX + 95, symbolScale + 215.5 + 15)))
patternPoster.blit(patternAbove, (patternPosterX + 25, symbolScale + 242.5))
patternPoster.blit(textAbove, textAbove.get_rect(center=(patternPosterX + 108, symbolScale + 242.5 + 15)))
patternPoster.blit(patternBelow, (patternPosterX + 25, symbolScale + 269.5))
patternPoster.blit(textBelow, textBelow.get_rect(center=(patternPosterX + 110, symbolScale + 269.5 + 15)))
patternPoster.blit(patternEye, (patternPosterX + 25, symbolScale + 296.5))
patternPoster.blit(textEye, textEye.get_rect(center=(patternPosterX + 92, symbolScale + 296.5 + 15)))
patternPoster.blit(patternJackpot, (patternPosterX + 25, symbolScale + 323.5))
patternPoster.blit(textJackpot, textJackpot.get_rect(center=(patternPosterX + 120, symbolScale + 323.5 + 15)))
patternPoster.blit(coin, (patternPosterX + 200, symbolScale + 377.5))


##############################################################################################################
# the window
running = True
clock = pygame.time.Clock()

deltaTime = 0.1

while running:
    screen.fill((0, 0, 0))
    screen.blit(symbolsPoster, (30, 30))
    screen.blit(patternPoster, (375, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    deltaTime = max(0.001, min(0.1, deltaTime))


pygame.quit()