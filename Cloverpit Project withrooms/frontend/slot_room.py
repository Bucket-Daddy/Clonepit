#slot machine frontend script
import pygame
import random
import math
import config.game_config as game_config

from backend.spin_engine import GameState, spin


class SlotRoom:

    def __init__(self):

        #Definerer grafik variabler
        self.overallScale = 2
        self.symbolScale = 2 * self.overallScale
        self.symbolSpaceVer = 16 * self.overallScale
        self.spinSpeed = 20 * self.overallScale
        self.symbolSpaceHor = 100 * self.overallScale
        self.squareDist = 5 * self.overallScale
        self.frameRate = 60
        self.font = pygame.font.Font(None, size = 30 * self.overallScale)
        self.dividerLineWidth = 8 * self.overallScale

        #Skærmstørrelse - slot machine surface dækker hele skærmen
        self.screenW = 1200
        self.screenH = 750
        self.slotMachine = pygame.Surface((self.screenW, self.screenH), pygame.SRCALPHA)

        #X og Y offset så reelsene er centreret på skærmen
        #reelOriginX bruges til både at placere reels og til at tegne highlight kasser
        self.reelOriginX = (self.screenW - self.symbolSpaceHor * 5) // 2
        self.reelOriginY = (self.screenH - ((18 * self.symbolScale + self.symbolSpaceVer) * 3 + self.symbolSpaceVer)) // 2

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

        golden = pygame.image.load('assets/ModifierGolden.webp')
        token = pygame.image.load('assets/ModifierToken.webp')
        ticket = pygame.image.load('assets/ModifierTicket.webp')
        repetition = pygame.image.load('assets/ModifierRepetition.webp')
        battery = pygame.image.load('assets/ModifierBattery.webp')
        chain = pygame.image.load('assets/ModifierChain.webp')

        #Loader lydeffekter
        self.scoreSFX = pygame.mixer.Sound('assets/1-18. Slot Machine Scored.mp3')
        self.jackpotSFX = pygame.mixer.Sound('assets/1-17. Slot Machine Jackpot.mp3')
        self.rollingSFX = pygame.mixer.Sound('assets/2-228. Slotmachinerollingtick.mp3')

        #Skalerer billeder
        lemon = pygame.transform.scale(lemon, (18 * self.symbolScale, 18 * self.symbolScale))
        cherry = pygame.transform.scale(cherry, (18 * self.symbolScale, 18 * self.symbolScale))
        clover = pygame.transform.scale(clover, (18 * self.symbolScale, 18 * self.symbolScale))
        bell = pygame.transform.scale(bell, (18 * self.symbolScale, 18 * self.symbolScale))
        diamond = pygame.transform.scale(diamond, (18 * self.symbolScale, 18 * self.symbolScale))
        treasure = pygame.transform.scale(treasure, (18 * self.symbolScale, 18 * self.symbolScale))
        seven = pygame.transform.scale(seven, (18 * self.symbolScale, 18 * self.symbolScale))
        six = pygame.transform.scale(six, (18 * self.symbolScale, 18 * self.symbolScale))

        golden = pygame.transform.scale(golden, (9 * self.symbolScale, 9 * self.symbolScale))
        token = pygame.transform.scale(token, (9 * self.symbolScale, 9 * self.symbolScale))
        ticket = pygame.transform.scale(ticket, (9 * self.symbolScale, 9 * self.symbolScale))
        repetition = pygame.transform.scale(repetition, (9 * self.symbolScale, 9 * self.symbolScale))
        battery = pygame.transform.scale(battery, (9 * self.symbolScale, 9 * self.symbolScale))
        chain = pygame.transform.scale(chain, (9 * self.symbolScale, 9 * self.symbolScale))

        #Tuples og dictionaries til fortolkning af resultat
        self.symbolsTuple = (lemon, cherry, clover, bell, diamond, treasure, seven, six)
        self.modifiersTuple = (None, golden, token, ticket, repetition, battery, chain)
        self.patterns = {'hor1.1':(0, 1, 2), 'hor1.2':(1, 2, 3), 'hor1.3':(2, 3, 4), 'hor2.1':(5, 6, 7), 'hor2.2':(6, 7, 8), 'hor2.3':(7, 8, 9),
                    'hor3.1':(10, 11, 12), 'hor3.2':(11, 12, 13), 'hor3.3':(12, 13, 14), 'vert1':(0, 5, 10), 'vert2':(1, 6, 11), 'vert3':(2, 7, 12),
                    'vert4':(3, 8, 13), 'vert5':(4, 9, 14), 'bckDiag1':(0, 6, 12), 'bckDiag2':(1, 7, 13), 'bckDiag3':(2, 8, 14),
                    'fwdDiag1':(2, 6, 10), 'fwdDiag2':(3, 7, 11), 'fwdDiag3':(4, 8, 12), 'horL1.1':(0, 1, 2, 3), 'horL1.2':(1, 2, 3, 4),
                    'horL2.1':(5, 6, 7, 8), 'horL2.2':(6, 7, 8, 9), 'horL3.1':(10, 11, 12, 13), 'horL3.2':(11, 12, 13, 14),
                    'horXL1':(0, 1, 2, 3, 4), 'horXL2':(5, 6, 7, 8, 9), 'horXL3':(10, 11, 12, 13, 14), 'zig':(2, 6, 8, 10, 14),
                    'zag':(0, 4, 6, 8, 12), 'above':(2, 6, 8, 10, 11, 12, 13, 14), 'below':(0, 1, 2, 3, 4, 6, 8, 12),
                    'eye':(1, 2, 3, 5, 6, 8, 9, 11, 12, 13), 'jackpot':(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)}

        #Opretter game state - ingen spin endnu, venter på space
        self.gameState = GameState()
        self.spinning = False
        self.hasSpun = False
        self.reels = []
        self.res = []
        self.modifiers = []
        self.result = []
        self.is666 = False
        self.reelsY = [-(18 * self.symbolScale + self.symbolSpaceVer) * 30] * 5
        self.patternTimer = 0
        self.patternDuration = 1

    def _build_reels(self):
        #Danner reels ud fra det nuværende resultat
        self.reels = []
        for i in range(5):
            reel = pygame.Surface((18 * self.symbolScale, (18 * self.symbolScale + self.symbolSpaceVer) * 30), pygame.SRCALPHA)

            if self.is666:
                reel.blit(random.choice(self.symbolsTuple), (0, 0))
                if i < 4 and i > 0:
                    reel.blit(self.six, (0, 18 * self.symbolScale + self.symbolSpaceVer))
                else:
                    reel.blit(random.choice(self.symbolsTuple), (0, 18 * self.symbolScale + self.symbolSpaceVer))
                reel.blit(random.choice(self.symbolsTuple), (0, 36 * self.symbolScale + 2 * self.symbolSpaceVer))
            else:
                for slot in range(3):
                    reel.blit(self.symbolsTuple[self.res[slot * 5 + i]], (0, slot * (18 * self.symbolScale + self.symbolSpaceVer)))
                    if self.modifiers[slot * 5 + i] > 0:
                        reel.blit(self.modifiersTuple[self.modifiers[slot * 5 + i]], (self.symbolScale * 9, slot * (18 * self.symbolScale + self.symbolSpaceVer) + 9 * self.symbolScale))

            for slot in range(27):
                reel.blit(random.choice(self.symbolsTuple), (0, (18 * self.symbolScale + self.symbolSpaceVer) * 3 + slot * (18 * self.symbolScale + self.symbolSpaceVer)))

            self.reels.append(reel)

    def on_space(self):
        #Spinner kun hvis reelsene er landet (ikke midt i en animation)
        if self.spinning:
            return

        #Henter nyt resultat fra spin engine
        self.res, self.modifiers, self.result = spin(self.gameState)
        self.is666 = game_config.is666

        #Nulstiller reel animation og pattern timer
        self.reelsY = [-(18 * self.symbolScale + self.symbolSpaceVer) * 30] * 5
        self.patternTimer = 0
        self.spinning = True
        self.hasSpun = True

        #Bygger reels og spiller rullende lyd
        self._build_reels()
        self.rollingSFX.play()

    def draw(self, screen):
        self.slotMachine.fill((0, 0, 0))

        #Viser ingenting før første spin
        if not self.hasSpun:
            screen.blit(self.slotMachine, (0, 0))
            return

        #Flytter reels ned langs skærmen
        allLanded = True
        for reel in range(5):
            if self.reelsY[reel] < self.reelOriginY + self.symbolSpaceVer:
                self.reelsY[reel] += self.spinSpeed - reel * self.spinSpeed / 10
                allLanded = False
            else:
                self.reelsY[reel] = self.reelOriginY + self.symbolSpaceVer

        #Når alle reels lander sættes spinning til False så man kan spinne igen
        if allLanded:
            self.spinning = False

        #Loader reels til slot machine surface - centreret horisontalt og vertikalt
        for reel in range(5):
            self.slotMachine.blit(self.reels[reel], (self.reelOriginX + reel * self.symbolSpaceHor, self.reelsY[reel]))

        #Tegner linjer mellem reels
        for i in range(4):
            pygame.draw.rect(self.slotMachine, (120, 95, 26), pygame.Rect(self.reelOriginX + (i + 1) * self.symbolSpaceHor - self.symbolScale * 9 - 0.5 * self.dividerLineWidth, self.reelOriginY, self.dividerLineWidth, (18 * self.symbolScale + self.symbolSpaceVer) * 3 + self.symbolSpaceVer))

        #Når reelsene har nået bunden af skærmen vises hvert pattern i {patternDuration} sekunder
        if self.reelsY.count(self.reelOriginY + self.symbolSpaceVer) == 5 and self.patternTimer < len(self.result) * self.frameRate * 1.25 * self.patternDuration and not self.is666:

            #Spiller lydeffekten for hvert pattern
            if self.patternTimer == self.frameRate * 1.25 * self.patternDuration * math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration)):
                if self.result[math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))][0] == 'jackpot':
                    self.jackpotSFX.play()
                else:
                    self.scoreSFX.play()

            #Tegner kasser om hvert symbol i et givent pattern
            #X bruger reelOriginX som base så kasserne sidder præcis over symbolerne
            if self.patternTimer <= self.frameRate * self.patternDuration * math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration) + 1) + self.frameRate * self.patternDuration * 0.25 * math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration)):
                for slot in self.patterns[self.result[math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))][0]]:
                    boxX = self.reelOriginX + slot % 5 * self.symbolSpaceHor - self.squareDist
                    boxY = self.reelOriginY + self.symbolSpaceVer - self.squareDist + math.floor(slot / 5) * (18 * self.symbolScale + self.symbolSpaceVer)
                    pygame.draw.rect(self.slotMachine, (36, 252, 3), pygame.Rect(boxX, boxY, 18 * self.symbolScale + 2 * self.squareDist, 18 * self.symbolScale + 2 * self.squareDist), 2, 3)

                #Viser værdien af et givent pattern
                if len(str(self.result[math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))][1])) > 7:
                    patternPayout = round(self.result[math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))][1] * 10**(-1 * (len(str(self.result[math.floor(self.patternTimer / (self.frameRate * self.patternDuration))][1])) - 1)), 5)
                    text = self.font.render('+' + str(patternPayout) + 'E+' + str(len(str(self.result[math.floor(self.patternTimer / (self.frameRate * self.patternDuration))][1])) - 1), True, (250, 10, 10))
                else:
                    text = self.font.render('+' + str(self.result[math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))][1]), True, (246, 250, 10))

                self.slotMachine.blit(text, text.get_rect(center=(self.screenW / 2, self.screenH / 2)))

            self.patternTimer += 1

        screen.blit(self.slotMachine, (0, 0))
