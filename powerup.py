import pygame
import random


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, coordx, coordy):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.power = random.randint(0, len(self.sprites))
        self.x = coordx
        self.y = coordy
        self.actual = 0
        self.image = self.sprites[self.actual]
        self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))
        self.rect = self.image.get_rect()
        self.speed_y = 3

    def update(self):
        self.actual += 0.05
        if self.actual >= len(self.sprites):
            self.actual = 0
        self.image = self.sprites[int(self.actual)]
        self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))

    def move(self):
        while True:
            self.rect.y += self.speed_y



