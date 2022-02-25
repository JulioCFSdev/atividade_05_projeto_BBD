import pygame


def create_ball():
    return pygame.Rect(500, 400, 20, 20)


def draw_ball(screen, color, ball):
    pygame.draw.ellipse(screen, color, ball)


def move_ball(ball):
    ball_dx = 1
    ball_dy = 1
    ball.x += ball_dx
    ball.y += ball_dy