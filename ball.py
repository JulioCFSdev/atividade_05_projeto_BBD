import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        # calling the parent class
        super().__init__()
        # ball velocity
        self.dx = 3
        self.dy = 3
        ball_width = 20
        ball_height = 20
        self.ball = pygame.Rect(500, 400, ball_width, ball_height)

    def draw_ball(self, color, display):
        pygame.draw.rect(display, color, self.ball)


    # ball movement function
    def move(self):
        self.ball.x += self.dx
        self.ball.y += self.dy