#ATM script
import math
import pygame


class ATMRoom:

    def __init__(self):

        overallScale = 2

        self.font = pygame.font.Font(None, size = 15 * overallScale)
        self.font2 = pygame.font.Font(None, size = 13 * overallScale)
        self.font3 = pygame.font.Font(None, size = 8 * overallScale)

        # importer billeder fra assets-mappen
        atmBackground = pygame.image.load('assets/Atm.png')
        atmBackground = pygame.transform.scale(atmBackground, (atmBackground.get_width() * 0.67 * overallScale, atmBackground.get_height() * 0.67 * overallScale))
        atmBackground.set_colorkey((163, 73, 164))
        coin = pygame.image.load('assets/Coin.webp')
        coin = pygame.transform.scale(coin, (coin.get_width() * 0.065 * overallScale, coin.get_height() * 0.065 * overallScale))
        self.cloverSkull = pygame.image.load('assets/cloverSkull.png')
        self.cloverSkull = pygame.transform.scale(self.cloverSkull, (self.cloverSkull.get_width() * 0.22 * overallScale, self.cloverSkull.get_height() * 0.22 * overallScale))

        # importere variabler
        self.debtNum = 1
        self.roundNum = 1
        self.debtAmount = 75
        self.depositedAmount = 30
        self.interest = 7.00

        # Opretter atm surface og danner baggrunden
        self.atm = pygame.Surface((1200, 750), pygame.SRCALPHA)
        background = pygame.image.load('assets/Background.png')
        background = pygame.transform.scale(background, (1200, 750))
        self.atm.blit(background, (-3, -3))

        # Blit atm på overfladen
        self.atm.blit(atmBackground, (0, 0))

        # texten med deadline placeres
        deadlineX = 275
        deadlineY = 50

        textDeadline = self.font.render('DEADLINE: ' + '#' + str(self.debtNum), True, (246, 250, 10))
        self.atm.blit(textDeadline, textDeadline.get_rect(center=(deadlineX, deadlineY)))

        # Runder tilbage før man dør osv.
        debtX = deadlineX - 80
        debtY = deadlineY + 235

        textRoundsLeft = self.font2.render(str(self.roundNum) + ' ROUNDS LEFT', True, (246, 250, 10))
        textDebt = self.font3.render('DEBT:', True, (246, 250, 10))
        textDeposited = self.font3.render('DEPOSITED:', True, (246, 250, 10))
        textInterest = self.font3.render('INTEREST:', True, (246, 250, 10))
        textInterestValue = self.font3.render(str(self.interest) + '% ', True, (246, 250, 10))
        textScreenLine = self.font3.render('-------------------------------------------------', True, (246, 250, 10))

        # Blit teksten og mønterne på ATM-overfladen
        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY - 20)))

        self.atm.blit(self.cloverSkull, (debtX - 102, debtY - 18))
        self.atm.blit(textRoundsLeft, textRoundsLeft.get_rect(center=(debtX - 10, debtY - 6)))
        self.atm.blit(self.cloverSkull, (debtX + 60, debtY - 18))

        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 6)))
        self.atm.blit(textDebt, textDebt.get_rect(center=(debtX - 92, debtY + 16)))
        self.atm.blit(coin, (debtX + 68, debtY + 18))

        if math.log10(self.debtAmount) >= 7 and math.log10(self.debtAmount) < 100:
            deposit = round(self.debtAmount * 10**(-1 * (len(str(self.debtAmount)) - 1)), 2)
            textDebtAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.debtAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 35, debtY + 30)))
        if math.log10(self.debtAmount) >= 100:
            deposit = round(self.debtAmount * 10**(-1 * (len(str(self.debtAmount)) - 1)), 2)
            textDebtAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.debtAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 30, debtY + 30)))
        if math.log10(self.debtAmount) < 7:
            textDebtAmount = self.font2.render(str(self.debtAmount), True, (246, 250, 10))
            self.atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 50 - math.log10(self.debtAmount)**(1.50 - 0.012 * math.log10(self.debtAmount)), debtY + 30)))

        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 45)))
        self.atm.blit(textDeposited, textDeposited.get_rect(center=(debtX - 75, debtY + 55)))
        self.atm.blit(coin, (debtX + 68, debtY + 55))

        if math.log10(self.depositedAmount) >= 6 and math.log10(self.depositedAmount) < 100:
            deposit = round(self.depositedAmount * 10**(-1 * (len(str(self.depositedAmount)) - 1)), 2)
            textDepositedAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.depositedAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 30, debtY + 70)))
        if math.log10(self.depositedAmount) >= 100:
            deposit = round(self.depositedAmount * 10**(-1 * (len(str(self.depositedAmount)) - 1)), 2)
            textDepositedAmount = self.font2.render(str(deposit) + 'E+' + str(len(str(self.depositedAmount)) - 1), True, (246, 250, 10))
            self.atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 25, debtY + 70)))
        if math.log10(self.depositedAmount) < 6:
            textDepositedAmount = self.font2.render(str(self.depositedAmount), True, (246, 250, 10))
            self.atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 50 - math.log10(self.depositedAmount)**(1.50 - 0.012 * math.log10(self.depositedAmount)), debtY + 70)))

        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 82.5)))
        self.atm.blit(textInterest, textInterest.get_rect(center=(debtX - 79, debtY + 92.5)))
        self.atm.blit(textInterestValue, textInterestValue.get_rect(center=(debtX + 70, debtY + 92.5)))
        self.atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 100)))

    def draw(self, screen):
        screen.blit(self.atm, (0, 0))
