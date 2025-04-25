from maps import * 
from utils import *
from game_text import game_text

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
    text_background (tuple, optional): RGB color tuple for the background behind each char.
        Defaults to None.
    title_box (bool, optional): For special title screen background.
"""

def pause_quit(screen, quitting=False): # From KINGDOM.PAS (lines 49-69)
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
                        sign_off(screen)
                        return True
                    else:
                        paused = False
                else:
                    paused = False  # Resume game
                    
    return False  # User didn't quit
                    
def hud(values=None): # From KINGDOM4.INC (lines 96-183)

    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Cloaks"]
    option_list = ["Cloak", "Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]
    
    pygame.draw.rect(screen, BLUE, (0, (TILE_HEIGHT * 25), WIDTH, HEIGHT - (TILE_HEIGHT * 25)))
    game_text(29, "         Level", YELLOW, False, False)
    game_text(27, "  Score     Gems      Whips     ", YELLOW)
    game_text(32, "Teleports   Keys      Cloaks    ", YELLOW)
    game_text(27, "*" * 48 + "Options", LIGHT_AQUA, False, False, ("ONLY_TEXT", RED))

    for i, word in enumerate(option_list):
        game_text(29+i, " " * 48 + word[0], None, False, False)
        game_text(29+i, " " * 49 + word[1:], LIGHT_GRAY, False, False)

    def format_centered_int(value, width) -> str:
      s_value = str(value)
      padding = width - len(s_value)
      if padding < 0:
        return s_value 
      left_padding = padding // 2
      right_padding = (padding + 1) // 2
      return ' ' * left_padding + s_value + ' ' * right_padding
    
    game_text(29, "*" * 18 + format_centered_int(values[0], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)
    game_text(31, "*" * 8  + format_centered_int(values[1], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)
    game_text(29, "*" * 28 + format_centered_int(values[2], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)
    game_text(29, "*" * 38 + format_centered_int(values[3], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)
    game_text(34, "*" * 18 + format_centered_int(values[4], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)
    game_text(34, "*" * 28 + format_centered_int(values[5], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)
    game_text(34, "*" * 38 + format_centered_int(values[6], 7), DARK_RED, False, False, ("ONLY_TEXT", LIGHT_GRAY), True)

def hud_right(screen, WIDTH, HEIGHT, color="C", values=None):  # From KINGDOM4.PAS (lines 96-183)
    is_monochrome = True if color == "M" else False

    hud_width = 130
    hud_x = WIDTH - hud_width  # Right-hand side

    # Create sidebar surface with monochrome handling
    hud_surface = pygame.Surface((hud_width, HEIGHT))
    hud_surface.fill(BLUE)
    if is_monochrome:
        hud_surface = apply_grayscale_f(hud_surface)
    screen.blit(hud_surface, (hud_x, 0))  # Apply sidebar

    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Cloak", "Options"]
    option_list = ["Cloak", "Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]

    font = load_font(11)

    word_x = hud_x + 35
    word_y = 5

    rect_width = 88
    rect_height = 25

    for i, word in enumerate(item_tracker):
        # Color logic (monochrome-aware)
        if is_monochrome:
            label_color = GRAY
            value_color = GRAY
            box_color = SILVER
            options_box_color = SILVER
        else:
            label_color = CYAN if word == "Options" else YELLOW
            value_color = DARK_RED
            box_color = LIGHT_GRAY
            options_box_color = DARK_RED

        if word == "Options":
            word_y += group_height - 43
            word_surface = font.render(word, True, label_color)

            pygame.draw.rect(screen, options_box_color, (word_x - 12, word_y + 7, word_surface.get_width() + 6, 30))
            screen.blit(word_surface, (word_x - 8, word_y + 15))

            word_y += word_surface.get_height() + 15
        else:
            render_x = word_x - 25 if word == "Teleports" else word_x
            word_surface = font.render(word, True, label_color)
            screen.blit(word_surface, (render_x, word_y))

        if i < len(values):
            value_surface = font.render(str(values[i]), True, value_color)
            box_x = word_x - 12
            box_y = word_y + word_surface.get_height() + 5

            pygame.draw.rect(screen, box_color, (box_x, box_y, rect_width, rect_height))
            value_x = box_x + (rect_width - value_surface.get_width()) // 2
            screen.blit(value_surface, (value_x, box_y + 5))

        group_height = word_surface.get_height() + rect_height
        word_y += group_height + 15

    # Draw options list below stats
    y_offset = word_y - 40
    for choice in option_list:
        first_color = GRAY if is_monochrome else WHITE
        rest_color = GRAY

        first_letter_surface = font.render(choice[0], True, first_color)
        rest_surface = font.render(choice[1:], True, rest_color)

        first_rect = first_letter_surface.get_rect(topleft=(word_x - 10, y_offset))
        rest_rect = rest_surface.get_rect(topleft=(first_rect.right, y_offset))

        screen.blit(first_letter_surface, first_rect)
        screen.blit(rest_surface, rest_rect)

        y_offset += 14

def levels(screen, difficulty_input, color="C", mixUp=False, hud=""):
    WIDTH, HEIGHT = screen.get_size()
    
    screen.fill(BLACK)

    huds = {
        "R": hud_right,
        "O": hud_original,
        "": hud_original  # fallback default
    }
    main_hud = huds.get(hud, hud_original)

    """ huds = {
        "R": hud_right,
        "O": hud_original,
        "": hud_original  # fallback default
    }
    main_hud = huds.get(hud, hud_original) """

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
               "trap10", "trap11", "trap12", "trap13", "message", "whip1", "whip2", "whip3", "whip4",]

    assets_path = os.path.join("src", "assets")
    images = {}

    special_cases = {
        "enemy1": "enemy1a",
        "enemy2": "enemy2a"
    }

    for sprite in sprites:
        filename = special_cases.get(sprite, sprite) + ".png"
        full_path = os.path.join(assets_path, filename)

        img = pygame.image.load(full_path)
        images[sprite] = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))
    
            
    if color == "M":
        for sprite in sprites:
            images[sprite] = apply_grayscale_f(images[sprite])
            images[sprite] = pygame.transform.scale(images[sprite], (TILE_WIDTH, TILE_HEIGHT))

    tile_mapping = {
        "^": images["border"], # Add border mapping
        "X": images["block"],
        "#": images["wall"],
        "C": images["chest"],
        "W": images["whip"],
        "1": images["enemy1"],
        "2": images["enemy2"],
        "3": images["enemy3"],
        "+": images["gem"],
        "T": images["teleport"],
        "_": images["teleport_player"],
        ".": images["trap"],
        "L": images["stairs"],
        "P": images["player"],
        "TP": images["teleport_player"],
        "S": images["slowTime"],
        "I": images["invisible"],
        "K": images["key"],
        "D": images["door"],
        "F": images["speedTime"],
        "R": images["river"],
        "Q": images["power"],
        "/": images["forest"],
        "J": images["tree"],
        "B": images["bomb"],
        "V": images["lava"],
        "=": images["pit"],
        "A": images["tome"],
        "U": images["tunnel"],
        "Z": images["freeze"],
        "*": images["nugget"],
        "E": images["quake"],
        ";": images["iBlock"],
        ":": images["iWall"],
        "`": images["iDoor"],
        "-": images["stop"],
        "@": images["trap2"],
        "%": images["zap"],
        "]": images["create"],
        "G": images["generator"],
        ")": images["trap3"],
        "M": images["mBlock"],
        "(": images["trap4"],
        "&": images["showGems"],
        "!": images["tablet"],
        "O": images["zBlock"],
        "H": images["blockSpell"],
        "?": images["chance"],
        ">": images["statue"],
        "N": images["wallVanish"],
        "<": images["krozK"],
        "[": images["krozR"],
        "|": images["krozO"],
        ",": images["krozZ"],
        "4": images["oWall1"],
        "5": images["oWall2"],
        "6": images["oWall3"],
        "7": images["cWall1"],
        "8": images["cWall2"],
        "9": images["cWall3"],
        "±": images["oSpell1"],
        "≥": images["oSpell2"],
        "≤": images["oSpell3"],
        "⌠": images["cSpell1"],
        "⌡": images["cSpell2"],
        "÷": images["cSpell3"],
        "Y": images["gBlock"],
        "0": images["rock"],
        "~": images["eWall"],
        "$": images["trap5"],
        "æ": images["tBlock"],
        "Æ": images["tRock"],
        "ô": images["tGem"],
        "ö": images["tBlind"],
        "ò": images["tWhip"],
        "û": images["tGold"],
        "ù": images["tTree"],
        "¿": images["rope"],
        "┤": images["dropRope1"],
        "│": images["dropRope2"],
        "┐": images["dropRope3"],
        "┘": images["dropRope4"],
        "╜": images["dropRope5"],
        "â": images["amulet"],
        "»": images["shootRight"],
        "«": images["shootLeft"],
        "α": images["trap6"],
        "β": images["trap7"],
        "┌": images["trap8"],
        "π": images["trap9"],
        "∑": images["trap10"],
        "σ": images["trap11"],
        "μ": images["trap12"],
        "τ": images["trap13"],
        "ⁿ": images["message"],
        "whip1": images["whip1"],
        "whip2": images["whip2"],
        "whip3": images["whip3"],
        "whip4": images["whip4"]
    }

    level_maps = [level1_map, level2_map, level4_map, level6_map, level8_map, level10_map,
                  level12_map, level14_map, level16_map, level18_map, level20_map, level22_map,
                  level24_map, level25_map]
    current_level_index = 0
    grid = [list(row) for row in level_maps[current_level_index]]

    collidable_tiles = {"X", "#", ";", "/", "J", "R", "4", "5", "6", "8", "9"}

    dynamic_tiles = {"P", "1", "2", "3"}
    # Game state
    grid = [list(row) for row in level1_map]
    collidable_tiles = {"X", "#"}
    slow_enemies = []
    medium_enemies = []
    keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, 
                    pygame.K_LEFT: False, pygame.K_RIGHT: False,
                    pygame.K_w: False}
    
    # Find player and enemies
    player_row, player_col = 0, 0
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == "P":
                player_row, player_col = r, c
            elif tile == "1":
                slow_enemies.append({"row": r, "col": c})
            elif tile == "2":
                medium_enemies.append({"row": r, "col": c})  # Fixed: added colon after "col"

    # Initialize score tracking variables *Based off difficulty*
    match(difficulty_input):
        case "E":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        case "A":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 2, 0, 0, 0, 0
        case "N", " ":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        case "X":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 250, 100, 50, 0, 10
        case _:
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 50, 50, 10, 0, 5
        
    if mixUp:
        score, level_num, gems, whips, teleports, keys = 0, 1, gems + 60, whips + 30, teleports + 15, 2
    
    values = [score, level_num, gems, whips, teleports, keys, cloaks]
    hud(values)
        
    # Function to change to the next level
    def change_level(next_level_index):
        nonlocal grid, player_row, player_col, slow_enemies, medium_enemies, fast_enemies, level_num
        nonlocal waiting_for_start_key # <<< Make sure to access the flag
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
        
        # Find new player position and enemies
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == "P":
                    player_row, player_col = r, c
                elif tile == "1":
                    slow_enemies.append({"row": r, "col": c})
                elif tile == "2":
                    medium_enemies.append({"row": r, "col": c})

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
            pass
        else:
            """Move an enemy toward the player if they can see the player"""
            row, col = enemy["row"], enemy["col"]
            
            # Check if enemy was removed
            if grid[row][col] != enemy_type:
                return True  # Remove enemy
            
            # Random chance for player move
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
            
            if player_col < col:
                new_col -= 1
                x_dir = 1
            elif player_col > col:
                new_col += 1
                x_dir = -1
            
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
                return True  # Enemy dies when breaking block
            
            # Handle collision with gems, whips, teleports
            elif grid[new_row][new_col] == "+":  # Gem
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3
                
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
                return True  # Enemy dies
                
            # Blocked - stay in place
            else:
                grid[row][col] = enemy_type
                return False

    def use_whip():
        """Handle the whip animation and enemy interactions, keeping HUD and border visible, with color cycling."""
        # Access game state variables from enclosing scope
        nonlocal score # Keep score nonlocal if it's modified directly here

        # Check if player has whips
        if whips <= 0:
            return 0, [], [], []  # No whips to use

        # Define the whip animation positions (counter-clockwise)
        whip_positions = [
            {"row": -1, "col": -1, "sprite": "whip1"},  # Top-left
            {"row": -1, "col":  0, "sprite": "whip3"},  # Top
            {"row": -1, "col":  1, "sprite": "whip2"},  # Top-right
            {"row":  0, "col":  1, "sprite": "whip4"},  # Right
            {"row":  1, "col":  1, "sprite": "whip1"},  # Bottom-right
            {"row":  1, "col":  0, "sprite": "whip3"},  # Bottom
            {"row":  1, "col": -1, "sprite": "whip2"},  # Bottom-left
            {"row":  0, "col": -1, "sprite": "whip4"},  # Left
        ]

        # Track affected enemies
        enemies_hit = []

        # Timing values
        delay = 25  # milliseconds per frame

        # Grid offsets
        grid_offset_x = TILE_WIDTH
        grid_offset_y = TILE_HEIGHT

        # Whip animation loop
        for position in whip_positions:
            # Calculate target position
            whip_row = player_row + position["row"]
            whip_col = player_col + position["col"]

            # Check if position is in bounds (relative to grid, not screen)
            if not (0 <= whip_row < len(grid) and 0 <= whip_col < len(grid[0])):
                continue

            # Original tile at this position (for collision logic)
            original_tile = grid[whip_row][whip_col]

            # Check for enemy hits at this position *before* visual overlay
            if original_tile in ["1", "2", "3"]:
                 # Only add if not already hit in this whip sequence
                is_already_hit = False
                for r, c, _ in enemies_hit:
                    if r == whip_row and c == whip_col:
                        is_already_hit = True
                        break
                if not is_already_hit:
                    enemies_hit.append((whip_row, whip_col, original_tile))

            # --- Color Cycling Logic ---
            whip_sprite_key = position["sprite"]
            colored_whip_image = None # Initialize
            if whip_sprite_key in images: # Ensure the key exists
                original_whip_image = images[whip_sprite_key]
                random_color = random.choice(whip_cycle_colors)
                colored_whip_image = original_whip_image.copy()
                colored_whip_image.fill(random_color, special_flags=pygame.BLEND_RGB_MULT)
            # --- End Color Cycling Logic ---

            # --- Direct Drawing within Whip Loop ---
            screen.fill(BLACK) # Clear screen before redraw

            # Draw the border
            border_image = tile_mapping['^']
            for r_idx, row_str in enumerate(level_border):
                if r_idx * TILE_HEIGHT >= HEIGHT: continue
                for c_idx, char in enumerate(row_str):
                    if c_idx * TILE_WIDTH >= WIDTH: continue
                    if char == '^':
                        screen.blit(border_image, (c_idx * TILE_WIDTH, r_idx * TILE_HEIGHT))

            # Draw the main game grid (offset)
            for r_idx, row in enumerate(grid):
                 screen_y = grid_offset_y + (r_idx * TILE_HEIGHT)
                 if screen_y >= HEIGHT - TILE_HEIGHT: continue
                 for c_idx, char in enumerate(row):
                     screen_x = grid_offset_x + (c_idx * TILE_WIDTH)
                     if screen_x >= WIDTH - TILE_WIDTH: continue

                     # Draw the colored whip sprite at the current animation position
                     if r_idx == whip_row and c_idx == whip_col and colored_whip_image:
                          # Calculate screen coordinates for the whip with offset
                          whip_screen_x = grid_offset_x + whip_col * TILE_WIDTH
                          whip_screen_y = grid_offset_y + whip_row * TILE_HEIGHT
                          # Ensure whip is within drawable area before blitting
                          if whip_screen_x < WIDTH - TILE_WIDTH and whip_screen_y < HEIGHT - TILE_HEIGHT:
                              screen.blit(colored_whip_image, (whip_screen_x, whip_screen_y))
                     # Otherwise, draw the normal tile from the map (unless it's the whip position being drawn)
                     elif not (r_idx == whip_row and c_idx == whip_col):
                         if r_idx == player_row and c_idx == player_col: # Draw player
                             player_sprite = tile_mapping['TP'] if is_cloaked else tile_mapping['P']
                             screen.blit(player_sprite, (screen_x, screen_y))
                         elif char in tile_mapping: # Draw other tiles
                             screen.blit(tile_mapping[char], (screen_x, screen_y))
            
            hud(values)

            pygame.display.flip()
            pygame.time.wait(delay)

        # Process enemy hits and update game state
        new_slow_enemies = []
        new_medium_enemies = []
        new_fast_enemies = []

        # Define score values for each enemy type
        enemy_scores = {"1": 10, "2": 20, "3": 30}

        # Clear enemies hit by whip from both grid and enemy lists
        for r, c, enemy_type in enemies_hit:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == enemy_type: # Check bounds and if enemy still exists
                grid[r][c] = " "  # Clear enemy from grid
                # Add score based on enemy type using the dictionary
                score += enemy_scores.get(enemy_type, 0)

        # Rebuild enemy lists excluding the killed ones
        for enemy in slow_enemies:
            if 0 <= enemy["row"] < len(grid) and 0 <= enemy["col"] < len(grid[0]) and grid[enemy["row"]][enemy["col"]] == "1":
                new_slow_enemies.append(enemy)

        for enemy in medium_enemies:
             if 0 <= enemy["row"] < len(grid) and 0 <= enemy["col"] < len(grid[0]) and grid[enemy["row"]][enemy["col"]] == "2":
                new_medium_enemies.append(enemy)

        for enemy in fast_enemies:
             if 0 <= enemy["row"] < len(grid) and 0 <= enemy["col"] < len(grid[0]) and grid[enemy["row"]][enemy["col"]] == "3":
                new_fast_enemies.append(enemy)

        return new_slow_enemies, new_medium_enemies, new_fast_enemies

    is_cloaked = False
    cloak_start_time = 0
    CLOAK_DURATION = 3000

    def cloak(): 
        """ Handles cloak pickup, activation, and duration. """
        nonlocal cloaks, is_cloaked, cloak_start_time, values, CLOAK_DURATION
        
        cloak_start_time = pygame.time.get_ticks()
        is_cloaked = True
        cloaks -= 1
        print(f"{cloaks}")

    def teleport(grid, player_row, player_col, tile_mapping, screen):
        """Teleports the player to a random empty space on the grid with a flickering effect before and after teleporting."""

        # Define grid offsets (assuming they are defined in the outer scope, like in the main drawing loop)
        grid_offset_x = TILE_WIDTH
        grid_offset_y = TILE_HEIGHT

        # Find all empty spaces
        empty_spaces = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == ' ']

        if not empty_spaces:
            return player_row, player_col

        # Calculate screen coordinates for the original position with offset
        original_screen_x = grid_offset_x + player_col * TILE_WIDTH
        original_screen_y = grid_offset_y + player_row * TILE_HEIGHT
        original_rect = pygame.Rect(original_screen_x, original_screen_y, TILE_WIDTH, TILE_HEIGHT)

        # Flicker at the original position
        for _ in range(20):
            random_color = random.choice(blinking_text_color_list)

            # Fill original position with random color (using offset)
            screen.fill(random_color, original_rect)

            # Draw the player sprite at the original location (using offset)
            screen.blit(tile_mapping['P'], (original_screen_x, original_screen_y))

            pygame.display.update(original_rect)
            pygame.time.delay(40)

        # Clear the player's original position (using offset)
        screen.fill(BLACK, original_rect)
        pygame.display.update(original_rect)

        # --- Intermediate Flicker Loop ---
        last_intermediate_rect = None # To clear the last drawn TP icon
        for _ in range(250):
            # Select a random empty space
            new_row, new_col = random.choice(empty_spaces)

            # Calculate screen coordinates for the intermediate position with offset
            intermediate_screen_x = grid_offset_x + new_col * TILE_WIDTH
            intermediate_screen_y = grid_offset_y + new_row * TILE_HEIGHT
            intermediate_rect = pygame.Rect(intermediate_screen_x, intermediate_screen_y, TILE_WIDTH, TILE_HEIGHT)

            # Clear previous intermediate TP icon if it exists
            if last_intermediate_rect:
                screen.fill(BLACK, last_intermediate_rect)
                pygame.display.update(last_intermediate_rect)

            # Draw the TP icon at the new location (using offset)
            screen.blit(tile_mapping['TP'], (intermediate_screen_x, intermediate_screen_y))
            pygame.display.update(intermediate_rect)
            last_intermediate_rect = intermediate_rect # Store current rect for next clear

            pygame.time.delay(8)

        # Clear the last intermediate TP icon after the loop finishes
        if last_intermediate_rect:
            screen.fill(BLACK, last_intermediate_rect)
            pygame.display.update(last_intermediate_rect)
        # --- End Intermediate Flicker Loop ---


        # --- Final Destination Flicker ---
        # Use the last selected new_row, new_col as the final destination
        final_screen_x = grid_offset_x + new_col * TILE_WIDTH
        final_screen_y = grid_offset_y + new_row * TILE_HEIGHT
        final_rect = pygame.Rect(final_screen_x, final_screen_y, TILE_WIDTH, TILE_HEIGHT)

        for _ in range(20):
            random_color = random.choice(blinking_text_color_list)

            # Fill final position with random color (using offset)
            screen.fill(random_color, final_rect)

            # Draw the player sprite at the final location (using offset)
            screen.blit(tile_mapping['P'], (final_screen_x, final_screen_y))

            pygame.display.update(final_rect)
            pygame.time.delay(40)

        # Clear the final position before placing the player (using offset)
        screen.fill(BLACK, final_rect)
        pygame.display.update(final_rect)
        # --- End Final Destination Flicker ---


        # Clear old player position from the grid (logical update, no drawing)
        grid[player_row][player_col] = ' '

        # Update the grid with new player position (logical update, no drawing)
        grid[new_row][new_col] = 'P'

        # Ensure final player placement is visible (using offset)
        screen.blit(tile_mapping['P'], (final_screen_x, final_screen_y))
        pygame.display.update(final_rect)

        # Return new player position (logical coordinates)
        return new_row, new_col

    # Movement settings - simplified for consistent movement
    movement_cooldown = 100  # ms between moves (one space per 100ms)
    last_move_time = 0
    keys_held_time = {
        pygame.K_UP: 0,
        pygame.K_DOWN: 0, 
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0
    }
    momentum = {
        pygame.K_UP: 0,
        pygame.K_DOWN: 0, 
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0
    }
    
    # How long a key needs to be held to generate momentum (in ms)
    MOMENTUM_THRESHOLD = 300
    # Maximum momentum value (number of extra moves)
    MAX_MOMENTUM = 5

    def player_input():
        """Handle player movement with consistent rate and momentum"""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys, cloaks, is_cloaked
        nonlocal slow_enemies, medium_enemies, fast_enemies, last_move_time
        # Need access to these for drawing during whip
        nonlocal WIDTH, HEIGHT, values

        current_time = pygame.time.get_ticks()
        current_keys = pygame.key.get_pressed()
        action_performed = False

        # Handle whip activation with the 'W' key
        if current_keys[pygame.K_w]:
            if not keys_pressed[pygame.K_w]:  # Key just pressed
                keys_pressed[pygame.K_w] = True
                if whips > 0:
                    # Pass necessary drawing info to use_whip
                    slow_enemies, medium_enemies, fast_enemies = use_whip()
                    whips -= 1 # Decrement whip after use
                    action_performed = True
        else:
            keys_pressed[pygame.K_w] = False

        # Handle Teleport activation with the 't' key
        if current_keys[pygame.K_t]:
            if not keys_pressed.get(pygame.K_t, False): # Use .get for safety if key not initialized
                keys_pressed[pygame.K_t] = True
                if teleports > 0:
                    # Pass necessary variables to teleport
                    player_row, player_col = teleport(grid, player_row, player_col, tile_mapping, screen)
                    teleports -= 1
                    action_performed = True # Mark action performed
            # No else needed here, key remains pressed until released

        # Handle key release for teleport
        elif not current_keys[pygame.K_t] and keys_pressed.get(pygame.K_t, False):
             keys_pressed[pygame.K_t] = False


        # Handle cloak activation with the 'c' key
        # Activate cloak if 'c' is pressed
        if current_keys[pygame.K_c]:
            if not keys_pressed.get(pygame.K_c, False): # Use .get for safety
                keys_pressed[pygame.K_c] = True
                if cloaks > 0 and not is_cloaked:
                    cloak()
                    action_performed = True # Mark action performed
            # No else needed here, key remains pressed until released

        # Handle key release for cloak
        elif not current_keys[pygame.K_c] and keys_pressed.get(pygame.K_c, False):
             keys_pressed[pygame.K_c] = False


        # Check if enough time has passed since last move
        time_since_last_move = current_time - last_move_time
        if time_since_last_move < movement_cooldown and not action_performed: # Only return if no other action was taken
            return action_performed # Not time to move yet, but might have performed an action

        # Ready to make a move or already performed an action
        move_made = False

        # Define all direction keys with their movement vectors (delta_row, delta_col)
        direction_keys = [
            (pygame.K_UP, (-1, 0)),
            (pygame.K_DOWN, (1, 0)),
            (pygame.K_LEFT, (0, -1)),
            (pygame.K_RIGHT, (0, 1)),

            # UIOJLNM, keys
            (pygame.K_u, (-1, -1)),  # Up-left
            (pygame.K_i, (-1, 0)),   # Up
            (pygame.K_o, (-1, 1)),   # Up-right
            (pygame.K_j, (0, -1)),   # Left
            (pygame.K_l, (0, 1)),    # Right
            (pygame.K_n, (1, -1)),   # Down-left
            (pygame.K_m, (1, 0)),    # Down
            (pygame.K_COMMA, (1, 1)) # Down-right
        ]

        # Check movement keys only if enough time has passed
        if time_since_last_move >= movement_cooldown:
            # First check keys being held down - using all direction keys
            for key, (delta_row, delta_col) in direction_keys:
                if current_keys[key]:
                    if not keys_pressed.get(key, False):  # Key just pressed
                        keys_pressed[key] = True
                        keys_held_time[key] = current_time

                    # Try to move in the direction
                    move_made = process_move(player_row + delta_row, player_col + delta_col)
                    if move_made:
                        last_move_time = current_time
                        # Reset momentum for the key used
                        if key in momentum: momentum[key] = 0
                        break # Exit loop once a move is made
                else:
                    # Key released or not pressed
                    if keys_pressed.get(key, False):
                        hold_duration = current_time - keys_held_time.get(key, current_time) # Use .get with default
                        if hold_duration > MOMENTUM_THRESHOLD:
                            # Add momentum based on hold duration
                            momentum[key] = min(MAX_MOMENTUM, int((hold_duration - MOMENTUM_THRESHOLD) / 100))
                        keys_pressed[key] = False

            # If no key is pressed but we have momentum, apply it
            if not move_made:
                for key, (delta_row, delta_col) in direction_keys:
                    if momentum.get(key, 0) > 0: # Use .get with default
                        move_made = process_move(player_row + delta_row, player_col + delta_col)
                        if move_made:
                            momentum[key] -= 1
                            last_move_time = current_time
                            break # Exit loop once a move is made

        return action_performed or move_made
    
    def process_move(new_row, new_col):
        """Process a player movement to a new position"""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys, level_num, cloaks
        
        # Check if position is valid
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        
        # Check if destination is not a wall
        if grid[new_row][new_col] not in collidable_tiles:
            # Collect items
            if grid[new_row][new_col] == "+":  # Gem
                gems += 1
                score += 1  # Original game awards 1 point per gem
            elif grid[new_row][new_col] == "W":  # Whip
                whips += 1
                score += 1  # Original game awards 1 point per whip
            elif grid[new_row][new_col] == "T":  # Teleport
                teleports += 1
                score += 1  # Original game awards 1 point per teleport
            elif grid[new_row][new_col] == "K":  # Key
                keys += 1
                score += 10  # Original game doesn't specify key points explicitly
            elif grid[new_row][new_col] == "L":  # Stairs to next level
                level_num += 1
                score += 1000
            elif grid[new_row][new_col] == "_":  # Cloak
                cloaks += 1
                score += 60  # optional value
            elif grid[new_row][new_col] == "*":  # Nugget
                score += 50  # Gold nuggets are worth 50 points
            elif grid[new_row][new_col] == "S":  # SlowTime
                score += 5  # SlowTime bonus
            elif grid[new_row][new_col] == "I":  # Invisible
                score += 10  # Invisible bonus
            elif grid[new_row][new_col] == "F":  # SpeedTime
                score += 20  # SpeedTime bonus
            elif grid[new_row][new_col] == "C":  # Chest
                score += 50  # Chest bonus
            elif grid[new_row][new_col] == "!":  # Tablet
                score += level_num + 250  # Tablet bonus (level + fixed bonus)
            
            # Move player
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            return True
        
        # Movement was blocked
        if grid[new_row][new_col] in ["X", "#"]:  # Wall or block
            if score > 2:  # Only subtract if score is greater than 2
                score -= 2  # Original game deducts 2 points for hitting walls
        return False
    
    # Game constants
    SLOW_TIMER = 5
    MEDIUM_TIMER = 6
    GAME_TICK_RATE = 12.0
    
     # Game loop
    running = True
    clock = pygame.time.Clock()
    tick_counter = 0

    wait = True

    # Ensure the "saves" directory exists
    saves_dir = os.path.join("src", "saves")
    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)

    def save_game(state, slot):
        """Save the game state to a JSON file."""
        save_path = os.path.join(saves_dir, f"KINGDOM{slot}.json")  # Use saves_dir from utils
        with open(save_path, "w") as save_file:
            json.dump(state, save_file, indent=4)  # Save only the player state
        print(f"Saving to file {slot}...")
        pygame.time.wait(2000)  # Wait for 2 seconds

    def restore_game(slot):
        """Restore the game state from a JSON file."""
        save_path = os.path.join(saves_dir, f"KINGDOM{slot}.json")  # Use saves_dir from utils
        if os.path.exists(save_path):
            with open(save_path, "r") as save_file:
                state = json.load(save_file)
            print(f"Restoring from file {slot}...")
            pygame.time.wait(2000)  # Wait for 2 seconds
            return state  # Return the restored state
        else:
            print(f"No save file found for slot {slot}.")
            return None

    def handle_save(screen, state):
        """Handle the save process."""
        paused = True
        print("\nGame is PAUSED.\n")  # Output when the game is paused for saving
        print("Are you sure you want to SAVE (Y/N)?")
        while paused:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        paused = False
                        save_slot = prompt_save_restore(screen, "SAVE")
                        if save_slot:
                            save_game({
                                "player_row": state["player_row"],
                                "player_col": state["player_col"],
                                "Score": state["Score"],
                                "level_num": state["level_num"],  # Save the level number
                                "gems": state["gems"],
                                "whips": state["whips"],
                                "teleports": state["teleports"],
                                "keys": state["keys"]
                            }, save_slot)
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        paused = False
        print("\nGame RESUMED.\n")  # Output when the game resumes after saving

    def handle_restore(screen):
        """Handle the restore process."""
        paused = True
        print("\nGame is PAUSED.\n")  # Output when the game is paused for restoring
        print("Are you sure you want to RESTORE (Y/N)?")
        while paused:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        paused = False
                        restore_slot = prompt_save_restore(screen, "RESTORE")
                        if restore_slot:
                            restored_state = restore_game(restore_slot)
                            if restored_state:
                                # Regenerate the grid based on the saved level number
                                grid = generate_grid_for_level(restored_state["level_num"])
                                return {
                                    "grid": grid,  # Regenerated grid
                                    "player_row": restored_state["player_row"],
                                    "player_col": restored_state["player_col"],
                                    "Score": restored_state["Score"],
                                    "level_num": restored_state["level_num"],
                                    "gems": restored_state["gems"],
                                    "whips": restored_state["whips"],
                                    "teleports": restored_state["teleports"],
                                    "keys": restored_state["keys"]
                                }
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        paused = False
        print("\nGame RESUMED.\n")  # Output when the game resumes after restoring
        return None

    def prompt_save_restore(screen, action):
        """Prompt the user to pick a save/restore slot."""
        slot = None
        print(f"Pick which letter to {action} to/from: A, B, or C? A")  # Print the prompt once
        while slot not in {"A", "B", "C"}:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_a, pygame.K_b, pygame.K_c):
                        slot = chr(event.key).upper()
                        return slot
                    
    def generate_grid_for_level(level_num):
        """Generate the grid for the given level number."""
        # Ensure the level number is valid
        if 1 <= level_num <= len(level_maps):
            return [list(row) for row in level_maps[level_num - 1]]  # Convert strings to lists of characters
        else:
            raise ValueError(f"Level {level_num} is not defined in level_maps.")
        
    def draw_grid():
        screen.fill(BLACK)

        # Draw the border first
        border_image = tile_mapping['^']
        for row_index, row_str in enumerate(level_border):
            # Ensure row_index is within screen bounds if border map is larger than screen rows
            if row_index * TILE_HEIGHT >= HEIGHT: continue
            for col_index, char in enumerate(row_str):
                # Ensure col_index is within screen bounds
                if col_index * TILE_WIDTH >= WIDTH: continue
                if char == '^':
                    screen.blit(border_image, (col_index * TILE_WIDTH, row_index * TILE_HEIGHT))

        # Draw the main game grid, offset by one tile
        grid_offset_x = TILE_WIDTH
        grid_offset_y = TILE_HEIGHT
        for row_index, row in enumerate(grid):
             # Calculate screen coordinates with offset
             screen_y = grid_offset_y + (row_index * TILE_HEIGHT)
             # Ensure row_index is within screen bounds (considering offset)
             if screen_y >= HEIGHT - TILE_HEIGHT: continue # Stop if tile goes beyond bottom border area

             for col_index, char in enumerate(row):
                 # Calculate screen coordinates with offset
                 screen_x = grid_offset_x + (col_index * TILE_WIDTH)
                 # Ensure col_index is within screen bounds (considering offset)
                 if screen_x >= WIDTH - TILE_WIDTH: continue # Stop if tile goes beyond right border area

                 if char == "P":
                     if is_cloaked: # Changed player icon
                         screen.blit(tile_mapping['TP'], (screen_x, screen_y))
                     else:
                         screen.blit(tile_mapping['P'], (screen_x, screen_y))
                 elif char in tile_mapping:
                     screen.blit(tile_mapping[char], (screen_x, screen_y))

        # Update the item tracking UI with current values
        values = [score, level_num, gems, whips, teleports, keys, cloaks]
        hud(values)

        # Display level-specific messages
        if level_num == 1:
             game_text(24, "KINGDOM OF KROZ II BY SCOTT MILLER", WHITE, False, True, None)

    waiting_for_start_key = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # If waiting, any key press starts the level
                if waiting_for_start_key:
                    waiting_for_start_key = False
                    pygame.event.clear(pygame.KEYDOWN) # Clear the keydown queue to prevent immediate move
                    continue # Skip the rest of the keydown handling for this frame

                # --- Existing keydown handling (only runs if not waiting) ---
                if event.key == pygame.K_p:
                    pause_quit(screen, quitting=False)
                elif event.key in (pygame.K_q, pygame.K_ESCAPE): # ASCII value # 81 & 27
                    if pause_quit(screen, quitting=True):
                        running = False   
                elif event.key == pygame.K_TAB:
                    # Go to next level when Tab is pressed
                    current_level_index = (current_level_index + 1) % len(level_maps)
                    change_level(current_level_index)
                elif event.key == pygame.K_s:
                    handle_save(screen, {
                        "player_row": player_row,
                        "player_col": player_col,
                        "Score": score,
                        "level_num": level_num,
                        "gems": gems,
                        "whips": whips,
                        "teleports": teleports,
                        "keys": keys
                    })
                elif event.key == pygame.K_r:
                    restored_state = handle_restore(screen)
                    if restored_state:
                        # Apply the restored state
                        grid = restored_state["grid"] # Use the grid returned by handle_restore
                        player_row = restored_state["player_row"]
                        player_col = restored_state["player_col"]
                        score = restored_state["Score"]
                        level_num = restored_state["level_num"]
                        gems = restored_state["gems"]
                        whips = restored_state["whips"]
                        teleports = restored_state["teleports"]
                        keys = restored_state["keys"]
                        waiting_for_start_key = True

                        # Reset enemy lists based on the restored grid
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

            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False

        # --- Game Logic Updates (conditional) ---
        if not waiting_for_start_key:
            # Process player input
            action_performed = player_input()

            # Auto-deactivate cloak after duration
            if is_cloaked and pygame.time.get_ticks() - cloak_start_time > CLOAK_DURATION: # Use constant
                is_cloaked = False

            # Update spell effect timers
            if slow_time_effect > 0: slow_time_effect -= 1
            if invisible_effect > 0: invisible_effect -= 1
            if speed_time_effect > 0: speed_time_effect -= 1
            if freeze_effect > 0: freeze_effect -= 1

            # Update movement thresholds based on spell effects
            if speed_time_effect > 0:
                # Speed time makes enemies move very fast
                slow_threshold = 6
                medium_threshold = 5
                fast_threshold = 4
            elif slow_time_effect > 0:
                # Slow time makes enemies move much slower
                slow_threshold = 30
                medium_threshold = 25
                fast_threshold = 20
            else:
                # Normal speeds
                slow_threshold = 10
                medium_threshold = 7
                fast_threshold = 4
            
            # Update game state and enemy movement counters
            tick_counter += 1
            
            # Only increment counters and allow movement if freeze effect is inactive
            if freeze_effect <= 0:
                # Increment individual enemy counters
                slow_counter += 1
                medium_counter += 1
                fast_counter += 1
                
                # Move slow enemies (type 1)
                if slow_counter >= slow_threshold:
                    for i in range(len(slow_enemies)-1, -1, -1):
                        if i < len(slow_enemies):  # Make sure the enemy still exists
                            if move_enemy(slow_enemies[i], "1", 8):
                                del slow_enemies[i]
                    slow_counter = 0  # Reset the counter
                    
                # Move medium enemies (type 2)
                if medium_counter >= medium_threshold:
                    for i in range(len(medium_enemies)-1, -1, -1):
                        if i < len(medium_enemies):  # Make sure the enemy still exists
                            if move_enemy(medium_enemies[i], "2", 7):
                                del medium_enemies[i]
                    medium_counter = 0  # Reset the counter
                    
                # Move fast enemies (type 3)
                if fast_counter >= fast_threshold:
                    for i in range(len(fast_enemies)-1, -1, -1):
                        if i < len(fast_enemies):  # Make sure the enemy still exists
                            if move_enemy(fast_enemies[i], "3", 6):
                                del fast_enemies[i]
                    fast_counter = 0  # Reset the counter

            # Handle powerups pickup logic
            for row_index, row in enumerate(grid):
                for col_index, char in enumerate(row):
                    # If player is on the slowtime powerup
                    if char == "S" and row_index == player_row and col_index == player_col:
                        slow_time_effect = 70 if not FAST_PC else 100
                        grid[row_index][col_index] = " "
                        # Visual/sound effects would go here
                        
                    # If player is on the speedtime powerup
                    if char == "F" and row_index == player_row and col_index == player_col:
                        speed_time_effect = 50 if not FAST_PC else 80
                        grid[row_index][col_index] = " "
                        # Visual/sound effects would go here
                        
                    # If player is on the freeze powerup
                    if char == "Z" and row_index == player_row and col_index == player_col:
                        freeze_effect = 55 if not FAST_PC else 60
                        grid[row_index][col_index] = " "
                        # Visual/sound effects would go here

        draw_grid()

        if waiting_for_start_key:
            game_text(25, "Press any key to begin this level.", "CHANGING", False, True, BLACK)

        pygame.display.flip()
        clock.tick(GAME_TICK_RATE)
levels(screen, difficulty_input, mixUp = False)