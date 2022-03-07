import pygame
import config
from powerup import PowerUp


# define the wall blocks function
conf = config.Config()

power_up_sprites = pygame.sprite.Group()
powerups = []


# Create the wall blocks stage 1
def create_stage_1():
    for row in range(conf.row_bricks_1):
        for col in range(conf.col_bricks_1):
            block_x = col * conf.block_width + 10
            block_y = row * conf.block_height + 180

            score = 5

            # Determining block types
            if row == 6:
                block_type = 0
            elif row == 6:
                block_type = 0
            elif row == 5:
                block_type = 0
            elif row == 4:
                block_type = 0
            elif row == 3:
                block_type = 3
            elif row == 2:
                block_type = 1
            elif row == 1:
                block_type = 0
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

    for row in range(conf.row_bricks_11):
        for col in range(conf.col_bricks_11):
            block_x = col * conf.block_width + 645
            block_y = row * conf.block_height + 180

            score = 5

            # Determining block types
            if row == 6:
                block_type = 0
            elif row == 6:
                block_type = 0
            elif row == 5:
                block_type = 0
            elif row == 4:
                block_type = 0
            elif row == 3:
                block_type = 3
            elif row == 2:
                block_type = 1
            elif row == 1:
                block_type = 0
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

# Create the wall blocks stage 2
def create_stage_2():
    for row in range(conf.row_bricks_2):
        for col in range(conf.col_bricks_2):
            block_x = col * conf.block_width + 20
            block_y = row * conf.block_height + 100

            score = 5

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
                block_type = 3
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


# Create the wall blocks stage 3
def create_stage_3():
    for row in range(conf.row_bricks_3):
        for col in range(conf.col_bricks_3):
            block_x = col * conf.block_width + 20
            block_y = row * conf.block_height + 100

            score = 5

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
                block_type = 3
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
def create_stage_4():
    for row in range(conf.row_bricks_boss):
        for col in range(conf.col_bricks_boss):
            block_x = col * conf.block_width + 20
            block_y = row * conf.block_height + 115

            if row == 0 and col == 3:
                block_type = 4
            elif row == 1 and col == 1:
                block_type = 4
            elif row == 2 and col == 8:
                block_type = 4
            elif row == 3 and col == 17:
                block_type = 4
            elif row == 4 and col == 14:
                block_type = 4
            elif row == 5 and col == 1:
                block_type = 4
            elif row == 6 and col == 9:
                block_type = 4
            elif row == 7 and col == 11:
                block_type = 4
            elif row == 8 and col == 2:
                block_type = 4
            elif row == 9 and col == 15:
                block_type = 4
            else:
                block_type = 5
            
            if block_type == 4:
                block_life = 1
            else:
                block_life = 999

            score = 5

            block = pygame.Rect(block_x, block_y, conf.block_width, conf.block_height)
            conf.block_individual_boss = [block, score, block_type, block_life]
            conf.block_list_boss.append(conf.block_individual_boss)


# Draw wall brick function
def draw_bricks(screen):
    # Determining which block wall to check
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
            elif block[2] == 0:
                color = conf.yellow
            if conf.stage == 4:
                color = conf.orange
        elif block[3] == 2:
            color = conf.green
        elif block[3] == 3:
            color = conf.red
        if conf.stage == 4 and block[3] > 3:
            color = conf.gray

        pygame.draw.rect(screen, color, block[0])
        pygame.draw.rect(screen, conf.black, (block[0]), 1)


