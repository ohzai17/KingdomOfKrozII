import pygame
import random
import os
import time
import json
import sys
import numpy as np

pygame.init()
# 16:9
WIDTH, HEIGHT = 1452, 1
HEIGHT = int(WIDTH * 9 / 16)
resolution = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
GRID_WIDTH, GRID_HEIGHT = 80, 25
GAME_WIDTH = 66
TILE_WIDTH, TILE_HEIGHT = 0, 0
CHAR_WIDTH, CHAR_HEIGHT = WIDTH / 80, HEIGHT / 25
pygame.display.set_caption("Kingdom of Kroz II")

color_input = ""
difficulty_input = ""
hud_input = ""

def rgb(r, g, b):
    return (r, g, b)

# Colors used in the game
BLACK = rgb(0, 0, 0)
DARK_GRAY = rgb(85, 85, 85)
BLUE = rgb(0, 0, 170)
LIGHT_BLUE = rgb(85, 85, 255)
GREEN = (0, 170, 0)
LIGHT_GREEN = rgb(85, 255, 85)
CYAN = (0, 170, 170)
LIGHT_CYAN = (85, 255, 255)
RED = rgb(170, 0, 0)
LIGHT_RED = rgb(255, 85, 85)
MAGENTA = rgb(170, 0, 170)
LIGHT_MAGENTA = rgb(255, 85, 255)
BROWN = rgb(170, 85, 0)
YELLOW = rgb(255, 255, 85)
LIGHT_GRAY = rgb(170, 170, 170)
WHITE = rgb(255, 255, 255)
BACKGROUND = BLUE

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock() # Used in flash, returns the number of milliseconds since pygame.init()

square_size = 8 # Used for square bullets

logo_color_list = [DARK_GRAY, BLUE, LIGHT_BLUE, GREEN, LIGHT_GREEN, CYAN, LIGHT_CYAN, RED, LIGHT_RED, MAGENTA, LIGHT_MAGENTA, BROWN, YELLOW, LIGHT_GRAY, WHITE]
blinking_text_color_list = [BLACK, DARK_GRAY, BLUE, LIGHT_BLUE, GREEN, LIGHT_GREEN, CYAN, LIGHT_CYAN, RED, LIGHT_RED, MAGENTA, LIGHT_MAGENTA, BROWN, YELLOW, LIGHT_GRAY, WHITE]
flash_colors = [MAGENTA, YELLOW, WHITE]  # Colors 13-15 in VGA Palette
whip_cycle_colors = [RED, YELLOW, GREEN, BLUE, CYAN, MAGENTA, WHITE]

rand_color = random.choice(logo_color_list)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # Base path is the root of the temporary folder
        base_path = sys._MEIPASS
        # Spec file places assets in 'src/assets' relative to bundle root
        final_path = os.path.join(base_path, 'src', 'assets', relative_path)
        # print(f"DEBUG (Bundled): final='{final_path}'") # Optional bundle debug

    except Exception:
        # utils.py is directly inside 'src'. Assets are in 'src/assets'.
        src_dir = os.path.dirname(os.path.abspath(__file__)) # This IS the 'src' directory
        assets_folder = os.path.join(src_dir, 'assets')      # Correctly gets 'src/assets'
        final_path = os.path.join(assets_folder, relative_path) # Joins 'src/assets' with the relative file path
        # --- End Correction ---

    return final_path

# --- Asset Paths (Using resource_path) ---
# Pass the path *relative* to the 'assets' folder structure defined in the spec file ('src/assets')
sprites_dir = resource_path("sprites")
screen_assets_dir = resource_path("screens_assets")
audio_dir = resource_path("audio")
font_path = resource_path("PressStart2P-Regular.ttf") # Font path relative to assets
logo_path = resource_path("kroz_logo.png")           # Logo path relative to assets
right_hud_path = resource_path("right_hud.png")
bottom_hud_path = resource_path("original_hud.png")

