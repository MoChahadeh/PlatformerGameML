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

    # Game loop
    WINDOW.fill(BGCOLOR)
    ball.update()
    pygame.display.update()
    clock.tick(FPS)