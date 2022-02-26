import pygame
import wall
import ball
import player
from config import Config
import brick

# Shrinking class call characters
conf = Config()
paddler = player.Player()
bricks = brick

# Class to start our game
class EldenBlocks:

    # Initial variables and set screen
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.clock = pygame.time.Clock()
        self.ball = ball.create_ball()
        self.ball_velocity = ball.ball_velocity(conf.ball_speed_x, conf.ball_speed_y)
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.display.set_caption(conf.bg_name)
        self.screen = pygame.display.set_mode((conf.screen_width, conf.screen_height))
        self.brick = bricks.create_wall()

    # Game loop
    def main_loop(self):
        while True:
            self.handle_input()
            self.game_logic()
            self.draw()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(conf.fps)

    # keyboard inputs
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                conf.time_counter -= 1
                conf.time_text = str(conf.time_counter).rjust(
                    3) if conf.time_counter > 0 else "X"
            if conf.time_text == "X":
                font2 = pygame.font.Font("wall_dependencies/DSEG14Classic-Bold.ttf", 34)
                text = font2.render("GAME OVER", True, (255, 255, 255))
                self.screen.blit(text, (conf.screen_width / 2 - 100, conf.screen_height / 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
            if event.type == pygame.QUIT:
                quit()
        # Keywords paddler
        # Keywords pause(?)

    # Mechanics and world rules
    def game_logic(self):
        ball.move_ball(self.ball, self.ball_velocity[0], self.ball_velocity[1])  # movement ball
        paddler.move()  # movement paddler
        # collision ball/paddler
        self.ball_velocity = ball.paddler_collision(self.ball, self.ball_velocity, paddler)
        # collision ball/blocks
        # left wall collision
        self.ball_velocity[0] *= ball.left_wall_collision(self.ball)
        # right wall collision
        self.ball_velocity[0] *= ball.right_wall_collision(self.ball)
        # upper wall collision
        self.ball_velocity[1] *= ball.upper_wall_collision(self.ball)
        # death point - (collision ball/wall down)
        self.ball_velocity[0] *= ball.lower_wall_collision(self.ball)

    # Drawing the screen and its factors
    def draw(self):
        self.screen.fill(conf.black)

        # draw screen
        wall.bg_run("wall_dependencies/bg_test.png", conf.coord_bg, self.screen)
        wall.hud_score(self.screen, conf.screen_width, conf.pos_money, self.score, conf.pos_score)
        wall.hud_lives(self.screen, conf.screen_width, conf.pos_life_icon, self.lives,
                       conf.pos_life_var)
        wall.hud_time(self.screen, conf.screen_width, conf.pos_time_icon, conf.time_text,
                      conf.pos_time_value)
        wall.screen_lines(self.screen, conf.pink, conf.screen_width, conf.screen_height,
                          conf.line_size)

        # draw ball
        ball.draw_ball(self.screen, self.ball)
        # draw paddler
        paddler.draw(self.screen, conf.pink)
        # draw blocks
        bricks.draw_bricks(self.screen)
        # draw power-ups (?)
