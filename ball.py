from distutils.command.config import config
import pygame
from config import Config
conf = Config()


def create_ball():
    return pygame.Rect(conf.ball_x_init, conf.ball_y_init, conf.ball_width, conf.ball_heigth)


def draw_ball(screen, ball):
    pygame.draw.ellipse(screen, conf.white, ball)


def move_ball(ball, ball_dx, ball_dy):
    ball.x += ball_dx
    ball.y += ball_dy


def ball_velocity(ball_dx, ball_dy):
    return [ball_dx, ball_dy]


# left wall collision
def left_wall_collision(ball):
    if ball.x < conf.tresh_left_wall:
        return conf.reverse_speed
    else:
        return conf.normal_speed


# right wall collision
def right_wall_collision(ball):
    if ball.x + conf.tresh_right_wall > conf.screen_width:
        return conf.reverse_speed
    else:
        return conf.normal_speed


# lower wall collision
def lower_wall_collision(ball):
    if ball.y + conf.tresh_lower_wall > conf.screen_height:
        ball.x = conf.ball_x_init
        ball.y = conf.ball_y_init
        return conf.reverse_speed
    else:
        return conf.normal_speed


# upper wall collision
def upper_wall_collision(ball):
    if ball.y < conf.tresh_upper_wall:
        return conf.reverse_speed
    else:
        return conf.normal_speed


def paddler_collision(ball, velocity,paddler):
    # velocity A left
    if paddler.rect.x < ball.x < paddler.rect.x + 30 and paddler.rect.y < ball.y + conf.player_heigth < paddler.rect.y + conf.player_heigth/2:
        return [-5, -3]
    # velocitye A right
    elif paddler.rect.x + 80 < ball.x < paddler.rect.x + 110 and paddler.rect.y < ball.y + conf.player_heigth < paddler.rect.y + conf.player_heigth/2:
        return [5, -3]
    # velocity B left
    elif paddler.rect.x + 30 < ball.x < paddler.rect.x + 50 and paddler.rect.y < ball.y + conf.player_heigth < paddler.rect.y + conf.player_heigth/2:
        return [-3, -3]
    # velocity B left
    elif paddler.rect.x + 60 < ball.x < paddler.rect.x + 80 and paddler.rect.y < ball.y + conf.player_heigth < paddler.rect.y + conf.player_heigth/2:
        return [3, -3]
    # velocity C
    elif paddler.rect.x + 50 < ball.x < paddler.rect.x + 60 and paddler.rect.y < ball.y + conf.player_heigth < paddler.rect.y + conf.player_heigth/2:
        return [0, -3]
    # no collision
    else:
        return velocity

