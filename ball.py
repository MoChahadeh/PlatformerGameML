import pygame.gfxdraw
import pygame
from settings import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, *groups, index: int) -> None:
        super().__init__(*groups)
        self.index = index
        self.radius = 10
        self.pos = pygame.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, GRAVITY)

        self.rect = pygame.rect.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
    
    def draw(self):
        # pygame.draw.rect(WINDOW, BALLCOLOR, pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height))
        pygame.gfxdraw.aacircle(WINDOW, int(self.pos.x), int(self.pos.y), self.radius, WHITECOLOR)
        pygame.gfxdraw.filled_circle(WINDOW, int(self.pos.x), int(self.pos.y), self.radius, WHITECOLOR)

    
    def update(self):

        self.vel = self.acc
        self.pos += self.vel
        self.pos.x -= self.pos.x * FRICTION


        self.rect = pygame.rect.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
        self.draw()
