import pygame

pygame.init()

# CONSTANTS NEEDED IN THE LOOP

# width = 1000
# height = 800
# score = 0
# lives = 3
# time = "3:00"
# size = (width, height)
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()



def bg_run(image_file, pos, display):
    bg = pygame.image.load(image_file)
    display.blit(bg, pos)

    # FILE DIRECTORY WITH FILE TYPE AT THE END, EXAMPLE = image.jpeg, pos = x and y
    # in the following form [x, y]

    # IDEALLY, YOU'LL WANT TO DO THIS MANUALLY, SO THAT WHEN WE NEED TO CHANGE THE
    # BG, ONLY THE VARIABLE bg IS CHANGED, in that case, do the bg outside
    # the loop, then change it inside afterwards


def hud(display, size, score_value, life_value, time_value, pos_money_icon_var, pos_score_value_var,
        pos_life_icon_var, pos_lives_value_var, pos_time_icon_var, pos_time_value_var):
    WHITE = (255, 255, 255)
    font = pygame.font.Font("EmojiOneColor.otf", 34)
    font2 = pygame.font.Font("DSEG14Classic-Bold.ttf", 34)
    text = font.render("💰", True, WHITE)
    display.blit(text, (size - (size / pos_money_icon_var), 1))  # 1.05
    text2 = font2.render(":  " + str(score_value), True, WHITE)
    display.blit(text2, (size - (size / pos_score_value_var), 1))  # 1.15
    text = font.render("💕", True, WHITE)
    display.blit(text, (size / pos_life_icon_var, 1))  # 2.35
    text2 = font2.render(": " + str(life_value), True, WHITE)
    display.blit(text2, (size - (size / pos_lives_value_var), 1))  # 2
    text = font.render("⏱", True, WHITE)
    display.blit(text, (size - (size / pos_time_icon_var), 1))  # 4
    text2 = font2.render(": " + str(time_value), True, WHITE)
    display.blit(text2, (size - (size / pos_time_value_var), 1))  # 5.5

    # MAIN SETTING =  hud(score, lives, time, 1.05, 1.15, 2.35, 2, 4, 5.5)



def screen_lines(display, color, WIDTH, HEIGHT, line_size):
    # Color must be in the rgb format(x, x, x) or with an equivalent constant
    # horizontal lines
    pygame.draw.line(display, color, [0, 50], [WIDTH, 50], line_size)

    # vertical lines
    pygame.draw.line(display, color, [0, 0], [0, HEIGHT], line_size)
    pygame.draw.line(display, color, [WIDTH, 0], [WIDTH, HEIGHT], line_size)

    # MAIN SETTING = screen_lines((255, 0, 255), 12)


