import pygame
import wall
import ball
from player import (
    all_sprite,
    player,
    player_power_up_collision,
    power_up_on,
    conf1,
)
from config import Config
import brick
from brick import power_up_sprites, powerups
import sys

# Shrinking class call characters
conf = Config()
paddler = player
bricks = brick


# Class to start our game
class EldenBlocks:

    # Initial variables and set screen
    def __init__(self):
        self.score = 0
        self.lives = 15
        self.stage = [1, False]
        self.clock = pygame.time.Clock()
        self.power_ups = power_up_on()
        self.ball = ball.create_ball()
        self.ball2 = ball.create_ball()
        self.ball3 = ball.create_ball()
        self.ball_speed_x = 3
        self.ball_speed_y = 3
        self.ball_speed_x2 = 3
        self.ball_speed_y2 = 3
        self.ball_speed_x3 = 3
        self.ball_speed_y3 = 3
        self.ball_velocity = ball.ball_velocity(
            self.ball_speed_x, self.ball_speed_y
        )
        self.ball_velocity2 = ball.ball_velocity(
            self.ball_speed_x2, self.ball_speed_y2
        )
        self.ball_velocity3 = ball.ball_velocity(
            self.ball_speed_x3, self.ball_speed_y3
        )
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.display.set_caption(conf.bg_name)
        self.screen = pygame.display.set_mode(
            (conf.screen_width, conf.screen_height)
        )
        self.brick_1 = brick.create_stage_1()
        self.brick_2 = brick.create_stage_2()
        self.brick_3 = brick.create_stage_3()
        self.brick_boss = brick.create_stage_4()

    # Main Menu:
    def menu(self):
        pygame.mixer.music.load("wall_dependencies/main_loop_song.mp3")
        pygame.mixer.music.play()
        menu_txt = conf.font.render("Menu Principal", 1, conf.white)
        play_txt = conf.font.render("Play", 1, conf.white)
        quit_txt = conf.font.render("Quit", 1, conf.white)
        click = False
        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blit(conf.bg_menu, (0, 0))
            self.screen.blit(menu_txt, ((conf.screen_width / 2) - 100, 40))
            mx, my = pygame.mouse.get_pos()

            play_button = self.screen.blit(
                play_txt, ((conf.screen_width / 2) - 30, 300)
            )
            quit_button = self.screen.blit(
                quit_txt, ((conf.screen_width / 2) - 30, 500)
            )
            if play_button.collidepoint((mx, my)):
                if click:
                    self.main_loop()
            if quit_button.collidepoint((mx, my)):
                if click:
                    pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
            self.clock.tick(conf.fps)

    # Game loop
    def main_loop(self):
        pygame.mixer.music.load("wall_dependencies/menu_song.mp3")
        pygame.mixer.music.play()
        while True:
            self.handle_input()
            self.game_logic()
            if self.power_ups[3]:
                self.multi_ball()
            self.draw()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(conf.fps)

    # keyboard inputs
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                conf.time_counter -= 1
                conf.time_text = (
                    str(conf.time_counter).rjust(3)
                    if conf.time_counter > 0
                    else "X"
                )
            if conf.time_text == "X" or self.lives == 0:
                game_over_text = conf.font.render(
                    "GAME OVER", True, (255, 255, 255)
                )
                self.screen.blit(
                    game_over_text,
                    (conf.screen_width / 2 - 100, conf.screen_height / 2),
                )
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
            if event.type == pygame.QUIT:
                quit()
        # Keywords paddler
        # Keywords pause(?)

    # Mechanics and world rules
    def game_logic(self):

        if self.power_ups[4]:
            conf1.extra_life = False
            self.lives += 1
        ball.move_ball(
            self.ball, self.ball_velocity[0], self.ball_velocity[1]
        )  # movement ball

        # collision ball/paddler
        self.ball_velocity = ball.paddler_collision(
            self.ball,
            self.ball_velocity,
            paddler,
            self.ball_speed_x,
            self.ball_speed_y,
            self.power_ups,
        )
        # collision ball/blocks
        self.ball_velocity = brick.brick_collision(
            self.ball,
            player.lasers,
            self.ball_velocity[0],
            self.ball_velocity[1],
            self.stage[0],
            self.power_ups,
            self.power_ups,
        )
        # left wall collision
        self.ball_velocity[0] *= ball.left_wall_collision(self.ball)
        # right wall collision
        self.ball_velocity[0] *= ball.right_wall_collision(self.ball)
        # upper wall collision
        self.ball_velocity[1] *= ball.upper_wall_collision(self.ball)
        # death point - (collision ball/wall down)
        self.ball_velocity = ball.lower_wall_collision(
            self.ball, self.ball_velocity, self.ball_speed_x, self.ball_speed_y
        )

        # Money up
        money_condition = brick.money_up()
        if money_condition == 1:
            self.score += 5
        elif money_condition > 1:
            self.score += 10
        live_condition = ball.live_lost()
        if live_condition:
            self.lives -= 1
        self.stage = brick.next_stage()

        # powerups collision
        player_power_up_collision(player, self.stage[1])

        # Stage win screen
        if self.stage[1]:
            stage_clear_text = conf.font.render(
                "STAGE CLEAR", True, conf.white
            )
            self.screen.blit(
                stage_clear_text,
                (conf.screen_width / 2 - 100, conf.screen_height / 2),
            )
            pygame.display.flip()
            pygame.time.wait(2000)
            self.stage[1] = False
            conf.time_counter = 180

    def multi_ball(self):
        # collision ball/paddler
        ball.move_ball(
            self.ball2, -self.ball_velocity2[0], self.ball_velocity2[1] + 1
        )
        self.ball_velocity2 = ball.paddler_collision(
            self.ball2,
            self.ball_velocity2,
            paddler,
            self.ball_speed_x2,
            self.ball_speed_y2,
            self.power_ups,
        )
        # collision ball/blocks
        self.ball_velocity2 = brick.brick_collision(
            self.ball2,
            player.lasers,
            self.ball_velocity2[0],
            self.ball_velocity2[1],
            self.stage[0],
            self.power_ups,
            self.power_ups,
        )
        # left wall collision
        self.ball_velocity2[0] *= ball.left_wall_collision(self.ball2)
        # right wall collision
        self.ball_velocity2[0] *= ball.right_wall_collision(self.ball2)
        # upper wall collision
        self.ball_velocity2[1] *= ball.upper_wall_collision(self.ball2)
        # death point - (collision ball/wall down)
        self.ball_velocity2 = ball.lower_wall_collision_mult(
            self.ball2,
            self.ball_velocity2
        )

        # Ball 3

        ball.move_ball(
            self.ball3, -self.ball_velocity3[0], self.ball_velocity3[1] - 1
        )
        self.ball_velocity3 = ball.paddler_collision(
            self.ball3,
            self.ball_velocity3,
            paddler,
            self.ball_speed_x3,
            self.ball_speed_y3,
            self.power_ups,
        )
        # collision ball/blocks
        self.ball_velocity3 = brick.brick_collision(
            self.ball3,
            player.lasers,
            self.ball_velocity3[0],
            self.ball_velocity3[1],
            self.stage[0],
            self.power_ups,
            self.power_ups,
        )
        # left wall collision
        self.ball_velocity3[0] *= ball.left_wall_collision(self.ball3)
        # right wall collision
        self.ball_velocity3[0] *= ball.right_wall_collision(self.ball3)
        # upper wall collision
        self.ball_velocity3[1] *= ball.upper_wall_collision(self.ball3)
        # death point - (collision ball/wall down)
        self.ball_velocity3 = ball.lower_wall_collision_mult(
            self.ball3,
            self.ball_velocity3
        )

    # Drawing the screen and its factors
    def draw(self):
        self.screen.fill(conf.black)
        # draw screen
        self.screen.blit(conf.bg_main_1, (0, 0))
        wall.hud_score(
            self.screen,
            conf.screen_width,
            conf.pos_money,
            self.score,
            conf.pos_score,
        )
        wall.hud_lives(
            self.screen,
            conf.screen_width,
            conf.pos_life_icon,
            self.lives,
            conf.pos_life_var,
        )
        wall.hud_time(
            self.screen,
            conf.screen_width,
            conf.pos_time_icon,
            conf.time_text,
            conf.pos_time_value,
        )
        wall.screen_lines(self.screen, conf.pink, conf.line_size)

        # draw ball
        ball.draw_ball(self.screen, self.ball)
        if self.power_ups[3]:
            ball.draw_ball(self.screen, self.ball2)
            ball.draw_ball(self.screen, self.ball3)
        # draw paddler
        all_sprite.draw(self.screen)
        all_sprite.update()
        player.move()

        # draw blocks
        brick.draw_bricks(self.screen)

        # power ups
        power_up_sprites.draw(self.screen)

        player.lasers.draw(self.screen)
        player.lasers.update()

        for powerup in powerups:
            powerup.move()
