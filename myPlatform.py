#Oct 13th, 2022, 1:47AM Thursday.
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

import pygame
from random import randint
from settings import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, *groups, group, x: float, y: float, width: float, height: float) -> None:
        super().__init__(*groups)
        self.pos = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.group = group
        self.rect = pygame.rect.Rect(self.pos.x-(self.width/2), self.pos.y-(self.height/2), self.width, self.height)

    def draw(self):
        pygame.draw.rect(WINDOW, PLATFORMCOLOR, self.rect)

    def update(self):
        self.checkDeath()
        self.draw()            
    
    def checkDeath(self):
        if self.rect.top > HEIGHT:
            fitness[0] += 1
            self.group.add(Platform(group= self.group,x = randint(50, WIDTH-50),y= randint(-60,-10),width= 100,height= 10))
            self.kill()