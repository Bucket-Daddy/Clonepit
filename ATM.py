#ATM script
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

# pictures
coin = pygame.image.load('assets/coin.webp')
coin2 = pygame.image.load('assets/coin2.webp')
coin = pygame.transform.scale(coin, (coin.get_width() * 0.075 * overallScale, coin.get_height() * 0.075 * overallScale))
coin2 = pygame.transform.scale(coin2, (coin2.get_width() * 0.0395 * overallScale, coin2.get_height() * 0.0395 * overallScale))

# variables
debtNum = 1
roundNum = 1
debtAmount = 75
depositedAmount = 30
interest = 7.0

# deadline
deadlineX = 300  
deadlineY = 100

textDeadline = font.render('DEADLINE: ' + '#' + str(debtNum), True, (246, 250, 10))
atm.blit(textDeadline, textDeadline.get_rect(center=(deadlineX, deadlineY)))

# Rounds left and debt and so on
debtX = deadlineX - 40
debtY = deadlineY + 100

textRoundsLeft = font.render(str(roundNum) + ' ROUNDS LEFT', True, (246, 250, 10))
textDebt = font2.render('DEBT:', True, (246, 250, 10))
textDebtAmount = font.render(str(debtAmount), True, (246, 250, 10))
textDeposited = font2.render('DEPOSITED:', True, (246, 250, 10))
textDepositedAmount = font.render(str(depositedAmount), True, (246, 250, 10))
textInterest = font2.render('INTEREST:', True, (246, 250, 10))
textInterestValue = font2.render(str(interest) + '% ' + '(' + str(interest * depositedAmount / 100) + '    )', True, (246, 250, 10))
textScreenLine = font.render('-----------------------', True, (246, 250, 10))

# Blit teksten og mønterne på ATM-overfladen
atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY - 20)))

atm.blit(textRoundsLeft, textRoundsLeft.get_rect(center=(debtX, debtY)))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 20)))

atm.blit(textDebt, textRoundsLeft.get_rect(center=(debtX, debtY + 35)))
atm.blit(textDebtAmount, textDebtAmount.get_rect(center=(debtX + 45, debtY + 40)))
atm.blit(coin, (debtX + 60, debtY + 26))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 60)))

atm.blit(textDeposited, textDeposited.get_rect(center=(debtX - 45, debtY + 70)))
if len(str(depositedAmount)) >= 10:
    deposit = round(depositedAmount * 10**(-1 * (len(str(depositedAmount)) - 1)), 2)
    textDepositedAmount = font.render(str(deposit) + 'E+' + str(len(str(depositedAmount)) - 1), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 50, debtY + 82)))
    atm.blit(coin, (debtX + textDepositedAmount.get_width() + 45, debtY + 65))
else:
    textDepositedAmount = font.render(str(depositedAmount), True, (246, 250, 10))
    atm.blit(textDepositedAmount, textDepositedAmount.get_rect(center=(debtX + 50, debtY + 82)))
    atm.blit(coin, (debtX + textDepositedAmount.get_width() + 45, debtY + 65))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 100)))

atm.blit(textInterest, textInterest.get_rect(center=(debtX - 50, debtY + 110)))
atm.blit(textInterestValue, textInterestValue.get_rect(center=(debtX + 50, debtY + 110)))
atm.blit(coin2, (debtX + 65, debtY + 101))

atm.blit(textScreenLine, textScreenLine.get_rect(center=(debtX, debtY + 120)))

    
# updateDebtAndDeposited()
    

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

