import pygame
from config import Config

pygame.init()
conf = Config()


def hud_score(display, size, pos_money_icon_var, score_value, pos_score_value_var):
    text = conf.font2.render("💰", True, conf.white)
    display.blit(text, (size - (size / pos_money_icon_var), 1))  # 1.05
    text2 = conf.font.render(":  " + str(score_value), True, conf.white)
    display.blit(text2, (size - (size / pos_score_value_var + 70), -15))  # 1.15

    # MAIN SETTING = hud_score(screen, width, 1.05, 1.15)


def hud_lives(display, size, pos_lives_icon_var, life_value, pos_lives_value_var):
    text = conf.font2.render("💕", True, conf.white)
    display.blit(text, (size / pos_lives_icon_var, 1))  # 2.35
    text2 = conf.font.render(": " + str(life_value), True, conf.white)
    display.blit(text2, (size - (size / pos_lives_value_var), -15))  # 2

    # MAIN SETTING = hud_lives(screen, width, 2.35, 2)


def hud_time(display, size, pos_time_icon_var, time_value, pos_time_value_var):
    text = conf.font2.render("⏱", True, conf.white)
    display.blit(text, (size - (size / pos_time_icon_var), 1))  # 4
    time_txt = conf.font.render(": " + time_value, True, conf.white)
    display.blit(time_txt, (size - (size / pos_time_value_var), -15))  # 5.5

    # MAIN SETTING = hud_time(screen, width, 4, time_text, 5.5)


def screen_lines(display, color, line_size):
    # Color must be in the rgb format(x, x, x) or with an equivalent constant
    # horizontal lines
    pygame.draw.line(display, color, [0, 70], [conf.screen_width, 70], line_size)

    # vertical lines
    pygame.draw.line(display, color, [0, 0], [0, conf.screen_height], line_size)
    pygame.draw.line(display, color, [conf.screen_width, 0], [conf.screen_width, conf.screen_height], line_size)

    # MAIN SETTING = screen_lines((255, 0, 255), 12)
