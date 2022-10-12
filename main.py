# Oct 13th, 2022, 1:47AM Thursday.
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

from myPlatform import Platform
from settings import *
from ball import *

ball = Ball(index = 0)

plat1 = Platform(x = WIDTH/2, y = HEIGHT/2 + 100, width = 75, height = 10)
plat2 = Platform(x = WIDTH/3, y = HEIGHT/3 + 100, width = 75, height = 10)

platforms.add(plat1)
platforms.add(plat2)

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

    keyDownEvents = pygame.key.get_pressed()

    if keyDownEvents[pygame.K_UP]:
        ball.jump()
    if keyDownEvents[pygame.K_RIGHT]:
        ball.acc.x = 1
    if keyDownEvents[pygame.K_LEFT]:
        ball.acc.x = -1


    # Game loop
    WINDOW.fill(BGCOLOR)
    ball.update()
    platforms.update()
    pygame.display.update()
    clock.tick(FPS)