#Posters script
import pygame
import config.game_config as config

class PostersRoom:

    def __init__(self, resolution, xScaling, yScaling):

        posterScale = 0.80
        self.symbolScale = 1
        overallScale = 2
        self.font = pygame.font.Font(None, size = round(15 * overallScale * xScaling))
    
        #Loader billeder
        self.lemon = pygame.image.load('assets/SymbolLemon.webp')
        self.lemon = pygame.transform.scale(self.lemon, (round(36 * self.symbolScale * xScaling), round(36 * self.symbolScale * yScaling)))
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
        self.cherry = pygame.transform.scale(self.cherry, (36 * self.symbolScale * xScaling, 36 * self.symbolScale * yScaling))
        self.clover = pygame.transform.scale(self.clover, (36 * self.symbolScale * xScaling, 36 * self.symbolScale * yScaling))
        self.bell = pygame.transform.scale(self.bell, (36 * self.symbolScale * xScaling, 36 * self.symbolScale * yScaling))
        self.diamond = pygame.transform.scale(self.diamond, (36 * self.symbolScale * xScaling, 36 * self.symbolScale * yScaling))
        self.treasure = pygame.transform.scale(self.treasure, (36 * self.symbolScale * xScaling, 36 * self.symbolScale * yScaling))
        self.seven = pygame.transform.scale(self.seven, (36 * self.symbolScale * xScaling, 36 * self.symbolScale * yScaling))
        self.patternHor = pygame.transform.scale(self.patternHor, (self.patternHor.get_width() * 2/7 * xScaling, self.patternHor.get_height() * 2/7 * yScaling))
        self.patternVer = pygame.transform.scale(self.patternVer, (self.patternVer.get_width() * 2/7 * xScaling, self.patternVer.get_height() * 2/7 * yScaling))
        self.patternDiag = pygame.transform.scale(self.patternDiag, (self.patternDiag.get_width() * 2/7 * xScaling, self.patternDiag.get_height() * 2/7 * yScaling))
        self.patternHorL = pygame.transform.scale(self.patternHorL, (self.patternHorL.get_width() * 2/7 * xScaling, self.patternHorL.get_height() * 2/7 * yScaling))
        self.patternHorXL = pygame.transform.scale(self.patternHorXL, (self.patternHorXL.get_width() * 2/7 * xScaling, self.patternHorXL.get_height() * 2/7 * yScaling))
        self.patternZag = pygame.transform.scale(self.patternZag, (self.patternZag.get_width() * 2/7 * xScaling, self.patternZag.get_height() * 2/7 * yScaling))
        self.patternZig = pygame.transform.scale(self.patternZig, (self.patternZig.get_width() * 2/7 * xScaling, self.patternZig.get_height() * 2/7 * yScaling))
        self.patternAbove = pygame.transform.scale(self.patternAbove, (self.patternAbove.get_width() * 2/7 * xScaling, self.patternAbove.get_height() * 2/7 * yScaling))
        self.patternBelow = pygame.transform.scale(self.patternBelow, (self.patternBelow.get_width() * 2/7 * xScaling, self.patternBelow.get_height() * 2/7 * yScaling))
        self.patternEye = pygame.transform.scale(self.patternEye, (self.patternEye.get_width() * 2/7 * xScaling, self.patternEye.get_height() * 2/7 * yScaling))
        self.patternJackpot = pygame.transform.scale(self.patternJackpot, (self.patternJackpot.get_width() * 2/7 * xScaling, self.patternJackpot.get_height() * 2/7 * yScaling))
        self.coin = pygame.transform.scale(self.coin, (self.coin.get_width() * 0.15 * xScaling, self.coin.get_height() * 0.15 * yScaling))
        self.coin2 = pygame.transform.scale(self.coin2, (self.coin2.get_width() * 0.12 * xScaling, self.coin2.get_height() * 0.12 * yScaling))
        self.dice = pygame.transform.scale(self.dice, (self.dice.get_width() * 0.05 * xScaling, self.dice.get_height() * 0.05 * yScaling)).convert()
        self.dice.set_colorkey((255, 0, 214))
        self.posterBackground = pygame.transform.scale(self.posterBackground,
            (round(self.posterBackground.get_width() * 0.80 * xScaling),
             round(self.posterBackground.get_height() * 0.80 * yScaling)))
        self.posterBackground.set_colorkey((0, 0, 0))

        # danner baggrunden
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, resolution)
        self.posters = pygame.Surface(resolution, pygame.SRCALPHA)
        self.posters.blit(background, (-3, -3))

    def draw(self, screen, resolution, xScaling, yScaling):
        screen.blit(self.posters, (0, 0))

        sx, sy = xScaling, yScaling

        ##############################################################################################################
        # Symbol-plakat
        symbolPosterX = round(30  * sx)
        symbolPosterY = round(45  * sy)
        self.posters.blit(self.posterBackground, (symbolPosterX, symbolPosterY - round(15 * sy)))

        # texten på plakaten defineres
        textSymbols = self.font.render('---     SYMBOLS     ---', True, (0, 0, 0))
        textSymbolsMult = self.font.render('  SYMBOLS     MULTIPLIER ', True, (0, 0, 0))
        SymbolsMult = self.font.render(' X ' + str(config.symbolMult), True, (0, 0, 0))

        # værdien for hver symbol, hvis værdien er >= 7 cifre, vil den blive vist i videnskabelig notation
        # Lemon placering af værdi
        if len(str(config.symbolValues[0])) >= 7:
            symbolValue = round(config.symbolValues[0] * 10**(-1 * (len(str(config.symbolValues[0])) - 1)), 2)
            textLemonValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[0])) - 1), True, (0, 0, 0))
        else:
            textLemonValue = self.font.render(': ' + str(config.symbolValues[0]), True, (0, 0, 0))

        if len(str(config.symbolValues[1])) >= 7:
            symbolValue = round(config.symbolValues[1] * 10**(-1 * (len(str(config.symbolValues[1])) - 1)), 2)
            textCherryValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[1])) - 1), True, (0, 0, 0))
        else:
            textCherryValue = self.font.render(': ' + str(config.symbolValues[1]), True, (0, 0, 0))

        if len(str(config.symbolValues[2])) >= 7:
            symbolValue = round(config.symbolValues[2] * 10**(-1 * (len(str(config.symbolValues[2])) - 1)), 2)
            textCloverValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[2])) - 1), True, (0, 0, 0))
        else:
            textCloverValue = self.font.render(': ' + str(config.symbolValues[2]), True, (0, 0, 0))

        if len(str(config.symbolValues[3])) >= 7:
            symbolValue = round(config.symbolValues[3] * 10**(-1 * (len(str(config.symbolValues[3])) - 1)), 2)
            textBellValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[3])) - 1), True, (0, 0, 0))
        else:
            textBellValue = self.font.render(': ' + str(config.symbolValues[3]), True, (0, 0, 0))

        if len(str(config.symbolValues[4])) >= 7:
            symbolValue = round(config.symbolValues[4] * 10**(-1 * (len(str(config.symbolValues[4])) - 1)), 2)
            textDiamondValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[4])) - 1), True, (0, 0, 0))
        else:
            textDiamondValue = self.font.render(': ' + str(config.symbolValues[4]), True, (0, 0, 0))

        if len(str(config.symbolValues[5])) >= 7:
            symbolValue = round(config.symbolValues[5] * 10**(-1 * (len(str(config.symbolValues[5])) - 1)), 2)
            textTreasureValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[5])) - 1), True, (0, 0, 0))
        else:
            textTreasureValue = self.font.render(': ' + str(config.symbolValues[5]), True, (0, 0, 0))

        if len(str(config.symbolValues[6])) >= 7:
            symbolValue = round(config.symbolValues[6] * 10**(-1 * (len(str(config.symbolValues[6])) - 1)), 2)
            textSevenValue = self.font.render(': ' + str(symbolValue) + 'E+' + str(len(str(config.symbolValues[6])) - 1), True, (0, 0, 0))
        else:
            textSevenValue = self.font.render(': ' + str(config.symbolValues[6]), True, (0, 0, 0))

        textLemonChance   = self.font.render(': ' + str(round(config.symbolWeights[0]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textCherryChance  = self.font.render(': ' + str(round(config.symbolWeights[1]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textCloverChance  = self.font.render(': ' + str(round(config.symbolWeights[2]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textBellChance    = self.font.render(': ' + str(round(config.symbolWeights[3]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textDiamondChance = self.font.render(': ' + str(round(config.symbolWeights[4]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textTreasureChance= self.font.render(': ' + str(round(config.symbolWeights[5]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))
        textSevenChance   = self.font.render(': ' + str(round(config.symbolWeights[6]/sum(config.symbolWeights)*100, 1)) + '%', True, (0, 0, 0))

        # Rækker er 40px fra hinanden på 1200×750; skaleres med sy
        row = [round((symbolPosterY + 40 + i * 40) * sy / sy) for i in range(7)]
        # (symbolPosterY er allerede skaleret, brug blot offset * sy)
        rows = [symbolPosterY + round(40 * sy) + i * round(40 * sy) for i in range(7)]

        self.posters.blit(textSymbols,      textSymbols.get_rect(center=(self.posterBackground.get_width() // 2 + symbolPosterX, symbolPosterY + round(30 * sy))))
        self.posters.blit(textSymbolsMult,  textSymbolsMult.get_rect(center=(self.posterBackground.get_width() // 2 + symbolPosterX, symbolPosterY + round(340 * sy))))
        self.posters.blit(self.coin,        (symbolPosterX + round(200 * sx), symbolPosterY + round(355 * sy)))
        self.posters.blit(SymbolsMult,      SymbolsMult.get_rect(center=(symbolPosterX + round(240 * sx), symbolPosterY + round(365 * sy))))

        valueX  = symbolPosterX + round(100 * sx)
        chanceX = symbolPosterX + round(220 * sx)
        iconX   = symbolPosterX + round(25  * sx)
        coinX   = symbolPosterX + round(75  * sx)
        diceX   = symbolPosterX + round(190 * sx)

        symbolTexts  = [textLemonValue,   textCherryValue,  textCloverValue,  textBellValue,  textDiamondValue,  textTreasureValue,  textSevenValue]
        chanceTexts  = [textLemonChance,  textCherryChance, textCloverChance, textBellChance, textDiamondChance, textTreasureChance, textSevenChance]
        iconImgs     = [None, self.cherry, self.clover, self.bell, self.diamond, self.treasure, self.seven]

        for i, r in enumerate(rows):
            self.posters.blit(symbolTexts[i],  (valueX,  r))
            self.posters.blit(chanceTexts[i],  (chanceX, r))
            self.posters.blit(self.coin,        (coinX,   r + round(2 * sy)))
            self.posters.blit(self.dice,        (diceX,   r + round(3 * sy)))

        # Lemon har ikke scaled sprite i listen blit separat
        self.posters.blit(self.lemon,  (iconX, rows[0]))
        for i in range(1, 7):
            self.posters.blit(iconImgs[i], (iconX, rows[i]))

        self.posters.blit(self.coin, (symbolPosterX + round(200 * sx), symbolPosterY + round(355 * sy)))

        ##############################################################################################################
        # Plakaten med værdierne for mønstrene
        patternPosterX = symbolPosterX + round(self.posterBackground.get_width() * sx + 30 * sx)
        patternPosterY = symbolPosterY
        self.posters.blit(self.posterBackground, (patternPosterX, patternPosterY - round(15 * sy)))

        # Tekst-labels
        textPatterns    = self.font.render('---     PATTERNS     ---', True, (0, 0, 0))
        textPatternsMult= self.font.render('  PATTERN     MULTIPLIER ', True, (0, 0, 0))
        PatternsMult    = self.font.render(' X ' + str(config.patternMult), True, (0, 0, 0))
        textHor     = self.font.render('HOR',     True, (0, 0, 0))
        textVer     = self.font.render('VER',     True, (0, 0, 0))
        textDiag    = self.font.render('DIAG',    True, (0, 0, 0))
        textHorL    = self.font.render('HOR-L',   True, (0, 0, 0))
        textHorXL   = self.font.render('HOR-XL',  True, (0, 0, 0))
        textZig     = self.font.render('ZIG',     True, (0, 0, 0))
        textZag     = self.font.render('ZAG',     True, (0, 0, 0))
        textAbove   = self.font.render('ABOVE',   True, (0, 0, 0))
        textBelow   = self.font.render('BELOW',   True, (0, 0, 0))
        textEye     = self.font.render('EYE',     True, (0, 0, 0))
        textJackpot = self.font.render('JACKPOT', True, (0, 0, 0))

        # Hjælpefunktion til at rendere en pattern-linje
        def blitPatternRow(patternKey, rowImg, rowLabel, rowY, labelOffX=105):
            val = config.patternValues[patternKey]
            valStr = str(val)
            if len(valStr) >= 8:
                v = round(val * 10 ** (-(len(valStr) - 1)), 2)
                multText = self.font.render('X ' + str(v) + 'E+' + str(len(valStr) - 1), True, (0, 0, 0))
            else:
                multText = self.font.render('X ' + valStr, True, (0, 0, 0))
            coinOffX = round(250 * sx) - round(5 * len(str(val)) ** (1.50 - 0.012 * len(str(val))) * sx)
            self.posters.blit(rowImg,   (patternPosterX + round(25 * sx), rowY))
            self.posters.blit(rowLabel, rowLabel.get_rect(center=(patternPosterX + round(labelOffX * sx), rowY + round(15 * sy))))
            self.posters.blit(self.coin2, (patternPosterX + coinOffX, rowY - round(3 * sy)))
            self.posters.blit(multText,   (patternPosterX + coinOffX + round(20 * sx), rowY))

        # Rækker 27px mellemrum på 750px høj, skaleret med sy
        step = round(27 * sy)
        pr = [patternPosterY + round(40 * sy) + i * step for i in range(11)]

        blitPatternRow('hor',     self.patternHor,     textHor,     pr[0])
        blitPatternRow('vert',    self.patternVer,     textVer,     pr[1])
        blitPatternRow('diag',    self.patternDiag,    textDiag,    pr[2])
        blitPatternRow('horL',    self.patternHorL,    textHorL,    pr[3])
        blitPatternRow('horXL',   self.patternHorXL,   textHorXL,   pr[4])
        blitPatternRow('zig',     self.patternZig,     textZig,     pr[5])
        blitPatternRow('zag',     self.patternZag,     textZag,     pr[6])
        blitPatternRow('above',   self.patternAbove,   textAbove,   pr[7])
        blitPatternRow('below',   self.patternBelow,   textBelow,   pr[8])
        blitPatternRow('eye',     self.patternEye,     textEye,     pr[9])
        blitPatternRow('jackpot', self.patternJackpot, textJackpot, pr[10], labelOffX=130)

        self.posters.blit(textPatterns,     textPatterns.get_rect(center=(self.posterBackground.get_width() // 2 + patternPosterX, patternPosterY + round(30 * sy))))
        self.posters.blit(textPatternsMult, textPatternsMult.get_rect(center=(self.posterBackground.get_width() // 2 + patternPosterX, patternPosterY + round(355 * sy))))
        self.posters.blit(PatternsMult,     PatternsMult.get_rect(center=(patternPosterX + round(240 * sx), patternPosterY + round(380 * sy))))
        self.posters.blit(self.coin,        (patternPosterX + round(200 * sx), patternPosterY + round(364 * sy)))




