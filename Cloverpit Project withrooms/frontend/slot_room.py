#slot machine frontend script
import pygame
import random
import math
import config.game_config as config
from backend.spin_engine import GameState, spin
from frontend.mouseCheck import isSelected
from backend.shelf_backend import buttonTrigger, lastSpinTrigger, roundEndTrigger


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

        #temp skærmstørrelse slot machine surface dækker hele skærmen
        self.screenW = 1200
        self.screenH = 750
        self.slotMachine = pygame.Surface((self.screenW, self.screenH))

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

        self.machine = pygame.image.load('assets/SlotMachine.png')
        self.button = pygame.image.load('assets/Button.png')
        self.crancker = pygame.image.load('assets/Handle.png')

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

        self.Button = pygame.transform.scale(self.button, (self.button.get_width(), self.button.get_height()))
        self.Crancker = pygame.transform.scale(self.crancker, (self.crancker.get_width() * 0.5, self.crancker.get_height() * 0.5))
        self.machineX = self.slotMachine.get_width() // 2.6 - self.machine.get_width() // 2
        self.machineY = self.slotMachine.get_height() // 2 - self.machine.get_height() // 7.2
        self.buttonX = self.slotMachine.get_width() // 1.17 - self.Button.get_width() // 2
        self.buttonY = self.slotMachine.get_height() // 1.17 - self.Button.get_height() // 2
        
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
        self.roundEndDelayFrames = 30  # 0.5 sekunder ved 60fps

        #Coin ikon til køb-skærmen
        self.coinImg = pygame.transform.scale(pygame.image.load('assets/Coin.webp'), (36, 36))

        #Knap rektangler for buyschreen beregnes en gang her
        self.btn3Rect = pygame.Rect(self.screenW // 2 - 300, self.screenH // 2 + 50, 280, 100)
        self.btn7Rect = pygame.Rect(self.screenW // 2 + 20, self.screenH // 2 + 50, 280, 100)

        # Per-pattern frame offsets beregnes i _build_pattern_offsets() ved hvert nyt spin.
        # patternFrameOffsets[i] = total frames brugt op til (ikke inklusiv) pattern i.
        self.patternFrameOffsets = [0]

        #Fonts caches en gang dosnt do pygame.font.Font inde i draw()
        self.buyFont      = pygame.font.Font(None, size=40)
        self.subFont      = pygame.font.Font(None, size=30)
        self.msgFont      = pygame.font.Font(None, size=50)
        self.loseFont     = pygame.font.Font(None, size=80)
        self.loseSubFont  = pygame.font.Font(None, size=36)
        self.spinCountFont = pygame.font.Font(None, size=50)

        #Divider rektangler beregnes en gang ændres ikke under kørsel
        self.dividerRects = [
            pygame.Rect(
                self.reelOriginX + (i + 1) * self.symbolSpaceHor - self.symbolScale * 9 - self.dividerLineWidth // 2,
                self.reelOriginY,
                self.dividerLineWidth,
                int((18 * self.symbolScale + self.symbolSpaceVer) * 2.8 + self.symbolSpaceVer)
            )
            for i in range(4)
        ]

    def _build_pattern_offsets(self):
        # Beregner start-frame for hvert pattern med aftagende varighed.
        # Første pattern får fuld tid (baseDur), derefter falder mod minDur.
        # Jackpot får altid fuld tid.
        baseDur = self.frameRate * 1.25 * self.patternDuration
        minDur  = self.frameRate * 0.35 * self.patternDuration
        n = len(self.result)
        offsets = [0]
        for i in range(n):
            if self.result[i][0] == 'jackpot':
                dur = baseDur
            elif n <= 1:
                dur = baseDur
            else:
                t = i / (n - 1)
                dur = baseDur + t * (minDur - baseDur)
            offsets.append(offsets[-1] + int(dur))
        self.patternFrameOffsets = offsets

    def _build_reels(self):
        #Danner reels ud fra det nuværende resultat
        self.reels = []
        for i in range(5):
            reel = pygame.Surface((18 * self.symbolScale, (18 * self.symbolScale + self.symbolSpaceVer) * 30), pygame.SRCALPHA)

            if self.is666:
                reel.blit(random.choice(self.symbolsTuple2), (0, 0))
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
        totalPatternFrames = self.patternFrameOffsets[-1] if len(self.patternFrameOffsets) > 1 else 0
        patternsDone = self.patternTimer >= totalPatternFrames or config.is666
        if self.spinning or not patternsDone or config.spinsLeft <= 0:
            return

        #Fyrer lastSpinTrigger hvis dette er det sidste spin i runden
        if config.spinsLeft == 1:
            lastSpinTrigger()

        # Forbrug eventuelle fake coin ekstra-spins akkumuleret af randomTrigger
        if config.fakeCoinSpins > 0:
            config.spinsLeft += config.fakeCoinSpins
            config.tempLuck += 4 * config.fakeCoinSpins
            config.fakeCoinSpins = 0

        #Henter nyt resultat fra spin engine
        config.is666 = False
        self.res, self.modifiers, self.result = spin(self.gameState)
        self.is666 = config.is666

        #Opbygger frame-offsets for pattern animation (accelererer ved lange patterns)
        self._build_pattern_offsets()

        #Trækker et spin fra
        config.spinsLeft -= 1

        #Nulstiller reel animation, pattern timer og runde slut forsinkelse
        self.reelsY = [-(18 * self.symbolScale + self.symbolSpaceVer) * 30] * 5
        self.patternTimer = 0
        self.lastPaidPattern = -1
        self.roundEndDelay = 0
        self.spinning = True
        self.hasSpun = True

        #Bygger reels og spiller rullende lyd
        self._build_reels()
        self.rollingSFX.play()

    def _get_spin_options(self):
        # Beregner hvilke spin-pakker der er tilgængelige baseret på debtNum og coins.
        # Returnerer (big_spins, big_cost, big_tickets, small_spins, small_cost, small_tickets)
        # big = venstre knap, small = højre knap. None = knap vises ikke.
        # Baseret på originale Cloverpit-priser.
        d = config.debtNum
        c = config.coins

        # Tabeller per deadline: (min_coins, big_spins, big_cost, small_spins, small_cost)
        # small_spins = None betyder kun én knap vises
        # big_spins = 0 og big_cost = 0 betyder gratis spin
        if d == 1:
            tiers = [
                (7,  7, 7,  3, 3),
                (6,  6, 6,  3, 3),
                (5,  5, 5,  2, 2),
                (4,  4, 4,  2, 2),
                (3,  3, 3,  1, 1),
                (2,  2, 2,  1, 1),
                (1,  1, 1,  None, None),
                (0,  1, 0,  None, None),   # gratis spin
            ]
        elif d == 2:
            tiers = [
                (14, 7, 14, 3, 6),
                (12, 6, 12, 3, 6),
                (10, 5, 10, 2, 4),
                (8,  4, 8,  2, 4),
                (6,  3, 6,  1, 2),
                (4,  2, 4,  1, 2),
                (2,  1, 2,  None, None),
                (0,  1, 0,  None, None),   # gratis spin
            ]
        elif d == 3:
            tiers = [
                (28, 7, 28, 3, 12),
                (24, 6, 24, 3, 12),
                (20, 5, 20, 2, 8),
                (16, 4, 16, 2, 8),
                (12, 3, 12, 1, 4),
                (8,  2, 8,  1, 4),
                (4,  1, 4,  None, None),
                (0,  1, 0,  None, None),
            ]
        elif d == 4:
            tiers = [
                (42, 7, 42, 3, 18),
                (36, 6, 36, 3, 18),
                (30, 5, 30, 2, 12),
                (24, 4, 24, 2, 12),
                (18, 3, 18, 1, 6),
                (12, 2, 12, 1, 6),
                (6,  1, 6,  None, None),
                (0,  1, 0,  None, None),
            ]
        else:
            tiers = [
                (56, 7, 56, 3, 24),
                (48, 6, 48, 3, 24),
                (40, 5, 40, 2, 16),
                (32, 4, 32, 2, 16),
                (24, 3, 24, 1, 8),
                (16, 2, 16, 1, 8),
                (8,  1, 8,  None, None),
                (0,  1, 0,  None, None),
            ]

        for min_c, bs, bc, ss, sc in tiers:
            if c >= min_c:
                return (bs, bc, 1, ss, sc, 2 if ss is not None else None)

        # Fallback gratis spin
        return (1, 0, 1, None, None, None)

    def on_click(self, mousePos):
        #Håndterer klik på køb knapper når buyschreen vises
        if config.spinsLeft > 0:
            return
        # Bloker mens reels spinner eller pattern animation kører
        if self.spinning:
            return
        totalPatternFrames = self.patternFrameOffsets[-1] if len(self.patternFrameOffsets) > 1 else 0
        if self.patternTimer < totalPatternFrames and not config.is666:
            return
        # Bloker mens runde-slut forsinkelsen kører
        if self.hasSpun and self.roundEndDelay < self.roundEndDelayFrames:
            return
        # Bloker køb hvis runde 3 er brugt spilleren skal til ATM
        if config.roundNum > 3:
            return

        big, big_cost, big_tick, small, small_cost, small_tick = self._get_spin_options()

        if self.btn7Rect.collidepoint(mousePos) and big is not None and (big_cost == 0 or config.coins >= big_cost):
            config.coins = max(0, config.coins - big_cost)
            config.spinsLeft += big + config.bonusSpins
            config.tickets += big_tick
            config.roundNum += 1
            # Akkumuler rente, uindsamelet rente fra forrige runder lægges ovenpå
            config.interestStorage += round(config.depositedAmount * (config.interest / 100))
            roundEndTrigger()
            self.roundEndDelay = 0
            self.hasSpun = False
        elif self.btn3Rect.collidepoint(mousePos) and small is not None and config.coins >= small_cost:
            config.coins -= small_cost
            config.spinsLeft += small + config.bonusSpins
            config.tickets += small_tick
            config.roundNum += 1
            # Akkumuler rente, uindsamelet rente fra forrige runder lægges ovenpå
            config.interestStorage += round(config.depositedAmount * (config.interest / 100))
            roundEndTrigger()
            self.roundEndDelay = 0
            self.hasSpun = False

    def _draw_buy_screen(self):
        #Tegner buyschreen når spilleren ikke har flere spins (sort baggrund)
        self.slotMachine.fill((0, 0, 0))

        buyFont = self.buyFont
        subFont = self.subFont
        mousePos = pygame.mouse.get_pos()

        #Tjek for tab eller tvunget ATM-besøg efter runde 3
        isLastRound = config.roundNum > 3
        totalAvailable = config.coins + round(config.interestStorage)
        canPayDebt = config.depositedAmount + totalAvailable >= config.debtAmount
        if isLastRound and canPayDebt:
            # Har råd til debt vis besked om at gå til ATM, ingen køb-knapper
            msg = self.msgFont.render("Go to the ATM to pay your debt!", True, (246, 250, 10))
            self.slotMachine.blit(msg, msg.get_rect(center=(self.screenW // 2, self.screenH // 2)))
            self.slotMachine.blit(self.machine, (self.machineX, self.machineY))
            self.slotMachine.blit(self.Button, (self.buttonX, self.buttonY))
            return
        if isLastRound and not canPayDebt:
            # Vis deathschreen
            loseText    = self.loseFont.render('GAME OVER', True, (200, 40, 40))
            loseSubText  = self.loseSubFont.render('You could not pay the debt on deadline #' + str(config.debtNum), True, (200, 200, 200))
            loseSubText2 = self.loseSubFont.render('Reached deadline ' + str(config.debtNum) + ' round ' + str(config.roundNum), True, (160, 160, 160))
            self.slotMachine.blit(loseText,     loseText.get_rect(center=(self.screenW // 2, self.screenH // 2 - 80)))
            self.slotMachine.blit(loseSubText,  loseSubText.get_rect(center=(self.screenW // 2, self.screenH // 2)))
            self.slotMachine.blit(loseSubText2, loseSubText2.get_rect(center=(self.screenW // 2, self.screenH // 2 + 50)))
            self.slotMachine.blit(self.machine, (self.machineX, self.machineY))
            self.slotMachine.blit(self.Button, (self.buttonX, self.buttonY))
            return

        #Rundenummer og deadline øverst i midten
        roundText = buyFont.render('ROUND ' + str(config.roundNum) + '  |  DEADLINE #' + str(config.debtNum), True, (246, 250, 10))
        self.slotMachine.blit(roundText, roundText.get_rect(center=(self.screenW // 2, 80)))

        big, big_cost, big_tick, small, small_cost, small_tick = self._get_spin_options()

        def draw_btn(rect, spins, cost, tickets, active):
            # Farver baseret på om knappen er aktiv og om musen er over den
            if not active:
                bg, border, tc, sc = (15,15,15), (40,35,15), (60,60,60), (50,50,50)
            elif rect.collidepoint(mousePos):
                bg, border, tc, sc = (60,60,20), (246,250,10), (246,250,10), (220,220,220)
            else:
                bg, border, tc, sc = (40,40,40), (120,95,26), (246,250,10), (200,200,200)
            pygame.draw.rect(self.slotMachine, bg, rect, border_radius=8)
            pygame.draw.rect(self.slotMachine, border, rect, 3, border_radius=8)
            if spins == 0:
                label = buyFont.render('FREE SPIN', True, tc)
                sub   = subFont.render('+' + str(tickets) + ' ticket', True, sc)
            else:
                label = buyFont.render(str(spins) + ' SPINS', True, tc)
                costStr = (str(cost) + ' coins') if cost > 0 else 'FREE'
                tickStr = '+' + str(tickets) + ' ticket' + ('s' if tickets > 1 else '')
                sub = subFont.render(costStr + '  ' + tickStr, True, sc)
            self.slotMachine.blit(label, label.get_rect(center=rect.center + pygame.math.Vector2(0, -18)))
            self.slotMachine.blit(sub,   sub.get_rect(center=rect.center + pygame.math.Vector2(0, 18)))

        # Venstre knap (stor pakke) altid vist
        draw_btn(self.btn7Rect, big if big is not None else 0,
                 big_cost if big_cost is not None else 0,
                 big_tick if big_tick is not None else 0,
                 big is not None)

        # Højre knap (lille pakke) kun vist når small ikke er None
        if small is not None:
            draw_btn(self.btn3Rect, small, small_cost, small_tick, True)
        else:
            # Tegner grå tom knap når der kun er en mulighed
            pygame.draw.rect(self.slotMachine, (15,15,15), self.btn3Rect, border_radius=8)
            pygame.draw.rect(self.slotMachine, (40,35,15), self.btn3Rect, 3, border_radius=8)

        #Tegner slot machine surface på skærmen
        self.slotMachine.blit(self.machine, (self.machineX, self.machineY))
        self.slotMachine.blit(self.Button, (self.buttonX, self.buttonY))

    def draw(self, screen):
        self.slotMachine.fill((0, 0, 0))

        #Tegner slot machine surface på skærmen
        self.slotMachine.blit(self.machine, (self.machineX, self.machineY))
        self.slotMachine.blit(self.Button, (self.buttonX, self.buttonY))

        #Buyschreen vises kun når spins er 0, animation er færdig, og forsinkelsen er talt ned
        totalPatternFrames = self.patternFrameOffsets[-1] if len(self.patternFrameOffsets) > 1 else 0
        patternsDone = self.patternTimer >= totalPatternFrames or config.is666
        roundOver = config.spinsLeft <= 0 and not self.spinning and patternsDone

        if roundOver:
            if self.hasSpun and self.roundEndDelay < self.roundEndDelayFrames:
                #Tæller forsinkelsen op viser stadig reelsene i mellemtiden
                self.roundEndDelay += 1
            else:
                self._draw_buy_screen()
                screen.blit(self.slotMachine, (0, 0))
                return

        #Viser spin-tæller øverst i midten under normal spil
        spinCountText = self.spinCountFont.render('SPINS: ' + str(config.spinsLeft), True, (246, 250, 10))
        self.slotMachine.blit(spinCountText, spinCountText.get_rect(center=(self.screenW // 2 - 30, 70)))

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

        #Tegner linjer mellem reels (pre-cached rects)
        for rect in self.dividerRects:
            pygame.draw.rect(self.slotMachine, (120, 95, 26), rect)

        #Pattern animation — aftagende varighed via patternFrameOffsets
        totalPatternFrames = self.patternFrameOffsets[-1] if len(self.patternFrameOffsets) > 1 else 0
        if self.reelsY.count(self.reelOriginY + self.symbolSpaceVer) == 5 and self.patternTimer < totalPatternFrames and not self.is666:

            # Find currentPatternIdx via offsets
            currentPatternIdx = 0
            for k in range(len(self.patternFrameOffsets) - 1):
                if self.patternTimer >= self.patternFrameOffsets[k]:
                    currentPatternIdx = k
            patternStart = self.patternFrameOffsets[currentPatternIdx]
            patternEnd   = self.patternFrameOffsets[currentPatternIdx + 1]
            patternLen   = patternEnd - patternStart
            # Highlight vises i de første 80% af patternets tid
            showHighlight = self.patternTimer < patternStart + int(patternLen * 0.8)

            #Spiller lydeffekten og giver belønning når et nyt pattern starter
            if self.patternTimer == patternStart:
                if self.result[currentPatternIdx][0] == 'jackpot':
                    self.jackpotSFX.play()
                else:
                    self.scoreSFX.play()
                if currentPatternIdx != self.lastPaidPattern:
                    config.coins += self.result[currentPatternIdx][1]
                    #Giver tickets for ticket modifiers
                    config.tickets += self.result[currentPatternIdx][2].count(3)
                    #Giver coins for token modifiers (10% af pattern-udbetaling per token)
                    config.coins += round(self.result[currentPatternIdx][2].count(2) * self.result[currentPatternIdx][1] * 0.1)
                    #Giver item charges for battery modifiers
                    for i in range(self.result[currentPatternIdx][2].count(5)):
                        battItems = []
                        for item in config.shelfItems:
                            if item.type == 'button' and item.charges < item.chargeSlots:
                                battItems.append(item)
                        if len(battItems) != 0:
                            config.shelfItems[config.shelfItems.index(random.choice(battItems))].charges += 1
                    self.lastPaidPattern = currentPatternIdx

            #Tegner kasser og payout-tekst mens highlight er aktiv
            if showHighlight:
                for slot in config.patterns[self.result[currentPatternIdx][0]]:
                    boxX = self.reelOriginX + slot % 5 * self.symbolSpaceHor - self.squareDist
                    boxY = self.reelOriginY + self.symbolSpaceVer - self.squareDist + math.floor(slot / 5) * (18 * self.symbolScale + self.symbolSpaceVer)
                    pygame.draw.rect(self.slotMachine, (36, 252, 3), pygame.Rect(boxX, boxY, 18 * self.symbolScale + 2 * self.squareDist, 18 * self.symbolScale + 2 * self.squareDist), 2, 3)

                if len(str(self.result[currentPatternIdx][1])) > 7:
                    patternPayout = round(self.result[currentPatternIdx][1] * 10**(-1 * (len(str(self.result[currentPatternIdx][1])) - 1)), 5)
                    text = self.font.render('+' + str(patternPayout) + 'E+' + str(len(str(self.result[currentPatternIdx][1])) - 1), True, (250, 10, 10))
                else:
                    text = self.font.render('+' + str(self.result[currentPatternIdx][1]), True, (246, 250, 10))
                self.slotMachine.blit(text, text.get_rect(center=(self.screenW / 2, self.screenH / 2)))

            self.patternTimer += 1
        
        # Tegner slot machine surface på skærmen
        self.slotMachine.blit(self.machine, (self.machineX, self.machineY))
        self.slotMachine.blit(self.Button, (self.buttonX, self.buttonY))

        # Får knappen til at knappe
        if isSelected(self.Button, (self.buttonX, self.buttonY), self.slotMachine) and pygame.mouse.get_just_pressed()[0]:
            buttonTrigger()

        screen.blit(self.slotMachine, (0, 0))
