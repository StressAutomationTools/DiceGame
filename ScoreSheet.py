import pygame

pygame.init()
cellfont = pygame.font.SysFont('Arial', 12)
pygame.display.set_caption('Yahtzee')
smallGap = 5
largeGap = 10
games = 6
cellWidth = 30
cellHeight = 16
mainWindowSize = windowWidth, windowHeight = 90 + games * cellWidth + 5, 20*16 + 7*smallGap + largeGap

white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode(mainWindowSize)
screen.fill(white)
topLabels = ("Ones", "Twos", "Threes", "Fours", "Fifes", "Sixes")
topSums = ("Total", "Bonus", "Total Top")
bottomLabels = ("Three of a kind", "Four of a kind", "Full House", "Small straight", "Large straight", "Yahtzee", "Chance")
bottomSums = ("Total Bottom", "Final Total")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #text and grid
    screen.blit(cellfont.render('Column State', True, black, white), [5, 5+1])
    pygame.draw.line(screen, black, (smallGap, 5), (windowWidth - 5,5), 1)
    pygame.draw.line(screen, black, (smallGap, 5+cellHeight), (windowWidth - 5,5+cellHeight), 1)
    for m in range(0, games+1):
        pygame.draw.line(screen, black, (90+m * cellWidth, 5), (90+m * cellWidth,cellHeight*(19)+smallGap*2+largeGap+3), 1)
    #top
    for n in range(0, 6):
        screen.blit(cellfont.render(topLabels[n], True, black, white), [5, cellHeight*(n+1)+smallGap*2+1])
        pygame.draw.line(screen, black, (smallGap, cellHeight*(n+1)+smallGap*2), (windowWidth - 5,cellHeight*(n+1)+smallGap*2), 1)
    pygame.draw.line(screen, black, (smallGap, cellHeight*(6+1)+smallGap*2), (windowWidth - 5,cellHeight*(6+1)+smallGap*2), 2)
    for n in range(0, 3):
        screen.blit(cellfont.render(topSums[n], True, black, white), [5, cellHeight*(n+7)+smallGap*2+3])
        pygame.draw.line(screen, black, (smallGap, cellHeight*(n+8)+smallGap*2+2), (windowWidth - 5,cellHeight*(n+8)+smallGap*2+2), 1)
    pygame.draw.line(screen, black, (smallGap, cellHeight*(3+7)+smallGap*2+largeGap), (windowWidth - 5,cellHeight*(3+7)+smallGap*2+largeGap), 3)
    #bottom
    for n in range(0, 7):
        screen.blit(cellfont.render(bottomLabels[n], True, black, white), [5, cellHeight*(n+10)+smallGap*3+largeGap])
        pygame.draw.line(screen, black, (smallGap, cellHeight*(n+11)+smallGap*2+largeGap+2), (windowWidth - 5,cellHeight*(n+11)+smallGap*2+largeGap+2), 1)
    pygame.draw.line(screen, black, (smallGap, cellHeight*(6+11)+smallGap*2+largeGap+2), (windowWidth - 5,cellHeight*(6+11)+smallGap*2+largeGap+2), 2)
    for n in range(0, 2):
        screen.blit(cellfont.render(bottomSums[n], True, black, white), [5, cellHeight*(n+17)+smallGap*2+largeGap+4])
        pygame.draw.line(screen, black, (smallGap, cellHeight*(n+18)+smallGap*2+largeGap+3), (windowWidth - 5,cellHeight*(n+18)+smallGap*2+largeGap+3), 1)
    screen.blit(cellfont.render("Overall Total", True, black, white), [5, cellHeight*(n+17)+smallGap*5+largeGap*3])

    

    pygame.display.flip()
