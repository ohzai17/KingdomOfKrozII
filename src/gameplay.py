from maps import *
from utils import *
from draw_text import draw_text

"""
draw_text(row, text, text_color=None, flashing=False, center=True, text_background=None, title_box = False)
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
        flash_c(screen, message)
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
                    
def hud(screen, WIDTH, HEIGHT, values=None): # From KINGDOM4.INC (lines 96-183)
    
    pygame.draw.rect(screen, BLUE, (0, (TILE_HEIGHT * 23) + 20, WIDTH, HEIGHT - (TILE_HEIGHT * 23)))


    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Cloaks", "Options"]
    option_list = ["Cloaks", "Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]

    font = load_font(13)  
    
    word_x = 5  # Starting X coordinate of words
    word_y = (TILE_HEIGHT * 23) + 30  # Y coordinate

    rect_width = 78  # Width of gray rec
    rect_height = 30  # Height of gray re

    for i, word in enumerate(item_tracker):
        
        match(word): # Display items
            case ("Options"): # Rendered differently
                word_x += 5
                word_surface = font.render(word, True, CYAN)
                pygame.draw.rect(screen, DARK_RED, (word_x - 1, word_y - 8, word_surface.get_width() + 1, 30))
                screen.blit(word_surface, (word_x, word_y)) 
            case _: 

                word_surface = font.render(word, True, (YELLOW))
                screen.blit(word_surface, (word_x, word_y))

        if i < len(values): # Values and gray box
            if item_tracker[i] == "Teleports":  # handled differently due to placement issues
                value_surface = font.render(str(values[i]), True, DARK_RED)
                box_x = word_x + ((word_surface.get_width() // 2) - (rect_width // 2) - 18)
                value_x = (box_x + ((rect_width - value_surface.get_width()) // 2) + 16)
                pygame.draw.rect(screen, LIGHT_GRAY, (box_x, word_y + word_surface.get_height() + 10, rect_width + 35, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17))
            else:
                value_surface = font.render(str(values[i]), True, DARK_RED)
                box_x = (word_x + (word_surface.get_width() // 2) - (rect_width // 2) + 5)
                value_x = box_x + (rect_width - value_surface.get_width()) // 2
                pygame.draw.rect(screen, LIGHT_GRAY, (box_x, word_y + word_surface.get_height() + 10, rect_width, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17))

        # Update word_x based on word width
        word_x += word_surface.get_width() + 30

    y_offset = word_y + 30  # Start position of the options_list (below "Options")
    for choice in option_list:
        first_letter_surface = font.render(choice[0], True, WHITE)
        rest_surface = font.render(choice[1:], True, GRAY)

        first_rect = first_letter_surface.get_rect(topleft=(word_x - 120, y_offset))
        rest_rect = rest_surface.get_rect(topleft=(first_rect.right, y_offset))

        screen.blit(first_letter_surface, first_rect)
        screen.blit(rest_surface, rest_rect)
        
        # Move the y_offset down
        y_offset += 20

def levels(screen, difficulty_input, mixUp=False):

    WIDTH, HEIGHT = screen.get_size()
    
    screen.fill(BLACK)

    sprites = ["block", "chest", "enemy1", "enemy2", "enemy3", "gem", "player", "teleport_player","stairs", "teleport", 
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
    
    TILE_WIDTH, TILE_HEIGHT = 13, 17

    for sprite in sprites:
        filename = special_cases.get(sprite, sprite) + ".png"
        full_path = os.path.join(assets_path, filename)

        img = pygame.image.load(full_path)
        images[sprite] = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))

    tile_mapping = {
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
    fast_enemies = []
    keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, 
                    pygame.K_LEFT: False, pygame.K_RIGHT: False,
                    pygame.K_w: False,
                    pygame.K_u: False, pygame.K_i: False, pygame.K_o: False,
                    pygame.K_j: False, pygame.K_l: False, 
                    pygame.K_n: False, pygame.K_m: False, pygame.K_COMMA: False}
    
    # Add key hold time tracking for new keys
    keys_held_time = {
        pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0,
        pygame.K_u: 0, pygame.K_i: 0, pygame.K_o: 0,
        pygame.K_j: 0, pygame.K_l: 0, 
        pygame.K_n: 0, pygame.K_m: 0, pygame.K_COMMA: 0
    }
    
    # Add momentum tracking for new keys
    momentum = {
        pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0,
        pygame.K_u: 0, pygame.K_i: 0, pygame.K_o: 0,
        pygame.K_j: 0, pygame.K_l: 0, 
        pygame.K_n: 0, pygame.K_m: 0, pygame.K_COMMA: 0
    }
    
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
            elif tile == "3":
                fast_enemies.append({"row": r, "col": c})

    # Initialize score tracking variables *Based off difficulty*
    match(difficulty_input):
        case "E":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        case "A":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 2, 0, 0, 0, 0
        case "N", " ":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        case "X":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 250, 100, 50, 0, 0
        case _:
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        
    if mixUp:
        score, level_num, gems, whips, teleports, keys = 0, 1, gems + 60, whips + 30, teleports + 15, 2
    
    values = [score, level_num, gems, whips, teleports, keys, cloaks]
    hud(screen, WIDTH, HEIGHT, values)
        
    # Function to change to the next level
    def change_level(next_level_index):
        nonlocal grid, player_row, player_col, slow_enemies, medium_enemies, fast_enemies, level_num
        
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
                    slow_enemies.append({"row": r, "col":c})
                elif tile == "2":
                    medium_enemies.append({"row": r, "col": c})
                elif tile == "3":
                    fast_enemies.append({"row": r, "col": c})

    # Core functions
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
            nonlocal Score, gems  # Access Score and gems from the outer scope
        
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
                if enemy_type == "1": Score += 1
                elif enemy_type == "2": Score += 2
                elif enemy_type == "3": Score += 3
                return True  # Enemy dies when breaking block
            
            # Handle collision with gems, whips, teleports
            elif grid[new_row][new_col] == "+":  # Gem
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3
                
                if gems < 0:
                    # Ideally call a death function here
                    return True
                
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
                    # Ideally call a death function here
                    pass
                    
                return True  # Enemy dies
                
            # Blocked - stay in place
            else:
                grid[row][col] = enemy_type
                return False
        else:
            grid[row][col] = enemy_type  # Stay in place
            return False

    def use_whip(screen, grid, player_row, player_col, whips, slow_enemies, medium_enemies, fast_enemies, images, tile_mapping, TILE_WIDTH, TILE_HEIGHT):
        """Handle the whip animation and enemy interactions"""
        # Access game state variables from enclosing scope
        nonlocal Score, level_num, gems, teleports, keys, WIDTH, HEIGHT
        
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
        
        # Original grid state before whip animation
        original_grid = [row[:] for row in grid]
        
        # Whip animation loop
        for position in whip_positions:
            # Calculate target position
            whip_row = player_row + position["row"]
            whip_col = player_col + position["col"]
            
            # Check if position is in bounds
            if not (0 <= whip_row < len(grid) and 0 <= whip_col < len(grid[0])):
                continue
            
            # Original tile at this position
            original_tile = grid[whip_row][whip_col]
            
            # Check for enemy hits at this position
            if original_tile in ["1", "2", "3"]:
                enemies_hit.append((whip_row, whip_col, original_tile))
            
            # Place whip sprite
            grid[whip_row][whip_col] = position["sprite"]
            
            # Render the grid
            screen.fill((BLACK))
            for r_idx, row in enumerate(grid):
                for c_idx, tile in enumerate(row):
                    if tile in tile_mapping:
                        screen.blit(tile_mapping[tile], (c_idx * TILE_WIDTH, r_idx * TILE_HEIGHT))
                        
            pygame.display.flip()
            pygame.time.wait(delay)
            
            # Restore original tile at this position
            grid[whip_row][whip_col] = original_tile

            # Draw HUD with updated whip count (show whip being used)
            hud(screen, WIDTH, HEIGHT, values)
        
        # Process enemy hits and update game state
        kills = 0
        new_slow_enemies = []
        new_medium_enemies = []
        new_fast_enemies = []
        
        # Clear enemies hit by whip from both grid and enemy lists
        for r, c, enemy_type in enemies_hit:
            grid[r][c] = " "  # Clear enemy from grid
            # Add points based on enemy type (1, 2, or 3 points)
            Score += int(enemy_type)
            kills += 1
            
        # Rebuild enemy lists excluding the killed ones
        for enemy in slow_enemies:
            if grid[enemy["row"]][enemy["col"]] == "1":
                new_slow_enemies.append(enemy)
                
        for enemy in medium_enemies:
            if grid[enemy["row"]][enemy["col"]] == "2":
                new_medium_enemies.append(enemy)
                
        for enemy in fast_enemies:
            if grid[enemy["row"]][enemy["col"]] == "3":
                new_fast_enemies.append(enemy)
        
        return kills, new_slow_enemies, new_medium_enemies, new_fast_enemies
    
    cloaks = 0
    is_cloaked = False
    cloak_start_time = 0
    CLOAK_DURATION = 8000

    def cloak(): 
        """ Handles cloak pickup, activation, and duration. """
        nonlocal cloaks, is_cloaked, cloak_start_time, values, CLOAK_DURATION
        
        cloak_start_time = pygame.time.get_ticks()
        is_cloaked = True
        cloaks -= 1
        print(f"{cloaks}")

    def teleport2(grid, player_row, player_col, tile_mapping, screen):  
        """Teleports the player to a random empty space on the grid with a flickering effect before and after teleporting."""
    
        if teleports <= 0:
            return player_row, player_col

        # Find all empty spaces
        empty_spaces = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == ' ']

        if not empty_spaces:
            return player_row, player_col

        # Flicker at the original position 
        for _ in range(20):  
            random_color = random.choice(blinking_text_color_list)

            # Fill original position with random color
            screen.fill(random_color, (player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

            # Draw the player sprite at the original location
            screen.blit(tile_mapping['P'], (player_col * TILE_WIDTH, player_row * TILE_HEIGHT))

            pygame.display.update(pygame.Rect(player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.time.delay(40)

        # Clear the player's original position
        screen.fill((BLACK), (player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
        pygame.display.update([pygame.Rect(player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)])

        for _ in range(250): 
            # Select a random empty space
            new_row, new_col = random.choice(empty_spaces)

            # Flicker at the intermediate locations with only the TP icon (no random colors)
            screen.fill((BLACK), (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))  # Clear previous

            # Draw the TP icon at the new location
            screen.blit(tile_mapping['TP'], (new_col * TILE_WIDTH, new_row * TILE_HEIGHT))

            pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.time.delay(8)
            screen.fill((BLACK), (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

        # Flicker at the final destination (10 times)
        for _ in range(20):  
            random_color = random.choice(blinking_text_color_list)

            # Fill final position with random color
            screen.fill(random_color, (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

            # Draw the player sprite at the final location
            screen.blit(tile_mapping['P'], (new_col * TILE_WIDTH, new_row * TILE_HEIGHT))

            pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.time.delay(40)

        # Clear the final position before placing the player
        screen.fill((BLACK), (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
        pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))


        # Clear old player position from the grid
        grid[player_row][player_col] = ' '

        # Update the grid with new player position
        grid[new_row][new_col] = 'P'

        # Ensure final player placement is visible
        screen.blit(tile_mapping['P'], (new_col * TILE_WIDTH, new_row * TILE_HEIGHT))
        pygame.display.update([pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)])

        # Return new player position
        return new_row, new_col

    # Movement settings - simplified for consistent movement
    movement_cooldown = 100  # ms between moves (one space per 100ms)
    last_move_time = 0
    keys_held_time = {
        pygame.K_UP: 0,
        pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0,
        pygame.K_u: 0, pygame.K_i: 0, pygame.K_o: 0,
        pygame.K_j: 0, pygame.K_l: 0, pygame.K_n: 0, pygame.K_m: 0, pygame.K_COMMA: 0
    }
    momentum = {
        pygame.K_UP: 0,
        pygame.K_DOWN: 0, 
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0,
        pygame.K_u: 0, pygame.K_i: 0, pygame.K_o: 0,
        pygame.K_j: 0, pygame.K_l: 0, 
        pygame.K_n: 0, pygame.K_m: 0, pygame.K_COMMA: 0
    }
    
    # How long a key needs to be held to generate momentum (in ms)
    MOMENTUM_THRESHOLD = 300
    # Maximum momentum value (number of extra moves)
    MAX_MOMENTUM = 5

    def player_input():
        """Handle player movement with consistent rate and momentum"""
        nonlocal player_row, player_col, Score, gems, whips, teleports, keys
        nonlocal slow_enemies, medium_enemies, fast_enemies, last_move_time, cloaks, is_cloaked
        
        current_time = pygame.time.get_ticks()
        current_keys = pygame.key.get_pressed()
        action_performed = False
        
        # Handle whip activation with the 'W' key
        if current_keys[pygame.K_w]:
            if not keys_pressed[pygame.K_w]:  # Key just pressed
                keys_pressed[pygame.K_w] = True
                if whips > 0:
                    kills, slow_enemies, medium_enemies, fast_enemies = use_whip(
                        screen, grid, player_row, player_col, whips, 
                        slow_enemies, medium_enemies, fast_enemies, images, tile_mapping, 
                        TILE_WIDTH, TILE_HEIGHT
                    )
                    whips -= 1
                    Score += kills * 150  # Award points for kills
                    action_performed = True
        else:
            keys_pressed[pygame.K_w] = False

        # Handle Teleport activation with the 't' key
        if current_keys[pygame.K_t]:
            if not keys_pressed[pygame.K_t]:
                keys_pressed[pygame.K_t] = True
                if teleports > 0:
                    player_row, player_col = teleport2(grid, player_row, player_col, tile_mapping, screen)
                    teleports -= 1
                action_performed = True
        else:
            keys_pressed[pygame.K_t] = False

        # Handle cloak activation with the 'c' key
        # Activate cloak if 'c' is pressed
        if current_keys[pygame.K_c]:
            if not keys_pressed[pygame.K_c]:
                keys_pressed[pygame.K_c] = True
                if cloaks > 0 and not is_cloaked:
                    cloak()  
                action_performed = True
        else:
            keys_pressed[pygame.K_c] = False


        # Check if enough time has passed since last move
        time_since_last_move = current_time - last_move_time
        if time_since_last_move < movement_cooldown:
            return action_performed  # Not time to move yet
        
        # Ready to make a move
        move_made = False
        
        # Define all direction keys with their movement vectors (delta_row, delta_col)
        direction_keys = [
            # Arrow keys
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
        
        # First check keys being held down - using all direction keys
        for key, (delta_row, delta_col) in direction_keys:
            if current_keys[key]:
                if not keys_pressed[key]:  # Key just pressed
                    keys_pressed[key] = True
                    keys_held_time[key] = current_time
                
                # Try to move in the direction
                move_made = process_move(player_row + delta_row, player_col + delta_col)
                if move_made:
                    last_move_time = current_time
                    break
            else:
                # Key released
                if keys_pressed[key]:
                    hold_duration = current_time - keys_held_time[key]
                    if hold_duration > MOMENTUM_THRESHOLD:
                        # Add momentum based on hold duration
                        momentum[key] = min(MAX_MOMENTUM, int((hold_duration - MOMENTUM_THRESHOLD) / 100))
                    keys_pressed[key] = False
        
        # If no key is pressed but we have momentum, apply it
        if not move_made:
            for key, (delta_row, delta_col) in direction_keys:
                if momentum[key] > 0:
                    move_made = process_move(player_row + delta_row, player_col + delta_col)
                    if move_made:
                        momentum[key] -= 1
                        last_move_time = current_time
                        break
        
        return action_performed or move_made
    
    def process_move(new_row, new_col):
        """Process a player movement to a new position"""
        nonlocal player_row, player_col, Score, gems, whips, teleports, keys, level_num, cloaks
        
        # Check if position is valid
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        
        # Check if destination is not a wall
        if grid[new_row][new_col] not in collidable_tiles:
            # Collect items
            if grid[new_row][new_col] == "+":  # Gem
                gems += 1
                Score += 1  # Original game awards 1 point per gem
            elif grid[new_row][new_col] == "W":  # Whip
                whips += 1
                Score += 1  # Original game awards 1 point per whip
            elif grid[new_row][new_col] == "T":  # Teleport
                teleports += 1
                Score += 1  # Original game awards 1 point per teleport
            elif grid[new_row][new_col] == "K":  # Key
                keys += 1
                Score += 1  # Original game doesn't specify key points explicitly
            elif grid[new_row][new_col] == "L":  # Stairs to next level
                level_num += 1
                Score += level_num  # Original game awards points equal to the level number
            elif grid[new_row][new_col] == "_":  # Cloak
                cloaks += 1
                score += 60  # optional, just for fun
                # Could add level change logic here
            elif grid[new_row][new_col] == "*":  # Nugget
                Score += 50  # Gold nuggets are worth 50 points
            elif grid[new_row][new_col] == "S":  # SlowTime
                Score += 5  # SlowTime bonus
            elif grid[new_row][new_col] == "I":  # Invisible
                Score += 10  # Invisible bonus
            elif grid[new_row][new_col] == "F":  # SpeedTime
                Score += 2  # SpeedTime bonus
            elif grid[new_row][new_col] == "C":  # Chest
                Score += 5  # Chest bonus
            elif grid[new_row][new_col] == "!":  # Tablet
                Score += level_num + 250  # Tablet bonus (level + fixed bonus)
            
            # Move player
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            return True
        
        # Movement was blocked
        if grid[new_row][new_col] in ["X", "#"]:  # Wall or block
            if Score > 2:  # Only subtract if score is greater than 2
                Score -= 2  # Original game deducts 2 points for hitting walls
        return False
    
    # Game constants
    FAST_PC = True  # Modern computers are "fast" compared to original era
    
    # Timer initialization (from KINGDOM4.INC lines 61-63)
    if FAST_PC:
        BASE_SLOW_TIMER = 10
        BASE_MEDIUM_TIMER = 8
        BASE_FAST_TIMER = 6
    else:
        BASE_SLOW_TIMER = 3
        BASE_MEDIUM_TIMER = 2
        BASE_FAST_TIMER = 1
    
    # Current timer values
    SLOW_TIMER = BASE_SLOW_TIMER
    MEDIUM_TIMER = BASE_MEDIUM_TIMER
    FAST_TIMER = BASE_FAST_TIMER
    
    # Spell effect timers
    slow_time_effect = 0  # T[4] in original
    invisible_effect = 0  # T[5] in original
    speed_time_effect = 0 # T[6] in original
    freeze_effect = 0     # T[7] in original
    
    # Higher rate faster enemies move
    GAME_TICK_RATE = 16.0
    
    # Game loop
    running = True
    clock = pygame.time.Clock()
    tick_counter = 0
    
    # Individual enemy movement counters - separate timing for each enemy type
    slow_counter = 0
    medium_counter = 0
    fast_counter = 0

    # How many ticks to wait between enemy movements (higher = slower)
    slow_threshold = 4  # Slowest enemy (type 1)
    medium_threshold = 2  # Medium speed enemy (type 2)
    fast_threshold = 1  # Fastest enemy (type 3)
    
    wait = True

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

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # ASCII value 80 
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
                        "Score": Score,
                        "level_num": level_num,
                        "gems": gems,
                        "whips": whips,
                        "teleports": teleports,
                        "keys": keys
                    })
                elif event.key == pygame.K_r:
                    restored_state = handle_restore(screen)
                    if restored_state:
                        grid = generate_grid_for_level(restored_state["level_num"])  # Regenerate grid
                        player_row = restored_state["player_row"]
                        player_col = restored_state["player_col"]
                        Score = restored_state["Score"]
                        level_num = restored_state["level_num"]
                        gems = restored_state["gems"]
                        whips = restored_state["whips"]
                        teleports = restored_state["teleports"]
                        keys = restored_state["keys"]
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False
        
        # Process player input
        action_performed = player_input()

         # Auto-deactivate cloak after duration
        if is_cloaked and pygame.time.get_ticks() - cloak_start_time > 5000:
            is_cloaked = False

        # Draw the grid
        screen.fill(BLACK)
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char == "P":
                    if is_cloaked: # Changed player icon
                        screen.blit(tile_mapping['TP'], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT)) 
                    else:
                        screen.blit(tile_mapping['P'], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT))
                elif char in tile_mapping:
                    screen.blit(tile_mapping[char], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT))

        # Update the item tracking UI with current values
        values = [Score, level_num, gems, whips-1, teleports, keys, cloaks]
        hud(screen, WIDTH, HEIGHT, values)
        
        # Update spell effect timers
        if slow_time_effect > 0:
            slow_time_effect -= 1
        if invisible_effect > 0:
            invisible_effect -= 1
        if speed_time_effect > 0:
            speed_time_effect -= 1
        if freeze_effect > 0:
            freeze_effect -= 1
        
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
        
        # Handle speed and slow time powerups
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

        pygame.display.flip()
        clock.tick(GAME_TICK_RATE)
levels(screen, difficulty_input, mixUp = False)