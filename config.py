import pygame


class Config:

    def __init__(self):
        # screen values
        self.screen_width = 1000
        self.screen_height = 800
        self.size = (self.screen_width, self.screen_height)
        # Background
        self.bg_name = "Elden Blocks"
        self.coord_bg = [0, 0]
        self.bg_main_1 = pygame.image.load("wall_dependencies/bg1.png")
        self.bg_menu = pygame.image.load("wall_dependencies/bg.png")
        # Fonts and Texts
        self.font2 = pygame.font.Font("wall_dependencies/EmojiOneColor.otf", 34)
        self.font = pygame.font.Font("wall_dependencies/ENDOR___.ttf", 34)
        # Stage values
        self.stage = 2
        self.stage_clear = False
        # Score value
        self.money_up = False
        self.live_loss = False
        # Icon and character position constants
        self.pos_money = 1.05
        self.pos_score = 1.15
        self.pos_life_icon = 2.35
        self.pos_life_var = 2
        self.pos_time_icon = 4
        self.pos_time_value = 5.5
        # Power up variables
        self.power_shot = False
        self.power_growth = False
        self.power_small = False
        self.power_gyro = False
        self.power_mult = False
        self.power_ultra = False
        self.extra_life = False
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
        self.orange = (255, 127, 39)
        self.gray = (88, 88, 88)
        # Ball dimension values
        self.ball_width = 20
        self.ball_heigth = 20
        # Ball initial coordinates values
        self.ball_x_init = 500
        self.ball_y_init = 400
        # Block values (Coluns and rows, dimensions, list)
        self.row_bricks_1 = 6
        self.col_bricks_1 = 7
        self.row_bricks_11 = 6
        self.col_bricks_11 = 7
        self.row_bricks_2 = 6
        self.col_bricks_2 = 10
        self.row_bricks_22 = 6
        self.col_bricks_22 = 10
        self.row_bricks_3 = 9 
        self.col_bricks_3 = 4 
        self.row_bricks_33 = 3
        self.col_bricks_33 = 19
        self.row_bricks_boss = 10
        self.col_bricks_boss = 19
        self.all_bricks = 50
        self.block_width = 50
        self.block_height = 25
        self.block_individual_1 = []
        self.block_list_1 = []
        self.block_individual_2 = []
        self.block_list_2 = []
        self.block_individual_3 = []
        self.block_list_3 = []
        self.block_individual_boss = []
        self.block_list_boss = []
        # Player position
        self.actual = 0
        # Player dimension values
        self.player_width = 180
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

        self.powerup = 1

        self.size = 5
