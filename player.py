import pygame
from pygame.locals import *

# player paddle's color
PINK = '#9957CD'

# player class
class Player():
    def __init__(self):
        self.height = 20
        self.width = 110
        self.x = 390
        self.y = 650
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

    def move(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 1
        if self.rect.right >= 800:
            self.rect.right = 800

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

# create player
player_1 = Player()

clock = pygame.time.Clock()
fps = 60
