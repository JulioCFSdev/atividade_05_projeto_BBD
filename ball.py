import pygame

<<<<<<< HEAD
def draw_ball(screen, white):
    # ball size
    ball_width = 20
    ball_height = 20
    ball_x = 500
    ball_y = 400
    # image surface and rectangle
    ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)
    pygame.draw.ellipse(screen, white, ball)
    trator = ball.x 

def move_ball(ball_x, ball_y, ball_dx, ball_dy):
    # ball movement function
    ball_x += ball_dx
    ball_y += ball_dy
=======

def create_ball():
    return pygame.Rect(500, 400, 20, 20)


def draw_ball(screen, color, ball):
    pygame.draw.rect(screen, color, ball)


def move_ball(ball):
    ball_dx = 1
    ball_dy = 1
    ball.x += ball_dx
    ball.y += ball_dy
>>>>>>> 077bb90c3893fc22d23b1c5e0d12e5801c3791be
