class Config:

    def __init__(self):
        # screen values
        self.screen_width = 1000
        self.screen_height = 800
        self.size = (self.screen_width, self.screen_height)
        self.coord_bg = [0, 0]
        # Values ​​to assign colors
        self.white = (255, 255, 255)
        self.pink = '#9957CD'
        # Ball dimension values
        self.ball_width = 20
        self.ball_heigth = 20
        # Ball initial coordinates values
        self.ball_x_init = 500
        self.ball_y_init = 400
        # Player dimension values
        self.player_width = 110
        self.player_heigth = 20
        # Player initial coordinates values
        self.player_x = 390
        self.player_y = 650
        # Player speed
        self.speed = 10
        # Ball speed controler
        self.reverse_speed = -1
        self.normal_speed = 1
        # Parameter values ​​for collisions
        self.tresh_lower_wall = 20
        self.tresh_right_wall = 26
        self.tresh_left_wall = 6
        self.tresh_upper_wall = 58

        