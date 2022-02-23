import pygame
from wall_v3 import bg_run, screen_lines, hud

pygame.init()
width = 1000
height = 800
score = 0
lives = 3
time = "3:00"
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


while True:
    screen.fill((0, 0, 0))
    bg_run("bg_test.png", [0, 0], screen)
    hud(screen, width, score, lives, time, 1.05, 1.15, 2.35, 2, 4, 5.5)
    screen_lines(screen, (255, 0, 255), width, height, 12)
    pygame.display.flip()
    clock.tick(60)