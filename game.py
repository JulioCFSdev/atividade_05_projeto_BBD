import pygame
import wall
import ball
import player
from config import Config


# Class to start our game
class BlocksAge:

    # Initial variables and set screen
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.white = (255, 255, 255)
        self.pink = '#9957CD'
        self.score = 0
        self.lives = 3
        self.time = "3:00"
        self.clock = pygame.time.Clock()

        self.bola = ball.create_ball()
        self.bola_velocity = ball.ball_velocity(3, 3)

        self.paddler = player.Player()
        self.player_width = 100
        self.player_heigth = 20
        self.player_x = 350
        self.player_y = 650

        pygame.init()
        pygame.display.set_caption("Blocks Age")
        self.screen = pygame.display.set_mode((self.width, self.height))

    # Game loop
    def main_loop(self):
        while True:
            self.handle_input()
            self.game_logic()
            self.draw()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

    # keyboard inputs
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        # Keywords paddler
        # Keywords pause(?)

    # Mechanics and world rules
    def game_logic(self):
        ball.move_ball(self.bola, self.bola_velocity[0], self.bola_velocity[1])  # movement ball
        self.paddler.move()  # movement paddler
        # collision ball/paddler
        self.bola_velocity[1] *= ball.paddler_collision(self.bola, self.paddler)
        # collision ball/blocks
        # collision ball/wall (left, right, up)
        # left wall collision
        self.bola_velocity[0] *= ball.left_wall_collision(self.bola)
        # right wall collision
        self.bola_velocity[0] *= ball.right_wall_collision(self.bola)
        # upper wall collision
        self.bola_velocity[1] *= ball.upper_wall_collision(self.bola)
        # death point - (collision ball/wall down)
        self.bola_velocity[0] *= ball.lower_wall_collision(self.bola)

    # Drawing the screen and its factors
    def draw(self):
        self.screen.fill((0, 0, 0))

        # draw screen
        wall.bg_run("wall_dependencies/bg_test.png", [0, 0], self.screen)
        wall.hud(self.screen, self.width, self.score, self.lives, self.time, 1.05, 1.15, 2.35, 2, 4, 5.5)
        wall.screen_lines(self.screen, (255, 0, 255), self.width, self.height, 12)

        # draw ball
        ball.draw_ball(self.screen, self.white, self.bola)
        # draw paddler
        self.paddler.draw(self.screen, self.pink)
        # draw blocks
        # draw power-ups (?)
        
