#   Oct 12th, 2022, 10:37PM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh


# libraries and classes
import pygame
from neuralnet import *


# Width and Height of pygame window
WIDTH = 300
HEIGHT = 600


# Game windows initialization
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PlatformerGameML")


# fps of game loop
FPS = 60
clock = pygame.time.Clock()


# gameplay settings
population = 300
initialMoves = 200
copyBest = 15
mutationRate = 0.12
foodReward = 150


# colors used in game
BGCOLOR = (100,100,100)
SNAKECOLOR = (50,200,80)
WHITECOLOR = (255,255,255)


# text writer intialization
pygame.font.init()
writer = pygame.font.SysFont("Roboto", 20)


# Snake Sprites Group
snakes = pygame.sprite.Group()


# State variables
genNumber = 1
nets: list[NeuralNet] = []
fitness = [0] * population
dead = [False] * population