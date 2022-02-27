import pygame
import config 
# define the wall blocks function
conf = config.Config()

def create_wall():

    for row in range(conf.row_bricks):
        for col in range(conf.col_bricks):
            block_x = col * conf.col_bricks + 10
            block_y = row * conf.row_bricks + 100

            score = 500

            block = pygame.Rect(block_x, block_y, conf.block_width, conf.block_height)
            conf.block_individual = [block, conf.pink ,score]
            conf.block_list.append(conf.block_individual)

def draw_bricks(screen):
        for block in conf.block_list:
                pygame.draw.rect(screen, block[1], block[0])
                pygame.draw.rect(screen, conf.black, (block[0]), 1)


def brick_collision(ball, velocity_0, velocity_1):
    for block in conf.block_list:
        if ball.colliderect(block[0]):
            # checking the collision side
            print('teste colisão')
            conf.block_list.remove(block)
    return [velocity_0, velocity_1]
