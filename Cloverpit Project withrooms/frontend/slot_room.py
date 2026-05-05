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
        self.symbolsTuple2 = (lemon, cherry, clover, bell, diamond, treasure, seven)
        self.modifiersTuple = (None, golden, token, ticket, repetition, battery, chain)

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
        self.lastPaidPattern = -1

        #Forsinkelse efter sidste spin før køb-skærmen vises (i frames)
        self.roundEndDelay = 0
        self.roundEndDelayFrames = 90  # 1.5 sekunder ved 60fps

        #Coin ikon til køb-skærmen
        self.coinImg = pygame.transform.scale(pygame.image.load('assets/Coin.webp'), (36, 36))

        #Knap rektangler for buyschreen beregnes en gang her
        self.btn3Rect = pygame.Rect(self.screenW // 2 - 300, self.screenH // 2 + 50, 280, 100)
        self.btn7Rect = pygame.Rect(self.screenW // 2 + 20, self.screenH // 2 + 50, 280, 100)

    def _build_reels(self):
        #Danner reels ud fra det nuværende resultat
        self.reels = []
        for i in range(5):
            reel = pygame.Surface((18 * self.symbolScale, (18 * self.symbolScale + self.symbolSpaceVer) * 30), pygame.SRCALPHA)

            if self.is666:
                reel.blit(random.choice(self.symbolsTuple), (0, 0))
                if i < 4 and i > 0:
                    reel.blit(self.symbolsTuple[7], (0, 18 * self.symbolScale + self.symbolSpaceVer))
                else:
                    reel.blit(random.choice(self.symbolsTuple2), (0, 18 * self.symbolScale + self.symbolSpaceVer))
                reel.blit(random.choice(self.symbolsTuple2), (0, 36 * self.symbolScale + 2 * self.symbolSpaceVer))
            else:
                for slot in range(3):
                    reel.blit(self.symbolsTuple[self.res[slot * 5 + i]], (0, slot * (18 * self.symbolScale + self.symbolSpaceVer)))
                    if self.modifiers[slot * 5 + i] > 0:
                        reel.blit(self.modifiersTuple[self.modifiers[slot * 5 + i]], (self.symbolScale * 9, slot * (18 * self.symbolScale + self.symbolSpaceVer) + 9 * self.symbolScale))

            for slot in range(27):
                reel.blit(random.choice(self.symbolsTuple2), (0, (18 * self.symbolScale + self.symbolSpaceVer) * 3 + slot * (18 * self.symbolScale + self.symbolSpaceVer)))

            self.reels.append(reel)

    def on_space(self):
        #Spinner kun hvis reelsene er landet, pattern animationen er færdig, og der er spins tilbage
        patternsDone = self.patternTimer >= len(self.result) * self.frameRate * 1.25 * self.patternDuration
        if self.spinning or not patternsDone or game_config.spinsLeft <= 0:
            return

        #Henter nyt resultat fra spin engine
        self.res, self.modifiers, self.result = spin(self.gameState)
        self.is666 = game_config.is666

        #Trækker et spin fra
        game_config.spinsLeft -= 1

        #Nulstiller reel animation, pattern timer og runde-slut forsinkelse
        self.reelsY = [-(18 * self.symbolScale + self.symbolSpaceVer) * 30] * 5
        self.patternTimer = 0
        self.lastPaidPattern = -1
        self.roundEndDelay = 0
        self.spinning = True
        self.hasSpun = True

        #Bygger reels og spiller rullende lyd
        self._build_reels()
        self.rollingSFX.play()

    def on_click(self, mousePos):
        #Håndterer klik på køb knapper når buyschreen vises
        if game_config.spinsLeft > 0:
            return
        if self.btn3Rect.collidepoint(mousePos) and game_config.coins >= 3:
            game_config.coins -= 3
            game_config.spinsLeft += 3 + game_config.bonusSpins
            game_config.tickets += 2
            self.roundEndDelay = 0
        elif self.btn7Rect.collidepoint(mousePos) and game_config.coins >= 7:
            game_config.coins -= 7
            game_config.spinsLeft += 7 + game_config.bonusSpins
            game_config.tickets += 1
            self.roundEndDelay = 0

    def _draw_buy_screen(self):
        #Tegner buyschreen når spilleren ikke har flere spins (sort baggrund)
        self.slotMachine.fill((0, 0, 0))

        #Rundenummer øverst i midten
        buyFont = pygame.font.Font(None, size = 40)
        roundText = buyFont.render('ROUND ' + str(game_config.roundNum), True, (246, 250, 10))
        self.slotMachine.blit(roundText, roundText.get_rect(center=(self.screenW // 2, 80)))

        mousePos = pygame.mouse.get_pos()
        canAfford3 = game_config.coins >= 3
        canAfford7 = game_config.coins >= 7

        #Knap 3 spins
        btn3BgColor = (40, 40, 40) if canAfford3 else (20, 20, 20)
        btn3BorderColor = (120, 95, 26) if canAfford3 else (60, 50, 20)
        btn3TextColor = (246, 250, 10) if canAfford3 else (100, 100, 100)
        btn3SubColor = (200, 200, 200) if canAfford3 else (80, 80, 80)
        pygame.draw.rect(self.slotMachine, btn3BgColor, self.btn3Rect, border_radius=8)
        pygame.draw.rect(self.slotMachine, btn3BorderColor, self.btn3Rect, 3, border_radius=8)
        if self.btn3Rect.collidepoint(mousePos) and canAfford3:
            pygame.draw.rect(self.slotMachine, (246, 250, 10), self.btn3Rect, 3, border_radius=8)
        btn3Label = buyFont.render('3 SPINS', True, btn3TextColor)
        btn3Cost = pygame.font.Font(None, size=30).render('3 coins  +2 tickets', True, btn3SubColor)
        self.slotMachine.blit(btn3Label, btn3Label.get_rect(center=self.btn3Rect.center + pygame.math.Vector2(0, -18)))
        self.slotMachine.blit(btn3Cost, btn3Cost.get_rect(center=self.btn3Rect.center + pygame.math.Vector2(0, 18)))

        #Knap 7 spins
        btn7BgColor = (40, 40, 40) if canAfford7 else (20, 20, 20)
        btn7BorderColor = (120, 95, 26) if canAfford7 else (60, 50, 20)
        btn7TextColor = (246, 250, 10) if canAfford7 else (100, 100, 100)
        btn7SubColor = (200, 200, 200) if canAfford7 else (80, 80, 80)
        pygame.draw.rect(self.slotMachine, btn7BgColor, self.btn7Rect, border_radius=8)
        pygame.draw.rect(self.slotMachine, btn7BorderColor, self.btn7Rect, 3, border_radius=8)
        if self.btn7Rect.collidepoint(mousePos) and canAfford7:
            pygame.draw.rect(self.slotMachine, (246, 250, 10), self.btn7Rect, 3, border_radius=8)
        btn7Label = buyFont.render('7 SPINS', True, btn7TextColor)
        btn7Cost = pygame.font.Font(None, size=30).render('7 coins  +1 ticket', True, btn7SubColor)
        self.slotMachine.blit(btn7Label, btn7Label.get_rect(center=self.btn7Rect.center + pygame.math.Vector2(0, -18)))
        self.slotMachine.blit(btn7Cost, btn7Cost.get_rect(center=self.btn7Rect.center + pygame.math.Vector2(0, 18)))

    def draw(self, screen):
        self.slotMachine.fill((0, 0, 0))

        #Buyschreen vises kun når spins er 0, animation er færdig, og forsinkelsen er talt ned
        patternsDone = self.patternTimer >= len(self.result) * self.frameRate * 1.25 * self.patternDuration
        roundOver = game_config.spinsLeft <= 0 and not self.spinning and patternsDone

        if roundOver:
            if self.roundEndDelay < self.roundEndDelayFrames:
                #Tæller forsinkelsen op viser stadig reelsene i mellemtiden
                self.roundEndDelay += 1
            else:
                self._draw_buy_screen()
                screen.blit(self.slotMachine, (0, 0))
                return

        #Viser tomt felt hvis der ikke er spinnet endnu i denne runde
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

        #Loader reels til slot machine surface centreret horisontalt og vertikalt
        for reel in range(5):
            self.slotMachine.blit(self.reels[reel], (self.reelOriginX + reel * self.symbolSpaceHor, self.reelsY[reel]))

        #Tegner linjer mellem reels
        for i in range(4):
            pygame.draw.rect(self.slotMachine, (120, 95, 26), pygame.Rect(self.reelOriginX + (i + 1) * self.symbolSpaceHor - self.symbolScale * 9 - 0.5 * self.dividerLineWidth, self.reelOriginY, self.dividerLineWidth, (18 * self.symbolScale + self.symbolSpaceVer) * 3 + self.symbolSpaceVer))

        #Når reelsene har nået bunden af skærmen vises hvert pattern i {patternDuration} sekunder
        if self.reelsY.count(self.reelOriginY + self.symbolSpaceVer) == 5 and self.patternTimer < len(self.result) * self.frameRate * 1.25 * self.patternDuration and not self.is666:

            #Spiller lydeffekten for hvert pattern
            if self.patternTimer == self.frameRate * 1.25 * self.patternDuration * math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration)):
                currentPatternIdx = math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))
                if self.result[currentPatternIdx][0] == 'jackpot':
                    self.jackpotSFX.play()
                else:
                    self.scoreSFX.play()
                #Giver coins for pattern når animationen starter
                if currentPatternIdx != self.lastPaidPattern:
                    game_config.coins += self.result[currentPatternIdx][1]
                    self.lastPaidPattern = currentPatternIdx

            #Tegner kasser om hvert symbol i et givent pattern
            #X bruger reelOriginX som base så kasserne sidder præcis over symbolerne
            if self.patternTimer <= self.frameRate * self.patternDuration * math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration) + 1) + self.frameRate * self.patternDuration * 0.25 * math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration)):
                for slot in game_config.patterns[self.result[math.floor(self.patternTimer / (self.frameRate * 1.25 * self.patternDuration))][0]]:
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
