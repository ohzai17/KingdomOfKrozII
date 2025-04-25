import pygame
import random
import os
import time
import json
import sys
import numpy as np

pygame.init()
pygame.mixer.init()
# 16:9
WIDTH, HEIGHT = 1200, 1
HEIGHT = int(WIDTH * 9 / 16)
resolution = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
GRID_WIDTH, GRID_HEIGHT = 80, 25
TILE_WIDTH, TILE_HEIGHT = WIDTH // 66, WIDTH // 66
CHAR_WIDTH, CHAR_HEIGHT = WIDTH / 80, HEIGHT / 25 - 0.1 # Fix cutoff text
pygame.display.set_caption("Kingdom of Kroz II")

def rgb(r, g, b):
    return (r, g, b)

# Colors used in the game
BLACK = rgb(0, 0, 0)
BLUE = rgb(8,4,180)
DARK_BLUE = rgb(3, 3, 178)
OLD_BLUE = rgb(44, 0, 180)
CYAN = rgb(0, 255, 255)
GREEN = rgb(0, 128, 0)
AQUA = rgb(0, 242, 250)
RED = rgb(255, 0, 0)
PURPLE = rgb(128, 0, 128)
ORANGE = rgb(255, 66, 77)
BROWN  = rgb(170, 85, 0)
YELLOW = rgb(254, 254, 6)
WHITE = rgb(255, 255, 255)
GRAY = rgb(128, 128, 128)
SILVER = rgb(192, 192, 192)
MAGENTA = rgb(255, 0, 255)
LIGHT_GRAY = rgb(150, 150, 150)
LIGHT_BLUE = rgb(173, 216, 230)
LIGHT_GREEN = rgb(0, 241, 54)
LIGHT_AQUA = rgb(224, 255, 255)
LIGHT_RED = rgb(255, 182, 193) 
LIGHT_PURPLE = rgb(221, 160, 221)
LIGHT_YELLOW = rgb(255, 255, 224)
DARK_RED = rgb(140, 0, 0)
BACKGROUND = BLUE

TILE_WIDTH, TILE_HEIGHT = WIDTH // 66, WIDTH // 66

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock() # Used in flash, returns the number of milliseconds since pygame.init()

square_size = 8 # Used for square bullets