# brick colission function
def brick_collision(ball, laser, velocity_0, velocity_1, stage, power_gyro, power_ultra):
    n = 0
    conf.money_up = 0

    # Moving to the next stage
    if conf.all_bricks < 1:
        conf.stage += 1
        conf.stage_clear = True
        conf.all_bricks = 100

    # Determining which block wall to check
    if stage == 1:
        wall_block = conf.block_list_1
    elif stage == 2:
        wall_block = conf.block_list_2
    elif stage == 3:
        wall_block = conf.block_list_3
    elif stage == 4:
        wall_block = conf.block_list_boss

    for block in wall_block:
        if power_gyro[1] and ball.colliderect(block[0]):
            conf.power_ultra = False
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

            if block[2] == 3:
                powerup = PowerUp(block[0].x, block[0].y)
                powerups.append(powerup)
                power_up_sprites.add(powerup)


            if block[2] == 0 or block[2] == 3:
                conf.money_up = 1
            elif block[2] == 1:
                conf.money_up = 2
            elif block[2] == 2:
                conf.money_up = 3

            wall_block.remove(block)
            conf.all_bricks -= 1


        elif power_ultra[2] and ball.colliderect(block[0]):
            conf.power_gyro = False
            # checking the collision side
            if abs(block[0].y - (ball.y + conf.ball_heigth)) < 5 and velocity_1 > 0:
                velocity_1 = velocity_1
            # bottom collision
            elif abs((block[0].y + conf.block_height) - ball.y) < 5 and velocity_1 < 0:
                velocity_1 = velocity_1
            # right collision
            elif abs(block[0].x - (ball.x + conf.ball_width)) < 5 and velocity_0 > 0:
                velocity_1 = velocity_1
            # left collision
            elif abs((block[0].x + conf.block_width) - ball.x) < 5 and velocity_0 < 0:
                velocity_1 = velocity_1

            if block[2] == 3:
                    powerup = PowerUp(block[0].x, block[0].y)
                    powerups.append(powerup)
                    power_up_sprites.add(powerup)

            if block[2] == 0 or block[2] == 3:
                conf.money_up = 1
            elif block[2] == 1:
                conf.money_up = 2
            elif block[2] == 2:
                conf.money_up = 3

            wall_block.remove(block)
            conf.all_bricks -= 1


        elif conf.stage == 4 and ball.colliderect(block[0]):
            # checking the collision side
            if abs(block[0].y - (ball.y + conf.ball_heigth)) < 5 and velocity_1 > 0:
                    velocity_1 *= -1
            # bottom collision
            elif abs((block[0].y + conf.block_height) - ball.y) < 5 and velocity_1 < 0:
                    velocity_1 *= -1
            # explosion block        
            if block[2] == 4:
                for remover in range(len(wall_block) - 1, len(wall_block) - 20, -1):
                    wall_block.remove(wall_block[remover])

        elif conf.stage != 4:
            if power_gyro[2] and ball.colliderect(block[0]):
                conf.power_ultra = False
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

                if block[2] == 3:
                    powerup = PowerUp(block[0].x, block[0].y)
                    powerups.append(powerup)
                    power_up_sprites.add(powerup)

                if block[2] == 0 or block[2] == 3:
                    conf.money_up = 1
                elif block[2] == 1:
                    conf.money_up = 2
                elif block[2] == 2:
                    conf.money_up = 3

                wall_block.remove(block)
                conf.all_bricks -= 1


            elif power_ultra[3] and ball.colliderect(block[0]):
                conf.power_gyro = False
                # checking the collision side
                if abs(block[0].y - (ball.y + conf.ball_heigth)) < 5 and velocity_1 > 0:
                    velocity_1 = velocity_1
                # bottom collision
                elif abs((block[0].y + conf.block_height) - ball.y) < 5 and velocity_1 < 0:
                    velocity_1 = velocity_1
                # right collision
                elif abs(block[0].x - (ball.x + conf.ball_width)) < 5 and velocity_0 > 0:
                    velocity_1 = velocity_1
                # left collision
                elif abs((block[0].x + conf.block_width) - ball.x) < 5 and velocity_0 < 0:
                    velocity_1 = velocity_1

                if block[2] == 0 or block[2] == 3:
                    conf.money_up = 1
                elif block[2] == 1:
                    conf.money_up = 2
                elif block[2] == 2:
                    conf.money_up = 3

                wall_block.remove(block)
                conf.all_bricks -= 1


            elif ball.colliderect(block[0]):
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

                if block[2] == 3:
                    powerup = PowerUp(block[0].x, block[0].y)
                    powerups.append(powerup)
                    power_up_sprites.add(powerup)

                if block[3] != 1:
                    wall_block[n][3] -= 1

                else:
                    if block[2] == 0 or block[2] == 3:
                        conf.money_up = 1
                    elif block[2] == 1:
                        conf.money_up = 2
                    elif block[2] == 2:
                        conf.money_up = 3

                    wall_block.remove(block)
                    conf.all_bricks -= 1
            for shot in laser:
                p = 0
                if block[0].x - conf.block_width < shot.rect.x < block[0].x + conf.block_width and \
                        block[0].y < shot.rect.y + conf.block_height < block[0].y + conf.block_height:
                    if block[3] != 1:
                        wall_block[n][3] -= 1
                        shot.kill()

                    else:
                        if block[2] == 0 or block[2] == 3:
                            conf.money_up = 1
                        elif block[2] == 1:
                            conf.money_up = 2
                        elif block[2] == 2:
                            conf.money_up = 3

                        wall_block.remove(block)
                        conf.all_bricks -= 1
                        shot.kill()
                p += 1
        n += 1
    return [velocity_0, velocity_1]


def money_up():
    return conf.money_up


def next_stage():
    if conf.stage_clear == True:
        conf.stage_clear = False
        return [conf.stage, True]

    return [conf.stage, conf.stage_clear]
