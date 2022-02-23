import pygame

pygame.init()


def variables(TIME, SCORE, LIVES):
    global time
    time = TIME
    global score
    score = SCORE
    global lives
    lives = LIVES

    
# MAIN SETTING = variables("3:00", 0, 3)

def screen_set(WIDTH, HEIGHT):
    size = (WIDTH, HEIGHT)

    global width
    width = WIDTH

    global height
    height = HEIGHT

    global screen
    screen = pygame.display.set_mode(size)
    return screen


# MAIN SETTING = screen_set(1000,600)

def hud(score_value, life_value, time_value, pos_money_icon_var, pos_score_value_var,
        pos_life_icon_var, pos_lives_value_var, pos_time_icon_var, pos_time_value_var):
    WHITE = (255, 255, 255)
    font = pygame.font.Font("EmojiOneColor.otf", 34)
    font2 = pygame.font.Font("DSEG14Classic-Bold.ttf", 34)
    text = font.render("💰", True, WHITE)
    screen.blit(text, (width - (width / pos_money_icon_var), 1))  # 1.05
    text2 = font2.render(":  " + str(score_value), True, WHITE)
    screen.blit(text2, (width - (width / pos_score_value_var), 1))  # 1.15
    text = font.render("💕", True, WHITE)
    screen.blit(text, (width / pos_life_icon_var, 1))  # 2.35
    text2 = font2.render(": " + str(life_value), True, WHITE)
    screen.blit(text2, (width - (width / pos_lives_value_var), 1))  # 2
    text = font.render("⏱", True, WHITE)
    screen.blit(text, (width - (width / pos_time_icon_var), 1))  # 4
    text2 = font2.render(": " + str(time_value), True, WHITE)
    screen.blit(text2, (width - (width / pos_time_value_var), 1))  # 5.5


# MAIN SETTING =  hud(score, lives, time, 1.05, 1.15, 2.35, 2, 4, 5.5)
def screen_lines(color, line_size):
    # Color must be in the rgb format(x, x, x) or with an equivalent constant
    # horizontal lines
    pygame.draw.line(screen, color, [0, 50], [width, 50], line_size)

    # vertical lines
    pygame.draw.line(screen, color, [0, 0], [0, height], line_size)
    pygame.draw.line(screen, color, [width, 0], [width, height], line_size)


# MAIN SETTING = screen_lines((255, 0, 255), 12)

screen.fill((0, 0, 0))

# ORDER OF USAGE:

# variables -> screen_set -> (inside game loop) -> screen.fill - > hud -> screen lines
variables("3:00", 0, 3)
screen_set(1000, 600)
clock = pygame.time.Clock()

#  TESTING GROUND  #
while True:
    screen.fill((0, 0, 0))
    # Display
    hud(score, lives, time, 1.05, 1.15, 2.35, 2, 4, 5.5)
    screen_lines((255, 0, 255), 12)
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
