import pygame


def create_ball():
    return pygame.Rect(500, 400, 20, 20)


def draw_ball(screen, color, ball):
    pygame.draw.rect(screen, color, ball)


def move_ball(ball, ball_dx, ball_dy):
    ball.x += ball_dx
    ball.y += ball_dy


def ball_velocity(ball_dx, ball_dy):
    return [ball_dx, ball_dy]


# left wall collision
def left_wall_collision(ball):
    if ball.x < 6:
        return -1
    else:
        return 1


# right wall collision
def right_wall_collision(ball):
    if ball.x + 20 + 6 > 1000:
        return -1
    else:
        return 1


# lower wall collision
def lower_wall_collision(ball):
    if ball.y + 20 > 800:
        ball.x = 500
        ball.y = 400
        return -1
    else:
        return 1


# upper wall collision
def upper_wall_collision(ball):
    if ball.y < 58:
        return -1
    else:
        return 1


def paddler_collision(ball, paddler):
    if paddler.rect.x < ball.x < paddler.rect.x + 110 and paddler.rect.y < ball.y + 20 < paddler.rect.y + 10:
        return -1
    else:
        return 1
