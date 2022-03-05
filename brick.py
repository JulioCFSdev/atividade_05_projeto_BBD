import pygame
import config

# define the wall blocks function
conf = config.Config()


# Create the wall blocks
def create_stage_1():
    for row in range(conf.row_bricks_1):
        for col in range(conf.col_bricks_1):
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
            conf.block_individual_1 = [block, score, block_type, block_life]
            conf.block_list_1.append(conf.block_individual_1)


# Create the wall blocks
def create_stage_2():
    for row in range(conf.row_bricks_2):
        for col in range(conf.col_bricks_2):
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
            conf.block_individual_2 = [block, score, block_type, block_life]
            conf.block_list_2.append(conf.block_individual_2)


# Create the wall blocks
def create_stage_3():
    for row in range(conf.row_bricks_3):
        for col in range(conf.col_bricks_3):
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
            conf.block_individual_3 = [block, score, block_type, block_life]
            conf.block_list_3.append(conf.block_individual_3)


# Create the wall blocks
def create_boss_fight():
    for row in range(conf.row_bricks_boss):
        for col in range(conf.col_bricks_boss):
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
            conf.block_individual_boss = [block, score, block_type, block_life]
            conf.block_list_boss.append(conf.block_individual_boss)


def draw_bricks(screen):
    if conf.stage == 1:
        wall_block = conf.block_list_1
    elif conf.stage == 2:
        wall_block = conf.block_list_2
    elif conf.stage == 3:
        wall_block = conf.block_list_3
    elif conf.stage == 4:
        wall_block = conf.block_list_boss
    for block in wall_block:
        if block[3] == 1:
            if block[2] == 3:
                color = conf.blue
            else:
                color = conf.yellow
        elif block[3] == 2:
            color = conf.green
        elif block[3] == 3:
            color = conf.red
        pygame.draw.rect(screen, color, block[0])
        pygame.draw.rect(screen, conf.black, (block[0]), 1)


def brick_collision(ball, velocity_0, velocity_1):
    n = 0
    if conf.stage == 1:
        wall_block = conf.block_list_1
    elif conf.stage == 2:
        wall_block = conf.block_list_2
    elif conf.stage == 3:
        wall_block = conf.block_list_3
    elif conf.stage == 4:
        wall_block = conf.block_list_boss
    for block in wall_block:
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
            if block[3] != 1:
                wall_block[n][3] -= 1
            else:
                wall_block.remove(block)

        n += 1
    return [velocity_0, velocity_1]
