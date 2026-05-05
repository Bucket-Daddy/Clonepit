#Posters script
import pygame
import config.game_config as config

class PostersRoom:

    def __init__(self):

        posterScale = 0.80
        self.symbolScale = 1
        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)
    
        #Loader billeder
        self.lemon = pygame.image.load('assets/SymbolLemon.webp')
        self.cherry = pygame.image.load('assets/SymbolCherry.webp')
        self.clover = pygame.image.load('assets/SymbolClover.webp')
        self.bell = pygame.image.load('assets/SymbolBell.webp')
        self.diamond = pygame.image.load('assets/SymbolDiamond.webp')
        self.treasure = pygame.image.load('assets/SymbolTreasureChest.webp')
        self.seven = pygame.image.load('assets/SymbolSeven.webp')
        self.patternAbove = pygame.image.load('assets/PatternAbove.webp')
        self.patternBelow = pygame.image.load('assets/PatternBelow.webp')
        self.patternDiag = pygame.image.load('assets/PatternDiag.webp')
        self.patternEye = pygame.image.load('assets/PatternEye.webp')
        self.patternHor = pygame.image.load('assets/PatternHor.webp')
        self.patternHorL = pygame.image.load('assets/PatternHorL.webp')
        self.patternHorXL = pygame.image.load('assets/PatternHorXL.webp')
        self.patternJackpot = pygame.image.load('assets/PatternJackpot.webp')
        self.patternVer = pygame.image.load('assets/PatternVer.webp')
        self.patternZag = pygame.image.load('assets/PatternZag.webp')
        self.patternZig = pygame.image.load('assets/PatternZig.webp')
        self.coin = pygame.image.load('assets/Coin.webp')
        self.coin2 = pygame.image.load('assets/coin2.webp')
        self.dice = pygame.image.load('assets/D6.png').convert()
        self.posterBackground = pygame.image.load('assets/PosterBackground.png').convert()

        #Skalerer billeder
        self.lemon = pygame.transform.scale(self.lemon, (36 * self.symbolScale, 36 * self.symbolScale))
        self.cherry = pygame.transform.scale(self.cherry, (36 * self.symbolScale, 36 * self.symbolScale))
        self.clover = pygame.transform.scale(self.clover, (36 * self.symbolScale, 36 * self.symbolScale))
        self.bell = pygame.transform.scale(self.bell, (36 * self.symbolScale, 36 * self.symbolScale))
        self.diamond = pygame.transform.scale(self.diamond, (36 * self.symbolScale, 36 * self.symbolScale))
        self.treasure = pygame.transform.scale(self.treasure, (36 * self.symbolScale, 36 * self.symbolScale))
        self.seven = pygame.transform.scale(self.seven, (36 * self.symbolScale, 36 * self.symbolScale))
        self.patternHor = pygame.transform.scale(self.patternHor, (self.patternHor.get_width() * 2/7, self.patternHor.get_height() * 2/7))
        self.patternVer = pygame.transform.scale(self.patternVer, (self.patternVer.get_width() * 2/7, self.patternVer.get_height() * 2/7))
        self.patternDiag = pygame.transform.scale(self.patternDiag, (self.patternDiag.get_width() * 2/7, self.patternDiag.get_height() * 2/7))
        self.patternHorL = pygame.transform.scale(self.patternHorL, (self.patternHorL.get_width() * 2/7, self.patternHorL.get_height() * 2/7))
        self.patternHorXL = pygame.transform.scale(self.patternHorXL, (self.patternHorXL.get_width() * 2/7, self.patternHorXL.get_height() * 2/7))
        self.patternZag = pygame.transform.scale(self.patternZag, (self.patternZag.get_width() * 2/7, self.patternZag.get_height() * 2/7))
        self.patternZig = pygame.transform.scale(self.patternZig, (self.patternZig.get_width() * 2/7, self.patternZig.get_height() * 2/7))
        self.patternAbove = pygame.transform.scale(self.patternAbove, (self.patternAbove.get_width() * 2/7, self.patternAbove.get_height() * 2/7))
        self.patternBelow = pygame.transform.scale(self.patternBelow, (self.patternBelow.get_width() * 2/7, self.patternBelow.get_height() * 2/7))
        self.patternEye = pygame.transform.scale(self.patternEye, (self.patternEye.get_width() * 2/7, self.patternEye.get_height() * 2/7))
        self.patternJackpot = pygame.transform.scale(self.patternJackpot, (self.patternJackpot.get_width() * 2/7, self.patternJackpot.get_height() * 2/7))
        self.coin = pygame.transform.scale(self.coin, (self.coin.get_width() * 0.15, self.coin.get_height() * 0.15))
        self.coin2 = pygame.transform.scale(self.coin2, (self.coin2.get_width() * 0.12, self.coin2.get_height() * 0.12))
        self.dice = pygame.transform.scale(self.dice, (self.dice.get_width() * 0.05, self.dice.get_height() * 0.05)).convert()
        self.dice.set_colorkey((255, 0, 214))
        self.posterBackground = pygame.transform.scale(self.posterBackground, (self.posterBackground.get_width() * posterScale, self.posterBackground.get_height() * posterScale))
        self.posterBackground.set_colorkey((0, 0, 0))

        # danner baggrunden
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (1200, 750))
        self.posters = pygame.Surface((1200, 750), pygame.SRCALPHA)
        self.posters.blit(background, (-3, -3))

    def draw(self, screen):
        screen.blit(self.posters, (0, 0))

        ##############################################################################################################
        # placering af plakaten
        symbolPosterX = 30
        symbolPosterY = 45
        self.posters.blit(self.posterBackground, (symbolPosterX, symbolPosterY - 15))

        # texten på plakaten defineres
        textSymbols = self.font.render('---     SYMBOLS     ---', True, (0, 0, 0))
        textSymbolsMult = self.font.render('  SYMBOLS     MULTIPLIER ', True, (0, 0, 0))
        SymbolsMult = self.font.render(' X ' + str(config.symbolMult), True, (0, 0, 0))

        # værdien for hver symbol, hvis værdien er >= 7 cifre, vil den blive vist i videnskabelig notation
        # Lemon - placering af værdi
        if len(str(config.symbolValues[0])) >= 7:
            symbolValue = round(config.symbolValues[0] * 10**(-1 * (len(str(config.symbolValues[0])) - 1)), 2)
            textLemonValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[0])) - 1), True, (0, 0, 0))
        else:
            textLemonValue = self.font.render(': ' + str(config.symbolValues[0]), True, (0, 0, 0))

        # Cherry - placering af værdi
        if len(str(config.symbolValues[1])) >= 7:
            symbolValue = round(config.symbolValues[1] * 10**(-1 * (len(str(config.symbolValues[1])) - 1)), 2)
            textCherryValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[1])) - 1), True, (0, 0, 0))
        else:
            textCherryValue = self.font.render(': ' + str(config.symbolValues[1]), True, (0, 0, 0))

        # Clover - placering af værdi
        if len(str(config.symbolValues[2])) >= 7:
            symbolValue = round(config.symbolValues[2] * 10**(-1 * (len(str(config.symbolValues[2])) - 1)), 2)
            textCloverValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[2])) - 1), True, (0, 0, 0))
        else:
            textCloverValue = self.font.render(': ' + str(config.symbolValues[2]), True, (0, 0, 0))

        # Bell - placering af værdi
        if len(str(config.symbolValues[3])) >= 7:
            symbolValue = round(config.symbolValues[3] * 10**(-1 * (len(str(config.symbolValues[3])) - 1)), 2)
            textBellValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[3])) - 1), True, (0, 0, 0))
        else:
            textBellValue = self.font.render(': ' + str(config.symbolValues[3]), True, (0, 0, 0))

        # Diamond - placering af værdi
        if len(str(config.symbolValues[4])) >= 7:
            symbolValue = round(config.symbolValues[4] * 10**(-1 * (len(str(config.symbolValues[4])) - 1)), 2)
            textDiamondValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[4])) - 1), True, (0, 0, 0))
        else:
            textDiamondValue = self.font.render(': ' + str(config.symbolValues[4]), True, (0, 0, 0))

        # Treasure - placering af værdi
        if len(str(config.symbolValues[5])) >= 7:
            symbolValue = round(config.symbolValues[5] * 10**(-1 * (len(str(config.symbolValues[5])) - 1)), 2)
            textTreasureValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[5])) - 1), True, (0, 0, 0))
        else:
            textTreasureValue = self.font.render(': ' + str(config.symbolValues[5]), True, (0, 0, 0))

        # Seven - placering af værdi
        if len(str(config.symbolValues[6])) >= 7:
            symbolValue = round(config.symbolValues[6] * 10**(-1 * (len(str(config.symbolValues[6])) - 1)), 2)
            textSevenValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[6])) - 1), True, (0, 0, 0))
        else:
            textSevenValue = self.font.render(': ' + str(config.symbolValues[6]), True, (0, 0, 0))

        # Chancen for hver symbol, vist som en procentdel med 1 decimal.
        textLemonChance = self.font.render(': ' + str(round(config.symbolWeights[0]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textCherryChance = self.font.render(': ' + str(round(config.symbolWeights[1]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textCloverChance = self.font.render(': ' + str(round(config.symbolWeights[2]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textBellChance = self.font.render(': ' + str(round(config.symbolWeights[3]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textDiamondChance = self.font.render(': ' + str(round(config.symbolWeights[4]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textTreasureChance = self.font.render(': ' + str(round(config.symbolWeights[5]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textSevenChance = self.font.render(': ' + str(round(config.symbolWeights[6]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))

        # texten på plakaten
        self.posters.blit(textSymbols, textSymbols.get_rect(center=(self.posterBackground.get_width()/2 + symbolPosterX, symbolPosterY + 30)))
        self.posters.blit(textSymbolsMult, textSymbolsMult.get_rect(center=(self.posterBackground.get_width()/2 + symbolPosterX, symbolPosterY + 36 * self.symbolScale + 305)))
        self.posters.blit(SymbolsMult, SymbolsMult.get_rect(center=(symbolPosterX + 240, symbolPosterY + 370)))
        self.posters.blit(textLemonValue, (symbolPosterX + 100, symbolPosterY + 40))
        self.posters.blit(textCherryValue, (symbolPosterX + 100, symbolPosterY + 80))
        self.posters.blit(textCloverValue, (symbolPosterX + 100, symbolPosterY + 120))
        self.posters.blit(textBellValue, (symbolPosterX + 100, symbolPosterY + 160))
        self.posters.blit(textDiamondValue, (symbolPosterX + 100, symbolPosterY + 200))
        self.posters.blit(textTreasureValue, (symbolPosterX + 100, symbolPosterY + 245))
        self.posters.blit(textSevenValue, (symbolPosterX + 100, symbolPosterY + 288))
        self.posters.blit(textLemonChance, (symbolPosterX + 220, symbolPosterY + 40))
        self.posters.blit(textCherryChance, (symbolPosterX + 220, symbolPosterY + 80))
        self.posters.blit(textCloverChance, (symbolPosterX + 220, symbolPosterY + 120))
        self.posters.blit(textBellChance, (symbolPosterX + 220, symbolPosterY + 160))
        self.posters.blit(textDiamondChance, (symbolPosterX + 220, symbolPosterY + 200))
        self.posters.blit(textTreasureChance, (symbolPosterX + 220, symbolPosterY + 245))
        self.posters.blit(textSevenChance, (symbolPosterX + 220, symbolPosterY + 287.5))

        # Symboler på plakaten
        self.posters.blit(self.lemon, (symbolPosterX + 25, symbolPosterY + 40))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 40))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 40))
        self.posters.blit(self.cherry, (symbolPosterX + 25, symbolPosterY + 36 * self.symbolScale + 40))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 36 * self.symbolScale + 42))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 36 * self.symbolScale + 43))
        self.posters.blit(self.clover, (symbolPosterX + 25, symbolPosterY + 36 * self.symbolScale + 80))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 36 * self.symbolScale + 82))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 36 * self.symbolScale + 83))
        self.posters.blit(self.bell, (symbolPosterX + 25, symbolPosterY + 36 * self.symbolScale + 120))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 36 * self.symbolScale + 122))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 36 * self.symbolScale + 123))
        self.posters.blit(self.diamond, (symbolPosterX + 25, symbolPosterY + 36 * self.symbolScale + 162.5))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 36 * self.symbolScale + 164.5))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 36 * self.symbolScale + 163))
        self.posters.blit(self.treasure, (symbolPosterX + 25, symbolPosterY + 36 * self.symbolScale + 205))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 36 * self.symbolScale + 207))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 36 * self.symbolScale + 208))
        self.posters.blit(self.seven, (symbolPosterX + 25, symbolPosterY + 36 * self.symbolScale + 247.5))
        self.posters.blit(self.coin, (symbolPosterX + 75, symbolPosterY + 36 * self.symbolScale + 249.5))
        self.posters.blit(self.dice, (symbolPosterX + 190, symbolPosterY + 36 * self.symbolScale + 250))
        self.posters.blit(self.coin, (symbolPosterX + 200, symbolPosterY + 355))

        ##############################################################################################################
        # Plakaten med værdierne for mønstrene
        patternPosterX = symbolPosterX + self.posterBackground.get_width() + 30
        patternPosterY = symbolPosterY
        self.posters.blit(self.posterBackground, (patternPosterX, patternPosterY - 15))

        # texten på plakaten
        textPatterns = self.font.render('---     PATTERNS     ---', True, (0, 0, 0))
        textPatternsMult = self.font.render('  PATTERN     MULTIPLIER ', True, (0, 0, 0))
        PatternsMult = self.font.render(' X ' + str(config.patternMult), True, (0, 0, 0))
        textHor = self.font.render('HOR', True, (0, 0, 0))
        textVer = self.font.render('VER', True, (0, 0, 0))
        textDiag = self.font.render('DIAG', True, (0, 0, 0))
        textHorL = self.font.render('HOR-L', True, (0, 0, 0))
        textHorXL = self.font.render('HOR-XL', True, (0, 0, 0))
        textZig = self.font.render('ZIG', True, (0, 0, 0))
        textZag = self.font.render('ZAG', True, (0, 0, 0))
        textAbove = self.font.render('ABOVE', True, (0, 0, 0))
        textBelow = self.font.render('BELOW', True, (0, 0, 0))
        textEye = self.font.render('EYE', True, (0, 0, 0))
        textJackpot = self.font.render('JACKPOT', True, (0, 0, 0))

        # hor mønsteret
        if len(str(config.patternValues['hor'])) >= 11:
            patternValue = round(config.patternValues['hor'] * 10**(-1 * (len(str(config.patternValues['hor'])) - 1)), 2)
            textHorMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['hor'])) - 1), True, (0, 0, 0))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 40))
            self.posters.blit(textHorMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 40))
        else:
            textHorMult = self.font.render('X ' + str(config.patternValues['hor']), True, (0, 0, 0))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['hor']))**(1.50 - 0.012 * len(str(config.patternValues['hor']))), patternPosterY + 40))
            self.posters.blit(textHorMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['hor']))**(1.50 - 0.012 * len(str(config.patternValues['hor']))), patternPosterY + 40))

        # vert mønsteret
        if len(str(config.patternValues['vert'])) >= 11:
            patternValue = round(config.patternValues['vert'] * 10**(-1 * (len(str(config.patternValues['vert'])) - 1)), 2)
            textVerMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['vert'])) - 1), True, (0, 0, 0))
            self.posters.blit(textVerMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 68.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 65))
        else:
            textVerMult = self.font.render('X ' + str(config.patternValues['vert']), True, (0, 0, 0))
            self.posters.blit(textVerMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['vert']))**(1.50 - 0.012 * len(str(config.patternValues['vert']))), patternPosterY + 68.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['vert']))**(1.50 - 0.012 * len(str(config.patternValues['vert']))), patternPosterY + 65))

        # diag mønsteret
        if len(str(config.patternValues['diag'])) >= 11:
            patternValue = round(config.patternValues['diag'] * 10**(-1 * (len(str(config.patternValues['diag'])) - 1)), 2)
            textDiagMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['diag'])) - 1), True, (0, 0, 0))
            if len(str(config.patternValues['diag'])) >= 11:
                self.posters.blit(textDiagMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 96))
                self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 92.5))
            if len(str(config.patternValues['diag'])) < 11:
                self.posters.blit(textDiagMult, (patternPosterX + 212, patternPosterY + 96))
                self.posters.blit(self.coin2, (patternPosterX + 192, patternPosterY + 92.5))
        else:
            textDiagMult = self.font.render('X ' + str(config.patternValues['diag']), True, (0, 0, 0))
            self.posters.blit(textDiagMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['diag']))**(1.50 - 0.012 * len(str(config.patternValues['diag']))), patternPosterY + 96))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['diag']))**(1.50 - 0.012 * len(str(config.patternValues['diag']))), patternPosterY + 92.5))

        # horL mønsteret
        if len(str(config.patternValues['horL'])) >= 10:
            patternValue = round(config.patternValues['horL'] * 10**(-1 * (len(str(config.patternValues['horL'])) - 1)), 2)
            textHorLMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['horL'])) - 1), True, (0, 0, 0))
            if len(str(config.patternValues['horL'])) >= 10:
                self.posters.blit(textHorLMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 123.5))
                self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 119.5))
            if len(str(config.patternValues['horL'])) < 10:
                self.posters.blit(textHorLMult, (patternPosterX + 212, patternPosterY + 123.5))
                self.posters.blit(self.coin2, (patternPosterX + 192, patternPosterY + 119.5))
        else:
            textHorLMult = self.font.render('X ' + str(config.patternValues['horL']), True, (0, 0, 0))
            self.posters.blit(textHorLMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['horL']))**(1.50 - 0.012 * len(str(config.patternValues['horL']))), patternPosterY + 123.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['horL']))**(1.50 - 0.012 * len(str(config.patternValues['horL']))), patternPosterY + 119.5))

        # horXL mønsteret
        if len(str(config.patternValues['horXL'])) >= 8:
            patternValue = round(config.patternValues['horXL'] * 10**(-1 * (len(str(config.patternValues['horXL'])) - 1)), 2)
            textHorXLMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['horXL'])) - 1), True, (0, 0, 0))
            if len(str(config.patternValues['horXL'])) >= 10:
                self.posters.blit(textHorXLMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 151.5))
                self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 148.5))
            if len(str(config.patternValues['horXL'])) < 10:
                self.posters.blit(textHorXLMult, (patternPosterX + 212, patternPosterY + 151.5))
                self.posters.blit(self.coin2, (patternPosterX + 192, patternPosterY + 148.5))
        else:
            textHorXLMult = self.font.render('X ' + str(config.patternValues['horXL']), True, (0, 0, 0))
            self.posters.blit(textHorXLMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['horXL']))**(1.50 - 0.012 * len(str(config.patternValues['horXL']))), patternPosterY + 151.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['horXL']))**(1.50 - 0.012 * len(str(config.patternValues['horXL']))), patternPosterY + 146.5))

        # zig mønsteret
        if len(str(config.patternValues['zig'])) >= 11:
            patternValue = round(config.patternValues['zig'] * 10**(-1 * (len(str(config.patternValues['zig'])) - 1)), 2)
            textZigMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['zig'])) - 1), True, (0, 0, 0))
            self.posters.blit(textZigMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 179.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 176.5))
        else:
            textZigMult = self.font.render('X ' + str(config.patternValues['zig']), True, (0, 0, 0))
            self.posters.blit(textZigMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['zig']))**(1.50 - 0.012 * len(str(config.patternValues['zig']))), patternPosterY + 179.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['zig']))**(1.50 - 0.012 * len(str(config.patternValues['zig']))), patternPosterY + 176.5))

        # zag mønsteret
        if len(str(config.patternValues['zag'])) >= 11:
            patternValue = round(config.patternValues['zag'] * 10**(-1 * (len(str(config.patternValues['zag'])) - 1)), 2)
            textZagMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['zag'])) - 1), True, (0, 0, 0))
            self.posters.blit(textZagMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 206.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 204.5))
        else:
            textZagMult = self.font.render('X ' + str(config.patternValues['zag']), True, (0, 0, 0))
            self.posters.blit(textZagMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['zag']))**(1.50 - 0.012 * len(str(config.patternValues['zag']))), patternPosterY + 206.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['zag']))**(1.50 - 0.012 * len(str(config.patternValues['zag']))), patternPosterY + 204.5))

        # above mønsteret
        if len(str(config.patternValues['above'])) >= 8:
            patternValue = round(config.patternValues['above'] * 10**(-1 * (len(str(config.patternValues['above'])) - 1)), 2)
            textAboveMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['above'])) - 1), True, (0, 0, 0))
            if len(str(config.patternValues['above'])) >= 10:
                self.posters.blit(textAboveMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 233.5))
                self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 230.5))
            if len(str(config.patternValues['above'])) < 10:
                self.posters.blit(textAboveMult, (patternPosterX + 212, patternPosterY + 233.5))
                self.posters.blit(self.coin2, (patternPosterX + 192, patternPosterY + 230.5))
        else:
            textAboveMult = self.font.render('X ' + str(config.patternValues['above']), True, (0, 0, 0))
            self.posters.blit(textAboveMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['above']))**(1.50 - 0.012 * len(str(config.patternValues['above']))), patternPosterY + 233.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['above']))**(1.50 - 0.012 * len(str(config.patternValues['above']))), patternPosterY + 230.5))

        # below mønsteret
        if len(str(config.patternValues['below'])) >= 8:
            patternValue = round(config.patternValues['below'] * 10**(-1 * (len(str(config.patternValues['below'])) - 1)), 2)
            textBelowMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['below'])) - 1), True, (0, 0, 0))
            if len(str(config.patternValues['below'])) >= 10:
                self.posters.blit(textBelowMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 260))
                self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 257.5))
            if len(str(config.patternValues['below'])) < 10:
                self.posters.blit(textBelowMult, (patternPosterX + 212, patternPosterY + 260))
                self.posters.blit(self.coin2, (patternPosterX + 192, patternPosterY + 257.5))
        else:
            textBelowMult = self.font.render('X ' + str(config.patternValues['below']), True, (0, 0, 0))
            self.posters.blit(textBelowMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['below']))**(1.50 - 0.012 * len(str(config.patternValues['below']))), patternPosterY + 260.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['below']))**(1.50 - 0.012 * len(str(config.patternValues['below']))), patternPosterY + 257.5))

        # eye mønsteret
        if len(str(config.patternValues['eye'])) >= 11:
            patternValue = round(config.patternValues['eye'] * 10**(-1 * (len(str(config.patternValues['eye'])) - 1)), 2)
            textEyeMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['eye'])) - 1), True, (0, 0, 0))
            self.posters.blit(textEyeMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 287.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 284.5))
        else:
            textEyeMult = self.font.render('X ' + str(config.patternValues['eye']), True, (0, 0, 0))
            self.posters.blit(textEyeMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['eye']))**(1.50 - 0.012 * len(str(config.patternValues['eye']))), patternPosterY + 287.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['eye']))**(1.50 - 0.012 * len(str(config.patternValues['eye']))), patternPosterY + 284.5))

        # jackpot mønsteret
        if len(str(config.patternValues['jackpot'])) >= 8:
            patternValue = round(config.patternValues['jackpot'] * 10**(-1 * (len(str(config.patternValues['jackpot'])) - 1)), 2)
            textJackpotMult = self.font.render('X ' + str(patternValue) + 'E+' + str(len(str(config.patternValues['jackpot'])) - 1), True, (0, 0, 0))
            if len(str(config.patternValues['jackpot'])) >= 10:
                self.posters.blit(textJackpotMult, (patternPosterX + 270 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * (len(str(patternValue)))), patternPosterY + 314.5))
                self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * (len(str(patternValue)) + 3)**(1.50 - 0.012 * len(str(patternValue))), patternPosterY + 310.5))
            if len(str(config.patternValues['jackpot'])) < 10:
                self.posters.blit(textJackpotMult, (patternPosterX + 212, patternPosterY + 314.5))
                self.posters.blit(self.coin2, (patternPosterX + 192, patternPosterY + 310.5))
        else:
            textJackpotMult = self.font.render('X ' + str(config.patternValues['jackpot']), True, (0, 0, 0))
            self.posters.blit(textJackpotMult, (patternPosterX + 270 - 5 * len(str(config.patternValues['jackpot']))**(1.50 - 0.012 * len(str(config.patternValues['jackpot']))), patternPosterY + 314.5))
            self.posters.blit(self.coin2, (patternPosterX + 250 - 5 * len(str(config.patternValues['jackpot']))**(1.50 - 0.012 * len(str(config.patternValues['jackpot']))), patternPosterY + 310.5))

        # text og mønstre på plakaten
        self.posters.blit(self.patternHor, (patternPosterX + 25, patternPosterY + 40))
        self.posters.blit(textHor, textHor.get_rect(center=(patternPosterX + 95, patternPosterY + 55)))

        self.posters.blit(self.patternVer, (patternPosterX + 25, patternPosterY + 66))
        self.posters.blit(textVer, textVer.get_rect(center=(patternPosterX + 93, patternPosterY + 81)))

        self.posters.blit(self.patternDiag, (patternPosterX + 25, patternPosterY + 93.5))
        self.posters.blit(textDiag, textDiag.get_rect(center=(patternPosterX + 98, patternPosterY + 108.5)))

        self.posters.blit(self.patternHorL, (patternPosterX + 25, patternPosterY + 120.5))
        self.posters.blit(textHorL, textHorL.get_rect(center=(patternPosterX + 105, patternPosterY + 136.5)))

        self.posters.blit(self.patternHorXL, (patternPosterX + 25, patternPosterY + 146.5))
        self.posters.blit(textHorXL, textHorXL.get_rect(center=(patternPosterX + 110, patternPosterY + 161.5)))

        self.posters.blit(self.patternZig, (patternPosterX + 25, patternPosterY + 173.5))
        self.posters.blit(textZig, textZig.get_rect(center=(patternPosterX + 90, patternPosterY + 188.5)))

        self.posters.blit(self.patternZag, (patternPosterX + 25, patternPosterY + 200.5))
        self.posters.blit(textZag, textZag.get_rect(center=(patternPosterX + 95, patternPosterY + 215.5)))

        self.posters.blit(self.patternAbove, (patternPosterX + 25, patternPosterY + 227.5))
        self.posters.blit(textAbove, textAbove.get_rect(center=(patternPosterX + 108, patternPosterY + 242.5)))

        self.posters.blit(self.patternBelow, (patternPosterX + 25, patternPosterY + 254.5))
        self.posters.blit(textBelow, textBelow.get_rect(center=(patternPosterX + 110, patternPosterY + 269.5)))

        self.posters.blit(self.patternEye, (patternPosterX + 25, patternPosterY + 281.5))
        self.posters.blit(textEye, textEye.get_rect(center=(patternPosterX + 92, patternPosterY + 296.5)))

        self.posters.blit(self.patternJackpot, (patternPosterX + 25, patternPosterY + 308.5))
        self.posters.blit(textJackpot, textJackpot.get_rect(center=(patternPosterX + 120, patternPosterY + 323.5)))

        self.posters.blit(textPatterns, textPatterns.get_rect(center=(self.posterBackground.get_width()/2+patternPosterX, patternPosterY + 30)))
        self.posters.blit(textPatternsMult, textPatternsMult.get_rect(center=(self.posterBackground.get_width()/2+patternPosterX, patternPosterY + 355)))
        self.posters.blit(PatternsMult, PatternsMult.get_rect(center=(patternPosterX + 240, patternPosterY + 380)))
        self.posters.blit(self.coin, (patternPosterX + 200, patternPosterY + 364.5))

