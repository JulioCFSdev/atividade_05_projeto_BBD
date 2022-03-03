import pygame
class Config:

    def __init__(self):
        # screen values
        self.screen_width = 1000
        self.screen_height = 800
        self.size = (self.screen_width, self.screen_height)
        # Background
        self.bg_name = "Blocks Age"
        self.coord_bg = [0, 0]
        self.bg_main_1 = pygame.image.load("wall_dependencies/bg.png")
        self.bg_menu = pygame.image.load("wall_dependencies/bg.png")
        # Fonts and Texts
        self.font2 = pygame.font.Font("wall_dependencies/EmojiOneColor.otf", 34)
        self.font = pygame.font.Font("wall_dependencies/DSEG14Classic-Bold.ttf", 34)
        # Icon and character position constants
        self.pos_money = 1.05
        self.pos_score = 1.15
        self.pos_life_icon = 2.35
        self.pos_life_var = 2
        self.pos_time_icon = 4
        self.pos_time_value = 5.5
        # Line size on sides and top
        self.line_size = 12
        # Time related values
        self.time_text = '180'.rjust(3)
        self.time_counter = 180
        # Values ​​to assign colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.pink = '#9957CD'
        self.red = (139, 0, 0)
        self.blue = (63, 72, 204)
        self.green = (85, 212, 54)
        self.yellow = (255, 242, 0)
        # Ball dimension values
        self.ball_width = 20
        self.ball_heigth = 20
        # Ball initial coordinates values
        self.ball_x_init = 500
        self.ball_y_init = 400
        # Block values (Coluns and rows, dimensions, list)
        self.row_bricks = 10
        self.col_bricks = 19
        self.block_width = 50
        self.block_height = 25
        self.block_individual = []
        self.block_list = []
        # Player sprites

        # Player position
        self.actual = 0
        # Player dimension values
        self.player_width = 110
        self.player_heigth = 20
        # Player initial coordinates values
        self.player_x = 390
        self.player_y = 650
        # Player speed
        self.speed = 10
        # Ball speed
        self.ball_speed_x = 3
        self.ball_speed_y = 3
        # Ball speed controler
        self.reverse_speed = -1
        self.normal_speed = 1
        # Parameter values ​​for collisions
        self.tresh_lower_wall = 20
        self.tresh_right_wall = 26
        self.tresh_left_wall = 6
        self.tresh_upper_wall = 58
        # Frames por second value
        self.fps = 120
        # Paddler values 
        self.x = 340
        self.y = 570
        self.sprites_1 = []
        self.sprites_2 = []
        self.sprites_3 = []
        self.sprites_1.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.sprites_2.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.sprites_3.append(pygame.image.load('Player_sprite/l0_sprite_1.png'))
        self.sprites_2.append(pygame.image.load('Player_sprite/l0_sprite_2.png'))
        self.sprites_3.append(pygame.image.load('Player_sprite/l0_sprite_3.png'))
        self.actual = 0
        self.speed = 10
        self.direction = 0

        
