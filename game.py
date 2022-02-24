import pygame
import wall
from ball import Ball


class BlocksAge:


    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Blocks Age")

        wall.__init__("wall")
        self.screen = pygame.display.set_mode((1000, 800))

    
    def main_loop(self):
        while True:
            self.handle_input()
            self.game_logic()


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    
    def game_logic(self):
        bola = Ball()
        bola.ball_move()

