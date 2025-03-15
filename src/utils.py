import pygame
import random
import os
import sys
import time
import numpy as np

screen = pygame.display.set_mode((832, 624))
pygame.display.set_caption("Kingdom of Kroz II")

# Colors used in the game
BLACK = (0, 0, 0)
BLUE = (8,4,180)
DARK_BLUE = (3, 3, 178)
OLD_BLUE = (44, 0, 180)
CYAN = (0, 255, 255)
GREEN = (0, 128, 0)
AQUA = (0, 242, 250)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 66, 77)
BROWN  = (139, 69, 19)
YELLOW = (254, 254, 6)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
MAGENTA = (255, 0, 255)
LIGHT_GRAY =  (150, 150, 150)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (0, 241, 54)
LIGHT_AQUA = (224, 255, 255)
LIGHT_RED = (255, 182, 193) 
LIGHT_PURPLE = (221, 160, 221)
LIGHT_YELLOW = (255, 255, 224)
DARK_RED = (140, 0, 0)

TILE_WIDTH = 14
TILE_HEIGHT = 14

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock() # Used in flash, returns the number of milliseconds since pygame.init()

square_size = 8 # Used for square bullets

logo_color_list = [RED, AQUA, PURPLE, YELLOW, LIGHT_BLUE, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
blinking_text_color_list = [AQUA, PURPLE, YELLOW, GRAY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
rect_colors = [BLACK, PURPLE, GRAY, RED, GREEN, BROWN]
flash_colors = [MAGENTA, YELLOW, WHITE]  # Colors 13-15 in VGA Palette

# Define the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, "assets")
audio_dir = os.path.join(assets_dir, "audio")
font_path = os.path.join(assets_dir, "PressStart2P - Regular.ttf")

pygame.font.init() # Initialize fonts
def load_font(size):
    return pygame.font.Font(font_path, size)

def load_fonts(sizes):
    return [pygame.font.Font(font_path, size) for size in sizes]

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

# Load tiles, used in title screens
enemy3 = pygame.image.load(os.path.join(assets_dir, "enemy3.png"))
keys = pygame.image.load(os.path.join(assets_dir, "keys.png"))
power = pygame.image.load(os.path.join(assets_dir, "power.png"))
clues = pygame.image.load(os.path.join(assets_dir, "clues.png"))
surprise = pygame.image.load(os.path.join(assets_dir, "surprise.png"))

# Scale tiles, used in title screens
enemy3 = pygame.transform.scale(enemy3, (15, 15))
keys = pygame.transform.scale(keys, (15, 15))
power = pygame.transform.scale(power, (15, 15))
clues = pygame.transform.scale(clues, (15, 15))
surprise = pygame.transform.scale(surprise, (15, 15))

# Load tiles
block = pygame.image.load(os.path.join(assets_dir, "block.png"))
chest = pygame.image.load(os.path.join(assets_dir, "chest.png"))
enemy1 = pygame.image.load(os.path.join(assets_dir, "enemy1.png"))
enemy2 = pygame.image.load(os.path.join(assets_dir, "enemy2.png"))
gem = pygame.image.load(os.path.join(assets_dir, "gem.png"))
player = pygame.image.load(os.path.join(assets_dir, "player.png"))
stairs = pygame.image.load(os.path.join(assets_dir, "stairs.png"))
teleport = pygame.image.load(os.path.join(assets_dir, "teleport.png"))
trap = pygame.image.load(os.path.join(assets_dir, "trap.png"))
wall = pygame.image.load(os.path.join(assets_dir, "wall.png"))
whip = pygame.image.load(os.path.join(assets_dir, "whip.png"))

# Scale tiles
block    = pygame.transform.scale(block,    (TILE_WIDTH, TILE_HEIGHT))
chest    = pygame.transform.scale(chest,    (TILE_WIDTH, TILE_HEIGHT))
enemy1   = pygame.transform.scale(enemy1,   (TILE_WIDTH, TILE_HEIGHT))
enemy2   = pygame.transform.scale(enemy2,   (TILE_WIDTH, TILE_HEIGHT))
gem      = pygame.transform.scale(gem,      (TILE_WIDTH, TILE_HEIGHT))
player   = pygame.transform.scale(player,   (TILE_WIDTH, TILE_HEIGHT))
stairs   = pygame.transform.scale(stairs,   (TILE_WIDTH, TILE_HEIGHT))
teleport = pygame.transform.scale(teleport, (TILE_WIDTH, TILE_HEIGHT))
trap     = pygame.transform.scale(trap,     (TILE_WIDTH, TILE_HEIGHT))
wall     = pygame.transform.scale(wall,     (TILE_WIDTH, TILE_HEIGHT))
whip     = pygame.transform.scale(whip,     (TILE_WIDTH, TILE_HEIGHT))

def display_icons(screen):
    icons = [player, enemy1, enemy2, enemy3, gem, whip, teleport, chest, keys, power, clues, surprise, stairs]
    blit_y = 163
    for i, icon in enumerate(icons):
        icon = pygame.transform.scale(icon, (15, 15))
        screen.blit(icon, (40, blit_y + (i * 23)))

def flash(screen, text, WIDTH, HEIGHT): # Text disappear and appear rapidly
    if (pygame.time.get_ticks() // 80) % 2 == 0:
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT - 15))

def flash_color(screen, message):
    current_time = pygame.time.get_ticks()
    color = flash_colors[(current_time // 60) % len(flash_colors)]
    font = load_font(14)

    text_surface = font.render(message, True, color)  # Render text with current color
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)
        
def play_sound(frequency, duration, amplitude=4096):
    sample_rate = 44100
    n_samples = int(sample_rate * duration / 1000)
    t = np.linspace(0, duration / 1000, n_samples, False)
    wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    stereo_wave = np.column_stack((wave, wave))
    sound = pygame.sndarray.make_sound(stereo_wave.astype(np.int16))
    sound.play()
    time.sleep(duration / 1000)
    sound.stop()
        
def play_wav(file_name):
    file_path = os.path.join(audio_dir, file_name)
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    while pygame.mixer.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.time.delay(100)

def descent():
    play_wav('beginDescent.wav')
        