import pygame
from wall import bg_run, screen_lines, hud_time, hud_score, hud_lives

pygame.init()

width = 1000
height = 600
score = 0
lives = 3
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
time_counter = 5
time_text = '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


while True:
    screen.fill((0, 0, 0))
    bg_run("wall_dependencies/bg_test.png", [0, 0], screen)
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            time_counter -= 1
            time_text = str(time_counter).rjust(3) if time_counter > 0 else "X"
        if time_text == "X":
            font2 = pygame.font.Font("wall_dependencies/DSEG14Classic-Bold.ttf", 34)
            text = font2.render("GAME OVER", True, (255, 255, 255))
            screen.blit(text, (width / 2 - 100, height / 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
    hud_score(screen, width, 1.05, score, 1.15)
    hud_lives(screen, width, 2.35, lives, 2)
    hud_time(screen, width, 4, time_text, 5.5)
    screen_lines(screen, (139, 0, 0), width, height, 12)

    pygame.display.flip()
    clock.tick(60)
