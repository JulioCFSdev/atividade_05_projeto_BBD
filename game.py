import pygame
import wall 
import ball

# Class to start our game
class BlocksAge:

    # Initial variables and set screen
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.white = (255, 255, 255)
        self.score = 0
        self.lives = 3
        self.time = "3:00"
        self.clock = pygame.time.Clock()
        
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
        ball = pygame.Rect(500, 400, 20, 20)
        ball.move_ball(ball.x, ball.y, ball_dx=2, ball_dy=2)
        pass
        # movement ball
        # movement paddler
        # collision ball/paddler
        # colision ball/blocks
        # colision ball/wall (left, right, up)
        # death point - (collision ball/wall down)


    # Drawing the screen and its factors
    def draw(self):
        self.screen.fill((0, 0, 0))

        # draw screen
        wall.bg_run("wall_dependencies/bg_test.png", [0,0], self.screen)
        wall.hud(self.screen, self.width, self.score, self.lives, self.time, 1.05, 1.15, 2.35, 2, 4, 5.5)
        wall.screen_lines(self.screen, (255, 0, 255), self.width, self.height, 12)
        ball.draw_ball(self.screen, self.white)

        # draw ball
        # draw paddler
        # draw blocks
        # draw power-ups (?)

