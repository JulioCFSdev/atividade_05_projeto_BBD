import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # ball size
        self.width = 20
        self.height = 20
        self.dx = 1
        self.dy = 1
        # image surface and rectangle
        self.ball = pygame.Rect(500, 400, 20, 20)
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

    def draw_ball(self, color, screen):
        pygame.draw.rect(screen, color, self.ball)

    # ball movement function
    def move_ball(self):
        self.ball.x += self.dx
        self.ball.y += self.dy