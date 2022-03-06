import config
import pygame
from pygame.locals import *
from brick import powerups, power_up_sprites
conf = config.Config()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 340
        self.y = 570
        self.sprites_1 = []
        self.sprites_2 = []
        self.sprites_3 = []
        self.sprites_1.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.sprites_2.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.sprites_3.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.sprites_2.append(pygame.image.load('Player_sprite/l0_sprite_2.png'))
        self.sprites_3.append(pygame.image.load('Player_sprite/l0_sprite_3.png'))
        self.actual = 0
        self.image = self.sprites_1[self.actual]
        self.image = pygame.transform.scale(self.image, (32*5, 32*5))
        self.speed = 10
        self.direction = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
            self.actual = self.actual + 0.05
            if self.actual >= len(self.sprites_1):
                self.actual = 0
            self.image = self.sprites_1[int(self.actual)]
            self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))

    def move(self):
            self.direction = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = -1
                self.actual = self.actual + 1
                if self.actual >= len(self.sprites_3):
                    self.actual = 0
                self.image = self.sprites_3[int(self.actual)]
                self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))

            if key[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.direction = 1
                if self.rect.right >= 1000:
                    self.rect.right = 1000
                self.actual = self.actual + 1
                if self.actual >= len(self.sprites_2):
                    self.actual = 0
                self.image = self.sprites_2[int(self.actual)]
                self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))


all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)


def player_power_up_collision(player1):
    for powerup in powerups:
        if pygame.sprite.collide_mask(powerup, player1):
            power_up_sprites.remove(powerup)
