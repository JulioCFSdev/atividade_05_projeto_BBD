import pygame
import pygame.locals
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
def lower_wall_collision(ball, velocity, speedx, speedy):
    if ball.y + conf.tresh_lower_wall > conf.screen_height:
        ball.x = conf.ball_x_init
        ball.y = conf.ball_y_init
        conf.live_loss = True

        if velocity[0] > 0:
            return [-speedx, speedy]
        else:
            return [speedx, speedy]
    else:
        return velocity
def lower_wall_collision_mult(ball, velocity, speedx, speedy):
    if ball.y + conf.tresh_lower_wall > conf.screen_height:
        ball.x = 2000
        ball.y = 2000

        if velocity[0] > 0:
            return [0, 0]
        else:
            return [0, 0]
    else:
        return velocity


# upper wall collision
def upper_wall_collision(ball):
    if ball.y < conf.tresh_upper_wall:
        return conf.reverse_speed
    else:
        return conf.normal_speed


def paddler_collision(ball, velocity, paddler, speedx, speedy, power_growth):
    if power_growth[0]:
        # velocity A left
        if paddler.rect.x < ball.x < paddler.rect.x + 40*1.2 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [speedx - 2, -speedy]
        # velocity A right
        elif paddler.rect.x + 130*1.2 < ball.x < paddler.rect.x + 160*1.2 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [speedx + 2, -speedy]
        # velocity B left
        elif paddler.rect.x + 40*1.2 < ball.x < paddler.rect.x + 70*1.2 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [-speedx, -speedy]
        # velocity B right
        elif paddler.rect.x + 90*1.2 < ball.x < paddler.rect.x + 130*1.5 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [speedx, -speedy]
        # velocity C
        elif paddler.rect.x + 70*1.2 < ball.x < paddler.rect.x + 90*1.2 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [0, -speedy]
        # no collision
        else:
            return velocity
    else:
        # velocity A left
        if paddler.rect.x < ball.x < paddler.rect.x + 40 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [speedx-2, -speedy]
        # velocity A right
        elif paddler.rect.x + 130 < ball.x < paddler.rect.x + 160 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [speedx+2, -speedy]
        # velocity B left
        elif paddler.rect.x + 40 < ball.x < paddler.rect.x + 70 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [-speedx, -speedy]
        # velocity B right
        elif paddler.rect.x + 90 < ball.x < paddler.rect.x + 130 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [speedx, -speedy]
        # velocity C
        elif paddler.rect.x + 70 < ball.x < paddler.rect.x + 90 and \
                paddler.rect.y + 60 < ball.y + conf.player_heigth < paddler.rect.y + 65:
            return [0, -speedy]
        # no collision
        else:
            return velocity


def live_lost():
    if conf.live_loss:
        conf.live_loss = False
        return True
    else:
        return conf.live_loss
    