import config
import pygame
from brick import powerups, power_up_sprites
from laser import Laser

conf1 = config.Config()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 340
        self.y = 570
        self.sprites_1 = []
        self.sprites_2 = []
        self.sprites_3 = []
        self.sprites_1.append(
            pygame.image.load("Player_sprite/l0_sprite_1.png")
        )
        self.sprites_2.append(
            pygame.image.load("Player_sprite/l0_sprite_1.png")
        )
        self.sprites_3.append(
            pygame.image.load("Player_sprite/l0_sprite_1.png")
        )
        self.sprites_2.append(
            pygame.image.load("Player_sprite/l0_sprite_2.png")
        )
        self.sprites_3.append(
            pygame.image.load("Player_sprite/l0_sprite_3.png")
        )
        self.actual = 0
        self.image = self.sprites_1[self.actual]
        self.image = pygame.transform.scale(
            self.image, (conf1.player_width, 32 * 5)
        )
        self.speed = 10
        self.direction = 0

        self.lasers = pygame.sprite.Group()

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        self.actual = self.actual + 0.05
        if self.actual >= len(self.sprites_1):
            self.actual = 0
        self.image = self.sprites_1[int(self.actual)]
        self.image = pygame.transform.scale(
            self.image, (conf1.player_width, 32 * 5)
        )

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
            self.image = pygame.transform.scale(
                self.image, (conf1.player_width, 32 * 5)
            )
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 1
            if self.rect.right >= 1000:
                self.rect.right = 1000
            self.actual = self.actual + 1
            if self.actual >= len(self.sprites_2):
                self.actual = 0
            self.image = self.sprites_2[int(self.actual)]
            self.image = pygame.transform.scale(
                self.image, (conf1.player_width, 32 * 5)
            )
        elif key[pygame.K_SPACE] and conf1.power_shot:
            self.lasers.add(Laser(player.rect.center))
            pygame.time.wait(1)


all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)


def player_power_up_collision(player1, stage_clear):
    # Reset power-ups
    if stage_clear:
        conf1.power_growth = False
        conf1.power_gyro = False
        conf1.power_mult = False
        conf1.power_ultra = False
        conf1.extra_life = False
        conf1.power_small = False
        conf1.power_shot = False
    for powerup in powerups:
        if pygame.sprite.collide_mask(powerup, player1):
            power_up_sprites.remove(powerup)
            if powerup.power == 0 and conf1.power_growth is False:
                conf1.power_growth = True
                conf1.player_width *= 1.2
            if powerup.power == 1 and conf1.power_gyro is False:
                conf1.power_gyro = True
            if powerup.power == 2 and conf1.power_ultra is False:
                conf1.power_ultra = True
            if powerup.power == 3:
                conf1.power_mult = True
            if powerup.power == 4:
                conf1.extra_life = True
            if powerup.power == 5 and conf1.power_small is False:
                conf1.power_small = True
                conf1.player_width /= 1.2
            if powerup.power == 6 and conf1.power_shot is False:
                conf1.power_shot = True


def power_up_on():
    return [
        conf1.power_growth,
        conf1.power_gyro,
        conf1.power_ultra,
        conf1.power_mult,
        conf1.extra_life,
        conf1.power_small,
        conf1.power_shot,
    ]
