import pygame
import random
from config import Config


conf = Config()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, coordx, coordy):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("Powerup_big/sprite_big1.png"))
        self.sprites.append(
            pygame.image.load("Powerup_sprites/sprite_giroball1.png")
        )
        self.sprites.append(
            pygame.image.load("Powerup_sprites/sprite_ultraball.png")
        )
        self.sprites.append(
            pygame.image.load("Powerup_sprites/sprite_multiballs.png")
        )
        self.sprites.append(pygame.image.load("Powerup_life/sprite_life1.png"))
        self.sprites.append(
            pygame.image.load("Powerup_small/sprite_small1.png")
        )
        self.sprites.append(
            pygame.image.load("Powerup_sprites/sprite_shoot.png")
        )
        self.power = random.randint(0, 6)
        self.x = coordx
        self.y = coordy
        self.image = self.sprites[self.power]
        self.image = pygame.transform.scale(self.image, (32 * 2.5, 32 * 2.5))
        self.rect = self.image.get_rect()
        self.speed_y = 3
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def move(self):
        self.rect.y += self.speed_y