logo_color_list = [RED, AQUA, PURPLE, YELLOW, LIGHT_BLUE, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
blinking_text_color_list = [AQUA, PURPLE, YELLOW, GRAY, BLUE, GREEN, RED, PURPLE, YELLOW]
rect_colors_list = [BLACK, PURPLE, GRAY, RED, GREEN, BROWN]
rect_colors = [BLACK, PURPLE, GRAY, RED, GREEN, BROWN]
flash_colors = [MAGENTA, YELLOW, WHITE]  # Colors 13-15 in VGA Palette

# Random rectangle Colors to cycle through 
rect_colors_cycle = rect_colors_list
rand_color = random.choice(rect_colors_cycle)

# Define the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
saves_dir = os.path.join(base_dir, "saves")
assets_dir = os.path.join(base_dir, "assets")
screen_assets_dir = os.path.join(assets_dir, "screens_assets")
audio_dir = os.path.join(assets_dir, "audio")
font_path = os.path.join(assets_dir, "PressStart2P - Regular.ttf")
logo_path = os.path.join(assets_dir, "kroz_logo.png")

def set_monochrome_palette():
    global BACKGROUND, BLUE, DARK_BLUE, OLD_BLUE, CYAN, GREEN, AQUA, RED, PURPLE, ORANGE, BROWN, YELLOW, WHITE, GRAY, MAGENTA, LIGHT_GRAY, LIGHT_BLUE,LIGHT_GREEN, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW, DARK_RED
    BACKGROUND = BLACK
    BLUE = rgb(8,4,180)
    DARK_BLUE = rgb(3, 3, 178)
    OLD_BLUE = rgb(44, 0, 180)
    CYAN = rgb(0, 255, 255)
    GREEN = rgb(0, 128, 0)
    AQUA = rgb(0, 242, 250)
    RED = rgb(255, 0, 0)
    PURPLE = rgb(128, 0, 128)
    ORANGE = rgb(255, 66, 77)
    BROWN  = rgb(139, 69, 19)
    YELLOW = rgb(254, 254, 6)
    WHITE = rgb(255, 255, 255)
    GRAY = rgb(128, 128, 128)
    MAGENTA = rgb(255, 0, 255)
    LIGHT_GRAY =  (150, 150, 150)
    LIGHT_BLUE = rgb(173, 216, 230)
    LIGHT_GREEN = rgb(0, 241, 54)
    LIGHT_AQUA = rgb(224, 255, 255)
    LIGHT_RED = rgb(255, 182, 193) 
    LIGHT_PURPLE = rgb(221, 160, 221)
    LIGHT_YELLOW = rgb(255, 255, 224)
    DARK_RED = rgb(140, 0, 0)

pygame.font.init()
def load_font(size):
    return pygame.font.Font(font_path, size)

def apply_grayscale(image):
    grayscale_image = pygame.Surface(image.get_size(), pygame.SRCALPHA) # Create alpha channel over image
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r, g, b, a = image.get_at((x, y))
            gray_formula = int(0.299 * r + 0.587 * g + 0.114 * b) # Standard grayscale formula
            gray = min(255, gray_formula + 70) # Increase brightness
            grayscale_image.set_at((x, y), (gray, gray, gray, a))
    return grayscale_image

def apply_grayscale_f(surface):
    surface = surface.convert()  # Ensures it's in the RGB format (or RGBA)
    
    arr_rgb = pygame.surfarray.pixels3d(surface).copy()
    arr_alpha = pygame.surfarray.pixels_alpha(surface).copy() if surface.get_flags() & pygame.SRCALPHA else None

    # Apply grayscale formula
    gray = (0.3 * arr_rgb[:, :, 0] + 0.59 * arr_rgb[:, :, 1] + 0.11 * arr_rgb[:, :, 2]).astype("uint8")
    gray_3ch = np.stack((gray,)*3, axis=-1)

    # Create a new surface with the same size as the original surface and with alpha support
    gray_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    pygame.surfarray.blit_array(gray_surface, gray_3ch)

    # If the original surface had an alpha channel, restore it
    if arr_alpha is not None:
        pygame.surfarray.pixels_alpha(gray_surface)[:, :] = arr_alpha

    return gray_surface

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
enemy3 = pygame.image.load(os.path.join(assets_dir, "enemy3.png"))
keys = pygame.image.load(os.path.join(assets_dir, "keys.png"))
power = pygame.image.load(os.path.join(assets_dir, "power.png"))
clues = pygame.image.load(os.path.join(assets_dir, "clues.png"))
surprise = pygame.image.load(os.path.join(assets_dir, "surprise.png"))

# Scale tiles
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

def flash(screen, text, WIDTH, HEIGHT):
    if (pygame.time.get_ticks() // 80) % 2 == 0:
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT - 15))

def flash_c(screen, message):
    current_time = pygame.time.get_ticks()
    color = flash_colors[(current_time // 25) % len(flash_colors)]
    font = load_font(12)

    text_surface = font.render(message, True, color)  # Render text with current color
    text_rect = text_surface.get_rect(midbottom=(screen.get_width() // 2, screen.get_height() - 190))
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
    
def footStep():
    sound_file = random.choice(['footStep_1.wav', 'footStep_2.wav'])
    play_wav(sound_file)
    
def enemyCollision():
    play_wav('enemyCollision.wav')    


def wait_input(screen):
    paused = True

    while paused:
        message = "PRESS ANY KEY TO THIS LEVEL." 
        flash_c(screen, message)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                paused = False
                return
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()    