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
        self.acc = pygame.Vector2(0, 0)

        self.rect:pygame.rect.Rect = pygame.rect.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
    
    def draw(self):
        pygame.gfxdraw.aacircle(WINDOW, int(self.pos.x), int(self.pos.y), self.radius, WHITECOLOR)
        pygame.gfxdraw.filled_circle(WINDOW, int(self.pos.x), int(self.pos.y), self.radius, WHITECOLOR)

    
    def update(self):

        self.loop()

        self.vel += self.acc
        self.pos += self.vel
        self.vel.x -= self.vel.x * FRICTION.x
        self.vel.y -= self.vel.y * FRICTION.y


        self.rect = pygame.rect.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
        self.draw()

    def jump(self):
        self.vel.y = -JUMPIMPLUSE
    
    def loop(self):

        if self.rect.right < 0:
            self.pos.x = WIDTH+self.radius
        elif self.rect.left > WIDTH:
            self.pos.x = -self.radius

