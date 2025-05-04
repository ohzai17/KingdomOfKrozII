from levels.maps import *
from levels.traps import *
from utils import *
from utilities.game_text import game_text
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
    full_path = os.path.join(sprites_dir, filename) # Use assets_dir from utils
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
    VALUE_TEXT = RED
    TEXT_BOX = LIGHT_GRAY
    OPTIONS_TEXT = LIGHT_CYAN
    OPTIONS_BOX = RED

    option_list = ["Whip", "Teleport", "Cloak", "Pause", "Quit", "Save", "Restore"]

    is_monochrome = True if color_input == "M" else False

    if is_monochrome:
        BACKGROUND = BLACK
        TEXT = LIGHT_GRAY
        VALUE_TEXT = LIGHT_GRAY
        TEXT_BOX = BLACK
        OPTIONS_TEXT = LIGHT_GRAY
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
    global running # Make running accessible if wait_for_key_press needs to modify it

    screen.fill(BLACK)

    # Scale sprites based on current dimensions and color setting
    scale_gameplay_sprites((GP_TILE_WIDTH, GP_TILE_HEIGHT), color_input)

    level_maps = [level1_map, level2_map, level4_map, level6_map, level8_map, level10_map,
                  level12_map, level14_map, level16_map, level18_map, level20_map, level22_map,
                  level24_map, level25_map]
    current_level_index = 0
    grid = [list(row) for row in level_maps[current_level_index]]

    # Define collidable tiles (adjust as needed based on game rules)
    # Removed 'D' as it's handled separately
    collidable_tiles = {"X", "#", ";", "/", "J", "R", "4", "5", "6", "8", "9",
                        "M", "O", "Y", ">", "0"} # Added breakable objects from whip logic

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

    # Flags for first-time events
    first_solid_wall_hit = True
    first_breakable_wall_hit = True
    first_gem_pickup = True
    first_whip_pickup = True

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
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 20, 10, 0, 0, 0, 1 
        case "A":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 2, 0, 0, 0, 0, 1
        case "N" | " ":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 20, 10, 0, 0, 0, 1
        case "X":
            score, level_num, gems, whips, teleports, keys, cloaks, whip_power = 0, 1, 250, 100, 50, 0, 10, 1

    if mixUp:
        # Adjust starting values if mixUp is True
        gems += 60
        whips += 30
        teleports += 15
        cloaks += 2

    values = [score, level_num, gems, whips, teleports, keys, cloaks]

    # Helper function inside the levels function scope
    def wait_for_key_press(message):
        """Displays a message and waits for any key press."""
        waiting = True
        while waiting:
            # Draw the main grid first to keep the game state visible
            draw_grid()
            # Display the message on top
            game_text(25, message, "CHANGING", False, True, BLACK)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False # Signal main loop to stop
                    waiting = False # Exit this wait loop
                elif event.type == pygame.KEYDOWN:
                    waiting = False # Exit wait loop on any key press
            # Add a small delay to prevent high CPU usage in the wait loop
            pygame.time.wait(10)

    # Function to change to the next level
    def change_level(next_level_index):
        nonlocal grid, player_row, player_col, slow_enemies, medium_enemies, fast_enemies, level_num
        nonlocal waiting_for_start_key # Access the flag
        # Check if level index is valid
        if next_level_index >= len(level_maps):
            # Potentially end game or loop back
            print("Congratulations! You've completed all levels!") # Placeholder
            # For now, loop back
            next_level_index = 0

        # Update level number
        level_num = next_level_index + 1

        # Reset level grid
        grid = [list(row) for row in level_maps[next_level_index]]

        # Reset enemies
        slow_enemies = []
        medium_enemies = []
        fast_enemies = []

        # Find new player position and enemies
        player_found = False
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == "P":
                    player_row, player_col = r, c
                    player_found = True
                elif tile == "1":
                    slow_enemies.append({"row": r, "col": c})
                elif tile == "2":
                    medium_enemies.append({"row": r, "col": c})
                elif tile == "3":
                    fast_enemies.append({"row": r, "col": c})

        if not player_found:
            print(f"Error: Player 'P' not found in level {level_num}. Placing at default.")
            # Find first empty space or default to 1,1 (adjust as needed)
            found_space = False
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == ' ':
                        player_row, player_col = r, c
                        grid[r][c] = 'P'
                        found_space = True
                        break
                if found_space: break
            if not found_space: # Fallback if no empty space
                 player_row, player_col = 1, 1
                 if 0 <= player_row < len(grid) and 0 <= player_col < len(grid[0]):
                     grid[player_row][player_col] = 'P'


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
                # Only solid walls block vision (adjust if other tiles should block)
                if grid[row][col] == "#":
                    return False
        return True

    def move_enemy(enemy, enemy_type, move_prob):
        nonlocal score, gems, player_row, player_col, grid, is_cloaked # Ensure access

        if pygame.time.get_ticks() < freeze_effect:
            return False  # Enemy stays frozen, do not move

        if is_cloaked:
            return False # Enemies don't move if player is cloaked

        row, col = enemy["row"], enemy["col"]

        # Check if enemy was removed (e.g., by whip) before its turn
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != enemy_type:
            return True  # Signal that the enemy should be removed

        # Check line of sight first
        if not has_line_of_sight(row, col, player_row, player_col):
            return False # Stay still if can't see player

        # Original game had different odds for different enemy types
        # Fast enemies had 1/6 chance, medium 1/7, slow 1/8
        # Only give player a move chance if the player can see the enemy
        # (This logic might be complex - simplifying for now: enemy moves if it sees player)
        # if random.randint(0, move_prob-1) == 0:
        #     player_input() # Allow player reaction (might need careful timing)
        #     if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != enemy_type:
        #         return True # Enemy affected by player action

        # Calculate desired direction towards player (allows diagonal)
        dr = 0
        if player_row < row: dr = -1
        elif player_row > row: dr = 1
        dc = 0
        if player_col < col: dc = -1
        elif player_col > col: dc = 1

        if dr == 0 and dc == 0: return False # Already on player (collision handled elsewhere)

        new_row, new_col = row + dr, col + dc

        # Check if the new position is valid and handle collisions
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            target_char = grid[new_row][new_col]

            # Clear current position *before* placing enemy in new spot or handling collision
            grid[row][col] = " "

            # Breaking 'X' blocks
            if target_char == "X":
                grid[new_row][new_col] = " "  # Break the block
                if enemy_type == "1": score += 10
                elif enemy_type == "2": score += 20
                elif enemy_type == "3": score += 30
                enemyCollision()
                return True # Enemy dies breaking block

            # Destroying items
            elif target_char in {"+", "W", "T", "K", "_", "*", "S", "I", "F", "C", "!", "Z", "Q"}:
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type # Move onto item space
                return False # Enemy survives, item gone

            # Empty space
            elif target_char == " ":
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False # Enemy survives

            # Hit player
            elif target_char == "P":
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3

                if gems <= 0:
                    values = [score, level_num, gems, whips, teleports, keys, cloaks] # Update HUD values
                    draw_hud(values, color_input, hud_input)
                    player_death(score, level_num) # Handles game over
                    return True # Enemy caused death

                enemyCollision() # Play enemy hit sound

                # Enemy dies after hitting player
                return True

            # Blocked by wall or other obstacle
            else:
                grid[row][col] = enemy_type # Put enemy back in original spot
                return False
        else:
            # Tried to move out of bounds - stay put
            # grid[row][col] = enemy_type # Already cleared, put back
            return False # Stay in place (shouldn't happen with bounds check)

    def use_whip():
        """Handle the whip animation and enemy interactions, implementing object breaking logic."""
        nonlocal score, whips, slow_enemies, medium_enemies, fast_enemies, values, player_row, player_col, is_cloaked, grid, level_num, gems, teleports, keys, cloaks, hud_input, color_input, whip_power # Added whip_power

        # Check if player has whips
        if whips <= 0:
            zeroCollecible()
            return slow_enemies, medium_enemies, fast_enemies # Return original lists

        # Decrement whip count immediately
        whips -= 1
        values[3] = whips # Update HUD value immediately

        whip_audio() # Play whip sound once per use

        # Define the whip animation positions (counter-clockwise)
        whip_positions = [
            {"row": -1, "col": -1, "sprite_char": "whip1"}, {"row": -1, "col":  0, "sprite_char": "whip3"},
            {"row": -1, "col":  1, "sprite_char": "whip2"}, {"row":  0, "col":  1, "sprite_char": "whip4"},
            {"row":  1, "col":  1, "sprite_char": "whip1"}, {"row":  1, "col":  0, "sprite_char": "whip3"},
            {"row":  1, "col": -1, "sprite_char": "whip2"}, {"row":  0, "col": -1, "sprite_char": "whip4"},
        ]

        enemies_hit_coords = set() # Store coords (r, c) of enemies hit to avoid double counting
        objects_broken_coords = set() # Store coords (r, c) of objects broken
        delay = 25 # Animation delay

        # --- Calculate Grid Offsets (same as draw_grid) ---
        target_grid_width_px = (LOGICAL_GRID_WIDTH + 2) * GP_TILE_WIDTH
        target_grid_height_px = (LOGICAL_GRID_HEIGHT + 2) * GP_TILE_HEIGHT
        if hud_input == "O":
            offset_x = (WIDTH - target_grid_width_px) // 2; offset_y = 0
        elif hud_input == "R":
            offset_x = 0; offset_y = (HEIGHT - target_grid_height_px) // 2
        else:
            offset_x = (WIDTH - target_grid_width_px) // 2; offset_y = (HEIGHT - target_grid_height_px) // 2
        offset_x = max(0, offset_x); offset_y = max(0, offset_y)
        grid_content_offset_x = offset_x + GP_TILE_WIDTH
        grid_content_offset_y = offset_y + GP_TILE_HEIGHT
        bottom_boundary = HEIGHT - (GP_TILE_HEIGHT * 4) if hud_input == "O" else HEIGHT - GP_TILE_HEIGHT
        # --- End Offset Calculation ---

        # --- Whip animation loop ---
        for position in whip_positions:
            whip_row = player_row + position["row"]
            whip_col = player_col + position["col"]

            if not (0 <= whip_row < len(grid) and 0 <= whip_col < len(grid[0])):
                continue # Skip if whip position is out of bounds

            original_tile_char = grid[whip_row][whip_col]
            object_broken_this_step = False

            # --- Check for breakable objects ---
            # Block (X), Moving Block (M), Zap Block (O), Gravity Block (Y)
            if original_tile_char in ['X', 'M', 'O', 'Y']:
                if random.randint(0, 6) < whip_power:
                    object_broken_this_step = True
            # Forest (/), Tree (J)
            elif original_tile_char in ['/', 'J']:
                i_power = 8 if original_tile_char == '/' else whip_power
                if random.randint(0, 6) < i_power:
                    object_broken_this_step = True
            # Statue (>)
            elif original_tile_char == '>':
                if random.randint(0, 49) < whip_power:
                    object_broken_this_step = True
            # Rock (0)
            elif original_tile_char == '0':
                if random.randint(0, 29) < whip_power:
                    object_broken_this_step = True

            if object_broken_this_step:
                objects_broken_coords.add((whip_row, whip_col))
                # Don't check for enemy if object broke

            # --- Check for enemy hit (only if object wasn't broken) ---
            elif original_tile_char in ["1", "2", "3"]:
                enemies_hit_coords.add((whip_row, whip_col))

            # --- Prepare whip sprite ---
            whip_sprite_char = position["sprite_char"]
            colored_whip_image = None
            if whip_sprite_char in tile_mapping:
                original_whip_image = tile_mapping[whip_sprite_char]
                random_color = random.choice(whip_cycle_colors)
                colored_whip_image = original_whip_image.copy()
                colored_whip_image.fill(random_color, special_flags=pygame.BLEND_RGB_MULT)

            # --- Redraw Screen with Whip Animation ---
            screen.fill(BLACK)
            draw_borders(tile_mapping, offset_x, offset_y)

            # Draw the main game grid content
            max_draw_x = grid_content_offset_x + (LOGICAL_GRID_WIDTH * GP_TILE_WIDTH)
            max_draw_y = grid_content_offset_y + (LOGICAL_GRID_HEIGHT * GP_TILE_HEIGHT)

            for r_idx in range(min(LOGICAL_GRID_HEIGHT, len(grid))):
                screen_y = grid_content_offset_y + (r_idx * GP_TILE_HEIGHT)
                if screen_y >= max_draw_y or screen_y >= bottom_boundary: continue
                row_data = grid[r_idx]
                for c_idx in range(min(LOGICAL_GRID_WIDTH, len(row_data))):
                    screen_x = grid_content_offset_x + (c_idx * GP_TILE_WIDTH)
                    if screen_x >= max_draw_x: continue

                    char_to_draw = row_data[c_idx]
                    # Handle player cloak display
                    if r_idx == player_row and c_idx == player_col:
                        char_to_draw = 'TP' if is_cloaked else 'P'

                    # Is this the current whip position?
                    if r_idx == whip_row and c_idx == whip_col:
                        # If an object was broken, draw nothing (it will be ' ' later)
                        if (r_idx, c_idx) in objects_broken_coords:
                            pass # Draw nothing, grid update handles it
                        # If object hit but not broken, or enemy hit, or empty space
                        else:
                            # Draw original tile first (unless it's empty space)
                            if char_to_draw != ' ' and char_to_draw in tile_mapping:
                                screen.blit(tile_mapping[char_to_draw], (screen_x, screen_y))
                            # Draw colored whip sprite on top
                            if colored_whip_image:
                                screen.blit(colored_whip_image, (screen_x, screen_y))
                    # Draw normal tiles (not under the whip)
                    else:
                        char = row_data[c_idx]
                        draw_char = char
                        if r_idx == player_row and c_idx == player_col:
                            if pygame.time.get_ticks() < invisible_effect:
                                draw_char = None  # Fully invisible
                            else:
                                draw_char = 'TP' if is_cloaked else 'P'

                        if draw_char in tile_mapping:
                            screen.blit(tile_mapping[draw_char], (screen_x, screen_y))
                        elif char != ' ':
                            pygame.draw.rect(screen, RED, (screen_x, screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT), 1)

            # --- Draw HUD ---
            # values list already updated at the start of the function
            draw_hud(values, color_input, hud_input)
            # Display level-specific messages
            if level_num == 1:
                game_text(24, "KINGDOM OF KROZ II BY SCOTT MILLER", WHITE, False, True, None)

            pygame.display.flip()
            pygame.time.wait(delay)
        # --- End Whip Animation Loop ---

        # --- Process Hits AFTER Animation ---
        enemy_scores = {"1": 10, "2": 20, "3": 30}

        # Process broken objects (update grid)
        for r, c in objects_broken_coords:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                grid[r][c] = " "
                # Add sounds for breaking specific objects here if desired

        # Process enemy hits (update grid and score)
        enemies_killed_this_whip = []
        for r, c in enemies_hit_coords:
            # Check if the space wasn't an object that got broken
            if (r, c) not in objects_broken_coords and 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                enemy_char = grid[r][c]
                if enemy_char in enemy_scores: # Check if it's still an enemy
                    grid[r][c] = " " # Remove enemy from grid
                    score += enemy_scores[enemy_char]
                    enemies_killed_this_whip.append((r, c, enemy_char))
                    # Add general enemy hit sound here if desired

        # Rebuild enemy lists based on the *final* grid state and killed enemies
        new_slow_enemies = [e for e in slow_enemies if not (e["row"], e["col"]) in enemies_hit_coords]
        new_medium_enemies = [e for e in medium_enemies if not (e["row"], e["col"]) in enemies_hit_coords]
        new_fast_enemies = [e for e in fast_enemies if not (e["row"], e["col"]) in enemies_hit_coords]

        # Update the main enemy lists
        slow_enemies[:] = new_slow_enemies
        medium_enemies[:] = new_medium_enemies
        fast_enemies[:] = new_fast_enemies

        # Return the updated lists (though modified in place)
        return slow_enemies, medium_enemies, fast_enemies

    is_cloaked = False
    cloak_start_time = 0
    CLOAK_DURATION = 10000 # Milliseconds cloak lasts (e.g., 10 seconds)

    def cloak():
        """ Handles cloak activation. """
        nonlocal is_cloaked, cloak_start_time, cloaks, values
        if cloaks > 0 and not is_cloaked:
            cloaks -= 1
            values[6] = cloaks # Update HUD value
            cloak_start_time = pygame.time.get_ticks()
            is_cloaked = True
            # Play cloak sound?

    def teleport(t_trap=False):
        """Teleports the player to a random empty space on the grid with a flickering effect."""
        nonlocal player_row, player_col, grid, hud_input, values, color_input, teleports # Modifies player position, grid, teleports

        if not t_trap: # Only decrement if it's a scroll, not a trap
            if teleports <= 0:
                zeroCollecible()
                return
            teleports -= 1
            values[4] = teleports # Update HUD value

        # --- Recalculate Grid Offsets (same logic as draw_grid) ---
        target_grid_width_px = (LOGICAL_GRID_WIDTH + 2) * GP_TILE_WIDTH
        target_grid_height_px = (LOGICAL_GRID_HEIGHT + 2) * GP_TILE_HEIGHT
        if hud_input == "O":
            offset_x = (WIDTH - target_grid_width_px) // 2; offset_y = 0
        elif hud_input == "R":
            offset_x = 0; offset_y = (HEIGHT - target_grid_height_px) // 2
        else:
            offset_x = (WIDTH - target_grid_width_px) // 2; offset_y = (HEIGHT - target_grid_height_px) // 2
        offset_x = max(0, offset_x); offset_y = max(0, offset_y)
        grid_content_offset_x = offset_x + GP_TILE_WIDTH
        grid_content_offset_y = offset_y + GP_TILE_HEIGHT
        # --- End Offset Calculation ---

        # Find all empty spaces (' ') on the current grid
        empty_spaces = []
        for r, row_data in enumerate(grid):
            for c, char in enumerate(row_data):
                 if r < LOGICAL_GRID_HEIGHT and c < LOGICAL_GRID_WIDTH and char == ' ':
                     empty_spaces.append((r, c))

        if not empty_spaces:
            print("No empty spaces to teleport to!")
            # Refund teleport scroll if used?
            if not t_trap:
                teleports += 1
                values[4] = teleports
            return

        # --- Flicker at the original position ---
        original_screen_x = grid_content_offset_x + player_col * GP_TILE_WIDTH
        original_screen_y = grid_content_offset_y + player_row * GP_TILE_HEIGHT
        original_rect = pygame.Rect(original_screen_x, original_screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT)
        player_sprite = tile_mapping.get('P')
        if not player_sprite: return # Cannot proceed without player sprite

        # Determine background sprite under player (should be ' ' after move starts)
        original_bg_char = ' '
        original_bg_sprite = tile_mapping.get(original_bg_char)

        original_flicker_count = 6 # Reduced flickers
        original_flicker_delay = 60

        for _ in range(original_flicker_count):
            # Fill original position with random color, draw player
            random_color = random.choice(blinking_text_color_list)
            screen.fill(random_color, original_rect)
            screen.blit(player_sprite, original_rect.topleft)
            pygame.display.update(original_rect)
            pygame.time.delay(original_flicker_delay // 2)

            # Clear player (fill black/background color then draw original background tile)
            screen.fill(BLACK, original_rect)
            if original_bg_sprite: screen.blit(original_bg_sprite, original_rect.topleft)
            pygame.display.update(original_rect)
            pygame.time.delay(original_flicker_delay // 2)

        # --- Intermediate Flicker Loop ---
        last_intermediate_rect = None
        tp_sprite = tile_mapping.get('TP')
        if not tp_sprite: tp_sprite = player_sprite # Fallback

        intermediate_flicker_count = 15 # Reduced intermediate flickers
        intermediate_delay = 15
        if t_trap:
            intermediate_flicker_count = 1 # Very short flicker for trap
            teleportTrap()

        final_row, final_col = -1, -1 # Initialize final position
        final_screen_x, final_screen_y = -1, -1
        final_rect = None

        for i in range(intermediate_flicker_count):
            new_row, new_col = random.choice(empty_spaces)
            intermediate_screen_x = grid_content_offset_x + new_col * GP_TILE_WIDTH
            intermediate_screen_y = grid_content_offset_y + new_row * GP_TILE_HEIGHT
            intermediate_rect = pygame.Rect(intermediate_screen_x, intermediate_screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT)

            # Clear previous flicker location
            if last_intermediate_rect:
                prev_r, prev_c = -1, -1
                if GP_TILE_WIDTH > 0: prev_c = (last_intermediate_rect.x - grid_content_offset_x) // GP_TILE_WIDTH
                if GP_TILE_HEIGHT > 0: prev_r = (last_intermediate_rect.y - grid_content_offset_y) // GP_TILE_HEIGHT
                if 0 <= prev_r < len(grid) and 0 <= prev_c < len(grid[prev_r]):
                    original_char = grid[prev_r][prev_c]
                    # Ensure the char is not the player temporarily placed during flicker
                    if prev_r == player_row and prev_c == player_col and not t_trap: # Don't assume space if it was a trap activation
                         original_char = ' '
                    bg_sprite = tile_mapping.get(original_char)
                    if bg_sprite: screen.blit(bg_sprite, last_intermediate_rect.topleft)
                    else: screen.fill(BLACK, last_intermediate_rect)
                else: screen.fill(BLACK, last_intermediate_rect) # Fallback clear

            # Draw TP icon at new flicker location
            screen.blit(tp_sprite, (intermediate_screen_x, intermediate_screen_y))
            pygame.display.update([last_intermediate_rect, intermediate_rect] if last_intermediate_rect else [intermediate_rect])
            last_intermediate_rect = intermediate_rect

            pygame.time.delay(intermediate_delay)

            # Store the final destination from the last iteration
            if i == intermediate_flicker_count - 1:
                 final_row, final_col = new_row, new_col
                 final_screen_x = intermediate_screen_x
                 final_screen_y = intermediate_screen_y
                 final_rect = intermediate_rect

        # --- Clear the very last intermediate TP icon ---
        if last_intermediate_rect and 0 <= final_row < len(grid) and 0 <= final_col < len(grid[0]):
                # Use the character from the grid at the *final* destination
                original_char = grid[final_row][final_col] # Should be ' '
                bg_sprite = tile_mapping.get(original_char)
                if bg_sprite: screen.blit(bg_sprite, last_intermediate_rect.topleft)
                else: screen.fill(BLACK, last_intermediate_rect)
                pygame.display.update(last_intermediate_rect)
        elif last_intermediate_rect: # Fallback clear if final pos invalid
             screen.fill(BLACK, last_intermediate_rect)
             pygame.display.update(last_intermediate_rect)


        # --- Check if final position was determined ---
        if final_row == -1 or final_col == -1 or final_rect is None:
             print("Error: Final teleport position not determined.")
             # No need to clear last_intermediate_rect again, already done above
             return # Avoid errors if final position wasn't set

        # --- Final Destination Flicker (Moved outside the loop) ---
        final_bg_char = grid[final_row][final_col] # Should be ' '
        final_bg_sprite = tile_mapping.get(final_bg_char)
        final_flicker_count = 6 # Reduced final flickers
        final_flicker_delay = 50

        for _ in range(final_flicker_count):
            # Fill final position with random color, draw player
            random_color = random.choice(blinking_text_color_list)
            screen.fill(random_color, final_rect)
            screen.blit(player_sprite, (final_screen_x, final_screen_y))
            pygame.display.update(final_rect)
            pygame.time.delay(final_flicker_delay // 2)

            # Clear player (fill black/background color then draw background)
            screen.fill(BLACK, final_rect)
            if final_bg_sprite: screen.blit(final_bg_sprite, final_rect.topleft)
            pygame.display.update(final_rect)
            pygame.time.delay(final_flicker_delay // 2)

        # --- Update Game State ---
        # Clear old player position from the grid (logical update)
        # Check bounds before clearing old position
        if 0 <= player_row < len(grid) and 0 <= player_col < len(grid[0]):
            # Only clear if it's still the player (might have changed due to trap logic)
            if grid[player_row][player_col] == 'P':
                 grid[player_row][player_col] = ' '
        else:
            print(f"Warning: Original player position ({player_row}, {player_col}) was out of bounds before teleport.")

        # Update the grid with new player position (logical update)
        if 0 <= final_row < len(grid) and 0 <= final_col < len(grid[0]):
             grid[final_row][final_col] = 'P'
             # Update player's logical position
             player_row, player_col = final_row, final_col
        else:
             print(f"Error: Final teleport destination ({final_row}, {final_col}) is out of bounds.")
             # Potentially place player somewhere safe or handle error

    # --- Movement settings ---
    movement_cooldown = 100  # ms between moves
    last_move_time = 0
    # Momentum calculation removed for simplicity, can be added back if needed

    def player_input():
        """Handle player movement, whip, teleport, and cloak actions."""
        nonlocal player_row, player_col, last_move_time, keys_pressed
        nonlocal score, gems, whips, teleports, keys, cloaks, is_cloaked, values

        current_time = pygame.time.get_ticks()
        time_since_last_move = current_time - last_move_time

        # --- Handle Non-Movement Actions First (using key state) ---
        key_pressed = pygame.key.get_pressed() # Get current key state

        action_taken = False # Flag to see if an action consumed the turn

        # Check for actions like whip, teleport, cloak
        if key_pressed[pygame.K_w]: # Whip
            if whips > 0:
                use_whip() # This function now decrements whips and updates HUD
                action_taken = True
        elif key_pressed[pygame.K_t]: # Teleport
            if teleports > 0:
                teleport() # This function now decrements teleports and updates HUD
                action_taken = True
        elif key_pressed[pygame.K_c]: # Cloak
            if cloaks > 0 and not is_cloaked:
                cloak() # This function now decrements cloaks and updates HUD
                action_taken = True
        # Add other non-movement actions here (Pause, Quit, Save, Restore)
        elif key_pressed[pygame.K_p]: # Pause
             pause_quit(quitting=False)
             action_taken = True # Pausing counts as an action to reset cooldown
        elif key_pressed[pygame.K_q]: # Quit Prompt
             if pause_quit(quitting=True):
                 running = False # Signal main loop to stop
             action_taken = True # Prompting counts as an action
        elif key_pressed[pygame.K_s]: # Save
             handle_save()
             action_taken = True
        elif key_pressed[pygame.K_r]: # Restore
             handle_restore()
             action_taken = True # Restore pauses, counts as action

        # If an action was taken, apply cooldown and return
        if action_taken:
            last_move_time = current_time
            return

        # --- Handle Movement (only if no action taken and cooldown passed) ---
        if time_since_last_move >= movement_cooldown:
            move_attempted = False
            # Define movement keys (prioritize cardinal directions if needed)
            direction_keys = [
                (pygame.K_UP, (-1, 0)), (pygame.K_DOWN, (1, 0)),
                (pygame.K_LEFT, (0, -1)), (pygame.K_RIGHT, (0, 1)),
                (pygame.K_u, (-1, -1)), (pygame.K_i, (-1, 0)), (pygame.K_o, (-1, 1)),
                (pygame.K_j, (0, -1)),                         (pygame.K_l, (0, 1)),
                (pygame.K_n, (1, -1)), (pygame.K_m, (1, 0)), (pygame.K_COMMA, (1, 1))
            ]

            for key_code, (dr, dc) in direction_keys:
                if key_pressed[key_code]: # Check if this direction key is currently pressed
                    move_attempted = True
                    new_row, new_col = player_row + dr, player_col + dc
                    move_successful = process_move(new_row, new_col)

                    # Update Last Move Time REGARDLESS of success
                    # This prevents rapid attempts when blocked
                    last_move_time = current_time

                    if move_successful:
                        footStep() # Play footstep sound on successful move
                    # else: Collision sound handled in process_move or specific interactions

                    break # Process only the first pressed direction key found

            # If no direction key was pressed in this check, reset all momentum
            # (Momentum logic removed for simplicity)

    def nonlocal_set_freeze(end_time):
        nonlocal freeze_effect
        freeze_effect = end_time

    def nonlocal_set_invisible(end_time):
        nonlocal invisible_effect
        invisible_effect = end_time

    def process_move(new_row, new_col):
        """Process a player movement attempt to a new position."""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys, level_num, cloaks, whip_power
        nonlocal current_level_index, waiting_for_start_key
        nonlocal slow_enemies, medium_enemies, fast_enemies
        # Add nonlocal declarations for the new flags
        nonlocal first_solid_wall_hit, first_breakable_wall_hit, first_gem_pickup, first_whip_pickup
        # Add nonlocal for spell effect ticks
        nonlocal slow_time_effect_ticks, speed_time_effect_ticks, freeze_effect_ticks

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
            # Store original position before potentially waiting
            old_player_row, old_player_col = player_row, player_col
            # Move player logically first
            grid[old_player_row][old_player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            # Check for first-time pickup
            if first_gem_pickup:
                wait_for_key_press("Gems give you both points and strength")
                first_gem_pickup = False
            return True # Move successful
        elif target_char == "W": # Whip
            whips += 1
            score += 10
            # Store original position before potentially waiting
            old_player_row, old_player_col = player_row, player_col
            # Move player logically first
            grid[old_player_row][old_player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            # Check for first-time pickup
            if first_whip_pickup:
                wait_for_key_press("You found a Whip.")
                first_whip_pickup = False
            return True # Move successful
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
            slow_time_effect_ticks = SPELL_DURATION_TICKS # Activate effect
            moved = True
        elif target_char == "I": # Invisible (Placeholder - maybe cloak?)
            score += 10
            # Effect applied in main loop
            moved = True
        elif target_char == "F": # SpeedTime
            score += 20
            speed_time_effect_ticks = SPELL_DURATION_TICKS # Activate effect
            moved = True
        elif target_char == "C": # Chest
            score += 50
            grid[player_row][player_col] = " " # Clear old position
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Place player on trap temporarily
            draw_grid() # Redraw the entire grid with player on the trap
            pygame.display.flip() # Update the display to show this frame
            chestPickup() # Play sound for chest pickup
            wait_for_key_press("You found 4 gems and 3 whips inside the chest!")
            # Add random gems/whips logic here if needed
            # Since we return True, the standard move logic below won't run for chest
            # Need to add the gem/whip gain here directly
            gems += 4
            whips += 3
            return True # Move was successful (led to message)
        elif target_char == "!": # Tablet
            score += level_num + 250
            moved = True

        elif target_char == ".": # teleport trap
            score -= 50
            # Move player onto the trap space *before* teleporting
            grid[player_row][player_col] = " " # Clear old position
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Place player on trap temporarily
            draw_grid() # Redraw the entire grid with player on the trap
            pygame.display.flip() # Update the display to show this frame
            pygame.time.wait(150) # Pause briefly
            teleport(t_trap=True) # Call teleport immediately
            return True # Move was successful (led to teleport)
        elif target_char == "Q": # Power Ring
            score += 20
            whip_power += 1 # Increase whip power
            # Store original position before waiting
            old_player_row, old_player_col = player_row, player_col
            # Move player logically first
            grid[old_player_row][old_player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Player replaces enemy
            # Wait for player to press any key after picking up
            wait_for_key_press("A Power Ring--your whip is now a little stronger!")
            return True
        elif target_char == "L": # Stairs
            score += level_num * 100 # Example score for level change
            next_level_idx = (current_level_index + 1) # No modulo here if we want an end condition
            # Check if it's the last level before changing
            if next_level_idx >= len(level_maps):
                 print("Level change: Reached end of defined levels.")
                 # Handle game completion or loop back
                 # For now, let change_level handle looping or error
                 pass # Or add specific end-game logic here

            change_level(next_level_idx)
            current_level_index = next_level_idx % len(level_maps) # Update index tracker safely
            return True # Return True immediately as level changes

        # --- If moved onto a collectable or empty space (and not handled above) ---
        if moved:
            grid[player_row][player_col] = " " # Clear old position
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P" # Place player in new position
            return True

        # --- Check Collisions ---
        elif target_char in collidable_tiles:
            # Solid Wall ('#')
            if target_char == "#":
                if score > 20: score -= 20
                if first_solid_wall_hit:
                    wait_for_key_press("A Solid Wall blocks your way.")
                    first_solid_wall_hit = False
                return False # Movement blocked

            # Breakable Wall ('X') - Also check other breakables hit by whip
            elif target_char in ['X', 'M', 'O', 'Y', '/', 'J', '>', '0']:
                 if score > 20: score -= 20 # Penalty for hitting breakable walls?
                 if target_char == 'X' and first_breakable_wall_hit:
                     wait_for_key_press("A Breakable Wall blocks your way.")
                     first_breakable_wall_hit = False
                 # Add messages for other breakable types if desired
                 return False # Movement blocked (player cannot break by walking)

            # Default block for other collidable tiles in the set
            # (e.g., River 'R', specific wall types '4'-'9')
            # Add specific messages or sounds if needed
            return False

        # Handle door 'D' - requires a key (Not in collidable_tiles set)
        elif target_char == 'D':
            if keys > 0:
                keys -= 1
                grid[player_row][player_col] = " " # Clear old position
                player_row, player_col = new_row, new_col
                grid[player_row][player_col] = "P" # Move player onto door space (it becomes empty)
                # Play door opening sound?
                return True # Successful move through door
            else:
                # No key, cannot move
                # Play locked door sound?
                game_text(25, "You need a key to open this door.", "CHANGING", False, True, BLACK)
                pygame.display.flip()
                pygame.time.wait(1000) # Show message briefly
                return False # Movement blocked

        # --- Handle Enemy Collision (if player moves onto enemy) ---
        # This case might happen if player moves faster than enemy reaction
        elif target_char in ["1", "2", "3"]:
             # Player moving onto an enemy instantly triggers gem loss/death
             if target_char == "1": gems -= 1
             elif target_char == "2": gems -= 2
             elif target_char == "3": gems -= 3

             enemyCollision() # Play collision sound
        
             if gems <= 0:
                 values = [score, level_num, gems, whips, teleports, keys, cloaks] # Update HUD values
                 draw_hud(values, color_input, hud_input)
                 player_death(score, level_num)
                 return True # Move technically happened before death sequence

             # Clear old player position, place player, remove enemy from grid
             grid[player_row][player_col] = " "
             player_row, player_col = new_row, new_col
             grid[player_row][player_col] = "P" # Player replaces enemy

             # Remove the enemy from its list (important!)
             if target_char == "1": slow_enemies = [e for e in slow_enemies if not (e["row"] == new_row and e["col"] == new_col)]
             elif target_char == "2": medium_enemies = [e for e in medium_enemies if not (e["row"] == new_row and e["col"] == new_col)]
             elif target_char == "3": fast_enemies = [e for e in fast_enemies if not (e["row"] == new_row and e["col"] == new_col)]
             return True

        elif target_char in {"»", "«"}:
            direction = "right" if target_char == "»" else "left"
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            pygame.display.flip()
            spear_trap(
                grid,
                {"1": slow_enemies, "2": medium_enemies, "3": fast_enemies},
                player_row, player_col, direction,
                screen, tile_mapping, GP_TILE_WIDTH, GP_TILE_HEIGHT,
                draw_grid
            )
            return True

        elif target_char == "Z":  # Freeze
            score += 5 # Example score
            freeze_effect_ticks = SPELL_DURATION_TICKS # Activate effect
            moved = True
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            draw_grid()
            pygame.display.flip()

            # The freeze_trap function seems redundant if we use ticks now
            # from levels.traps import freeze_trap
            # freeze_trap(
            #     freeze_duration_ms=3000,
            #     get_ticks_fn=pygame.time.get_ticks,
            #     set_freeze_effect_fn=lambda end_time: nonlocal_set_freeze(end_time),
            # )
            return True

        elif target_char == "ö":
            from levels.traps import blindness_trap
            blindness_trap(
                duration_ms=3000,
                get_ticks_fn=pygame.time.get_ticks,
                set_invisible_effect_fn=nonlocal_set_invisible
            )
            score += 5
            moved = True
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"

            return True

        # Default case: If target_char is not handled above, it's likely an unhandled obstacle
        # or an error. For safety, block movement.
        print(f"Warning: Unhandled character '{target_char}' at ({new_row}, {new_col}). Blocking move.")
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
    freeze_effect = 0

    # Spell effect timers (in ticks)
    GAME_TICK_RATE = 16.0 # Target ticks per second
    SPELL_DURATION_SECONDS = 5 # How long spells last
    SPELL_DURATION_TICKS = int(SPELL_DURATION_SECONDS * GAME_TICK_RATE)

    # Initialize spell tick counters
    slow_time_effect_ticks = 0
    speed_time_effect_ticks = 0
    freeze_effect_ticks = 0
    # Note: invisible_effect seems to use a different mechanism (end time)
    invisible_effect = 0 # Keep this as end time for now, used by blindness trap

    waiting_for_start_key = True # Start paused

    # Ensure the "saves" directory exists
    saves_dir = os.path.join("src", "saves")
    if not os.path.exists(saves_dir):
        try:
            os.makedirs(saves_dir)
        except OSError as e:
            print(f"Error creating saves directory: {e}")
            # Handle error appropriately, maybe disable saving

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
                "cloaks": state["cloaks"],
                "whip_power": state["whip_power"],
                "current_level_index": state["current_level_index"],
                # Save first-time flags
                "first_solid_wall_hit": state["first_solid_wall_hit"],
                "first_breakable_wall_hit": state["first_breakable_wall_hit"],
                "first_gem_pickup": state["first_gem_pickup"],
                "first_whip_pickup": state["first_whip_pickup"],
                # Optionally save enemy positions (more complex restore)
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
            # Display prompt (redraw necessary elements)
            draw_grid() # Redraw background
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
                        draw_grid() # Redraw background
                        game_text(25, prompt_message + input_char, WHITE, False, True, BLACK)
                        pygame.display.flip()
                        pygame.time.wait(300)
                        return slot
                    elif event.key == pygame.K_ESCAPE:
                         draw_grid() # Redraw background
                         game_text(25, f"{action} Cancelled", YELLOW, False, True, BLACK)
                         pygame.display.flip()
                         pygame.time.wait(1000)
                         return None # User cancelled
                    # Ignore other keys
            pygame.time.wait(10) # Prevent high CPU usage

    def handle_save():
        """Handle the save confirmation and process."""
        nonlocal player_row, player_col, score, level_num, gems, whips, teleports, keys, cloaks, whip_power
        nonlocal current_level_index
        nonlocal first_solid_wall_hit, first_breakable_wall_hit, first_gem_pickup, first_whip_pickup

        # Display confirmation prompt
        draw_grid() # Redraw background
        game_text(25, "Are you sure you want to SAVE (Y/N)?", "CHANGING", False, True, BLACK)
        pygame.display.flip()

        confirmed = None # Use None to indicate waiting
        while confirmed is None: # Wait for Y/N input
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
            pygame.time.wait(10) # Prevent high CPU usage

        if confirmed:
            save_slot = prompt_save_restore("SAVE")
            if save_slot:
                # Gather current state
                current_state = {
                    "player_row": player_row, "player_col": player_col,
                    "score": score, "level_num": level_num, "gems": gems,
                    "whips": whips, "teleports": teleports, "keys": keys,
                    "cloaks": cloaks, "whip_power": whip_power,
                    "current_level_index": current_level_index,
                    "first_solid_wall_hit": first_solid_wall_hit,
                    "first_breakable_wall_hit": first_breakable_wall_hit,
                    "first_gem_pickup": first_gem_pickup,
                    "first_whip_pickup": first_whip_pickup,
                }
                save_game(current_state, save_slot)
        else:
             draw_grid() # Redraw background
             game_text(25, "Save Cancelled", YELLOW, False, True, BLACK)
             pygame.display.flip()
             pygame.time.wait(1000)


    def handle_restore():
        """Handle the restore confirmation and process."""
        nonlocal grid, player_row, player_col, score, level_num, gems, whips, teleports, keys, cloaks, whip_power
        nonlocal current_level_index, slow_enemies, medium_enemies, fast_enemies, waiting_for_start_key, values
        nonlocal first_solid_wall_hit, first_breakable_wall_hit, first_gem_pickup, first_whip_pickup

        # Display confirmation prompt
        draw_grid() # Redraw background
        game_text(25, "Are you sure you want to RESTORE (Y/N)?", "CHANGING", False, True, BLACK)
        pygame.display.flip()

        confirmed = None
        while confirmed is None: # Wait for Y/N input
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
            pygame.time.wait(10) # Prevent high CPU usage

        if confirmed:
            restore_slot = prompt_save_restore("RESTORE")
            if restore_slot:
                restored_state = restore_game(restore_slot)
                if restored_state:
                    try:
                        # Apply the restored state
                        current_level_index = restored_state["current_level_index"]
                        level_num = restored_state["level_num"]

                        # Regenerate grid from the correct level map
                        if 0 <= current_level_index < len(level_maps):
                            grid = [list(row) for row in level_maps[current_level_index]]
                        else:
                            raise IndexError(f"Restored level index {current_level_index} is out of bounds.")

                        # Restore player state
                        player_row = restored_state["player_row"]
                        player_col = restored_state["player_col"]
                        score = restored_state["score"]
                        gems = restored_state["gems"]
                        whips = restored_state["whips"]
                        teleports = restored_state["teleports"]
                        keys = restored_state["keys"]
                        cloaks = restored_state["cloaks"]
                        whip_power = restored_state.get("whip_power", 1) # Default if missing

                        # Restore first-time flags
                        first_solid_wall_hit = restored_state.get("first_solid_wall_hit", True)
                        first_breakable_wall_hit = restored_state.get("first_breakable_wall_hit", True)
                        first_gem_pickup = restored_state.get("first_gem_pickup", True)
                        first_whip_pickup = restored_state.get("first_whip_pickup", True)

                        # Clear existing player marker from regenerated grid (if any)
                        for r in range(len(grid)):
                            for c in range(len(grid[r])):
                                if grid[r][c] == 'P':
                                    grid[r][c] = ' ' # Assume space underneath

                        # Ensure player is placed correctly on the regenerated grid
                        if 0 <= player_row < len(grid) and 0 <= player_col < len(grid[0]):
                             # Check if the target space is walkable before placing
                             if grid[player_row][player_col] == ' ':
                                 grid[player_row][player_col] = "P"
                             else:
                                 print(f"Warning: Restored player position ({player_row}, {player_col}) is blocked on level {level_num}. Finding alternative.")
                                 # Find nearest empty space? For now, just warn.
                                 # Maybe place at default start?
                        else:
                             print(f"Warning: Restored player position ({player_row}, {player_col}) is out of bounds for level {level_num}. Resetting.")
                             # Find default start 'P' or first empty space
                             # (Add logic similar to change_level player finding)

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
                        # Redraw immediately to show restored state before unpausing
                        draw_grid()
                        pygame.display.flip()

                    except KeyError as e:
                         print(f"Error applying restored state: Missing key {e}")
                         draw_grid() # Redraw background
                         game_text(25, f"Error in Save Data!", RED, False, True, BLACK)
                         pygame.display.flip()
                         pygame.time.wait(1500)
                    except IndexError as e:
                         print(f"Error applying restored state: {e}")
                         draw_grid() # Redraw background
                         game_text(25, f"Error in Save Data!", RED, False, True, BLACK)
                         pygame.display.flip()
                         pygame.time.wait(1500)

        else: # Restore cancelled
             draw_grid() # Redraw background
             game_text(25, "Restore Cancelled", YELLOW, False, True, BLACK)
             pygame.display.flip()
             pygame.time.wait(1000)

    def draw_borders(mapping, offset_x=0, offset_y=0): # Add offset parameters
         """Draws the static level and window borders."""
         border_char = '^'
         if border_char not in mapping:
              # print("Warning: Border character '^' not found in tile_mapping.") # Reduce console noise
              return

         border_image = mapping[border_char]
         border_w, border_h = border_image.get_size()

         # Draw level_border (inner border) - Apply offsets
         for row_index, row_str in enumerate(level_border):
             screen_draw_y = offset_y + (row_index * border_h) # Use border height
             if screen_draw_y >= HEIGHT: continue
             for col_index, char in enumerate(row_str):
                 screen_draw_x = offset_x + (col_index * border_w) # Use border width
                 if screen_draw_x >= WIDTH: continue
                 if char == border_char:
                     screen.blit(border_image, (screen_draw_x, screen_draw_y))

         # Draw window_border (outer border, offset) - Apply offsets
         # Assumes window_border positions are relative to level_border origin (0,0)
         for row_index, row_str in enumerate(window_border):
             base_y = (row_index * border_h) - border_h # Offset by one tile height up
             screen_draw_y = offset_y + base_y # Apply main offset
             # Basic culling
             if screen_draw_y + border_h <= 0 or screen_draw_y >= HEIGHT: continue
             for col_index, char in enumerate(row_str):
                 base_x = (col_index * border_w) - border_w # Offset by one tile width left
                 screen_draw_x = offset_x + base_x # Apply main offset
                 # Basic culling
                 if screen_draw_x + border_w <= 0 or screen_draw_x >= WIDTH: continue
                 if char == border_char:
                     screen.blit(border_image, (screen_draw_x, screen_draw_y))

    def draw_grid():
        """Draws the game grid, borders, HUD, and messages."""
        nonlocal score, level_num, gems, whips, teleports, keys, cloaks, values # Ensure access to latest values
        screen.fill(BLACK)

        # --- Calculate Target Grid Pixel Size & Offsets ---
        target_grid_width_px = (LOGICAL_GRID_WIDTH + 2) * GP_TILE_WIDTH
        target_grid_height_px = (LOGICAL_GRID_HEIGHT + 2) * GP_TILE_HEIGHT
        if hud_input == "O":
            offset_x = (WIDTH - target_grid_width_px) // 2; offset_y = 0
        elif hud_input == "R":
            offset_x = 0; offset_y = (HEIGHT - target_grid_height_px) // 2
        else:
            offset_x = (WIDTH - target_grid_width_px) // 2; offset_y = (HEIGHT - target_grid_height_px) // 2
        offset_x = max(0, offset_x); offset_y = max(0, offset_y)
        grid_content_offset_x = offset_x + GP_TILE_WIDTH
        grid_content_offset_y = offset_y + GP_TILE_HEIGHT
        max_draw_x = grid_content_offset_x + (LOGICAL_GRID_WIDTH * GP_TILE_WIDTH)
        max_draw_y = grid_content_offset_y + (LOGICAL_GRID_HEIGHT * GP_TILE_HEIGHT)
        # Calculate bottom boundary for drawing content (consider HUD)
        bottom_boundary = HEIGHT
        if hud_input == "O":
             # Approximate HUD height (adjust if needed)
             hud_height_tiles = 8 # Example: 8 rows for bottom HUD text/boxes
             bottom_boundary = HEIGHT - (hud_height_tiles * GP_TILE_HEIGHT)
        # --- End Offset Calculation ---

        # Draw borders using the helper function with calculated offsets
        draw_borders(tile_mapping, offset_x, offset_y)

        # Draw the main game grid content
        for row_index in range(min(LOGICAL_GRID_HEIGHT, len(grid))):
             screen_y = grid_content_offset_y + (row_index * GP_TILE_HEIGHT)
             # Stop drawing rows if they start beyond the calculated bottom boundary or screen edge
             if screen_y >= max_draw_y or screen_y >= bottom_boundary: continue

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
                 elif char != ' ': # Don't warn/draw for empty space
                      # Optionally draw a placeholder for unknown characters
                      pygame.draw.rect(screen, RED, (screen_x, screen_y, GP_TILE_WIDTH, GP_TILE_HEIGHT), 1)

        # Update the values list with the current game state before drawing the HUD
        values = [score, level_num, gems, whips, teleports, keys, cloaks]
        # Draw HUD - HUD positioning is handled within draw_hud itself
        draw_hud(values, color_input, hud_input)

        # Display level-specific messages (using game_text)
        if level_num == 1:
            game_text(24, "KINGDOM OF KROZ II BY SCOTT MILLER", WHITE, False, True, None)
        # Add other level messages here if needed

        # Display pause message if waiting (using game_text)
        # Note: wait_for_key_press handles its own message display
        if waiting_for_start_key: # Avoid drawing if another wait loop is active
            game_text(25, "Press any key to begin this level.", "CHANGING", False, True, BLACK)


    # Enemy movement counters
    slow_counter = 0
    medium_counter = 0
    fast_counter = 0

    running = True # Main loop flag
    clock = pygame.time.Clock()

# ...existing code...
    # --- Main Game Loop ---
    while running:
        dt_ms = clock.tick(GAME_TICK_RATE) # Delta time in milliseconds
        # dt_sec = dt_ms / 1000.0 # Delta time in seconds if needed

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Optionally prompt before quitting
                if pause_quit(quitting=True):
                    running = False
                else:
                    # If quit cancelled, might need to reset key states or cooldowns
                    last_move_time = pygame.time.get_ticks() # Prevent immediate move
            elif event.type == pygame.KEYDOWN:
                # If waiting for level start, any key press starts it
                if waiting_for_start_key:
                    waiting_for_start_key = False
                    pygame.event.clear(pygame.KEYDOWN) # Prevent immediate move/action
                    last_move_time = pygame.time.get_ticks() # Reset cooldown
                    continue # Skip rest of keydown handling for this frame

                # --- Keydown handling (only runs if not waiting for level start) ---
                # Actions like pause, quit prompt, save, restore are handled directly
                # by player_input() using get_pressed() for responsiveness.
                # Debug/cheat keys can be handled here:
                if event.key == pygame.K_TAB: # Cheat: Next level
                    current_level_index = (current_level_index + 1) % len(level_maps)
                    change_level(current_level_index)
                    last_move_time = pygame.time.get_ticks() # Reset cooldown
                # Add other single-press debug keys if needed

            # KEYUP events are not explicitly handled here, but get_pressed() covers held keys

        # --- Game Logic Updates (only if not waiting for level start) ---
        if not waiting_for_start_key:
            # Process player input (handles movement and actions like whip/teleport/cloak)
            player_input() # This function now handles timing and actions

            # Auto-deactivate cloak after duration
            if is_cloaked and pygame.time.get_ticks() - cloak_start_time > CLOAK_DURATION:
                is_cloaked = False
                # Play cloak wear off sound?

            # --- Update spell effect timers (using ticks) ---
            tick_decrement = 1 # Decrement by 1 each game tick
            if slow_time_effect_ticks > 0: slow_time_effect_ticks -= tick_decrement
            if speed_time_effect_ticks > 0: speed_time_effect_ticks -= tick_decrement
            if freeze_effect > 0: freeze_effect -= tick_decrement

            # --- Update enemy movement thresholds based on spell effects ---
            if speed_time_effect_ticks > 0:
                slow_threshold = max(1, BASE_SLOW_TIMER // 2)
                medium_threshold = max(1, BASE_MEDIUM_TIMER // 2)
                fast_threshold = max(1, BASE_FAST_TIMER // 2)
            elif slow_time_effect_ticks > 0:
                slow_threshold = BASE_SLOW_TIMER * 2
                medium_threshold = BASE_MEDIUM_TIMER * 2
                fast_threshold = BASE_FAST_TIMER * 2
            else: # Reset to base speeds
                slow_threshold = BASE_SLOW_TIMER
                medium_threshold = BASE_MEDIUM_TIMER
                fast_threshold = BASE_FAST_TIMER

            # --- Enemy Movement Logic ---
            # Only move enemies if freeze effect is not active
            if pygame.time.get_ticks() >= freeze_effect:
                # Increment counters (could also use time-based accumulation with dt)
                slow_counter += 1
                medium_counter += 1
                fast_counter += 1

                # Move slow enemies (type 1)
                if slow_counter >= slow_threshold:
                    current_slow_enemies = list(slow_enemies) # Iterate over a copy
                    for i in range(len(current_slow_enemies) - 1, -1, -1):
                        enemy = current_slow_enemies[i]
                        # Check if enemy still exists in the main list before moving
                        if enemy in slow_enemies:
                            enemy_died = move_enemy(enemy, "1", 8)
                            if enemy_died:
                                # Remove from the original list if it exists there
                                if enemy in slow_enemies:
                                    slow_enemies.remove(enemy)
                    slow_counter = 0 # Reset counter

                # Move medium enemies (type 2)
                if medium_counter >= medium_threshold:
                    current_medium_enemies = list(medium_enemies)
                    for i in range(len(current_medium_enemies) - 1, -1, -1):
                            enemy = current_medium_enemies[i]
                            if enemy in medium_enemies:
                                enemy_died = move_enemy(enemy, "2", 7)
                                if enemy_died:
                                    if enemy in medium_enemies:
                                        medium_enemies.remove(enemy)
                    medium_counter = 0

                # Move fast enemies (type 3)
                if fast_counter >= fast_threshold:
                    current_fast_enemies = list(fast_enemies)
                    for i in range(len(current_fast_enemies) - 1, -1, -1):
                            enemy = current_fast_enemies[i]
                            if enemy in fast_enemies:
                                enemy_died = move_enemy(enemy, "3", 6)
                                if enemy_died:
                                    if enemy in fast_enemies:
                                        fast_enemies.remove(enemy)
                    fast_counter = 0

        # --- Drawing ---
        # Moved drawing inside the main loop
        # Only draw if the game loop is still running (might be set False by wait_for_key_press)
        if running:
            draw_grid() # Handles drawing grid, borders, HUD, and messages
            pygame.display.flip() # Update the full display

    # --- End of Main Game Loop ---
    print("Exiting game loop.") # Debug message
