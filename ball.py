import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # color
        self.color = (255, 255, 255)
        # ball size
        self.width = 20
        self.height = 20
        # ball velocity
        self.dx = 1
        self.dy = 1
        # image surface and rectangle
        self.ball = pygame.Rect(500, 400, 20, 20)
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

    def draw_ball(self):
        pygame.draw.rect(self.image, self.color, self.ball)

    # ball movement function
    def move_ball(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
