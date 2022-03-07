import pygame
import config

conf = config.Config()

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.laser = []
        self.laser.append(pygame.image.load('Powerup_sprites/sprite_shoot.png'))
        self.image = self.laser[0]
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center = pos)
        self.speed = 8

    def update(self): 
        self.rect.y -= self.speed