#   Oct 12th, 2022, 10:37PM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh


# libraries and classes
import pygame
from neuralnet import *


# Width and Height of pygame window
WIDTH: float = 400
HEIGHT: float = 600


# Game windows initialization
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PlatformerGameML")


# fps of game loop
FPS = 60
clock = pygame.time.Clock()


# gameplay settings
population = 300
initialMoves = 300
copyBest = 15
mutationRate = 0.15
foodReward = 150

# Physics Settings
GRAVITY = 0.5
FRICTION:pygame.Vector2 = pygame.Vector2(0.1, 0.02)
JUMPIMPLUSE = 15
BOUNCE = 0





# colors used in game
BGCOLOR = (100,100,100)
PLATFORMCOLOR = (50,200,80)
WHITECOLOR = (255,255,255)


# text writer intialization
pygame.font.init()
writer = pygame.font.SysFont("Roboto", 20)
writer_small = pygame.font.SysFont("Roboto", 10)


# Ball Sprites Group
balls = pygame.sprite.Group()


# State variables
genNumber = 1
nets: list[NeuralNet] = []
fitness = [0]*population
dead = [False] * population