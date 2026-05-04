#ATM script
import math
import pygame
from backend.ATM_backend import newDeadline
from frontend.mouseCheck import isSelected

class ATMRoom:

    def __init__(self):

        overallScale = 2
        self.font = pygame.font.Font(None, size = 15 * overallScale)
        self.font2 = pygame.font.Font(None, size = 13 * overallScale)
        self.font3 = pygame.font.Font(None, size = 8 * overallScale)

        # importere variabler
        self.debtNum = 1
        self.roundNum = 1
        self.debtAmount = 75
        self.depositedAmount = 30
        self.interest = 7.00

        # texten med deadline placeres
        self.deadlineX = 275
        self.deadlineY = 50

        # Runder tilbage før man dør osv.
        self.debtX = self.deadlineX - 80
        self.debtY = self.deadlineY + 235

        # importer billeder fra assets-mappen
        self.atmBackground = pygame.image.load('assets/Atm.png')
        self.atmBackground = pygame.transform.scale(self.atmBackground, (self.atmBackground.get_width() * 0.67 * overallScale, self.atmBackground.get_height() * 0.67 * overallScale))
        self.atmBackground.set_colorkey((163, 73, 164))
        self.atmButton = pygame.image.load('assets/AtmButton.png')
        self.atmButton = pygame.transform.scale(self.atmButton, (self.atmButton.get_width() * 0.4 * overallScale, self.atmButton.get_height() * 0.4 * overallScale))
        self.atmButton.set_colorkey((163, 73, 164))
        self.coin = pygame.image.load('assets/Coin.webp')
        self.coin = pygame.transform.scale(self.coin, (self.coin.get_width() * 0.065 * overallScale, self.coin.get_height() * 0.065 * overallScale))
        self.cloverSkull = pygame.image.load('assets/cloverSkull.png')
        self.cloverSkull = pygame.transform.scale(self.cloverSkull, (self.cloverSkull.get_width() * 0.22 * overallScale, self.cloverSkull.get_height() * 0.22 * overallScale))

        # Opretter atm surface og danner baggrunden
        self.atm = pygame.Surface((1200, 750), pygame.SRCALPHA)
        self.background = pygame.image.load('assets/Background.png')
        self.background = pygame.transform.scale(self.background, (1200, 750))

    def draw(self, screen):

        # blitter baggrunden på overfladen
        self.atm.blit(self.background, (-3, -3))

        # Blit atm på overfladen
        self.atm.blit(self.atmBackground, (0, 0))

        # Texten på maskinen
        textDeadline = self.font.render('DEADLINE: ' + '#' + str(self.debtNum), True, (246, 250, 10))
        self.atm.blit(textDeadline, textDeadline.get_rect(center=(self.deadlineX, self.deadlineY)))
        textRoundsLeft = self.font2.render(str(4 - self.roundNum) + ' ROUNDS LEFT', True, (246, 250, 10))
        textDebt = self.font3.render('DEBT:', True, (246, 250, 10))
        textDeposited = self.font3.render('DEPOSITED:', True, (246, 250, 10))
        textInterest = self.font3.render('INTEREST:', True, (246, 250, 10))
        textInterestValue = self.font3.render(str(self.interest) + '% ', True, (246, 250, 10))
        textScreenLine = self.font3.render('-------------------------------------------------', True, (246, 250, 10))

        # blit knappen og få den til at knappe
        self.atm.blit(self.atmButton, (self.debtX + 166, self.debtY + 58))

        if isSelected(self.atmButton, (self.debtX + 166, self.debtY + 58), self.atm) and pygame.mouse.get_just_pressed()[0]:
            self.depositedAmount += 40000000000

            if self.depositedAmount >= self.debtAmount:
                self.debtAmount = newDeadline(self.debtNum, 1)
                self.debtNum += 1
                self.roundNum = 1
            pass


        # Blit teksten og mønterne på ATM-overfladen
        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(self.debtX - 10, self.debtY - 20)))

        self.atm.blit(self.cloverSkull, (self.debtX - 102, self.debtY - 18))
        self.atm.blit(textRoundsLeft, textRoundsLeft.get_rect(center=(self.debtX - 10, self.debtY - 6)))
        self.atm.blit(self.cloverSkull, (self.debtX + 60, self.debtY - 18))

        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(self.debtX - 10, self.debtY + 6)))
        self.atm.blit(textDebt, textDebt.get_rect(center=(self.debtX - 92, self.debtY + 16)))
        self.atm.blit(self.coin, (self.debtX + 68, self.debtY + 18))

        if math.log10(self.debtAmount) >= 7 and math.log10(self.debtAmount) < 100:
            deposit = round(self.debtAmount * 10**(-1 * (len(str(self.debtAmount)) - 1)), 2)
            textDebtAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.debtAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(self.debtX + 35, self.debtY + 30)))
        if math.log10(self.debtAmount) >= 100:
            deposit = round(self.debtAmount * 10**(-1 * (len(str(self.debtAmount)) - 1)), 2)
            textDebtAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.debtAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(self.debtX + 30, self.debtY + 30)))
        if math.log10(self.debtAmount) < 7:
            textDebtAmount = self.font2.render(str(self.debtAmount), True, (246, 250, 10))
            self.atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(self.debtX + 50 - math.log10(self.debtAmount)**(1.50 - 0.012 * math.log10(self.debtAmount)), self.debtY + 30)))

        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(self.debtX - 10, self.debtY + 45)))
        self.atm.blit(textDeposited, textDeposited.get_rect(center=(self.debtX - 75, self.debtY + 55)))
        self.atm.blit(self.coin, (self.debtX + 68, self.debtY + 55))

        if math.log10(self.depositedAmount) >= 6 and math.log10(self.depositedAmount) < 100:
            deposit = round(self.depositedAmount * 10**(-1 * (len(str(self.depositedAmount)) - 1)), 2)
            textDepositedAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.depositedAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(self.debtX + 30, self.debtY + 70)))
        if math.log10(self.depositedAmount) >= 100:
            deposit = round(self.depositedAmount * 10**(-1 * (len(str(self.depositedAmount)) - 1)), 2)
            textDepositedAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.depositedAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(self.debtX + 25, self.debtY + 70)))
        if math.log10(self.depositedAmount) < 6:
            textDepositedAmount = self.font2.render(str(self.depositedAmount), True, (246, 250, 10))
            self.atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(self.debtX + 50 - math.log10(self.depositedAmount)**(1.50 - 0.012 * math.log10(self.depositedAmount)), self.debtY + 70)))

        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(self.debtX - 10, self.debtY + 82.5)))
        self.atm.blit(textInterest, textInterest.get_rect(center=(self.debtX - 79, self.debtY + 92.5)))
        self.atm.blit(textInterestValue, textInterestValue.get_rect(center=(self.debtX + 70, self.debtY + 92.5)))
        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(self.debtX - 10, self.debtY + 100)))
        
        
        
        screen.blit(self.atm, (0, 0))

