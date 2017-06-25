import pygame, sys, time, die

pygame.init()
font = pygame.font.SysFont('Arial', 25)
pygame.display.set_caption('Yahtzee')

mainWindowSize = windowWidth, windowHeight = 170 + 150*5, 147+5

white = 255, 255, 255
grey = 205, 201, 201
black = 0, 0, 0
btnsize = 10, 10, 150, 50
screen = pygame.display.set_mode(mainWindowSize)
screen.fill(white)

#inicialize dice
dice = [die.die(), die.die(), die.die(), die.die(), die.die()]
roll = 1

for n in range(0, 5):
    dice[n].setLocation(170 + 150*n, 5)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
           x, y = event.pos
           #roll button click
           if (x < 140 and y < 60) and (x > 10 and y > 10):
            roll += 1
            if roll > 3:
                roll = 1
                for n in range(0, 5):
                    dice[n].setKeep(False)
            for n in range(0, 5):
                dice[n].roll()
           #dice click
           elif (x > 170 and x < 170 + 5*150) and y < 147:
                for n in range(0, 5):
                    if (x > 170 + n*150 and x < 170 + (n+1)*150):
                        if dice[n].getKeep() == False:
                            dice[n].setKeep(True)
                        else:
                            dice[n].setKeep(False)
    #update screen
    screen.fill(white)
    for n in range(0, 5):
        image = dice[n].getValue()
        die = pygame.image.load(image)
        screen.blit(die, dice[n].getLocation())
        if dice[n].getKeep() == True:
            pygame.draw.rect(screen, black, (170 + n*150, 5, 140, 137), 10)
    pygame.draw.rect(screen, grey, btnsize, 0)
    screen.blit(font.render('Roll ' + str(roll), True, black, grey), [50, 20])
    pygame.display.flip()
