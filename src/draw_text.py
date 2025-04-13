import string
from utils import *

char_map = {}

# Define character sets
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_char_names = [
    "ampersand", "asterisk", "at", "backslash", "brace_close", "brace_open",
    "bracket_closed", "bracket_open", "bullet", "caret", "colon", "comma", "cursor",
    "dash", "dollar", "doublequote", "equals", "exclamation", "greater",
    "less", "minus", "paren_close", "paren_open", "percent", "period", "pipe",
    "question", "semicolon", "shade", "singlequote", "slash", "space", "tilde", "underscore"
]
# Map special character names to their symbols
special_char_symbols = {
    "ampersand": "&", "asterisk": "*", "at": "@", "backslash": "\\",
    "brace_close": "}", "brace_open": "{", "bracket_closed": "]",
    "bracket_open": "[", "bullet": "•", "caret": "^", "colon": ":", "comma": ",",
    "cursor": "█", "dash": "—", "dollar": "$", "doublequote": '"',
    "equals": "=", "exclamation": "!", "greater": ">",
    "less": "<", "minus": "-", "paren_close": ")", "paren_open": "(",
    "percent": "%", "period": ".", "pipe": "|", "question": "?", "semicolon": ";",
    "shade": "#", "singlequote": "'", "slash": "/", "space": " ", "tilde": "~", "underscore": "_"
}

def load_sprite(char_key, filename_base):
    filename = f"{filename_base}.png"
    full_path = os.path.join(screen_assets_dir, filename)
    try:
        sprite = pygame.image.load(full_path).convert_alpha()
        char_map[char_key] = sprite
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

def draw_text(row, text, text_color=None, flashing=False, center=True, text_background=None, title_box = False):
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
        text_background (tuple, optional): RGB color tuple for the background behind each char.
            Defaults to None.
    """
    y = (row * CHAR_HEIGHT) - CHAR_HEIGHT
    text_pixel_width = len(text) * CHAR_WIDTH
    grid_pixel_width = GRID_WIDTH * CHAR_WIDTH

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

    # Determine the actual color to use
    current_actual_color = None # The color to apply
    if text_color == "CHANGING":
        # Ensure the color list is not empty to avoid division by zero
        if blinking_text_color_list:
            color_index = (current_time // 150) % len(blinking_text_color_list)
            current_actual_color = blinking_text_color_list[color_index]
        else:
            current_actual_color = None
            print("Warning: blinking_text_color_list is empty, cannot use 'CHANGING'.")
    elif isinstance(text_color, tuple): # Check if it's a static color tuple
        current_actual_color = text_color
    # If text_color is None or an invalid type, current_actual_color remains None

    # Draw the special "title" background before drawing characters if specified
    if title_box:
        bg_x = start_x
        # Calculate extended Y position and height
        bg_y = y - int(0.5 * CHAR_HEIGHT)
        bg_height = CHAR_HEIGHT + int(0.5 * CHAR_HEIGHT) + int(0.5 * CHAR_HEIGHT) # Or simply 2 * CHAR_HEIGHT if integer extensions guaranteed
        bg_width = text_pixel_width
        # Ensure calculated dimensions are non-negative
        bg_y = max(0, bg_y)
        bg_height = max(0, bg_height)
        bg_width = max(0, bg_width)
        # Draw the single background rectangle for the title
        pygame.draw.rect(screen, text_background, (bg_x, bg_y, bg_width, bg_height))

    for i, char in enumerate(text):
        char_x = start_x + (i * CHAR_WIDTH)

        # Ensure the character position is within the screen bounds horizontally
        if char_x + CHAR_WIDTH <= 0 or char_x >= screen.get_width():
             continue

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

            # Draw background if specified
            if text_background is not None:
                pygame.draw.rect(screen, text_background, (char_x, y, CHAR_WIDTH, CHAR_HEIGHT))

            # Draw the character sprite
            screen.blit(sprite_to_draw, (char_x, y))

        else:
             if text_background is not None:
                 pygame.draw.rect(screen, text_background, (char_x, y, CHAR_WIDTH, CHAR_HEIGHT))