import pygame
import config

# define the wall blocks function
conf = config.Config()


# Create the wall blocks
def create_wall():
    for row in range(conf.row_bricks):
        for col in range(conf.col_bricks):
            block_x = col * conf.block_width + 20
            block_y = row * conf.block_height + 100

            score = 500

            # Determining block types
            if row == 9:
                block_type = 0
            elif row == 8:
                block_type = 1
            elif row == 7:
                block_type = 3
            elif row == 6:
                block_type = 0
            elif row == 5:
                block_type = 1
            elif row == 4:
                block_type == 3
            else:
                block_type = 2

            # Determining the life of blocks
            if block_type == 0 or block_type == 3:
                block_life = 1
            elif block_type == 1:
                block_life = 2
            else:
                block_life = 3

            block = pygame.Rect(block_x, block_y, conf.block_width, conf.block_height)
            conf.block_individual = [block, score, block_type, block_life]
            conf.block_list.append(conf.block_individual)


def draw_bricks(screen):
    for block in conf.block_list:
        if block[2] == 0:
            color = conf.yellow
        elif block[2] == 1:
            color = conf.green
        elif block[2] == 2:
            color = conf.red
        elif block[2] == 3:
            color = conf.blue
        pygame.draw.rect(screen, color, block[0])
        pygame.draw.rect(screen, conf.black, (block[0]), 1)


def brick_collision(ball, velocity_0, velocity_1):
    for block in conf.block_list:
        if ball.colliderect(block[0]):
            # checking the collision side
            if abs(block[0].y - (ball.y + conf.ball_heigth)) < 5 and velocity_1 > 0:
                velocity_1 *= -1
            # bottom collision
            elif abs((block[0].y + conf.block_height) - ball.y) < 5 and velocity_1 < 0:
                velocity_1 *= -1
            # right collision
            elif abs(block[0].x - (ball.x + conf.ball_width)) < 5 and velocity_0 > 0:
                velocity_0 *= -1
            # left collision
            elif abs((block[0].x + conf.block_width) - ball.x) < 5 and velocity_0 < 0:
                velocity_0 *= -1
            conf.block_list.remove(block)
    return [velocity_0, velocity_1]
