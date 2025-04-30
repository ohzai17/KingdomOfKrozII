import string
import os
import pygame
import utils
import gameplay as gp

char_map = {}
original_char_map = {}

# Define character sets
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_char_names = [
    "bullet", "colon", "comma", "cursor", "dash", "dollar", "doublequote", "equals", "exclamation",
    "minus", "paren_close", "paren_open", "percent", "period",
    "question", "shade", "singlequote", "slash", "space", "underscore", "special"
]
# Map special character names to their symbols
special_char_symbols = {
    "bullet": "•", "colon": ":", "comma": ",",
    "cursor": "█", "dash": "—", "dollar": "$", "doublequote": '"',
    "equals": "=", "exclamation": "!", "minus": "-", "paren_close": ")", "paren_open": "(",
    "percent": "%", "period": ".", "question": "?",
    "shade": "#", "singlequote": "'", "slash": "/", "space": " ", "underscore": "_",
    "special": "*"
}

def load_sprite(char_key, filename_base):
    filename = f"{filename_base}.png"
    full_path = os.path.join(utils.screen_assets_dir, filename)
    try:
        original_char_map[char_key] = pygame.image.load(full_path).convert_alpha()
    except pygame.error as e:
        print(f"Warning: Could not load image '{filename}': {e}")
    except FileNotFoundError:
        print(f"Warning: Image file not found: '{full_path}'")

# Load uppercase letters and digits
for char in uppercase_letters + digits:
    load_sprite(char, char)

# Load lowercase letters
for char in lowercase_letters:
    filename_base = f"l{char}"
    load_sprite(char, filename_base)

# Load special characters
for name in special_char_names:
    if name in special_char_symbols:
        char_symbol = special_char_symbols[name]
        load_sprite(char_symbol, name)
    else:
        print(f"Warning: No symbol mapping found for special character name: '{name}'")

def scale_loaded_sprites():
    """Scales all sprites stored in original_char_map and populates char_map."""
    global char_map # Ensure we are modifying the global char_map
    char_map.clear() # Clear any potentially pre-existing scaled sprites
    for char_key, original_sprite in original_char_map.items():
        try:
            resized_sprite = pygame.transform.scale(original_sprite, (gp.GP_TILE_WIDTH, gp.GP_TILE_HEIGHT))
            char_map[char_key] = resized_sprite
        except Exception as e:
            print(f"Error scaling sprite '{char_key}': {e}")

def game_text(row, text, text_color=None, flashing=False, center=True, text_background=None, title_box = False):
    """
    Draws a single row of text using character sprites onto the screen.

    Args:
        row (int): The grid row number (1-25) to draw the text on.
        text (str): The string of text to draw.
        text_color (tuple | str | None, optional): RGB color tuple for static text,
            the string "CHANGING" for cycling colors, or None to use the sprite's original color.
            Defaults to None.
        flashing (bool, optional): If True, make the text flash.
            Defaults to False.
        center (bool, optional): If True, center the text horizontally on the grid row.
            Defaults to True.
        text_background (tuple | str | None, optional): Background color specification.
            - None: No background.
            - (R, G, B): A tuple specifying the background color for all characters.
            - ("ONLY_TEXT", (R, G, B)): A tuple specifying the background color, drawn only behind non-space characters.
            Defaults to None.
        title_box (bool, optional): For special title screen background (uses the color from text_background).
    """
    y = (row * gp.GP_TILE_HEIGHT) - gp.GP_TILE_HEIGHT
    text_pixel_width = len(text) * gp.GP_TILE_WIDTH
    grid_pixel_width = utils.GAME_WIDTH * gp.GP_TILE_WIDTH

    if utils.hud_input == "O":
        grid_pixel_width = utils.WIDTH

    # Flashing
    current_time = pygame.time.get_ticks()
    is_visible = True
    if flashing:
        if (current_time // 250) % 2 != 0:
            is_visible = False

    if not is_visible:
        return

    # Centering
    start_x = 0
    if center:
        start_x = (grid_pixel_width - text_pixel_width) // 2
        # Ensure start_x is non-negative
        start_x = max(0, start_x)

    # Determine the actual text color to use
    current_actual_color = None # The color to apply to text sprites
    if text_color == "CHANGING":
        # Ensure the color list is not empty to avoid division by zero
        if utils.blinking_text_color_list:
            color_index = (current_time // 150) % len(utils.blinking_text_color_list)
            current_actual_color = utils.blinking_text_color_list[color_index]
        else:
            current_actual_color = None
            print("Warning: blinking_text_color_list is empty, cannot use 'CHANGING'.")
    elif isinstance(text_color, tuple): # Check if it's a static color tuple
        current_actual_color = text_color
    # If text_color is None or an invalid type, current_actual_color remains None

    # Determine background color and drawing condition
    actual_bg_color = None
    draw_bg_condition = lambda char: True # Default: draw if color exists
    if isinstance(text_background, tuple) and len(text_background) == 2 and \
        text_background[0] == "ONLY_TEXT" and isinstance(text_background[1], tuple):
        actual_bg_color = text_background[1]
        # Condition to draw background only if the character is not '*'
        draw_bg_condition = lambda char: char != '*' 
    elif isinstance(text_background, tuple): # Assume it's a direct color tuple
        actual_bg_color = text_background

    for i, char in enumerate(text):
        char_x = start_x + (i * gp.GP_TILE_WIDTH)

        # Ensure the character position is within the screen bounds horizontally
        if char_x + gp.GP_TILE_WIDTH <= 0 or char_x >= utils.screen.get_width():
             continue

        # Draw background first, based on the determined color and condition
        if actual_bg_color is not None and draw_bg_condition(char):
            # Determine background rectangle properties based on title_box
            if title_box:
                # Calculate extended Y position and height for title box style
                bg_y = y - int(0.5 * gp.GP_TILE_HEIGHT)
                bg_height = gp.GP_TILE_HEIGHT + int(0.5 * gp.GP_TILE_HEIGHT) + int(0.5 * gp.GP_TILE_HEIGHT)
                # Ensure calculated dimensions are non-negative
                bg_y = max(0, bg_y)
                bg_height = max(0, bg_height)
            else:
                # Standard background position and height
                bg_y = y
                bg_height = gp.GP_TILE_HEIGHT
            
            # Draw the background rectangle for the current character
            pygame.draw.rect(utils.screen, actual_bg_color, (char_x, bg_y, gp.GP_TILE_WIDTH, bg_height))

        if char in char_map:
            original_sprite = char_map[char]
            sprite_to_draw = original_sprite

            # Apply color modification if a color was determined
            if current_actual_color is not None:
                # Create a colored version
                color_surface = pygame.Surface(original_sprite.get_size(), pygame.SRCALPHA)
                # Fill with the target color
                color_surface.fill(current_actual_color)
                # Use the original sprite's alpha channel to mask the color
                color_surface.blit(original_sprite, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                sprite_to_draw = color_surface

            # Draw the character sprite (background was drawn above)
            utils.screen.blit(sprite_to_draw, (char_x, y))