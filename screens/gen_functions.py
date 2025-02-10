import pygame

# List of colors used in the game
RED = (144, 13, 13)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OLD_BLUE = (44, 0, 180)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)
PINK = (255, 0, 184)

# functions for fonts, returns the right font size... Needs to be changed to pressStart.ttf
def scale_title(text_font, WIDTH, HEIGHT):

    new_width = int(WIDTH // 6 )
    new_height = int(HEIGHT // 12)
    return pygame.transform.smoothscale(text_font, (new_width, new_height))


def scale_text(text_font, WIDTH, HEIGHT):

    new_width = int(WIDTH // 2)
    new_height = int(HEIGHT // 12)
    return pygame.transform.smoothscale(text_font, (new_width, new_height))