import pygame
from settings import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, *groups, x: float, y: float, width: float, height: float) -> None:
        super().__init__(*groups)
        self.pos = pygame.Vector2(x, y)
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(self.pos.x-(self.width/2), self.pos.y-(self.height/2), self.width, self.height)

    def draw(self):
        pygame.draw.rect(WINDOW, PLATFORMCOLOR, self.rect)

    def update(self):
        self.draw()            