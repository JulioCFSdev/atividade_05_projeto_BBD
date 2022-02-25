import pygame

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