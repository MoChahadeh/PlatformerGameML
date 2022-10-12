from matplotlib import backend_bases
import pygame
from settings import *
from ball import *

ball = Ball(index = 0)

while True: 

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.jump()
            if event.key == pygame.K_RIGHT:
                ball.acc.x = 1
            if event.key == pygame.K_LEFT:
                ball.acc.x = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ball.acc.x = 0
            if event.key == pygame.K_LEFT:
                ball.acc.x = 0

    # Game loop
    WINDOW.fill(BGCOLOR)
    ball.update()
    pygame.display.update()
    clock.tick(FPS)