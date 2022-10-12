import pygame
from settings import *

while True: 

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Game loop
    WINDOW.fill(BGCOLOR)
    pygame.display.update()
    clock.tick(FPS)