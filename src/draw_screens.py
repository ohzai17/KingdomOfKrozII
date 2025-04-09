from utils import *

# --- Configuration ---
# Screen grid dimensions
GRID_WIDTH = 80
GRID_HEIGHT = 25

# Text size based on screen resolution
TEXT_WIDTH = WIDTH // 80
TEXT_HEIGHT = HEIGHT // 25

# Characters to load sprites for
CHARACTERS_TO_LOAD = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
    "abcdefghijklmnopqrstuvwxyz" +
    "0123456789" +
    ".,;:!?\"'#$%&()*+-/=<>[]{}@^_|~ "
)
# Map problematic filenames (like ".") to safe names
FILENAME_MAP = {
    'a': 'la',
    'b': 'lb',
    'c': 'lc',
    'd': 'ld',
    'e': 'le',
    'f': 'lf',
    'g': 'lg',
    'h': 'lh',
    'i': 'li',
    'j': 'lj',
    'k': 'lk',
    'l': 'll',
    'm': 'lm',
    'n': 'ln',
    'o': 'lo',
    'p': 'lp',
    'q': 'lq',
    'r': 'lr',
    's': 'ls',
    't': 'lt',
    'u': 'lu',
    'v': 'lv',
    'w': 'lw',
    'x': 'lx',
    'y': 'ly',
    'z': 'lz',
    '.': 'period',
    ',': 'comma',
    ';': 'semicolon',
    ':': 'colon',
    '!': 'exclamation',
    '?': 'question',
    '"': 'doublequote',
    "'": 'singlequote',
    '#': 'hash',
    '$': 'dollar',
    '%': 'percent',
    '&': 'ampersand',
    '(': 'paren_open',
    ')': 'paren_close',
    '*': 'asterisk',
    '+': 'plus',
    '-': 'minus',
    '/': 'slash',
    '=': 'equals',
    '<': 'less',
    '>': 'greater',
    '[': 'bracket_open',
    ']': 'bracket_close',
    '{': 'brace_open',
    '}': 'brace_close',
    '@': 'at',
    '^': 'caret',
    '_': 'underscore',
    '|': 'pipe',
    '~': 'tilde',
    ' ': 'space'
}

def load_character_sprites():

    char_map = {}
    if not os.path.isdir(screens_assets_dir):
        print(f"Error: Assets directory not found at {screens_assets_dir}")
        return char_map

    print(f"Loading character sprites from: {screens_assets_dir}") # Debug print

    for char in CHARACTERS_TO_LOAD:
        filename_char = FILENAME_MAP.get(char, char) # Use mapped name if available
        # Assume PNG format
        filepath = os.path.join(screens_assets_dir, f"{filename_char}.png")

        try:
            # Load image with alpha transparency
            image = pygame.image.load(filepath).convert_alpha()
            # Scale image
            scaled_image = pygame.transform.scale(image, (TEXT_WIDTH, TEXT_HEIGHT))
            char_map[char] = scaled_image
        except pygame.error as e:
            print(f"Warning: Could not load or scale sprite for character '{char}' from {filepath}: {e}")
        except FileNotFoundError:
             print(f"Warning: Sprite file not found for character '{char}' at {filepath}")

    if not char_map:
        print("Error: No character sprites were loaded.")
    else:
        print(f"Loaded {len(char_map)} character sprites.")

    # Ensure space character has a sprite, even if just transparent
    if ' ' not in char_map:
        space_surface = pygame.Surface((TEXT_WIDTH, TEXT_HEIGHT), pygame.SRCALPHA)
        space_surface.fill((0,0,0,0)) # Fully transparent
        char_map[' '] = space_surface
        print("Created placeholder for space character.")


    return char_map

def draw_string(screen, text_string, char_map, text_color, bg_color, row, center=False, blink=False):
    """
    Draws a string to the screen using pre-loaded character sprites.

    Args:
        screen (pygame.Surface): The main screen surface to draw on.
        text_string (str): The string to draw.
        char_map (dict): The dictionary mapping characters to sprite Surfaces.
        text_color (tuple): RGB tuple for the text color.
        bg_color (tuple): RGB tuple for the background color of each character cell.
        row (int): The grid row number (1 to GRID_HEIGHT) to draw the text on.
        center (bool): If True, centers the string horizontally on the screen.
        blink (bool): If True, makes the text blink on and off.
    """
    if not char_map:
        print("Error in draw_string: Character map is empty.")
        return

    screen_width, screen_height = screen.get_size()
    # Calculate cell dimensions based on screen size and grid
    cell_width = screen_width // GRID_WIDTH
    cell_height = screen_height // GRID_HEIGHT

    # Calculate starting Y position based on row (adjust for 0-based index)
    start_y = (row - 1) * cell_height

    # Calculate starting X position
    if center:
        string_width_pixels = len(text_string) * cell_width
        start_x = (screen_width - string_width_pixels) // 2
    else:
        start_x = 0 # Start at the left edge

    # Blinking logic
    if blink:
        # Blink roughly twice a second (adjust 500 for speed)
        show_blink = (pygame.time.get_ticks() // 250) % 2 == 0
        if not show_blink:
            return # Don't draw anything if in the 'off' blink cycle

    current_x = start_x
    for char in text_string:
        if char in char_map:
            sprite_surface = char_map[char]

            # Determine the actual size to scale the sprite to (fit the cell)
            # This assumes TEXT_WIDTH/HEIGHT might be different from cell_width/height
            sprite_render_width = cell_width
            sprite_render_height = cell_height
            # Scale the original sprite from char_map if needed
            if sprite_surface.get_size() != (sprite_render_width, sprite_render_height):
                 try:
                     scaled_sprite = pygame.transform.scale(sprite_surface, (sprite_render_width, sprite_render_height))
                 except pygame.error as e:
                     print(f"Error scaling sprite for '{char}': {e}")
                     scaled_sprite = sprite_surface # Fallback to original
            else:
                scaled_sprite = sprite_surface

            # Create background surface for this character cell
            cell_surface = pygame.Surface((cell_width, cell_height))
            cell_surface.fill(bg_color)

            # Create a tinted version of the sprite
            # Make a copy to avoid modifying the original in char_map
            tinted_sprite = scaled_sprite.copy()
            # Apply tint using BLEND_RGB_MULT for colorization effect
            tinted_sprite.fill(text_color, special_flags=pygame.BLEND_RGB_MULT)

            # Blit the tinted sprite onto the cell background
            # Center the sprite within the cell if sprite size < cell size
            sprite_x_offset = (cell_width - sprite_render_width) // 2
            sprite_y_offset = (cell_height - sprite_render_height) // 2
            cell_surface.blit(tinted_sprite, (sprite_x_offset, sprite_y_offset))

            # Blit the character cell onto the main screen
            screen.blit(cell_surface, (current_x, start_y))

            # Move to the next character position
            current_x += cell_width
        else:
            # Handle characters not in char_map (e.g., draw a placeholder or skip)
            # Skipping for now:
            current_x += cell_width