import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        # color
        self.color = (255, 255, 255)
        # ball size
        self.width = 20
        self.height = 20
        # ball velocity
        self.dx = 1
        self.dy = 1
        # image surface and rectangle
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    # ball movement function
    def ball_move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
