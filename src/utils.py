import pygame
from levels.gameplay import *

# Colors used in the game
BLACK = (0, 0, 0)
BLUE = (8,4,180)
DARK_BLUE = (3, 3, 178)
OLD_BLUE = (44, 0, 180)
GREEN = (0, 128, 0)
AQUA = (0, 242, 250)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 66, 77)
BROWN  = (139, 69, 19)
YELLOW = (254, 254, 6)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (0, 241, 54)
LIGHT_AQUA = (224, 255, 255)
LIGHT_RED = (255, 182, 193) 
LIGHT_PURPLE = (221, 160, 221)
LIGHT_YELLOW = (255, 255, 224)

clock = pygame.time.Clock() # Used in flash, returns the number of milliseconds since pygame.init()

square_size = 8 # Used for square bullets

logo_color_list = [RED, AQUA, PURPLE, YELLOW, LIGHT_BLUE, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
blinking_text_color_list = [AQUA, PURPLE, YELLOW, GRAY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
rect_colors = [BLACK, PURPLE, GRAY, RED, GREEN, BROWN]
def load_font(size):
    return pygame.font.Font("/KingdomOfKrozII/assets/PressStart2P - Regular.ttf", size)

def load_fonts(sizes):
    return [pygame.font.Font("/KingdomOfKrozII/assets/PressStart2P - Regular.ttf", size) for size in sizes]

def render_text(font, text, color):
    return font.render(text, True, color)

def setup_cursor(timer_interval=250):
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, timer_interval)
    return cursor_visible, cursor_timer

def setup_blinking_text(timer_interval=250):
    blinking_text = True
    blinking_text_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(blinking_text_timer, timer_interval)
    return blinking_text, blinking_text_timer

def center_text_x(screen_width, text_width):
    return (screen_width - text_width) // 2

def position_text_y(screen_height, relative_position, font_height):
    return screen_height * relative_position - font_height

def position_subtext_y(base_y, font_height, index, spacing=2):
    return base_y + font_height * index * spacing

def apply_grayscale(image):
    grayscale_image = pygame.Surface(image.get_size(), pygame.SRCALPHA) # Create alpha channel over image
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r, g, b, a = image.get_at((x, y))
            gray_formula = int(0.299 * r + 0.587 * g + 0.114 * b) # Standard grayscale formula
            gray = min(255, gray_formula + 70) # Increase brightness
            grayscale_image.set_at((x, y), (gray, gray, gray, a))
    return grayscale_image

def change_logo_color(image, time, color_user_input):
    if color_user_input == "M":
        return apply_grayscale(image)
    else:
        color_index = (time // 150) % len(logo_color_list)
        current_color = logo_color_list[color_index] 
        color_filter = pygame.Surface(image.get_size()) # Create imaging surface
        color_filter.fill(current_color) 
        colorized_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        colorized_image.blit(image, (0, 0)) 
        colorized_image.blit(color_filter, (0, 0), special_flags=pygame.BLEND_RGB_MULT) # Apply color filter
        return colorized_image

def change_title_color(time, color_user_input):
    if color_user_input == "M":
        return BLACK
    else:
        color_index = (time // 150) % len(blinking_text_color_list)
        return blinking_text_color_list[color_index]

# Load Tiles, loading extra icons that are not in levels.gameplay
enemy3   = pygame.image.load("/KingdomOfKrozII/assets/enemy3.png")
keys     = pygame.image.load("/KingdomOfKrozII/assets/keys.png")
power    = pygame.image.load("/KingdomOfKrozII/assets/power.png")
clues    = pygame.image.load("/KingdomOfKrozII/assets/clues.png")
surprise = pygame.image.load("/KingdomOfKrozII/assets/surprise.png")
# Scale tiles
enemy3   = pygame.transform.scale(enemy3, (15, 15))
keys     = pygame.transform.scale(keys, (15, 15))
power    = pygame.transform.scale(power, (15, 15))
clues    = pygame.transform.scale(clues, (15, 15))
surprise = pygame.transform.scale(surprise, (15, 15))

def display_icons(screen):
    icons = [player, enemy1, enemy2, enemy3, gem, whip, teleport, chest, keys, power, clues, surprise, stairs]
    blit_y = 163
    for i, icon in enumerate(icons):
        icon = pygame.transform.scale(icon, (15, 15))
        screen.blit(icon, (40, blit_y + (i * 23)))

def flash(screen, text, WIDTH, HEIGHT):
    if (pygame.time.get_ticks() // 80) % 2 == 0:
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT - 15))