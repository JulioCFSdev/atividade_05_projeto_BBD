
import emoji
import pygame.freetype


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FUCHSIA = (255, 0, 255)

heart = emoji.emojize('❤')
money = emoji.emojize('💰')

time = "3:00"
score = 0
lives = 3

width = 800
height = 720
size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

all_sprites_list = pygame.sprite.Group()

# The loop will carry on until the user exits the game
# (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
    screen.fill(BLACK)

    # Display
    font = pygame.font.Font("EmojiOneColor.otf", 34)
    font2 = pygame.font.Font("DSEG14Classic-Bold.ttf", 34)
    text = font.render("💰", True, WHITE)
    screen.blit(text, (width-(width/1.05), 1))
    text2 = font2.render(":  " + str(score), True, WHITE)
    screen.blit(text2, (width-(width/1.15), 1))
    text = font.render("💕", True, WHITE)
    screen.blit(text, (width / 2.35, 1))
    text2 = font2.render(": " + str(lives), True, WHITE)
    screen.blit(text2, (width-(width/2), 1))
    text = font.render("⏱", True, WHITE)
    screen.blit(text, (width - (width / 4), 1))
    text2 = font2.render(": " + str(time), True, WHITE)
    screen.blit(text2, (width - (width / 5.5), 1))

    # horizontal lines
    pygame.draw.line(screen, FUCHSIA, [0, 50], [width, 50], 12)

    # vertical lines
    pygame.draw.line(screen, FUCHSIA, [0, 0], [0, height], 12)
    pygame.draw.line(screen, FUCHSIA, [width, 0], [width, height], 12)

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