# --- Saves Directory Handling ---
# Saves should NOT use resource_path, as they shouldn't be bundled inside.
try:
    if getattr(sys, 'frozen', False):
        # Running bundled: Create saves next to the .app or executable directory
        if sys.platform == "darwin":
            # Correct path for saves next to .app bundle
            app_dir = os.path.dirname(os.path.dirname(os.path.dirname(sys.executable)))
            saves_dir = os.path.join(app_dir, "saves") # Put in a clearly named folder
        else:
            # Windows/Linux: Create saves next to executable
            app_dir = os.path.dirname(sys.executable)
            saves_dir = os.path.join(app_dir, "saves")
    else:
        # Running from source: Use original location relative to project root
        # Assumes utils.py is in src/utilities
        project_root_dev = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        saves_dir = os.path.join(project_root_dev, "src", "saves") # Original location

    # --- Ensure saves directory exists at runtime ---
    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)
        # print(f"Created saves directory at: {saves_dir}") # Optional info message

    leaderboard_path = os.path.join(saves_dir, "leaderboard.json")

except Exception as e:
    print(f"ERROR: Could not set up saves directory: {e}")
    print("Saving/loading might fail.")
    leaderboard_path = None # Indicate saving might be broken
    saves_dir = None

def format_centered_int(value, width) -> str:
    s_value = str(value)
    padding = width - len(s_value)
    if padding < 0:
        return s_value
    left_padding = padding // 2
    right_padding = (padding + 1) // 2
    return ' ' * left_padding + s_value + ' ' * right_padding

def set_monochrome_palette():
    global BACKGROUND, BLACK, DARK_GRAY, BLUE, LIGHT_BLUE, GREEN, LIGHT_GREEN, CYAN, LIGHT_CYAN, RED, LIGHT_RED, MAGENTA, LIGHT_MAGENTA, BROWN, YELLOW, LIGHT_GRAY, WHITE
    BACKGROUND = BLACK
    BLACK = rgb(0, 0, 0)
    DARK_GRAY = rgb(85, 85, 85)
    BLUE = rgb(0, 0, 170)
    LIGHT_BLUE = rgb(85, 85, 255)
    GREEN = (0, 170, 0)
    LIGHT_GREEN = rgb(85, 255, 85)
    CYAN = (0, 170, 170)
    LIGHT_CYAN = (85, 255, 255)
    RED = rgb(170, 0, 0)
    LIGHT_RED = rgb(255, 85, 85)
    MAGENTA = rgb(170, 0, 170)
    LIGHT_MAGENTA = rgb(255, 85, 255)
    BROWN = rgb(170, 85, 0)
    YELLOW = rgb(255, 255, 85)
    LIGHT_GRAY = rgb(170, 170, 170)
    WHITE = rgb(255, 255, 255)

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

last_interval_index = -1
last_random_color = None

def change_logo_color(image, time, color_user_input):
    global last_interval_index, last_random_color # Use global variables to store state

    if color_user_input == "M":
        # Reset state if switching to monochrome
        last_interval_index = -1
        last_random_color = None
        return apply_grayscale(image)
    else:
        # Calculate the current time interval index (changes every 300ms)
        current_interval_index = time // 100

        # Check if the interval has changed since the last call
        if current_interval_index != last_interval_index:
            # If it changed, pick a new random color
            current_color = random.choice(logo_color_list)
            # Store the new color and the current interval index
            last_random_color = current_color
            last_interval_index = current_interval_index
        else:
            # If still within the same interval, use the previously chosen color
            current_color = last_random_color

        # Ensure a color was selected (handles the very first call)
        if current_color is None:
             current_color = random.choice(logo_color_list)
             last_random_color = current_color
             last_interval_index = current_interval_index

        # --- Original tinting logic ---
        color_filter = pygame.Surface(image.get_size()) # Create imaging surface
        color_filter.fill(current_color)
        colorized_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        colorized_image.blit(image, (0, 0))
        colorized_image.blit(color_filter, (0, 0), special_flags=pygame.BLEND_RGB_MULT) # Apply color filter
        return colorized_image

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