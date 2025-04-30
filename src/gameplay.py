from maps import *
from utils import *
from game_text import game_text
from audio import enemyCollision, electricWall, whip as whip_audio, footStep, zeroCollecible, teleportTrap, chestPickup

GP_TILE_WIDTH, GP_TILE_HEIGHT = 0, 0
LOGICAL_GRID_WIDTH, LOGICAL_GRID_HEIGHT = 64, 23
"""
game_text(row, text, text_color=None, flashing=False, center=True, text_background=None, title_box = False)
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

# Global dictionaries for sprite management
original_images = {}
tile_mapping = {}

# Load unscaled sprites at runtime
sprites = ["border", "block", "chest", "enemy1", "enemy2", "enemy3", "gem", "player", "teleport_player","stairs", "teleport",
            "trap", "wall", "whip", "slowTime", "invisible", "key", "door", "speedTime", "river",
            "power", "forest", "tree", "bomb", "lava", "pit", "tome", "tunnel", "freeze", "nugget",
            "quake", "iBlock", "iWall", "iDoor", "stop", "trap2", "zap", "create", "generator",
            "trap3", "mBlock", "trap4", "showGems", "tablet", "zBlock", "blockSpell", "chance",
            "statue", "wallVanish", "krozK", "krozR", "krozO", "krozZ", "oWall1", "oWall2", "oWall3",
            "cWall1", "cWall2", "cWall3", "oSpell1", "oSpell2", "oSpell3", "cSpell1", "cSpell2",
            "cSpell3", "gBlock", "rock", "eWall", "trap5", "tBlock", "tRock", "tGem", "tBlind",
            "tWhip", "tGold", "tTree", "rope", "dropRope1", "dropRope2", "dropRope3", "dropRope4",
            "dropRope5", "amulet", "shootRight", "shootLeft", "trap6", "trap7", "trap8", "trap9",
            "trap10", "trap11", "trap12", "trap13", "message", "whip1", "whip2", "whip3", "whip4"]

special_cases = {
    "enemy1": "enemy1a",
    "enemy2": "enemy2a"
}

for sprite_name in sprites:
    filename = special_cases.get(sprite_name, sprite_name) + ".png"
    full_path = os.path.join(assets_dir, filename) # Use assets_dir from utils
    try:
        img = pygame.image.load(full_path).convert_alpha() # Use convert_alpha() for potential transparency
        original_images[sprite_name] = img
    except pygame.error as e:
        print(f"Warning: Could not load image '{filename}' for sprite '{sprite_name}': {e}")
    except FileNotFoundError:
        print(f"Warning: Image file not found: '{full_path}' for sprite '{sprite_name}'")

def scale_gameplay_sprites(dimensions, color_input):
    """
    Scales sprites from original_images, applies grayscale if needed,
    and populates the global tile_mapping dictionary.
    """
    global tile_mapping
    tile_mapping.clear() # Clear existing scaled sprites

    tile_width, tile_height = dimensions

    # Define the mapping from characters to sprite names here
    char_to_sprite_map = {
        "^": "border", "X": "block", "#": "wall", "C": "chest", "W": "whip",
        "1": "enemy1", "2": "enemy2", "3": "enemy3", "+": "gem", "T": "teleport",
        "_": "teleport_player", ".": "trap", "L": "stairs", "P": "player",
        "TP": "teleport_player",
        "S": "slowTime", "I": "invisible", "K": "key", "D": "door", "F": "speedTime",
        "R": "river", "Q": "power", "/": "forest", "J": "tree", "B": "bomb",
        "V": "lava", "=": "pit", "A": "tome", "U": "tunnel", "Z": "freeze",
        "*": "nugget", "E": "quake", ";": "iBlock", ":": "iWall", "`": "iDoor",
        "-": "stop", "@": "trap2", "%": "zap", "]": "create", "G": "generator",
        ")": "trap3", "M": "mBlock", "(": "trap4", "&": "showGems", "!": "tablet",
        "O": "zBlock", "H": "blockSpell", "?": "chance", ">": "statue", "N": "wallVanish",
        "<": "krozK", "[": "krozR", "|": "krozO", ",": "krozZ", "4": "oWall1",
        "5": "oWall2", "6": "oWall3", "7": "cWall1", "8": "cWall2", "9": "cWall3",
        "±": "oSpell1", "≥": "oSpell2", "≤": "oSpell3", "⌠": "cSpell1", "⌡": "cSpell2",
        "÷": "cSpell3", "Y": "gBlock", "0": "rock", "~": "eWall", "$": "trap5",
        "æ": "tBlock", "Æ": "tRock", "ô": "tGem", "ö": "tBlind", "ò": "tWhip",
        "û": "tGold", "ù": "tTree", "¿": "rope", "┤": "dropRope1", "│": "dropRope2",
        "┐": "dropRope3", "┘": "dropRope4", "╜": "dropRope5", "â": "amulet",
        "»": "shootRight", "«": "shootLeft", "α": "trap6", "β": "trap7", "┌": "trap8",
        "π": "trap9", "∑": "trap10", "σ": "trap11", "μ": "trap12", "τ": "trap13",
        "ⁿ": "message",
        "whip1": "whip1", "whip2": "whip2", "whip3": "whip3", "whip4": "whip4"
    }

    for char, sprite_name in char_to_sprite_map.items():
        if sprite_name in original_images:
            original_img = original_images[sprite_name]
            scaled_img = pygame.transform.scale(original_img, (tile_width, tile_height))

            if color_input == "M":
                # Apply grayscale using the function from utils
                scaled_img = apply_grayscale_f(scaled_img)

            tile_mapping[char] = scaled_img
        else:
            print(f"Warning: Original image for sprite '{sprite_name}' (char '{char}') not found in original_images.")

def pause_quit(quitting=False): # From KINGDOM.PAS (lines 49-69)
    paused = True

    while paused:
        message = "Are you sure you want to quit (Y/N)?" if quitting else "Press any key to Resume"
        game_text(25, message, "CHANGING", False, True, BLACK)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if quitting:
                    if event.key == pygame.K_y:
                        from screens import sign_off
                        sign_off()
                        return True
                    else:
                        paused = False
                else:
                    paused = False  # Resume game

    return False  # User didn't quit

# Player Death Function (Copied from gameplayOLD.py.txt for dependency, may need adjustment if not used)
def player_death(score, level_num):
    """Handle player death when out of gems"""
    print("you have died")

    pygame.event.clear()  # Clear any pending events

    # Display death message on screen
    game_text(1, "YOU HAVE DIED!!!", BLACK, True, True, LIGHT_GRAY)
    game_text(16, "Press any key to continue...", WHITE, False, True, None)
    pygame.display.flip()

    pygame.time.delay(500)  # Pause to show message

    # Wait for user input
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting_for_input = False  # Exit loop on any key press

    # Go to leaderboard screen with score and level
    from screens import leaderboard_screen
    leaderboard_screen(score, level_num) # Adjusted call for current structure
    pygame.quit()
    exit()

def draw_hud(values=None, color_input="C", hud_input="O"): # From KINGDOM4.INC (lines 96-183)
    BACKGROUND = BLUE
    TEXT = YELLOW
    VALUE_TEXT = DARK_RED
    TEXT_BOX = LIGHT_GRAY
    OPTIONS_TEXT = LIGHT_AQUA
    OPTIONS_BOX = DARK_RED

    option_list = ["Whip", "Teleport", "Cloak", "Pause", "Quit", "Save", "Restore"]

    is_monochrome = True if color_input == "M" else False

    if is_monochrome:
        BACKGROUND = BLACK
        TEXT = GRAY
        VALUE_TEXT = GRAY
        TEXT_BOX = BLACK
        OPTIONS_TEXT = GRAY
        OPTIONS_BOX = BLACK

    if hud_input == "O":
        pygame.draw.rect(screen, BACKGROUND, (0, (GP_TILE_HEIGHT * 25), WIDTH, HEIGHT - (GP_TILE_HEIGHT * 25)))
        game_text(29, "         Level", TEXT, False, False)
        game_text(27, "  Score     Gems      Whips     ", TEXT)
        game_text(32, "Teleports   Keys      Cloaks    ", TEXT)
        game_text(27, "*" * 48 + "Options", OPTIONS_TEXT, False, False, ("ONLY_TEXT", OPTIONS_BOX))

        for i, word in enumerate(option_list):
            game_text(29+i, " " * 48 + word[0], None, False, False)
            game_text(29+i, " " * 49 + word[1:], LIGHT_GRAY, False, False)

        # Ensure values list has enough elements before accessing
        if values and len(values) >= 7:
             game_text(29, "*" * 18 + format_centered_int(values[0], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Score
             game_text(31, "*" * 8  + format_centered_int(values[1], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Level
             game_text(29, "*" * 28 + format_centered_int(values[2], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Gems
             game_text(29, "*" * 38 + format_centered_int(values[3], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Whips
             game_text(34, "*" * 18 + format_centered_int(values[4], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Teleports
             game_text(34, "*" * 28 + format_centered_int(values[5], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Keys
             game_text(34, "*" * 38 + format_centered_int(values[6], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX), True) # Cloaks

    else: # hud_input == "R" (Right sidebar)
        hud_width = WIDTH - (GP_TILE_WIDTH * 66) # Adjust width calculation if GAME_WIDTH is not the game area width
        hud_x = WIDTH - hud_width  # Right-hand side

        # Create sidebar surface with monochrome handling
        hud_surface = pygame.Surface((hud_width, HEIGHT))
        hud_surface.fill(BACKGROUND)
        # apply_grayscale_f should be available from utils
        if is_monochrome:
            hud_surface = apply_grayscale_f(hud_surface)
        screen.blit(hud_surface, (hud_x, 0))  # Apply sidebar

        game_text(2, " " * 70 + "Score", TEXT)
        game_text(4, " " * 70 + "Level", TEXT)
        game_text(6, " " * 70 + "Gems", TEXT)
        game_text(8, " " * 70 + "Whips", TEXT)
        game_text(10, " " * (70 - 2) + "Teleports", TEXT) # Adjust spacing for longer word
        game_text(12, " " * 70 + "Keys", TEXT)
        game_text(14, " " * 70 + "Cloaks", TEXT)
        game_text(17, "*" * (70-1) + "OPTIONS", OPTIONS_TEXT, False, False, ("ONLY_TEXT", OPTIONS_BOX))

        for i, word in enumerate(option_list):
            game_text(18+i, " " * 69 + word[0], None, False, False)
            game_text(18+i, " " * 70 + word[1:], LIGHT_GRAY, False, False)

        # Ensure values list has enough elements
        if values and len(values) >= 7:
            for i in range(7):
                 game_text(3+(i*2), "*" * (70-1) + format_centered_int(values[i], 7), VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX))
        else:
            for i in range(7):
                 game_text(3+(i*2), "*" * (70-1) + "   0   ", VALUE_TEXT, False, False, ("ONLY_TEXT", TEXT_BOX))


def levels(difficulty_input, color_input="C", hud_input="O", mixUp=False):
    """Main gameplay loop for Kroz levels."""
    global tile_mapping # Ensure we use the global tile_mapping

    screen.fill(BLACK)

    # Scale sprites based on current dimensions and color setting
    scale_gameplay_sprites((GP_TILE_WIDTH, GP_TILE_HEIGHT), color_input)

    level_maps = [level1_map, level2_map, level4_map, level6_map, level8_map, level10_map,
                  level12_map, level14_map, level16_map, level18_map, level20_map, level22_map,
                  level24_map, level25_map]
    current_level_index = 0
    grid = [list(row) for row in level_maps[current_level_index]]

    collidable_tiles = {"X", "#", ";", "/", "J", "R", "4", "5", "6", "8", "9"} # Example, adjust as needed

    # Game state
    slow_enemies = []
    medium_enemies = []
    fast_enemies = []
    keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False,
                    pygame.K_LEFT: False, pygame.K_RIGHT: False,
                    pygame.K_w: False, pygame.K_t: False, pygame.K_c: False,
                    pygame.K_u: False, pygame.K_i: False, pygame.K_o: False,
                    pygame.K_j: False, pygame.K_l: False,
                    pygame.K_n: False, pygame.K_m: False, pygame.K_COMMA: False}


    # Find player and enemies
    player_row, player_col = 0, 0
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == "P":
                player_row, player_col = r, c
            elif tile == "1":
                slow_enemies.append({"row": r, "col": c})
            elif tile == "2":
                medium_enemies.append({"row": r, "col": c})
            elif tile == "3":
                fast_enemies.append({"row": r, "col": c})

    # Initialize score tracking variables *Based off difficulty*
    match(difficulty_input):
        case "E":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 20, 10, 0, 0, 0, 2
        case "A":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 2, 0, 0, 0, 0, 2
        case "N", " ":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 20, 10, 0, 0, 0, 2
        case "X":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 250, 100, 50, 0, 10, 3
        case _:
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 50, 50, 10, 0, 5, 2

    if mixUp:
        score, level_num, gems, whips, teleports, keys = 0, 1, gems + 60, whips + 30, teleports + 15, cloaks + 2, whip_power

    values = [score, level_num, gems, whips, teleports, keys, cloaks]

    # Function to change to the next level
    def change_level(next_level_index):
        nonlocal grid, player_row, player_col, slow_enemies, medium_enemies, fast_enemies, level_num
        nonlocal waiting_for_start_key # Access the flag
        # Check if level index is valid
        if next_level_index >= len(level_maps):
            next_level_index = 0  # Loop back to first level

        # Update level number
        level_num = next_level_index + 1

        # Reset level grid
        grid = [list(row) for row in level_maps[next_level_index]]

        # Reset enemies
        slow_enemies = []
        medium_enemies = []
        fast_enemies = []

        # Find new player position and enemies
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == "P":
                    player_row, player_col = r, c
                elif tile == "1":
                    slow_enemies.append({"row": r, "col": c})
                elif tile == "2":
                    medium_enemies.append({"row": r, "col": c})
                elif tile == "3":
                    fast_enemies.append({"row": r, "col": c})

        # Reset the flag when changing levels
        waiting_for_start_key = True

    def has_line_of_sight(from_row, from_col, to_row, to_col):
        """Check if there's a direct line of sight between two positions"""
        # Bresenham's line algorithm for line of sight
        points = []
        dx, dy = abs(to_col - from_col), abs(to_row - from_row)
        sx = 1 if from_col < to_col else -1
        sy = 1 if from_row < to_row else -1
        err = dx - dy

        x, y = from_col, from_row
        while True:
            points.append((x, y))
            if x == to_col and y == to_row:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

        # Check if any solid walls block the line of sight
        # Enemies can now see through breakable blocks ("X")
        for col, row in points[1:-1]:  # Skip start and end points
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == "#":  # Only solid walls block vision
                    return False
        return True

    def move_enemy(enemy, enemy_type, move_prob):
        if is_cloaked:
            return False
        else:
            """Move an enemy toward the player if they can see the player"""
            nonlocal score, gems  # Access Score and gems from the outer scope
        
        row, col = enemy["row"], enemy["col"]
            
            # Check if enemy was removed
        if grid[row][col] != enemy_type:
                return True  # Remove enemy
            
        # Original game had different odds for different enemy types
        # Fast enemies had 1/6 chance, medium 1/7, slow 1/8
        # Only give player a move chance if the player can see the enemy
        if has_line_of_sight(row, col, player_row, player_col):
            if random.randint(0, move_prob-1) == 0:
                player_input()
        
        # Check if enemy can see player
        if not has_line_of_sight(row, col, player_row, player_col):
            return False  # Stay still if can't see player
        
        # Clear current position
        grid[row][col] = " "
        
        # Calculate move direction toward player
        new_row, new_col = row, col
        x_dir, y_dir = 0, 0
        
        # Try to move closer to the player along optimal axis first
        x_dist = abs(player_col - col)
        y_dist = abs(player_row - row)
        
        # Move along the axis with greater distance first
        # This makes enemies try to minimize the longest dimension first
        if x_dist > y_dist:
            # Move horizontally first
            if player_col < col:
                new_col -= 1
                x_dir = 1
            elif player_col > col:
                new_col += 1
                x_dir = -1
        else:
            # Move vertically first
            if player_row < row:
                new_row -= 1
                y_dir = 1
            elif player_row > row:
                new_row += 1
                y_dir = -1
        
        # If no movement was determined, try the other axis
        if new_row == row and new_col == col:
            if player_col < col:
                new_col -= 1
                x_dir = 1
            elif player_col > col:
                new_col += 1
                x_dir = -1
            elif player_row < row:
                new_row -= 1
                y_dir = 1
            elif player_row > row:
                new_row += 1
                y_dir = -1
        
        # Handle movement and collisions
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # Breaking X blocks
            if grid[new_row][new_col] == "X":
                grid[new_row][new_col] = " "  # Break the block
                # Award points based on enemy type
                if enemy_type == "1": score += 10
                elif enemy_type == "2": score += 20
                elif enemy_type == "3": score += 30
                enemyCollision()  # Play sound for breaking block
                return True  # Enemy dies when breaking block
            
            # Handle collision with gems, whips, teleports
            elif grid[new_row][new_col] == "+":  # Gem
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3
                
                if gems < 0:
                    player_death(screen)  # Call player_death when out of gems
                
                # Update display
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False
                
            # Collide with an item (whip, teleport)
            elif grid[new_row][new_col] in {"W", "T"}:
                # Destroy the item and move the enemy
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False
                
            # Empty space - move there
            elif grid[new_row][new_col] == " ":
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False

            # Hit player
            elif grid[new_row][new_col] == "P":
                # Attack player by taking gems
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3
                
                if gems < 0:
                    player_death(screen)  # Call player_death when out of gems
                enemyCollision()  # Play sound for enemy collision    
                return True  # Enemy dies
                
            # Blocked - stay in place
            else:
                grid[row][col] = enemy_type
                return False
        else:
            grid[row][col] = enemy_type  # Stay in place
            return False
            
    def use_whip():
        """Handle the whip animation and enemy interactions, keeping HUD and border visible, with color cycling."""
        nonlocal score, whips, slow_enemies, medium_enemies, fast_enemies, values, player_row, player_col, is_cloaked, grid, level_num, gems, teleports, keys, cloaks, hud_input, color_input # Add hud_input, color_input

        # Check if player has whips
        if whips <= 0:
            # Return current enemy lists if no whips
            zeroCollecible()  # Play sound for no whips
            return slow_enemies, medium_enemies, fast_enemies

        # Define the whip animation positions (counter-clockwise)
        whip_positions = [
            {"row": -1, "col": -1, "sprite_char": "whip1"},
            {"row": -1, "col":  0, "sprite_char": "whip3"},
            {"row": -1, "col":  1, "sprite_char": "whip2"},
            {"row":  0, "col":  1, "sprite_char": "whip4"},
            {"row":  1, "col":  1, "sprite_char": "whip1"},
            {"row":  1, "col":  0, "sprite_char": "whip3"},
            {"row":  1, "col": -1, "sprite_char": "whip2"},
            {"row":  0, "col": -1, "sprite_char": "whip4"},
        ]

        enemies_hit = []
        delay = 25
        # grid_offset_x = GP_TILE_WIDTH # Removed old simple offset
        # grid_offset_y = GP_TILE_HEIGHT # Removed old simple offset

        # --- MODIFIED: Calculate Grid Offsets (like draw_grid) ---
        target_grid_width_px = (LOGICAL_GRID_WIDTH + 2) * GP_TILE_WIDTH
        target_grid_height_px = (LOGICAL_GRID_HEIGHT + 2) * GP_TILE_HEIGHT

        if hud_input == "O": # Bottom HUD
            offset_x = (WIDTH - target_grid_width_px) // 2
            offset_y = 0
        elif hud_input == "R": # Right HUD
            hud_width = WIDTH - (GP_TILE_WIDTH * LOGICAL_GRID_WIDTH) # Assuming LOGICAL_GRID_WIDTH is game area
            available_width = WIDTH - hud_width
            offset_x = 0 # Align grid to the left
            offset_y = (HEIGHT - target_grid_height_px) // 2
        else: # No HUD or unknown type - center in full screen
            offset_x = (WIDTH - target_grid_width_px) // 2
            offset_y = (HEIGHT - target_grid_height_px) // 2

        offset_x = max(0, offset_x)
        offset_y = max(0, offset_y)

        # Grid content offset relative to screen, including border
        grid_content_offset_x = offset_x + GP_TILE_WIDTH
        grid_content_offset_y = offset_y + GP_TILE_HEIGHT
        # --- END OFFSET CALCULATION ---


        # --- MODIFIED: Calculate bottom boundary based on HUD ---
        # This boundary is still relative to the screen height for the HUD overlay case
        bottom_boundary = HEIGHT - GP_TILE_HEIGHT # Default for side HUD
        if hud_input == "O":
            # Adjust boundary higher to accommodate overlaid HUD (approx 3 tiles: border + 2 text rows)
            bottom_boundary = HEIGHT - (GP_TILE_HEIGHT * 4)
        # --- END MODIFICATION ---

        # --- Whip animation loop ---
        for position in whip_positions:
            whip_row = player_row + position["row"]
            whip_col = player_col + position["col"]

            if not (0 <= whip_row < len(grid) and 0 <= whip_col < len(grid[0])):
                continue

            original_tile_char = grid[whip_row][whip_col]
            if original_tile_char in ["1", "2", "3"]:
                is_already_hit = any(r == whip_row and c == whip_col for r, c, _ in enemies_hit)
                if not is_already_hit:
                    enemies_hit.append((whip_row, whip_col, original_tile_char))

            whip_sprite_char = position["sprite_char"]
            colored_whip_image = None
            if whip_sprite_char in tile_mapping:
                original_whip_image = tile_mapping[whip_sprite_char]
                random_color = random.choice(whip_cycle_colors)
                colored_whip_image = original_whip_image.copy()
                colored_whip_image.fill(random_color, special_flags=pygame.BLEND_RGB_MULT)
            else:
                print(f"Warning: Whip sprite character '{whip_sprite_char}' not found in tile_mapping.")

            # --- Direct Drawing within Whip Loop ---
            screen.fill(BLACK)
            # --- MODIFIED: Pass offsets to draw_borders ---
            draw_borders(tile_mapping, offset_x, offset_y)
            # --- END MODIFICATION ---

            # Draw the main game grid (using calculated content offsets)
            # Define the drawing boundaries based on the *logical* grid size and offset
            max_draw_x = grid_content_offset_x + (LOGICAL_GRID_WIDTH * GP_TILE_WIDTH)
            max_draw_y = grid_content_offset_y + (LOGICAL_GRID_HEIGHT * GP_TILE_HEIGHT)

            for r_idx in range(min(LOGICAL_GRID_HEIGHT, len(grid))):
                 # --- MODIFIED: Use grid_content_offset_y ---
                 screen_y = grid_content_offset_y + (r_idx * GP_TILE_HEIGHT)
                 # --- END MODIFICATION ---
                 # --- MODIFIED: Check against max_draw_y and bottom_boundary ---
                 if screen_y >= max_draw_y or screen_y >= bottom_boundary: continue
                 # --- END MODIFICATION ---

                 row_data = grid[r_idx]
                 for c_idx in range(min(LOGICAL_GRID_WIDTH, len(row_data))):
                     # --- MODIFIED: Use grid_content_offset_x ---
                     screen_x = grid_content_offset_x + (c_idx * GP_TILE_WIDTH)
                     # --- END MODIFICATION ---
                     # --- MODIFIED: Check against max_draw_x ---
                     if screen_x >= max_draw_x: continue # Right boundary check based on logical width
                     # --- END MODIFICATION ---

                     # Draw the colored whip sprite
                     if r_idx == whip_row and c_idx == whip_col and colored_whip_image:
                          # --- MODIFIED: Use grid_content_offset_x/y ---
                          whip_screen_x = grid_content_offset_x + whip_col * GP_TILE_WIDTH
                          whip_screen_y = grid_content_offset_y + whip_row * GP_TILE_HEIGHT
                          # --- END MODIFICATION ---
                          # --- MODIFIED: Check against max_draw_x/y and bottom_boundary ---
                          if whip_screen_x < max_draw_x and whip_screen_y < max_draw_y and whip_screen_y < bottom_boundary:
                              screen.blit(colored_whip_image, (whip_screen_x, whip_screen_y))
                          # --- END MODIFICATION ---
                     # Draw normal tiles
                     else:
                         char = row_data[c_idx]
                         draw_char = char
                         if r_idx == player_row and c_idx == player_col:
                              draw_char = 'TP' if is_cloaked else 'P'

                         if draw_char in tile_mapping:
                             screen.blit(tile_mapping[draw_char], (screen_x, screen_y))
                         elif char != ' ':
                             pygame.draw.rect(screen, RED, (screen_x, screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT), 1)


            # --- MODIFIED: Draw HUD *after* grid content ---
            current_values = [score, level_num, gems, whips, teleports, keys, cloaks] # Use current values
            draw_hud(current_values, color_input, hud_input) # Redraw HUD over the grid if hud_input == "O"
            # --- END MODIFICATION ---

            # Display level-specific messages (Consider adjusting Y if needed for hud_input == "O")
            if level_num == 1:
                game_text(24, "KINGDOM OF KROZ II BY SCOTT MILLER", WHITE, False, True, None)
            # ... other messages ...

            pygame.display.flip()
            pygame.time.wait(delay)

        # Process enemy hits and update game state
        new_slow_enemies = []
        new_medium_enemies = []
        new_fast_enemies = []
        enemy_scores = {"1": 10, "2": 20, "3": 30}

        for r, c, enemy_char in enemies_hit:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == enemy_char:
                grid[r][c] = " "
                score += enemy_scores.get(enemy_char, 0)

        # Rebuild enemy lists (no changes needed here)
        for enemy in slow_enemies:
            if 0 <= enemy["row"] < len(grid) and 0 <= enemy["col"] < len(grid[0]) and grid[enemy["row"]][enemy["col"]] == "1":
                new_slow_enemies.append(enemy)
        for enemy in medium_enemies:
             if 0 <= enemy["row"] < len(grid) and 0 <= enemy["col"] < len(grid[0]) and grid[enemy["row"]][enemy["col"]] == "2":
                new_medium_enemies.append(enemy)
        for enemy in fast_enemies:
             if 0 <= enemy["row"] < len(grid) and 0 <= enemy["col"] < len(grid[0]) and grid[enemy["row"]][enemy["col"]] == "3":
                new_fast_enemies.append(enemy)

        # Decrement whip count after use
        whips -= 1
        whip_audio()
        return new_slow_enemies, new_medium_enemies, new_fast_enemies

    is_cloaked = False
    cloak_start_time = 0
    CLOAK_DURATION = 3000 # Milliseconds cloak lasts

    def cloak():
        """ Handles cloak activation. """
        nonlocal is_cloaked, cloak_start_time
        cloak_start_time = pygame.time.get_ticks()
        is_cloaked = True
        # Note: Cloak decrement happens in player_input where the action is initiated

    def teleport(t_trap=False):
        """Teleports the player to a random empty space on the grid with a flickering effect."""
        nonlocal player_row, player_col # Modifies player position directly
        # Access necessary variables from the outer scope for offset calculation
        nonlocal hud_input, values, color_input # Added values, color_input


        # --- Recalculate Grid Offsets (same logic as draw_grid) ---
        target_grid_width_px = (LOGICAL_GRID_WIDTH + 2) * GP_TILE_WIDTH
        target_grid_height_px = (LOGICAL_GRID_HEIGHT + 2) * GP_TILE_HEIGHT

        if hud_input == "O": # Bottom HUD
            offset_x = (WIDTH - target_grid_width_px) // 2
            offset_y = 0
        elif hud_input == "R": # Right HUD
            # hud_width = WIDTH - (GP_TILE_WIDTH * LOGICAL_GRID_WIDTH) # Original calculation might be off if border included
            offset_x = 0
            offset_y = (HEIGHT - target_grid_height_px) // 2
        else: # No HUD or unknown type
            offset_x = (WIDTH - target_grid_width_px) // 2
            offset_y = (HEIGHT - target_grid_height_px) // 2

        offset_x = max(0, offset_x)
        offset_y = max(0, offset_y)

        # Define grid content offsets *relative to the screen*, including the border offset
        grid_content_offset_x = offset_x + GP_TILE_WIDTH
        grid_content_offset_y = offset_y + GP_TILE_HEIGHT
        # --- End Offset Calculation ---


        # Find all empty spaces (' ') on the current grid
        empty_spaces = []
        for r, row_data in enumerate(grid):
            # Ensure we only check within logical grid bounds if necessary, though iterating the actual grid is fine
            for c, char in enumerate(row_data):
                 # Optional: Add bounds check if grid can be larger than logical size
                 # if r < LOGICAL_GRID_HEIGHT and c < LOGICAL_GRID_WIDTH:
                 if char == ' ':
                     empty_spaces.append((r, c))


        if not empty_spaces:
            print("No empty spaces to teleport to!")
            return # Cannot teleport if no empty space

        # --- Flicker at the original position ---
        # Use the calculated grid_content_offset_x/y
        original_screen_x = grid_content_offset_x + player_col * GP_TILE_WIDTH
        original_screen_y = grid_content_offset_y + player_row * GP_TILE_HEIGHT
        original_rect = pygame.Rect(original_screen_x, original_screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT)
        player_sprite = tile_mapping.get('P')
        if not player_sprite:
             print("Warning: Player sprite 'P' not found in tile_mapping for teleport.")
             return # Cannot proceed without player sprite

        # --- MODIFIED: Initial Flicker Loop at Original Position with Color ---
        original_flicker_count = 10 # Number of flickers at start
        original_flicker_delay = 50 # Delay between flickers

        # Get the original tile character at the player's starting position (should be 'P', but could be something else if logic error)
        # We actually want the background tile *under* the player, which is ' ' after the move starts
        original_bg_char = ' ' # Assume empty space after player logically moves
        original_bg_sprite = tile_mapping.get(original_bg_char)

        for _ in range(original_flicker_count):
            # Fill original position with random color
            random_color = random.choice(blinking_text_color_list)
            screen.fill(random_color, original_rect)
            # Draw player sprite on top
            screen.blit(player_sprite, original_rect.topleft)
            pygame.display.update(original_rect)
            pygame.time.delay(original_flicker_delay // 2)

            # Clear player sprite (fill black/background color then draw original background tile)
            screen.fill(BLACK, original_rect) # Fill black first as a base
            if original_bg_sprite:
                screen.blit(original_bg_sprite, original_rect.topleft)
            pygame.display.update(original_rect)
            pygame.time.delay(original_flicker_delay // 2)
        # --- End Modified Initial Flicker ---

        # --- Intermediate Flicker Loop ---
        # ...existing code...
        last_intermediate_rect = None
        tp_sprite = tile_mapping.get('TP')
        if not tp_sprite:
             print("Warning: Teleport player sprite 'TP' not found.")
             tp_sprite = player_sprite # Fallback to normal player sprite

        intermediate_flicker_count = 250
        intermediate_delay = 6
        if t_trap:
            intermediate_flicker_count = 1

        final_row, final_col = -1, -1 # Initialize final position

        for i in range(intermediate_flicker_count):
            new_row, new_col = random.choice(empty_spaces)
            # Use the calculated grid_content_offset_x/y
            intermediate_screen_x = grid_content_offset_x + new_col * GP_TILE_WIDTH
            intermediate_screen_y = grid_content_offset_y + new_row * GP_TILE_HEIGHT
            intermediate_rect = pygame.Rect(intermediate_screen_x, intermediate_screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT)

            if last_intermediate_rect:
                # Need to redraw the correct background tile before clearing
                prev_r, prev_c = -1, -1
                if GP_TILE_WIDTH > 0: prev_c = (last_intermediate_rect.x - grid_content_offset_x) // GP_TILE_WIDTH
                if GP_TILE_HEIGHT > 0: prev_r = (last_intermediate_rect.y - grid_content_offset_y) // GP_TILE_HEIGHT

                # --- MODIFIED BOUNDS CHECK ---
                # Check against the length of the specific row grid[prev_r] for the column index
                if 0 <= prev_r < len(grid) and 0 <= prev_c < len(grid[prev_r]):
                # --- END MODIFICATION ---
                    original_char = grid[prev_r][prev_c] # Get char from logical grid
                    # Ensure the char is not the player temporarily placed during flicker
                    if prev_r == player_row and prev_c == player_col:
                        original_char = ' ' # Assume space under player
                    bg_sprite = tile_mapping.get(original_char)
                    if bg_sprite:
                        screen.blit(bg_sprite, last_intermediate_rect.topleft)
                    else: # If no specific tile, just fill black
                        screen.fill(BLACK, last_intermediate_rect)
                else: # Fallback if calculation failed or indices out of bounds for the specific row
                    screen.fill(BLACK, last_intermediate_rect)

            screen.blit(tp_sprite, (intermediate_screen_x, intermediate_screen_y)) # Draw TP icon
            pygame.display.update([last_intermediate_rect, intermediate_rect] if last_intermediate_rect else [intermediate_rect])
            last_intermediate_rect = intermediate_rect

            pygame.time.delay(intermediate_delay)

            # Store the final destination from the last iteration
            if i == intermediate_flicker_count - 1:
                 final_row, final_col = new_row, new_col
                 # Use the calculated grid_content_offset_x/y
                 final_screen_x = grid_content_offset_x + final_col * GP_TILE_WIDTH
                 final_screen_y = grid_content_offset_y + final_row * GP_TILE_HEIGHT
                 final_rect = intermediate_rect # The rect from the last intermediate step is the final one


        # Clear the last intermediate TP icon by redrawing the original tile
        if last_intermediate_rect and 0 <= final_row < len(grid) and 0 <= final_col < len(grid[0]):
             original_char = grid[final_row][final_col] # Should be ' ' but redraw just in case
             bg_sprite = tile_mapping.get(original_char)
             if bg_sprite:
                 screen.blit(bg_sprite, last_intermediate_rect.topleft)
             else:
                 screen.fill(BLACK, last_intermediate_rect)
             pygame.display.update(last_intermediate_rect)


        # --- MODIFIED: Final Destination Flicker with Color ---
        # Ensure final_rect is valid before proceeding
        if final_row != -1:
            final_bg_char = grid[final_row][final_col] # Should be ' '
            final_bg_sprite = tile_mapping.get(final_bg_char)
            final_flicker_count = 10 # Reduced flicker count
            final_flicker_delay = 40

            for _ in range(final_flicker_count):
                # Fill final position with random color
                random_color = random.choice(blinking_text_color_list)
                screen.fill(random_color, final_rect)
                # Draw player on top
                screen.blit(player_sprite, (final_screen_x, final_screen_y))
                pygame.display.update(final_rect)
                pygame.time.delay(final_flicker_delay)

                # Clear player (fill black/background color then draw background)
                screen.fill(BLACK, final_rect) # Fill black first
                if final_bg_sprite:
                     screen.blit(final_bg_sprite, final_rect.topleft)
                pygame.display.update(final_rect)
                pygame.time.delay(final_flicker_delay)
        else:
             print("Error: Final teleport position not determined.")
             # Clear the last intermediate flicker if it exists and final position failed
             if last_intermediate_rect:
                 # Attempt to redraw original background
                 prev_r, prev_c = -1, -1
                 if GP_TILE_WIDTH > 0: prev_c = (last_intermediate_rect.x - grid_content_offset_x) // GP_TILE_WIDTH
                 if GP_TILE_HEIGHT > 0: prev_r = (last_intermediate_rect.y - grid_content_offset_y) // GP_TILE_HEIGHT
                 if 0 <= prev_r < len(grid) and 0 <= prev_c < len(grid[0]):
                     original_char = grid[prev_r][prev_c]
                     bg_sprite = tile_mapping.get(original_char)
                     if bg_sprite: screen.blit(bg_sprite, last_intermediate_rect.topleft)
                     else: screen.fill(BLACK, last_intermediate_rect)
                 else: screen.fill(BLACK, last_intermediate_rect)
                 pygame.display.update(last_intermediate_rect)
             return # Avoid errors if final position wasn't set


        # --- Update Game State ---
        # Clear old player position from the grid (logical update)
        if 0 <= player_row < len(grid) and 0 <= player_col < len(grid[0]):
            grid[player_row][player_col] = ' '
        else:
            print(f"Warning: Original player position ({player_row}, {player_col}) was out of bounds before teleport.")


        # Update the grid with new player position (logical update)
        if 0 <= final_row < len(grid) and 0 <= final_col < len(grid[0]):
             grid[final_row][final_col] = 'P'
             # Update player's logical position
             player_row, player_col = final_row, final_col
             intermediate_flicker_count = 250 # Reset flicker count for next teleport
        else:
             print(f"Error: Final teleport destination ({final_row}, {final_col}) is out of bounds.")

    # --- Movement settings ---
    movement_cooldown = 100  # ms between moves
    last_move_time = 0
    keys_held_time = { k: 0 for k in keys_pressed } # Initialize based on keys_pressed dict
    momentum = { k: 0 for k in keys_pressed }

    MOMENTUM_THRESHOLD = 300
    MAX_MOMENTUM = 5

    def player_input():
        """Handle player movement, whip, teleport, and cloak actions."""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys, cloaks, is_cloaked
        nonlocal slow_enemies, medium_enemies, fast_enemies, last_move_time
        nonlocal values # Needed for drawing during actions like whip

        current_time = pygame.time.get_ticks()
        current_keys = pygame.key.get_pressed()
        action_performed = False # Tracks if non-movement action occurred

        # --- Action Handling (Whip, Teleport, Cloak) ---
        # Handle whip ('W')
        if current_keys[pygame.K_w] and not keys_pressed.get(pygame.K_w, False):
            keys_pressed[pygame.K_w] = True
            if whips > 0:
                # Decrement whip *before* calling use_whip to reflect cost
                whips -= 1
                values[3] = whips # Update HUD value immediately
                # Call use_whip and update enemy lists
                slow_enemies, medium_enemies, fast_enemies = use_whip()
                action_performed = True
                last_move_time = current_time # Reset move timer after action
        elif not current_keys[pygame.K_w]:
            keys_pressed[pygame.K_w] = False

        # Handle Teleport ('T')
        if current_keys[pygame.K_t] and not keys_pressed.get(pygame.K_t, False):
            keys_pressed[pygame.K_t] = True
            if teleports > 0:
                teleports -= 1
                values[4] = teleports # Update HUD
                teleport() # Calls the teleport function which handles animation and player pos update
                action_performed = True
                last_move_time = current_time # Reset move timer
        elif not current_keys[pygame.K_t]:
            keys_pressed[pygame.K_t] = False

        # Handle Cloak ('C')
        if current_keys[pygame.K_c] and not keys_pressed.get(pygame.K_c, False):
            keys_pressed[pygame.K_c] = True
            if cloaks > 0 and not is_cloaked:
                cloaks -= 1
                values[6] = cloaks # Update HUD
                cloak() # Activates cloak state and timer
                action_performed = True
                last_move_time = current_time # Reset move timer
        elif not current_keys[pygame.K_c]:
            keys_pressed[pygame.K_c] = False


        # --- Movement Handling ---
        time_since_last_move = current_time - last_move_time
        move_attempted = False # Tracks if a move was attempted this frame

        if time_since_last_move >= movement_cooldown:
            move_made = False # Tracks if a successful move was made this frame

            # Define all direction keys with their movement vectors (delta_row, delta_col)
            direction_keys = [
                (pygame.K_UP, (-1, 0)), (pygame.K_DOWN, (1, 0)),
                (pygame.K_LEFT, (0, -1)), (pygame.K_RIGHT, (0, 1)),
                (pygame.K_u, (-1, -1)), (pygame.K_i, (-1, 0)), (pygame.K_o, (-1, 1)),
                (pygame.K_j, (0, -1)), (pygame.K_l, (0, 1)),
                (pygame.K_n, (1, -1)), (pygame.K_m, (1, 0)), (pygame.K_COMMA, (1, 1))
            ]

            active_direction_key = None

            # Check currently pressed keys first
            for key, (dr, dc) in direction_keys:
                if current_keys[key]:
                    move_attempted = True
                    if not keys_pressed.get(key, False):  # Key just pressed
                        keys_pressed[key] = True
                        keys_held_time[key] = current_time
                        momentum[key] = 0 # Reset momentum on new press

                    # Try to move in this direction
                    if process_move(player_row + dr, player_col + dc):
                        move_made = True
                        footStep() # Play footstep sound
                        active_direction_key = key
                        break # Exit loop once a move is made

            # Handle key releases and momentum buildup for *all* direction keys
            for key, _ in direction_keys:
                 if not current_keys[key] and keys_pressed.get(key, False): # Key was pressed, now released
                     hold_duration = current_time - keys_held_time.get(key, current_time)
                     if hold_duration > MOMENTUM_THRESHOLD:
                         # Add momentum based on hold duration
                         momentum[key] = min(MAX_MOMENTUM, int((hold_duration - MOMENTUM_THRESHOLD) / 100))
                     keys_pressed[key] = False # Mark as released

            # If no key is currently pressed or move failed, check for momentum
            if not move_made and move_attempted: # Only apply momentum if a move was attempted but failed or no key is pressed now
                 # Find the key with the highest momentum
                 momentum_key = None
                 max_momentum = 0
                 for key, mom in momentum.items():
                     if mom > max_momentum:
                         max_momentum = mom
                         momentum_key = key

                 if momentum_key is not None and max_momentum > 0:
                     # Find the corresponding dr, dc
                     for key, (dr, dc) in direction_keys:
                         if key == momentum_key:
                             if process_move(player_row + dr, player_col + dc):
                                 move_made = True
                                 momentum[momentum_key] -= 1
                             else:
                                 momentum[momentum_key] = 0 # Clear momentum if move fails
                             break # Exit inner loop

            # Update last move time if a move was successful
            if move_made:
                last_move_time = current_time
                # Optionally reset momentum for the key that *caused* the move
                if active_direction_key:
                    momentum[active_direction_key] = 0


        return action_performed or move_attempted # Return true if any action or move attempt happened

    def process_move(new_row, new_col):
        """Process a player movement attempt to a new position."""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys, level_num, cloaks, whip_power
        nonlocal current_level_index, waiting_for_start_key
        nonlocal slow_enemies, medium_enemies, fast_enemies

        # Check bounds
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            electricWall()
            return False # Invalid move (out of bounds)

        target_char = grid[new_row][new_col]
        moved = False

        # Check non-collidable first (empty space or collectables)
        if target_char == " ":
            moved = True
        elif target_char == "+": # Gem
            gems += 1
            score += 10
            moved = True
        elif target_char == "W": # Whip
            whips += 1
            score += 10
            moved = True
        elif target_char == "T": # Teleport Scroll
            teleports += 1
            score += 10
            moved = True
        elif target_char == "K": # Key
            keys += 1
            score += 10
            moved = True
        elif target_char == "_": # Cloak item (using TP sprite visually)
            cloaks += 1
            score += 60
            moved = True
        elif target_char == "*": # Nugget
            score += 50
            moved = True
        elif target_char == "S": # SlowTime
            score += 5
            # Effect applied in main loop based on powerup pickup logic
            moved = True
        elif target_char == "I": # Invisible
            score += 10
            # Effect applied in main loop
            moved = True
        elif target_char == "F": # SpeedTime
            score += 20
            # Effect applied in main loop
            moved = True
        elif target_char == "C": # Chest
            score += 50
            chestPickup() # Play sound for chest pickup
            # Add random gems/whips logic here if needed
            moved = True
        elif target_char == "!": # Tablet
            score += level_num + 250
            moved = True
        elif target_char == "Z": # Freeze
            score += 5 # Example score
            # Effect applied in main loop
            moved = True
        elif target_char == ".": # teleport trap
            score -= 50
            teleportTrap()  # Play sound for teleport trap
            # Move player onto the trap space *before* teleporting
            grid[player_row][player_col] = " " # Clear old position
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Place player on trap temporarily
            draw_grid() # Redraw the entire grid with player on the trap
            pygame.display.flip() # Update the display to show this frame
            pygame.time.wait(150) # Pause briefly (e.g., 150 milliseconds)
            teleport(t_trap=True) # Call teleport immediately
            return True # Move was successful (led to teleport)
        elif target_char == "Q": # Power Ring
            score += 20
            whip_power += 1
            grid[player_row][player_col] = " " # Clear old position
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Place player on trap temporarily
            draw_grid() # Redraw the entire grid with player on the trap
            pygame.display.flip() # Update the display to show this frame
            # Wait for player to press any key
            waiting_for_key = True
            while waiting_for_key:
                game_text(25, "A Power Ring--your whip is now a little stronger!", "CHANGING", False, True, BLACK)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        waiting_for_key = False
            return True
        elif target_char == "L": # Stairs
            score += level_num * 100 # Example score for level change
            next_level_idx = (current_level_index + 1) % len(level_maps)
            change_level(next_level_idx)
            current_level_index = next_level_idx # Update the index tracker
            return True # Return True immediately as level changes

        # --- If moved onto a collectable or empty space ---
        if moved:
            grid[player_row][player_col] = " " # Clear old position
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Place player in new position
            return True

        # --- Check Collisions ---
        elif target_char in collidable_tiles:
            # Check if it's a breakable wall 'X' - original code deducted score for # too
            if target_char in ["X", "#"]:
                 if score > 20: # Only deduct if score is sufficient
                     score -= 20
            # Handle door 'D' - requires a key
            elif target_char == 'D':
                if keys > 0:
                    keys -= 1
                    grid[player_row][player_col] = " " # Clear old position
                    player_row, player_col = new_row, new_col
                    grid[player_row][player_col] = "P" # Move player onto door space (it becomes empty)
                    return True # Successful move through door
                else:
                    # No key, cannot move
                    return False
            return False # Movement blocked

        # --- Handle Enemy Collision (if player moves onto enemy) ---
        # This case shouldn't happen if enemies move first, but as a safeguard:
        elif target_char in ["1", "2", "3"]:
             # Player moving onto an enemy could instantly trigger gem loss/death
             if target_char == "1": gems -= 1
             elif target_char == "2": gems -= 2
             elif target_char == "3": gems -= 3

             if gems < 0:
                 player_death(score, level_num)
                 return True # Move technically happened before death sequence

             # Clear old player position, place player, remove enemy
             grid[player_row][player_col] = " "
             player_row, player_col = new_row, new_col
             grid[player_row][player_col] = "P"
             # Remove the enemy from its list
             if target_char == "1": slow_enemies = [e for e in slow_enemies if not (e["row"] == new_row and e["col"] == new_col)]
             elif target_char == "2": medium_enemies = [e for e in medium_enemies if not (e["row"] == new_row and e["col"] == new_col)]
             elif target_char == "3": fast_enemies = [e for e in fast_enemies if not (e["row"] == new_row and e["col"] == new_col)]
             return True


        # Default case: if the target tile is not explicitly handled, block movement
        return False

    # --- Game constants and Timers ---
    FAST_PC = True # Assume modern PC

    BASE_SLOW_TIMER = 10 if FAST_PC else 3
    BASE_MEDIUM_TIMER = 8 if FAST_PC else 2
    BASE_FAST_TIMER = 6 if FAST_PC else 1

    # Current timer thresholds (can be modified by spells)
    slow_threshold = BASE_SLOW_TIMER
    medium_threshold = BASE_MEDIUM_TIMER
    fast_threshold = BASE_FAST_TIMER

    # Spell effect timers (in ticks)
    slow_time_effect = 0
    invisible_effect = 0 # Not implemented yet, placeholder
    speed_time_effect = 0
    freeze_effect = 0

    GAME_TICK_RATE = 16.0 # Target ticks per second



    waiting_for_start_key = True # Start paused

    # Ensure the "saves" directory exists
    saves_dir = os.path.join("src", "saves")
    if not os.path.exists(saves_dir):
        try:
            os.makedirs(saves_dir)
        except OSError as e:
            print(f"Error creating saves directory: {e}")
            # Handle error appropriately, maybe exit or disable saving

    def save_game(state, slot):
        """Save the relevant game state to a JSON file."""
        save_path = os.path.join(saves_dir, f"KINGDOM{slot}.json")
        try:
            # Include essential state variables
            save_data = {
                "player_row": state["player_row"],
                "player_col": state["player_col"],
                "score": state["score"],
                "level_num": state["level_num"],
                "gems": state["gems"],
                "whips": state["whips"],
                "teleports": state["teleports"],
                "keys": state["keys"],
                "cloaks": state["cloaks"], # Save cloaks
                "whip_power": state["whip_power"], # Save whip power
                "current_level_index": state["current_level_index"], # Save level index
                # Optionally save enemy positions if desired (more complex restore)
                # "slow_enemies": state["slow_enemies"],
                # "medium_enemies": state["medium_enemies"],
                # "fast_enemies": state["fast_enemies"],
                # Optionally save grid state (large file)
                # "grid": state["grid"],
            }
            with open(save_path, "w") as save_file:
                json.dump(save_data, save_file, indent=4)
            print(f"Game saved to slot {slot}...")
            game_text(25, f"Game Saved to Slot {slot}", WHITE, False, True, BLACK) # Display confirmation
            pygame.display.flip()
            pygame.time.wait(1500)
        except Exception as e:
             print(f"Error saving game to slot {slot}: {e}")
             game_text(25, f"Error Saving Game!", RED, False, True, BLACK)
             pygame.display.flip()
             pygame.time.wait(1500)


    def restore_game(slot):
        """Restore the game state from a JSON file."""
        save_path = os.path.join(saves_dir, f"KINGDOM{slot}.json")
        if os.path.exists(save_path):
            try:
                with open(save_path, "r") as save_file:
                    state = json.load(save_file)
                print(f"Restoring from file {slot}...")
                game_text(25, f"Restoring from Slot {slot}...", WHITE, False, True, BLACK)
                pygame.display.flip()
                pygame.time.wait(1500)
                return state
            except Exception as e:
                 print(f"Error loading game from slot {slot}: {e}")
                 game_text(25, f"Error Loading Save!", RED, False, True, BLACK)
                 pygame.display.flip()
                 pygame.time.wait(1500)
                 return None
        else:
            print(f"No save file found for slot {slot}.")
            game_text(25, f"No Save File Found for Slot {slot}", YELLOW, False, True, BLACK)
            pygame.display.flip()
            pygame.time.wait(1500)
            return None

    def prompt_save_restore(action):
        """Prompt the user to pick a save/restore slot (A, B, or C)."""
        slot = None
        prompt_message = f"Pick slot to {action} (A, B, or C)? "
        input_char = ""

        while slot not in ["A", "B", "C"]:
            # Display prompt
            game_text(25, prompt_message + input_char + "█", WHITE, True, True, BLACK) # Blinking cursor
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    key_char = event.unicode.upper()
                    if key_char in ("A", "B", "C"):
                        input_char = key_char
                        slot = key_char
                        # Display final choice briefly
                        game_text(25, prompt_message + input_char, WHITE, False, True, BLACK)
                        pygame.display.flip()
                        pygame.time.wait(300)
                        return slot
                    elif event.key == pygame.K_ESCAPE:
                         game_text(25, f"{action} Cancelled", YELLOW, False, True, BLACK)
                         pygame.display.flip()
                         pygame.time.wait(1000)
                         return None # User cancelled
                    # Ignore other keys

    def handle_save():
        """Handle the save confirmation and process."""
        # Display confirmation prompt
        game_text(25, "Are you sure you want to SAVE (Y/N)?", "CHANGING", False, True, BLACK)
        pygame.display.flip()

        confirmed = False
        while True: # Wait for Y/N input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        confirmed = True
                        break
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        confirmed = False
                        break
            if confirmed is not None: break # Exit loop once Y or N is pressed

        if confirmed:
            save_slot = prompt_save_restore("SAVE")
            if save_slot:
                # Gather current state
                current_state = {
                    "player_row": player_row,
                    "player_col": player_col,
                    "score": score,
                    "level_num": level_num,
                    "gems": gems,
                    "whips": whips,
                    "teleports": teleports,
                    "keys": keys,
                    "cloaks": cloaks,
                    "whip_power": whip_power,
                    "current_level_index": current_level_index,
                    # "grid": grid, # Avoid saving grid by default unless necessary
                    # "slow_enemies": slow_enemies, # Avoid saving enemies unless necessary
                    # "medium_enemies": medium_enemies,
                    # "fast_enemies": fast_enemies,
                }
                save_game(current_state, save_slot)
        else:
             game_text(25, "Save Cancelled", YELLOW, False, True, BLACK)
             pygame.display.flip()
             pygame.time.wait(1000)


    def handle_restore():
        """Handle the restore confirmation and process."""
        nonlocal grid, player_row, player_col, score, level_num, gems, whips, teleports, keys, cloaks, whip_power
        nonlocal current_level_index, slow_enemies, medium_enemies, fast_enemies, waiting_for_start_key, values

        # Display confirmation prompt
        game_text(25, "Are you sure you want to RESTORE (Y/N)?", "CHANGING", False, True, BLACK)
        pygame.display.flip()

        confirmed = False
        while True: # Wait for Y/N input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        confirmed = True
                        break
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        confirmed = False
                        break
            if confirmed is not None: break

        if confirmed:
            restore_slot = prompt_save_restore("RESTORE")
            if restore_slot:
                restored_state = restore_game(restore_slot)
                if restored_state:
                    try:
                        # Apply the restored state
                        current_level_index = restored_state["current_level_index"]
                        level_num = restored_state["level_num"]
                        grid = [list(row) for row in level_maps[current_level_index]] # Regenerate grid

                        player_row = restored_state["player_row"]
                        player_col = restored_state["player_col"]
                        score = restored_state["score"]
                        gems = restored_state["gems"]
                        whips = restored_state["whips"]
                        teleports = restored_state["teleports"]
                        keys = restored_state["keys"]
                        cloaks = restored_state["cloaks"]
                        whip_power = restored_state["whip_power"] # Default to 1 if not found

                        # Ensure player is placed correctly on the regenerated grid
                        if 0 <= player_row < len(grid) and 0 <= player_col < len(grid[0]):
                             grid[player_row][player_col] = "P"
                        else:
                             print(f"Warning: Restored player position ({player_row}, {player_col}) is out of bounds for level {level_num}. Resetting.")
                             # Find a default starting 'P' or empty space if needed
                             # For simplicity, we might just let the game potentially error or place player at 0,0 if needed.

                        # Reset enemy lists based on the regenerated grid
                        slow_enemies = []
                        medium_enemies = []
                        fast_enemies = []
                        for r, row_data in enumerate(grid):
                            for c, tile in enumerate(row_data):
                                if tile == "1":
                                    slow_enemies.append({"row": r, "col": c})
                                elif tile == "2":
                                    medium_enemies.append({"row": r, "col": c})
                                elif tile == "3":
                                    fast_enemies.append({"row": r, "col": c})

                        values = [score, level_num, gems, whips, teleports, keys, cloaks] # Update HUD values
                        waiting_for_start_key = True # Pause after restore
                        print("Game restored successfully.")
                    except KeyError as e:
                         print(f"Error applying restored state: Missing key {e}")
                         game_text(25, f"Error in Save Data!", RED, False, True, BLACK)
                         pygame.display.flip()
                         pygame.time.wait(1500)
                    except IndexError:
                         print(f"Error applying restored state: Level index {current_level_index} out of bounds.")
                         game_text(25, f"Error in Save Data!", RED, False, True, BLACK)
                         pygame.display.flip()
                         pygame.time.wait(1500)

        else: # Restore cancelled
             game_text(25, "Restore Cancelled", YELLOW, False, True, BLACK)
             pygame.display.flip()
             pygame.time.wait(1000)

    def draw_borders(mapping, offset_x=0, offset_y=0): # Add offset parameters
         """Draws the static level and window borders."""
         border_char = '^'
         if border_char not in mapping:
              print("Warning: Border character '^' not found in tile_mapping.")
              return

         border_image = mapping[border_char]

         # Draw level_border (inner border) - Apply offsets
         for row_index, row_str in enumerate(level_border):
             screen_draw_y = offset_y + (row_index * GP_TILE_HEIGHT)
             if screen_draw_y >= HEIGHT: continue # Basic screen bounds check
             for col_index, char in enumerate(row_str):
                 screen_draw_x = offset_x + (col_index * GP_TILE_WIDTH)
                 if screen_draw_x >= WIDTH: continue # Basic screen bounds check
                 if char == border_char:
                     screen.blit(border_image, (screen_draw_x, screen_draw_y))

         # Draw window_border (outer border, offset) - Apply offsets
         for row_index, row_str in enumerate(window_border):
             # Original offset calculation relative to level_border
             base_y = (row_index * GP_TILE_HEIGHT) - GP_TILE_HEIGHT
             screen_draw_y = offset_y + base_y # Apply main offset
             if screen_draw_y >= HEIGHT or screen_draw_y + GP_TILE_HEIGHT <= 0: continue
             for col_index, char in enumerate(row_str):
                 base_x = (col_index * GP_TILE_WIDTH) - GP_TILE_WIDTH
                 screen_draw_x = offset_x + base_x # Apply main offset
                 if screen_draw_x >= WIDTH or screen_draw_x + GP_TILE_WIDTH <= 0: continue
                 if char == border_char:
                     screen.blit(border_image, (screen_draw_x, screen_draw_y))

    def draw_grid():
        """Draws the game grid, borders, HUD, and messages."""
        nonlocal score, level_num, gems, whips, teleports, keys, cloaks # Ensure access to latest values
        screen.fill(BLACK)

        # --- Calculate Target Grid Pixel Size (Based on Logical Size) ---
        # Add 2 for the border tiles on each side
        target_grid_width_px = (LOGICAL_GRID_WIDTH + 2) * GP_TILE_WIDTH
        target_grid_height_px = (LOGICAL_GRID_HEIGHT + 2) * GP_TILE_HEIGHT

        if hud_input == "O": # Bottom HUD
            # Center horizontally within the full screen width
            offset_x = (WIDTH - target_grid_width_px) // 2
            offset_y = 0 # Align grid to the top of its available space
        elif hud_input == "R": # Right HUD
            # Calculate HUD width based on logical grid size
            hud_width = WIDTH - (GP_TILE_WIDTH * LOGICAL_GRID_WIDTH)
            # Grid area is to the left of the HUD
            available_width = WIDTH - hud_width # Width available for the grid
            # Center vertically within the full screen height
            offset_x = 0 # Align grid to the left of its available space
            offset_y = (HEIGHT - target_grid_height_px) // 2
        else: # No HUD or unknown type - center in full screen
            offset_x = (WIDTH - target_grid_width_px) // 2
            offset_y = (HEIGHT - target_grid_height_px) // 2


        # Ensure offsets are not negative
        offset_x = max(0, offset_x)
        offset_y = max(0, offset_y)
        # --- End Offset Calculation ---


        # Draw borders using the helper function with calculated offsets
        draw_borders(tile_mapping, offset_x, offset_y)

        # Draw the main game grid, offset by one tile *relative to the border offset*
        grid_content_offset_x = offset_x + GP_TILE_WIDTH
        grid_content_offset_y = offset_y + GP_TILE_HEIGHT

        # Define the drawing boundaries based on the *logical* grid size and offset
        max_draw_x = grid_content_offset_x + (LOGICAL_GRID_WIDTH * GP_TILE_WIDTH)
        max_draw_y = grid_content_offset_y + (LOGICAL_GRID_HEIGHT * GP_TILE_HEIGHT)


        # Iterate through the logical grid dimensions or actual grid size, whichever is smaller
        for row_index in range(min(LOGICAL_GRID_HEIGHT, len(grid))):
             screen_y = grid_content_offset_y + (row_index * GP_TILE_HEIGHT)
             # Stop drawing rows if they start beyond the calculated bottom boundary or screen edge
             if screen_y >= max_draw_y or screen_y >= HEIGHT: continue

             row_data = grid[row_index]
             for col_index in range(min(LOGICAL_GRID_WIDTH, len(row_data))):
                 screen_x = grid_content_offset_x + (col_index * GP_TILE_WIDTH)
                 # Stop drawing columns if they start beyond the calculated right boundary or screen edge
                 if screen_x >= max_draw_x or screen_x >= WIDTH: continue

                 char = row_data[col_index]
                 # Determine character to draw (handle player cloak)
                 draw_char = char
                 if row_index == player_row and col_index == player_col:
                      draw_char = 'TP' if is_cloaked else 'P'

                 # Draw tile if it exists in the mapping
                 if draw_char in tile_mapping:
                     screen.blit(tile_mapping[draw_char], (screen_x, screen_y))
                 elif char != ' ': # Don't warn for empty space
                      # Optionally draw a placeholder for unknown characters
                      pygame.draw.rect(screen, RED, (screen_x, screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT), 1)


        # Update the values list with the current game state before drawing the HUD
        values = [score, level_num, gems, whips, teleports, keys, cloaks]
        # Draw HUD - HUD positioning is handled within draw_hud itself relative to screen edges/rows
        draw_hud(values, color_input, hud_input)

        # Display level-specific messages (using game_text, which handles its own positioning)
        if level_num == 1:
            game_text(24, "KINGDOM OF KROZ II BY SCOTT MILLER", WHITE, False, True, None)

        # Display pause message if waiting (using game_text)
        if waiting_for_start_key:
            game_text(25, "Press any key to begin this level.", "CHANGING", False, True, BLACK)


    # Enemy movement counters

    slow_counter = 0
    medium_counter = 0
    fast_counter = 0

    running = True
    clock = pygame.time.Clock()

    # --- Main Game Loop ---
    while running:
        dt = clock.tick(GAME_TICK_RATE) / 1000.0 # Delta time in seconds

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # If waiting, any key press starts the level
                if waiting_for_start_key:
                    waiting_for_start_key = False
                    pygame.event.clear(pygame.KEYDOWN) # Prevent immediate move
                    continue # Skip rest of keydown handling

                # --- Keydown handling (only runs if not waiting) ---
                if event.key == pygame.K_p:
                    pause_quit(quitting=False)
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    if pause_quit(quitting=True):
                        running = False # Quit game loop if confirmed
                elif event.key == pygame.K_TAB: # Cheat/Debug: Next level
                    current_level_index = (current_level_index + 1) % len(level_maps)
                    change_level(current_level_index)
                elif event.key == pygame.K_s:
                    handle_save()
                elif event.key == pygame.K_r:
                    handle_restore()
                # Player movement/action keys are handled in player_input()

            elif event.type == pygame.KEYUP:
                 # Handled within player_input() for momentum calculation
                 pass


        # --- Game Logic Updates (only if not waiting) ---
        if not waiting_for_start_key:
            # Process player input (handles movement and actions like whip/teleport/cloak)
            player_input() # This function now handles timing and momentum internally

            # Auto-deactivate cloak after duration
            if is_cloaked and pygame.time.get_ticks() - cloak_start_time > CLOAK_DURATION:
                is_cloaked = False

            # --- Update spell effect timers ---
            # Timers decrease each frame/tick based on dt, or simply decrement per tick if integer-based
            tick_decrement = 1 # Assume timers decrease by 1 each game tick
            if slow_time_effect > 0: slow_time_effect -= tick_decrement
            if invisible_effect > 0: invisible_effect -= tick_decrement
            if speed_time_effect > 0: speed_time_effect -= tick_decrement
            if freeze_effect > 0: freeze_effect -= tick_decrement

            # --- Update enemy movement thresholds based on spell effects ---
            if speed_time_effect > 0:
                slow_threshold = max(1, BASE_SLOW_TIMER // 2) # Faster
                medium_threshold = max(1, BASE_MEDIUM_TIMER // 2)
                fast_threshold = max(1, BASE_FAST_TIMER // 2)
            elif slow_time_effect > 0:
                slow_threshold = BASE_SLOW_TIMER * 2 # Slower
                medium_threshold = BASE_MEDIUM_TIMER * 2
                fast_threshold = BASE_FAST_TIMER * 2
            else: # Reset to base speeds
                slow_threshold = BASE_SLOW_TIMER
                medium_threshold = BASE_MEDIUM_TIMER
                fast_threshold = BASE_FAST_TIMER

            # --- Enemy Movement Logic ---
            # Only move enemies if freeze effect is not active
            if freeze_effect <= 0:
                # Increment counters (could also use time-based accumulation with dt)
                slow_counter += 1
                medium_counter += 1
                fast_counter += 1

                # Move slow enemies (type 1)
                if slow_counter >= slow_threshold:
                    # Iterate backwards for safe removal
                    for i in range(len(slow_enemies) - 1, -1, -1):
                        # Ensure index is still valid after potential player actions
                        if i < len(slow_enemies):
                            enemy_died = move_enemy(slow_enemies[i], "1", 8) # Pass move probability
                            if enemy_died:
                                # Check again if index is valid before deleting
                                if i < len(slow_enemies):
                                     del slow_enemies[i]
                    slow_counter = 0 # Reset counter

                # Move medium enemies (type 2)
                if medium_counter >= medium_threshold:
                    for i in range(len(medium_enemies) - 1, -1, -1):
                         if i < len(medium_enemies):
                             enemy_died = move_enemy(medium_enemies[i], "2", 7)
                             if enemy_died:
                                  if i < len(medium_enemies):
                                       del medium_enemies[i]
                    medium_counter = 0

                # Move fast enemies (type 3)
                if fast_counter >= fast_threshold:
                    for i in range(len(fast_enemies) - 1, -1, -1):
                         if i < len(fast_enemies):
                             enemy_died = move_enemy(fast_enemies[i], "3", 6)
                             if enemy_died:
                                  if i < len(fast_enemies):
                                       del fast_enemies[i]
                    fast_counter = 0

        # --- Drawing ---
        draw_grid() # Handles drawing grid, borders, HUD, and messages
        pygame.display.flip() # Update the full display