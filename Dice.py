import pygame, random, sys, time

pygame.init()

mainWindowSize = windowWidth, windowHeight = 900, 150

white = 255, 255, 255

screen = pygame.display.set_mode(mainWindowSize)

results = [0, 0, 0, 0, 0, 0] #first 5 for results, last for roll number
keep = [False, False, False, False, False] #if true don't reroll
n = 0
roll = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            n = 0
    
    if n < 5:
        result1 = random.randrange(1, 6, 1)
        die1 = pygame.image.load("./dice/die_face_"+str(result1)+".png")
        result2 = random.randrange(1, 6, 1)
        die2 = pygame.image.load("./dice/die_face_"+str(result2)+".png")
        result3 = random.randrange(1, 6, 1)
        die3 = pygame.image.load("./dice/die_face_"+str(result3)+".png")
        result4 = random.randrange(1, 6, 1)
        die4 = pygame.image.load("./dice/die_face_"+str(result4)+".png")
        result5 = random.randrange(1, 6, 1)
        die5 = pygame.image.load("./dice/die_face_"+str(result5)+".png")
        time.sleep(0.1)
        screen.fill(white)
        screen.blit(die1, [150, 0])
        screen.blit(die2, [300, 0])
        screen.blit(die3, [450, 0])
        screen.blit(die4, [600, 0])
        screen.blit(die5, [750, 0])
        pygame.display.flip()
        n = n + 1
    results = [result1, result2, result3, result4, result5, roll]



