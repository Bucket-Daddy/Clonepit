#ATM script
import math
import pygame

pygame.init()
overallScale = 2
font = pygame.font.Font(None, size = 15 * overallScale)
font2 = pygame.font.Font(None, size = 8 * overallScale)
running = True
clock = pygame.time.Clock()
deltaTime = 0.1
pygame.display.set_caption('Clonepit Slots - ATM')
screen = pygame.display.set_mode((800, 600))
atm = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)

# importer billeder fra assets-mappen
coin = pygame.image.load('assets/coin.webp')
coin2 = pygame.image.load('assets/coin2.webp')
cloverSkull = pygame.image.load('assets/cloverSkull.png')
coin = pygame.transform.scale(coin, (coin.get_width() * 0.075 * overallScale, coin.get_height() * 0.075 * overallScale))
coin2 = pygame.transform.scale(coin2, (coin2.get_width() * 0.0395 * overallScale, coin2.get_height() * 0.0395 * overallScale))
cloverSkull = pygame.transform.scale(cloverSkull, (cloverSkull.get_width() * 0.3 * overallScale, cloverSkull.get_height() * 0.3 * overallScale))

# importere variabler
debtNum = 1
roundNum = 1
debtAmount = 75
depositedAmount = 30
interest = 7.00

# texten med deadline placeres
deadlineX = 300  
deadlineY = 100

textDeadline = font.render('DEADLINE: ' + '#' + str(debtNum), True, (246, 250, 10))
atm.blit(textDeadline, textDeadline.get_rect(center=(deadlineX, deadlineY)))

# Runder tilbage før man dør osv.
debtX = deadlineX - 40
debtY = deadlineY + 100

textRoundsLeft = font.render(str(roundNum) + ' ROUNDS LEFT', True, (246, 250, 10))
textDebt = font2.render('DEBT:', True, (246, 250, 10))
textDeposited = font2.render('DEPOSITED:', True, (246, 250, 10))
textInterest = font2.render('INTEREST:', True, (246, 250, 10))
textInterestValue = font2.render(str(interest) + '% ', True, (246, 250, 10))
textScreenLine = font.render('-------------------------------', True, (246, 250, 10))

# Blit teksten og mønterne på ATM-overfladen
atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY - 30)))

atm.blit(cloverSkull, (debtX - 108, debtY - 25))
atm.blit(textRoundsLeft, textRoundsLeft.get_rect(center=(debtX, debtY- 10)))
atm.blit(cloverSkull, (debtX + 80, debtY - 25))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 10)))
atm.blit(textDebt, textDebt.get_rect(center=(debtX - 92, debtY + 20)))
atm.blit(coin, (debtX + 88, debtY + 20))

if math.log10(debtAmount) >= 10 and math.log10(debtAmount) < 100:
    deposit = round(debtAmount * 10**(-1 * (len(str(debtAmount)) - 1)), 2)
    textDebtAmount = font.render(str(deposit) + 'E+' + str(len(str(debtAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 45, debtY + 35)))
if math.log10(debtAmount) >= 100:
    deposit = round(debtAmount * 10**(-1 * (len(str(debtAmount)) - 1)), 2)
    textDebtAmount = font.render(str(deposit) + 'E+' + str(len(str(debtAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 40, debtY + 35)))
if math.log10(debtAmount) < 10:
    textDebtAmount = font.render(str(debtAmount), True, (246, 250, 10))
    atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 75 - len(str(debtAmount))**(1.50 - 0.012 * len(str(debtAmount))), debtY + 35)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 55)))
atm.blit(textDeposited, textDeposited.get_rect(center=(debtX - 75, debtY + 65)))
atm.blit(coin, (debtX + 88, debtY + 65))

if math.log10(depositedAmount) >= 10 and math.log10(depositedAmount) < 100:
    deposit = round(depositedAmount * 10**(-1 * (len(str(depositedAmount)) - 1)), 2)
    textDepositedAmount = font.render(str(deposit) + 'E+' + str(len(str(depositedAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 45, debtY + 82)))
if math.log10(depositedAmount) >= 100:
    deposit = round(depositedAmount * 10**(-1 * (len(str(depositedAmount)) - 1)), 2)
    textDepositedAmount = font.render(str(deposit) + 'E+' + str(len(str(depositedAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 40, debtY + 82)))
if math.log10(depositedAmount) < 10:
    textDepositedAmount = font.render(str(depositedAmount), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 73, debtY + 82)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 100)))
atm.blit(textInterest, textInterest.get_rect(center=(debtX - 79, debtY + 110)))
atm.blit(textInterestValue, textInterestValue.get_rect(center=(debtX + 96, debtY + 110)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 120)))
    

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

