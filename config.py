class Config:

    def __init__(self):
        # screen values
        self.screen_width = 1000
        self.screen_height = 800
        self.size = (self.screen_width, self.screen_height)
        # Background
        self.bg_name = "Blocks Age"
        self.coord_bg = [0, 0]
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
        # Ball dimension values
        self.ball_width = 20
        self.ball_heigth = 20
        # Ball initial coordinates values
        self.ball_x_init = 500
        self.ball_y_init = 400
        self.row_bricks = 14
        self.col_bricks = 31
        self.block_width = 40
        self.block_height = 20
        self.block_individual = []
        self.block_list = []
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
        self.fps = 60

        
