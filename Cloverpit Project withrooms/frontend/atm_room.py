#ATM script
import math
import pygame
import subprocess
from backend.ATM_backend import newDeadline
from frontend.mouseCheck import isSelected
import config.game_config as config
from backend.shelf_backend import deadlineEndTrigger


class ATMRoom:

    def __init__(self, resolution, xScaling, yScaling):

        overallScale = 2
        self.font = pygame.font.Font(None, size = round(15 * overallScale * xScaling))
        self.font2 = pygame.font.Font(None, size = round(13 * overallScale * xScaling))
        self.font3 = pygame.font.Font(None, size = round(8 * overallScale * xScaling))        

        # texten med deadline placeres
        self.deadlineX = 275
        self.deadlineY = 50

        # Runder tilbage før man dør osv.
        self.debtX = self.deadlineX - 80 * xScaling
        self.debtY = self.deadlineY + 235 * yScaling

        # importer billeder fra assets-mappen
        self.atmBackground = pygame.image.load('assets/Atm.png')
        self.atmBackground = pygame.transform.scale(self.atmBackground, (self.atmBackground.get_width() * 0.67 * overallScale* xScaling, self.atmBackground.get_height() * 0.67 * overallScale * yScaling))
        self.atmBackground.set_colorkey((163, 73, 164))
        self.atmButton = pygame.image.load('assets/AtmButton.png')
        self.atmButton = pygame.transform.scale(self.atmButton, (self.atmButton.get_width() * 0.42 * overallScale * xScaling, self.atmButton.get_height() * 0.42 * overallScale * yScaling))
        self.atmButton.set_colorkey((163, 73, 164))
        self.coin = pygame.image.load('assets/Coin.webp')
        self.coin = pygame.transform.scale(self.coin, (self.coin.get_width() * 0.065 * overallScale * xScaling, self.coin.get_height() * 0.065 * overallScale * yScaling))
        self.cloverSkull = pygame.image.load('assets/cloverSkull.png')
        self.cloverSkull = pygame.transform.scale(self.cloverSkull, (self.cloverSkull.get_width() * 0.22 * overallScale * xScaling, self.cloverSkull.get_height() * 0.22 * overallScale * yScaling))
        self.atmPayout = pygame.image.load('assets/AtmPayout.png')
        self.atmPayout = pygame.transform.scale(self.atmPayout, (self.atmPayout.get_width() * 0.67 * overallScale * xScaling, self.atmPayout.get_height() * 0.80 * overallScale * yScaling))
        self.atmPayout.set_colorkey((163, 73, 164))
        self.atmRoundBonus = pygame.image.load('assets/ATMRoundBonus.png')
        self.atmRoundBonus = pygame.transform.scale(self.atmRoundBonus, (self.atmRoundBonus.get_width() * 0.3 * overallScale * xScaling, self.atmRoundBonus.get_height() * 0.3 * overallScale * yScaling))
        self.atmCoinAndTicket = pygame.image.load('assets/ATMCoinAndTicket.png')
        self.atmCoinAndTicket = pygame.transform.scale(self.atmCoinAndTicket, (self.atmCoinAndTicket.get_width() * 0.3 * overallScale * xScaling, self.atmCoinAndTicket.get_height() * 0.3 * overallScale * yScaling))
        self.littleGuy = pygame.image.load('assets/little_guy.png')
        self.littleGuy.set_colorkey((0, 0, 0))
        self.phoneRing = pygame.mixer.Sound('assets/2-083. Phonering.mp3')

        # Opretter atm surface og danner baggrunden
        self.atmRoom = pygame.Surface(resolution, pygame.SRCALPHA)
        self.atmScreen = pygame.Surface((203.68 * xScaling, 135.34 * yScaling))
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, resolution)

        # Advarsel om spin-budget: WarnShown = advarsel synlig nu, WarnUsed = er allerede set dette deadline
        self.spinBudgetWarnShown = False
        self.spinBudgetWarnUsed  = False

    def _calcDepositChunk(self):
        # Returnerer (depositChunk, wouldDipSpinBudget).
        # wouldDipSpinBudget = True hvis indbetalingen ville tage coins under spinBudget.
        if config.coins <= 0:
            return 0, False
        d = config.debtNum
        if d == 1:   spinBudget, dripRate = 7,  1
        elif d == 2: spinBudget, dripRate = 14, 2
        elif d == 3: spinBudget, dripRate = 28, 4
        elif d == 4: spinBudget, dripRate = 42, 6
        else:        spinBudget, dripRate = 56, 8

        remaining = max(0, config.debtAmount - config.depositedAmount)
        rawChunk  = max(dripRate, int(config.debtAmount * 0.1))
        wouldDip  = config.coins - rawChunk < spinBudget

        if wouldDip:
            rawChunk = max(dripRate, config.coins - spinBudget)
        rawChunk = max(1, rawChunk)
        rawChunk = min(rawChunk, config.coins)
        rawChunk = min(rawChunk, remaining)
        return rawChunk, wouldDip

    def draw(self, screen, resolution, xScaling, yScaling):
        # blitter baggrunden på overfladen
        self.atmRoom.blit(self.background, (-3, -3))

        # Tegner baggrunden på skærmen
        self.atmScreen.fill((0, 0, 0))

        #Teksten på maskinen
        textDeadline = self.font.render('DEADLINE: ' + '#' + str(config.debtNum), True, (246, 250, 10))
        self.atmBackground.blit(textDeadline, textDeadline.get_rect(center=(self.deadlineX * xScaling, self.deadlineY * yScaling)))
        textRoundsLeft = self.font2.render(str(4 - config.roundNum) + ' ROUNDS LEFT', True, (246, 250, 10))
        textDebt = self.font3.render('DEBT:', True, (246, 250, 10))
        textDeposited = self.font3.render('DEPOSITED:', True, (246, 250, 10))
        textInterest = self.font3.render('INTEREST:', True, (246, 250, 10))
        textInterestValue = self.font3.render(str(config.interest) + '% ', True, (246, 250, 10))
        textScreenLine = self.font3.render('-----------------------------------------------------------------------------', True, (246, 250, 10))

        # blit knappen og få den til at knappe
        self.atmBackground.blit(self.atmButton, (271 * 0.67 * 2 * xScaling, 257 * 0.67 * 2 * yScaling))

        if isSelected(self.atmButton, (271 * 0.67 * 2 * xScaling, 257 * 0.67 * 2 * yScaling), self.atmBackground):
            previewChunk, wouldDip = self._calcDepositChunk()

            # Tooltip vis advarsel hvis warnflag er sat, ellers normal deposit preview
            if previewChunk > 0:
                if self.spinBudgetWarnShown:
                    # Rød advarsel
                    line1 = self.font2.render('Deposit: ' + str(previewChunk) + ' coins', True, (246, 250, 10))
                    line2 = self.font3.render("Don't forget to buy spins first!", True, (220, 160, 60))
                    tooltip = pygame.Surface((self.font2.size('Deposit: ' + str(previewChunk) + ' coins       ')[0], self.font2.size("A")[1] * 3))
                    tooltip.fill((0, 0, 0))
                    pygame.draw.rect(tooltip, (180, 40, 40), tooltip.get_rect(), 2, border_radius=6)
                    tooltip.blit(line1, line1.get_rect(center=(tooltip.get_width() / 2, tooltip.get_height() / 2)))
                    tooltip.blit(line2, line2.get_rect(center=(tooltip.get_width() / 2, tooltip.get_height() / 2 + self.font2.size("A")[1])))
                    self.atmRoom.blit(tooltip, (271 * 0.67 * 2 * xScaling + self.atmButton.get_width() / 2 - tooltip.get_width() / 2, 257 * 0.67 * 2 * yScaling - tooltip.get_height() - 20 * yScaling))
                else:
                    # Normal tooltip
                    tipText = self.font2.render('Deposit: ' + str(previewChunk) + ' coins', True, (246, 250, 10))
                    tooltip = pygame.Surface((self.font2.size('Deposit: ' + str(previewChunk) + ' coins')[0], self.font2.size("A")[1]))
                    tooltip.fill((0, 0, 0))
                    pygame.draw.rect(tooltip, (120, 95, 26), tooltip.get_rect(), 2, border_radius=6)
                    tooltip.blit(tipText, tipText.get_rect(center=(tooltip.get_width() / 2, tooltip.get_height() / 2)))
                    self.atmRoom.blit(tooltip, (271 * 0.67 * 2 * xScaling + self.atmButton.get_width() / 2 - tooltip.get_width() / 2, 257 * 0.67 * 2 * yScaling - tooltip.get_height() - 20 * yScaling))

            if pygame.mouse.get_just_pressed()[0]:
                if self.spinBudgetWarnShown:
                    # Andet klik advarsel skjules, indbetalingen sker
                    self.spinBudgetWarnShown = False
                    self.spinBudgetWarnUsed  = True
                    if config.coins > 0:
                        config.depositedAmount += previewChunk
                        config.coins -= previewChunk
                elif wouldDip and not self.spinBudgetWarnUsed:
                    # Første klik der ville ramme spin-budgettet vis advarsel
                    self.spinBudgetWarnShown = True
                else:
                    # Normalt klik
                    if config.coins > 0:
                        config.depositedAmount += previewChunk
                        config.coins -= previewChunk


        # Rente-udbetalings panel (atmPayout) vises når der er opsparet rente
        # interestStorage opbygges af slot_room ved rundesslut og akkumulerer hvis ikke hentet
        if config.interestStorage > 0:
            self.atmRoom.blit(self.atmPayout, (28 * 0.67 * 2 * xScaling, 358 * 0.67 * 2 * yScaling))
            interestText = self.font2.render(str(round(config.interestStorage)) + ' coins', True, (246, 250, 10))
            self.atmScreen.blit(interestText, textInterest.get_rect(center=(self.font3.size('INTEREST:')[0] / 2, self.atmScreen.get_height() / 1.3)))

            if isSelected(self.atmPayout, (27 * 0.67 * 2 * xScaling, 347 * 0.67 * 2 * yScaling), self.atmRoom) and pygame.mouse.get_just_pressed()[0]:
                config.coins += round(config.interestStorage)
                config.interestStorage = 0

        # Deadline bonus panel viser hvad der gives ved deadline slutning
        # Coins: 6 * deadline-nummer, Tickets: 4 per sprunget runde (maks 3 runder)
        roundBonusCoins = 6 * config.debtNum
        roundBonusTickets = 4 * max(0, 3 - config.roundNum)        

        # Dynamiske tal ved siden af mønt- og ticket-symbolerne
        roundBonusCoinText = self.font2.render(str(roundBonusCoins), True, (246, 250, 10))
        roundBonusTicketText = self.font2.render(str(roundBonusTickets), True, (246, 250, 10))
        self.atmRoundBonus.blit(roundBonusCoinText, (120 * 0.6 * xScaling, 200 * 0.6 * yScaling))
        self.atmRoundBonus.blit(roundBonusTicketText, (120 * 0.6 * xScaling, 260 * 0.6 * yScaling))

        self.atmRoundBonus.blit(self.atmCoinAndTicket, (175 * 0.6 * xScaling, 180 * 0.6 * yScaling))
        self.atmRoom.blit(self.atmRoundBonus, (self.atmRoom.get_width() / 2, self.atmRoom.get_height() / 2))

        # alt på den store skærm med info om deadline, gæld, indbetaling, rente osv.
        # Blit teksten og mønterne på ATM-overfladen
        self.atmScreen.blit(textScreenLine, textScreenLine.get_rect(center=(self.atmScreen.get_width() / 2, self.atmScreen.get_height() / 50)))

        self.atmScreen.blit(self.cloverSkull, (self.atmScreen.get_width() / 40, self.atmScreen.get_height() / 50))
        self.atmScreen.blit(textRoundsLeft, textRoundsLeft.get_rect(center=(self.atmScreen.get_width() / 2, self.atmScreen.get_height() / 9)))
        self.atmScreen.blit(self.cloverSkull, (self.atmScreen.get_width() / 1.15, self.atmScreen.get_height() / 50))

        self.atmScreen.blit(textScreenLine, textScreenLine.get_rect(center=(self.atmScreen.get_width() / 2, self.atmScreen.get_height() / 6)))
        self.atmScreen.blit(textDebt, textDebt.get_rect(center=(self.atmScreen.get_width() / 12.5, self.atmScreen.get_height() / 4.5)))
        self.atmScreen.blit(self.coin, (self.atmScreen.get_width() / 1.125, self.atmScreen.get_height() / 5.5))

        if math.log10(config.debtAmount) >= 7 and math.log10(config.debtAmount) < 100:
            deposit = round(config.debtAmount * 10**(-1 * (len(str(config.debtAmount)) - 1)), 2)
            textDebtAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(config.debtAmount)) - 1), True, (246, 250, 10))
            self.atmScreen.blit(textDebtAmount, textDebtAmount.get_rect(center=(self.atmScreen.get_width() / 1.35, self.atmScreen.get_height() / 3.5)))
        if math.log10(config.debtAmount) >= 100:
            deposit = round(config.debtAmount * 10**(-1 * (len(str(config.debtAmount)) - 1)), 2)
            textDebtAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(config.debtAmount)) - 1), True, (246, 250, 10))
            self.atmScreen.blit(textDebtAmount, textDebtAmount.get_rect(center=(self.atmScreen.get_width() / 1.3, self.atmScreen.get_height() / 3.5)))
        if math.log10(config.debtAmount) < 7:
            textDebtAmount = self.font2.render(str(config.debtAmount), True, (246, 250, 10))
            self.atmScreen.blit(textDebtAmount, textDebtAmount.get_rect(center=((self.atmScreen.get_width() / 1.2 - math.log10(config.debtAmount)**(1.50 - 0.012 * math.log10(config.debtAmount))), self.atmScreen.get_height() / 3.5)))

        self.atmScreen.blit(textScreenLine, textScreenLine.get_rect(center=(self.atmScreen.get_width() / 2, self.atmScreen.get_height() / 2.5)))
        self.atmScreen.blit(textDeposited, textDeposited.get_rect(center=(self.atmScreen.get_width() / 6, self.atmScreen.get_height() / 2.2)))
        self.atmScreen.blit(self.coin, (self.atmScreen.get_width() / 1.125, self.atmScreen.get_height() / 2.4))

        if config.depositedAmount <= 0:
            textDepositedAmount = self.font2.render('0', True, (246, 250, 10))
            self.atmScreen.blit(textDepositedAmount, textDepositedAmount.get_rect(center=((self.debtX + 50) * xScaling, self.atmScreen.get_height() / 2)))
        elif math.log10(config.depositedAmount) >= 6 and math.log10(config.depositedAmount) < 100:
            deposit = round(config.depositedAmount * 10**(-1 * (len(str(config.depositedAmount)) - 1)), 2)
            textDepositedAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(config.depositedAmount)) - 1), True, (246, 250, 10))
            self.atmScreen.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(self.atmScreen.get_width() / 1.35, self.atmScreen.get_height() / 2)))
        elif math.log10(config.depositedAmount) >= 100:
            deposit = round(config.depositedAmount * 10**(-1 * (len(str(config.depositedAmount)) - 1)), 2)
            textDepositedAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(config.depositedAmount)) - 1), True, (246, 250, 10))
            self.atmScreen.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(self.atmScreen.get_width() / 1.3, self.atmScreen.get_height() / 2)))
        else:
            textDepositedAmount = self.font2.render(str(config.depositedAmount), True, (246, 250, 10))
            self.atmScreen.blit(textDepositedAmount, textDepositedAmount.get_rect(center=((self.atmScreen.get_width() / 1.2 - math.log10(config.depositedAmount)**(1.50 - 0.012 * math.log10(config.depositedAmount))), self.atmScreen.get_height() / 2)))

        self.atmScreen.blit(textScreenLine, textScreenLine.get_rect(center=(self.atmScreen.get_width() / 2, self.atmScreen.get_height() / 1.65)))
        self.atmScreen.blit(textInterest, textInterest.get_rect(center=(self.font3.size('INTEREST:')[0] / 2, self.atmScreen.get_height() / 1.5)))
        self.atmScreen.blit(textInterestValue, textInterestValue.get_rect(center=(self.atmScreen.get_width() - self.font3.size(str(config.interest) + '% ')[0], self.atmScreen.get_height() / 1.5)))
        self.atmScreen.blit(textScreenLine, textScreenLine.get_rect(center=(self.atmScreen.get_width() / 2, self.atmScreen.get_height() / 1.05)))
        
        if config.depositedAmount >= config.debtAmount:
            bonusCoins   = 6 * config.debtNum
            bonusTickets = 4 * max(0, 3 - config.roundNum)
            config.coins   += bonusCoins
            config.tickets += bonusTickets
            config.debtAmount      = newDeadline(config.debtNum, 1)
            config.debtNum        += 1
            config.roundNum        = 1
            config.spinsLeft       = 0
            self.spinBudgetWarnShown = False
            self.spinBudgetWarnUsed  = False
            deadlineEndTrigger()
            for i in range(7):
                config.symbolWeights[i] -= config.tempSymbolWeights[i]
                config.tempSymbolWeights[i] = 0
            config.phoneIsActive = True
            self.phoneRing.play()
            if config.debtNum < 10:
                config.restockCost = config.restockCosts[config.debtNum]
            else:
                config.restockCost = config.debtAmount // 20
                    
            self.atmBackground = pygame.image.load('assets/Atm.png')
            self.atmBackground = pygame.transform.scale(self.atmBackground, (self.atmBackground.get_width() * 0.67 * 2 * xScaling, self.atmBackground.get_height() * 0.67 * 2 * yScaling))
            self.atmBackground.set_colorkey((163, 73, 164))
            self.atmRoundBonus = pygame.image.load('assets/ATMRoundBonus.png')
            self.atmRoundBonus = pygame.transform.scale(self.atmRoundBonus, (self.atmRoundBonus.get_width() * 0.3 * 2 * xScaling, self.atmRoundBonus.get_height() * 0.3 * 2 * yScaling))

        #Intet at se her
        self.atmRoom.blit(self.littleGuy, (500 * xScaling, 700 * yScaling))
        if isSelected(self.littleGuy, (500 * xScaling, 700 * yScaling), self.atmRoom) and pygame.mouse.get_just_pressed()[0]:
            subprocess.run('assets/Little Guy Goes To Verdun.exe')

        self.atmBackground.blit(self.atmScreen, (62 * 0.67 * xScaling * 2, 194 * 0.67 * yScaling * 2))
        screen.blit(self.atmRoom, (0, 0))
