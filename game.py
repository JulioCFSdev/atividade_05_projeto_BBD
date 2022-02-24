import pygame
import wall 
from ball import Ball


class BlocksAge:


    def __init__(self):
        self.width = 1000
        self.height = 800
        self.score = 0
        self.lives = 3
        self.time = "3:00"
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption("Blocks Age")

        wall.__init__("wall")
        self.screen = pygame.display.set_mode((self.width, self.height))

    
    def main_loop(self):
        while True:
            self.handle_input()
            self.game_logic()
            self.draw()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    
    def game_logic(self):
        bola = Ball()
        bola.ball_move()


    def draw(self):
        self.screen.fill((0, 0, 0))
        wall.hud(self.screen, self.width, self.score, self.lives, self.time, 1.05, 1.15, 2.35, 2, 4, 5.5)
        wall.screen_lines(self.screen, (255, 0, 255), self.width, self.height, 12)
        Ball()
        pygame.display.flip()

