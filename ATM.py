#ATM script
import math
import pygame

pygame.init()
overallScale = 2

font = pygame.font.Font(None, size = 15 * overallScale)
font2 = pygame.font.Font(None, size = 13 * overallScale)
font3 = pygame.font.Font(None, size = 8 * overallScale)
running = True
clock = pygame.time.Clock()
deltaTime = 0.1
pygame.display.set_caption('Clonepit Slots - ATM')
screen = pygame.display.set_mode((1000, 750))
atm = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)

# importer billeder fra assets-mappen
atmBackground = pygame.image.load('assets/Atm.png')
coin = pygame.image.load('assets/coin.webp')
cloverSkull = pygame.image.load('assets/cloverSkull.png')
atmBackground = pygame.transform.scale(atmBackground, (atmBackground.get_width() * 0.67 * overallScale, atmBackground.get_height() * 0.67 * overallScale))
atmBackground.set_colorkey((163, 73, 164))
coin = pygame.transform.scale(coin, (coin.get_width() * 0.065 * overallScale, coin.get_height() * 0.065 * overallScale))
cloverSkull = pygame.transform.scale(cloverSkull, (cloverSkull.get_width() * 0.22 * overallScale, cloverSkull.get_height() * 0.22 * overallScale))

# importere variabler
debtNum = 1
roundNum = 1
debtAmount = 75
depositedAmount = 30
interest = 7.00

# Blit atm baggrunden på overfladen
atm.blit(atmBackground, (0, 0))

# texten med deadline placeres
deadlineX = 275
deadlineY = 50

textDeadline = font.render('DEADLINE: ' + '#' + str(debtNum), True, (246, 250, 10))
atm.blit(textDeadline, textDeadline.get_rect(center=(deadlineX, deadlineY)))

# Runder tilbage før man dør osv.
debtX = deadlineX - 80
debtY = deadlineY + 235

textRoundsLeft = font2.render(str(roundNum) + ' ROUNDS LEFT', True, (246, 250, 10))
textDebt = font3.render('DEBT:', True, (246, 250, 10))
textDeposited = font3.render('DEPOSITED:', True, (246, 250, 10))
textInterest = font3.render('INTEREST:', True, (246, 250, 10))
textInterestValue = font3.render(str(interest) + '% ', True, (246, 250, 10))
textScreenLine = font3.render('-------------------------------------------------', True, (246, 250, 10))

# Blit teksten og mønterne på ATM-overfladen
atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY - 20)))

atm.blit(cloverSkull, (debtX - 102, debtY - 18))
atm.blit(textRoundsLeft, textRoundsLeft.get_rect(center=(debtX - 10, debtY - 6)))
atm.blit(cloverSkull, (debtX + 60, debtY - 18))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 6)))
atm.blit(textDebt, textDebt.get_rect(center=(debtX - 92, debtY + 16)))
atm.blit(coin, (debtX + 68, debtY + 18))

if math.log10(debtAmount) >= 7 and math.log10(debtAmount) < 100:
    deposit = round(debtAmount * 10**(-1 * (len(str(debtAmount)) - 1)), 2)
    textDebtAmount = font2.render(str(deposit) + 'E+' + str(len(str(debtAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 35, debtY + 30)))
if math.log10(debtAmount) >= 100:
    deposit = round(debtAmount * 10**(-1 * (len(str(debtAmount)) - 1)), 2)
    textDebtAmount = font2.render(str(deposit) + 'E+' + str(len(str(debtAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 30, debtY + 30)))
if math.log10(debtAmount) < 7:
    textDebtAmount = font2.render(str(debtAmount), True, (246, 250, 10))
    atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 50 - math.log10(debtAmount)**(1.50 - 0.012 * math.log10(debtAmount)), debtY + 30)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 45)))
atm.blit(textDeposited, textDeposited.get_rect(center=(debtX - 75, debtY + 55)))
atm.blit(coin, (debtX + 68, debtY + 55))

if math.log10(depositedAmount) >= 6 and math.log10(depositedAmount) < 100:
    deposit = round(depositedAmount * 10**(-1 * (len(str(depositedAmount)) - 1)), 2)
    textDepositedAmount = font2.render(str(deposit) + 'E+' + str(len(str(depositedAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 30, debtY + 70)))
if math.log10(depositedAmount) >= 100:
    deposit = round(depositedAmount * 10**(-1 * (len(str(depositedAmount)) - 1)), 2)
    textDepositedAmount = font2.render(str(deposit) + 'E+' + str(len(str(depositedAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 25, debtY + 70)))
if math.log10(depositedAmount) < 6:
    textDepositedAmount = font2.render(str(depositedAmount), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 50 - math.log10(depositedAmount)**(1.50 - 0.012 * math.log10(depositedAmount)), debtY + 70)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 82.5)))
atm.blit(textInterest, textInterest.get_rect(center=(debtX - 79, debtY + 92.5)))
atm.blit(textInterestValue, textInterestValue.get_rect(center=(debtX + 70, debtY + 92.5)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX - 10, debtY + 100)))


##############################################################################################################
# the window
while running:
    screen.fill((0, 0, 0))
    screen.blit(atm, (30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    deltaTime = max(0.001, min(0.1, deltaTime))


pygame.quit()

