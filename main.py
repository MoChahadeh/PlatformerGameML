# Oct 13th, 2022, 1:47AM Thursday.
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

import math
from settings import *
from ball import *
from random import randint
from copy import deepcopy

for i in range(population):
    balls.add(Ball(index=i))
    nets.append(NeuralNet(11, 18, 12, 2))


timelapse = False
ticks = -1


def drawLabels():

    genText = writer.render("Generation "+str(genNumber), True, (255,255,255))  #   Generation Number Label
    aliveText = writer.render("Alive: " + str(sum(map(lambda x : x ==False, dead))), True, (255,255,255))   #   number of birds alive Label
    bestFitness = writer.render("Best Fitness: " + str(max(fitness)), True, (255,255,255))  #   Fitness of best performing Model

    watermark = writer_small.render("©2023 MoChahadeh", True, (255,255,255))  #   Fitness of best performing Model


    #   Drawing the labels on the screen
    WINDOW.blit(watermark, (10,HEIGHT-30))
    WINDOW.blit(bestFitness, (10,50))
    WINDOW.blit(aliveText, (10,30))
    WINDOW.blit(genText, (10,10))

def restartAndMutate():
    global genNumber
    genNumber += 1  #   incrementing Generation Number
    maximums = np.flip(np.argsort(fitness)) #   sorts the indices of the fitnesses highest to lowest, which are the same indices for the corresponding neural nets
    fitness.clear() # resets the fitness list
    dead.clear()    # resets the dead list

    #   resetting the sprite groups:
    for ball in balls: ball.kill()

    #   re-assigns new values to the state variables
    for i in range(population):
        fitness.append(0)
        balls.add(Ball(index = i))
        dead.append(False)

        # Copies one of the best performing neurons and appends it the list of neurons
        nets[i] = deepcopy(nets[maximums[i%copyBest]])
        # Mutates the newly assigned neural net by a random rate between -+mutationRate defined in settings.py
        nets[i].mutate(mutationRate + (mutationRate * i%2))



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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                timelapse = not timelapse
            if event.key == pygame.K_SPACE:
                print(fitness)
                restartAndMutate()

    # keyDownEvents = pygame.key.get_pressed()

    # if keyDownEvents[pygame.K_UP]:
    #     ball.jump()
    # if keyDownEvents[pygame.K_RIGHT]:
    #     ball.acc.x = 1
    # if keyDownEvents[pygame.K_LEFT]:
    #     ball.acc.x = -1

    for ball in balls.sprites():

        if not ball.dead:                

            inputs = [[ball.inAir, ball.closestAbove.rect.centerx- ball.pos.x, ball.closestAbove.rect.centery-ball.pos.y, ball.closest.rect.centerx-ball.pos.y, ball.closest.rect.centery-ball.pos.y, ball.vel.x, ball.vel.y, ball.lowestAbove.rect.centerx-ball.pos.x, ball.lowestAbove.rect.centery-ball.pos.y, ball.highestBelow.rect.centerx-ball.pos.x, ball.highestBelow.rect.centery-ball.pos.y]]

            decision = nets[ball.index].forward(inputs)
            if (decision.T[0][0] >= 0.5): ball.jump()
            if (decision.T[0][1] < 0.5): ball.acc.x = -1
            elif (decision.T[0][1] > 0.5): ball.acc.x = 1
            elif (decision.T[0][1] == 0.5): ball.acc.x = 0

        else: 
            dead[ball.index] = True

    if (all(d == True for d in dead)):
        print(fitness)
        restartAndMutate()

    # Game loop
    WINDOW.fill(BGCOLOR)
    balls.update()
    ticks += 1
    if(not timelapse):
        balls.sprites()[np.flip(np.argsort(fitness))[0]].draw()
        drawLabels()        # draws the labels onto the screen in each frame
        pygame.display.update()     # updates the pygame window to show the new drawings on the screen
        clock.tick(FPS)     # sets the frame rate of the loop
    elif(ticks % 20 == 0):
        balls.sprites()[np.flip(np.argsort(fitness))[0]].draw()
        drawLabels()        # draws the labels onto the screen in each frame
        pygame.display.update()     # updates the pygame window to show the new drawings on the screen
