import pygame

pygame.init()
posterScale = 0.80
symbolScale = 2
font = pygame.font.Font(None, size = 30)
moneyMult = 1
lemonValue = 2
cherryValue = 2
cloverValue = 3
bellValue = 3
diamondValue = 5
treasureValue = 5
sevenValue = 7

pygame.display.set_caption('Clonepit Slots - Posters')
screen = pygame.display.set_mode((800, 600))

#Loader billeder
lemon = pygame.image.load('assets/SymbolLemon.webp')
cherry = pygame.image.load('assets/SymbolCherry.webp')
clover = pygame.image.load('assets/SymbolClover.webp')
bell = pygame.image.load('assets/SymbolBell.webp')
diamond = pygame.image.load('assets/SymbolDiamond.webp')
treasure = pygame.image.load('assets/SymbolTreasureChest.webp')
seven = pygame.image.load('assets/SymbolSeven.webp')
coin = pygame.image.load('assets/coin.webp')
dice = pygame.image.load('assets/D6.png')
posterBackground = pygame.image.load('assets/PosterBackground.png').convert()

#Skalerer billeder
lemon = pygame.transform.scale(lemon, (18 * symbolScale, 18 * symbolScale))
cherry = pygame.transform.scale(cherry, (18 * symbolScale, 18 * symbolScale))
clover = pygame.transform.scale(clover, (18 * symbolScale, 18 * symbolScale))
bell = pygame.transform.scale(bell, (18 * symbolScale, 18 * symbolScale))
diamond = pygame.transform.scale(diamond, (18 * symbolScale, 18 * symbolScale))
treasure = pygame.transform.scale(treasure, (18 * symbolScale, 18 * symbolScale))
seven = pygame.transform.scale(seven, (18 * symbolScale, 18 * symbolScale))
coin = pygame.transform.scale(coin, (138 * 0.15, 186 * 0.15))
dice = pygame.transform.scale(dice, (138 * 0.15, 186 * 0.15)).convert
posterBackground.set_colorkey((0, 0, 0))
posterBackground = pygame.transform.scale(posterBackground, (posterBackground.get_width() * posterScale, posterBackground.get_height() * posterScale))
posterBackground.set_colorkey((0, 0, 0))

# posters
posters = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
# Poster for symbol value
symbolPosterX = 0
symbolPosterY = 15
posters.blit(posterBackground, (symbolPosterX, symbolPosterY - 15))
    # text on poster
textSymbols = font.render('---     SYMBOLS     ---', True, (0, 0, 0))
textSymbolsMult = font.render('  SYMBOLS     MULTIPLIER ', True, (0, 0, 0))
SymbolsMult = font.render(' X ' + str(moneyMult), True, (0, 0, 0))
textLemonValue = font.render(': ' + str(lemonValue), True, (0, 0, 0))
textCherryValue = font.render(': ' + str(cherryValue), True, (0, 0, 0))
textCloverValue = font.render(': ' + str(cloverValue), True, (0, 0, 0))
textBellValue = font.render(': ' + str(bellValue), True, (0, 0, 0))
textDiamondValue = font.render(': ' + str(diamondValue), True, (0, 0, 0))
textTreasureValue = font.render(': ' + str(treasureValue), True, (0, 0, 0))
textSevenValue = font.render(': ' + str(sevenValue), True, (0, 0, 0))
posters.blit(textSymbols , textSymbols.get_rect(center=(posterBackground.get_width()/2, symbolPosterY + 30)))
posters.blit(textSymbolsMult , textSymbolsMult.get_rect(center=(posterBackground.get_width()/2, symbolPosterY + 18 * symbolScale + 305)))
posters.blit(SymbolsMult , SymbolsMult.get_rect(center=(symbolPosterX + 240, symbolPosterY + 370)))
posters.blit(textLemonValue , textLemonValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 53)))
posters.blit(textCherryValue , textCherryValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 93)))
posters.blit(textCloverValue , textCloverValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 133)))
posters.blit(textBellValue , textBellValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 173)))
posters.blit(textDiamondValue , textDiamondValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 213)))
posters.blit(textTreasureValue , textTreasureValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 258)))
posters.blit(textSevenValue , textSevenValue.get_rect(center=(symbolPosterX + 115, symbolPosterY + 300)))

    # Symbols on poster
posters.blit(lemon, (symbolPosterX + 25, symbolPosterY + 40))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 40))
posters.blit(cherry, (symbolPosterX + 25, symbolPosterY + 18 * symbolScale + 40))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 18 * symbolScale + 42))
posters.blit(clover, (symbolPosterX + 25, symbolPosterY + 18 * symbolScale + 80))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 18 * symbolScale + 82))
posters.blit(bell, (symbolPosterX + 25, symbolPosterY + 18 * symbolScale + 120))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 18 * symbolScale + 122))
posters.blit(diamond, (symbolPosterX + 25, symbolPosterY + 18 * symbolScale + 162.5))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 18 * symbolScale + 164.5))
posters.blit(treasure, (symbolPosterX + 25, symbolPosterY + 18 * symbolScale + 205))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 18 * symbolScale + 207))
posters.blit(seven, (symbolPosterX + 25, symbolPosterY + 18 * symbolScale + 247.5))
posters.blit(coin, (symbolPosterX + 75, symbolPosterY + 18 * symbolScale + 249.5))
posters.blit(coin, (symbolPosterX + 200, symbolPosterY + 355))

# - / symbols / -
# lemon / value / chance
# cherry / value / chance
# clover / value / chance
# bell / value / chance
# diamond / value / chance
# treasure / value / chance
# seven / value / chance
# symbols // multiplier
# /// money multiplier value

# Poster for pattern value
posters.blit(posterBackground, (360, 0))

running = True
clock = pygame.time.Clock()

deltaTime = 0.1

while running:
    screen.fill((0, 0, 0))
    screen.blit(posters, (30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    deltaTime = max(0.001, min(0.1, deltaTime))





pygame.quit()