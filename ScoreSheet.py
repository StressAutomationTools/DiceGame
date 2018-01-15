import pygame
import sys

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
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print pos
            r = 0
            c = 0
            if pos[0] > 90 and pos[0] < 120:
                c = 1
            elif pos[0] > 120 and pos[0] < 150:
                c = 2
            elif pos[0] > 150 and pos[0] < 180:
                c = 3
            elif pos[0] > 180 and pos[0] < 210:
                c = 4
            elif pos[0] > 210 and pos[0] < 240:
                c = 5
            elif pos[0] > 240 and pos[0] < 270:
                c = 6
            if pos[1] > 27 and pos[1] < 43:
                r = 1
            elif pos[1] > 43 and pos[1] < 59:
                r = 2
            elif pos[1] > 59 and pos[1] < 75:
                r = 3
            elif pos[1] > 75 and pos[1] < 91:
                r = 4
            elif pos[1] > 91 and pos[1] < 107:
                r = 5
            elif pos[1] > 107 and pos[1] < 123:
                r = 6
            elif pos[1] > 182 and pos[1] < 198:
                r = 7
            elif pos[1] > 198 and pos[1] < 214:
                r = 8
            elif pos[1] > 214 and pos[1] < 230:
                r = 9
            elif pos[1] > 230 and pos[1] < 246:
                r = 10
            elif pos[1] > 246 and pos[1] < 262:
                r = 11
            elif pos[1] > 262 and pos[1] < 278:
                r = 12
            elif pos[1] > 278 and pos[1] < 294:
                r = 13
            print "r "+str(r)
            print "c "+str(c)
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
