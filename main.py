# Oct 13th, 2022, 1:47AM Thursday.
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

from myPlatform import Platform
from settings import *
from ball import *
from random import randint
from copy import deepcopy

for i in range(population):
    balls.add(Ball(index=i))
    nets.append(NeuralNet(5, 8, 8, 2))


def drawLabels():

    genText = writer.render("Generation "+str(genNumber), True, (255,255,255))  #   Generation Number Label
    aliveText = writer.render("Alive: " + str(sum(map(lambda x : x ==False, dead))), True, (255,255,255))   #   number of birds alive Label
    bestFitness = writer.render("Best Fitness: " + str(max(fitness)), True, (255,255,255))  #   Fitness of best performing Model

    #   Drawing the labels on the screen
    WINDOW.blit(bestFitness, (10,50))
    WINDOW.blit(aliveText, (10,30))
    WINDOW.blit(genText, (10,10))

while True: 

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ball.acc.x = 0
            if event.key == pygame.K_LEFT:
                ball.acc.x = 0

    # keyDownEvents = pygame.key.get_pressed()

    # if keyDownEvents[pygame.K_UP]:
    #     ball.jump()
    # if keyDownEvents[pygame.K_RIGHT]:
    #     ball.acc.x = 1
    # if keyDownEvents[pygame.K_LEFT]:
    #     ball.acc.x = -1

    for ball in balls.sprites():
        closest = list(filter(lambda x : x.rect.top < ball.pos.y,ball.platforms.sprites()))[0]
        inputs = [[ball.pos.x, ball.pos.y, ball.inAir, closest.rect.left, closest.rect.right]]

        decision = nets[ball.index].forward(inputs)
        
        print(decision.T[0])
        if (decision.T[0][0] > 0.5): ball.jump()
        if (decision.T[0][1] < 0.5): ball.acc.x = -1
        elif (decision.T[0][1] > 0.5): ball.acc.x = 1
        elif (decision.T[0][1] == 0.5): ball.acc.x = 0


    # Game loop
    WINDOW.fill(BGCOLOR)
    balls.update()
    drawLabels()
    pygame.display.update()
    clock.tick(FPS)