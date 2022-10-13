# Oct 13th, 2022, 1:48AM Thursday.
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

import pygame.gfxdraw
import pygame
from random import randint
from settings import *
from myPlatform import Platform


class Ball(pygame.sprite.Sprite):

    def __init__(self, *groups, index: int) -> None:
        super().__init__(*groups)
        self.index = index
        self.radius = 10

        self.platforms = pygame.sprite.Group()

        for i in range(int(HEIGHT/60)):
            plat = Platform(group= self.platforms, x = randint(50, WIDTH-50),y= HEIGHT - i*60,width= 100,height= 10)
            self.platforms.add(plat)

        self.pos = pygame.Vector2(WIDTH/2, HEIGHT/2)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, GRAVITY)
        self.inAir = True

        self.rect:pygame.rect.Rect = pygame.rect.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)
    
    def draw(self):
        # pygame.gfxdraw.aacircle(WINDOW, int(self.pos.x), int(self.pos.y), self.radius, WHITECOLOR)
        # pygame.gfxdraw.filled_circle(WINDOW, int(self.pos.x), int(self.pos.y), self.radius, WHITECOLOR)
        pygame.draw.circle(WINDOW, WHITECOLOR, (int(self.pos.x), int(self.pos.y)), self.radius)
    
    def update(self):

        self.loop()

        if self.inAir:
            self.vel.y += self.acc.y
            self.pos.y += self.vel.y
        if self.pos.y <= HEIGHT/3 and self.vel.y < 0:
            self.pos.y += -self.vel.y*2
            for plat in self.platforms:
                plat.pos.y -= self.vel.y*2
                plat.rect.y -= self.vel.y*2

        self.vel.x += self.acc.x
        self.pos.x += self.vel.x
        self.vel.x -= self.vel.x * FRICTION.x
        self.vel.y -= self.vel.y * FRICTION.y
        self.rect = pygame.rect.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)

        # self.inAir = True
        self.checkCollision()
        self.checkDeath()
        self.platforms.update()
        self.draw()

    def jump(self):
        if not self.inAir:
            self.inAir = True
            self.vel.y = -JUMPIMPLUSE
    
    def loop(self):

        if self.rect.right < 0:
            self.pos.x = WIDTH+self.radius
        elif self.rect.left > WIDTH:
            self.pos.x = -self.radius

    def checkDeath(self):

        if self.pos.y > HEIGHT + self.radius:
            self.pos = pygame.Vector2(WIDTH/2, HEIGHT/2)
            self.vel = pygame.Vector2(0, 0)
            self.acc = pygame.Vector2(0, GRAVITY)
            self.inAir = False
            net.mutate(0.15)
    
    def checkCollision(self):
        self.inAir = True 
        for plat in self.platforms.sprites():
            if(plat.rect.top <= self.rect.bottom and plat.rect.bottom >= self.rect.top and plat.rect.left < self.rect.right and plat.rect.right > self.rect.left and self.vel.y > 0):
                if(self.vel.y < 0.5):
                    self.vel.y = 0
                    self.pos.y = plat.rect.top - self.radius 
                    self.inAir = False
                else:
                    self.vel.y = -self.vel.y*BOUNCE

                break
                


