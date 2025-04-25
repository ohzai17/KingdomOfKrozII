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
        draw_text(screen, 16, message, "CHANGING")
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

def player_death(screen, score, level_num):
    """Handle player death when out of gems"""
    print("you have died")
    
    pygame.event.clear()  # Clear any pending events
    
    # Display death message on screen
    draw_text(1, "YOU HAVE DIED!!!", BLACK, True, True, LIGHT_GRAY)
    draw_text(16, "Press any key to continue...", WHITE, False, True, None) # Add prompt
    pygame.display.flip()
    
    pygame.time.delay(500)  # Pause for 2 seconds to show message
    
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
    leaderboard_screen(screen, score, level_num)
    pygame.quit()
    exit()
                    
def hud_original(screen, WIDTH, HEIGHT, color="C", values=None):  # From KINGDOM4.PAS (lines 96-183)

    is_monochrome = True if color == "M" else False

    # Background rectangle
    rect_surface = pygame.Surface((WIDTH, HEIGHT - (TILE_HEIGHT * 23) - 20))
    rect_surface.fill(BLUE)
    if is_monochrome:
        rect_surface = apply_grayscale_f(rect_surface)
    screen.blit(rect_surface, (0, (TILE_HEIGHT * 23) + 20))

    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Cloaks", "Options"]
    option_list = ["Cloaks", "Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]

    font = load_font(13)
    word_x = 5
    word_y = (TILE_HEIGHT * 23) + 30

    rect_width = 78
    rect_height = 30

    for i, word in enumerate(item_tracker):
        if is_monochrome:
            label_color = GRAY
            value_color = GRAY
            box_color = SILVER
        else:
            label_color = CYAN if word == "Options" else YELLOW
            value_color = DARK_RED
            box_color = LIGHT_GRAY

        # Draw label
        word_surface = font.render(word, True, label_color)

        if word == "Options" and not is_monochrome:
            pygame.draw.rect(screen, DARK_RED, (word_x - 5, word_y, word_surface.get_width() + 10, word_surface.get_height() + 6))
            screen.blit(word_surface, (word_x, word_y + 3))  # slight padding inside the box
        else:
            screen.blit(word_surface, (word_x, word_y))

        # Draw value box + value
        if i < len(values):
            value_surface = font.render(str(values[i]), True, value_color)
            value_x = word_x + (word_surface.get_width() // 2) - (rect_width // 2)
            box_y = word_y + word_surface.get_height() + 10

            pygame.draw.rect(screen, box_color, (value_x, box_y, rect_width, rect_height))
            screen.blit(value_surface, (
                value_x + (rect_width - value_surface.get_width()) // 2,
                box_y + 5
            ))

        word_x += word_surface.get_width() + 30

    # Draw option list below
    y_offset = word_y + 30
    for choice in option_list:
        if is_monochrome:
            first_letter_color = GRAY
            rest_color = GRAY
        else:
            first_letter_color = WHITE
            rest_color = GRAY

        first_letter_surface = font.render(choice[0], True, first_letter_color)
        rest_surface = font.render(choice[1:], True, rest_color)

        first_rect = first_letter_surface.get_rect(topleft=(word_x - 120, y_offset))
        rest_rect = rest_surface.get_rect(topleft=(first_rect.right, y_offset))

        screen.blit(first_letter_surface, first_rect)
        screen.blit(rest_surface, rest_rect)

        y_offset += 20

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
    
            
    if color == "M":
        for sprite in sprites:
            images[sprite] = apply_grayscale_f(images[sprite])
            images[sprite] = pygame.transform.scale(images[sprite], (TILE_WIDTH, TILE_HEIGHT))

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
            score, level_num, gems, whips, teleports, keys, cloaks = 10, 1, 20, 10, 10, 10, 10
        
    if mixUp:
        score, level_num, gems, whips, teleports, keys = 0, 1, gems + 60, whips + 30, teleports + 15, 2
    
    values = [score, level_num, gems, whips, teleports, keys, cloaks]
    main_hud(screen, WIDTH, HEIGHT, color, values)
        
    # Function to change to the next level
    def change_level(next_level_index):
        nonlocal grid, player_row, player_col, slow_enemies, medium_enemies, level_num
        
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
                
                if gems < 0:
                    player_death(screen, score, level_num)  # Call player_death when out of gems
                
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
                    player_death(screen, score, level_num)  # Call player_death when out of gems
                    
                return True  # Enemy dies
                
            # Blocked - try to find another way
            else:
                grid[row][col] = enemy_type  # Stay in place
    
    def use_whip(screen, grid, player_row, player_col, whips, slow_enemies, medium_enemies, images, tile_mapping, TILE_WIDTH, TILE_HEIGHT):
        """Handle the whip animation and enemy interactions"""
        # Access game state variables from enclosing scope
        nonlocal score, level_num, gems, teleports, keys, WIDTH, HEIGHT
        
        # Check if player has whips
        if whips <= 0:
            return 0, [], []  # No whips to use
        
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
            main_hud(screen, WIDTH, HEIGHT, values)
        
        # Process enemy hits and update game state
        kills = 0
        new_slow_enemies = []
        new_medium_enemies = []
        
        # Clear enemies hit by whip from both grid and enemy lists
        for r, c, enemy_type in enemies_hit:
            grid[r][c] = " "  # Clear enemy from grid
            kills += 1
            
        # Rebuild enemy lists excluding the killed ones
        for enemy in slow_enemies:
            if grid[enemy["row"]][enemy["col"]] == "1":
                new_slow_enemies.append(enemy)
                
        for enemy in medium_enemies:
            if grid[enemy["row"]][enemy["col"]] == "2":
                new_medium_enemies.append(enemy)
        
        return kills, new_slow_enemies, new_medium_enemies
    
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
        nonlocal player_row, player_col, score, gems, whips, teleports, keys
        nonlocal slow_enemies, medium_enemies, last_move_time, cloaks, is_cloaked
        
        current_time = pygame.time.get_ticks()
        current_keys = pygame.key.get_pressed()
        action_performed = False
        
        # Handle whip activation with the 'W' key
        if current_keys[pygame.K_w]:
            if not keys_pressed[pygame.K_w]:  # Key just pressed
                keys_pressed[pygame.K_w] = True
                if whips > 0:
                    kills, slow_enemies, medium_enemies = use_whip(
                        screen, grid, player_row, player_col, whips, 
                        slow_enemies, medium_enemies, images, tile_mapping, 
                        TILE_WIDTH, TILE_HEIGHT
                    )
                    whips -= 1
                    score += kills * 150  # Award points for kills
                    action_performed = True
        else:
            keys_pressed[pygame.K_w] = False

        # Handle Teleport activation with the 't' key
        if current_keys[pygame.K_t]:
            if not keys_pressed[pygame.K_t]:
                keys_pressed[pygame.K_t] = True
                if teleports > 0:
                    player_row, player_col = teleport(grid, player_row, player_col, tile_mapping, screen)
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
        active_direction = None
        
        # Direction priority: UP, DOWN, LEFT, RIGHT
        direction_keys = [
            (pygame.K_UP, (-1, 0)),
            (pygame.K_DOWN, (1, 0)),
            (pygame.K_LEFT, (0, -1)),
            (pygame.K_RIGHT, (0, 1))
        ]
        
        # First check keys being held down
        for key, (delta_row, delta_col) in direction_keys:
            if current_keys[key]:
                if not keys_pressed[key]:  # Key just pressed
                    keys_pressed[key] = True
                    keys_held_time[key] = current_time
                
                # This is our active direction
                active_direction = key
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
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False
        
        # Process player input
        player_input()

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
        values = [score, level_num, gems, whips, teleports, keys, cloaks]
        main_hud(screen, WIDTH, HEIGHT, color, values)
        
        # Update game state
        tick_counter += 1
        
        # Move enemies on their respective timers
        if tick_counter % SLOW_TIMER == 0:
            # Move slow enemies
            for i in range(len(slow_enemies)-1, -1, -1):
                if move_enemy(slow_enemies[i], "1", 8):
                    del slow_enemies[i]
        
        if tick_counter % MEDIUM_TIMER == 0:
            # Move medium enemies
            for i in range(len(medium_enemies)-1, -1, -1):
                if move_enemy(medium_enemies[i], "2", 7):
                    del medium_enemies[i]

        if wait:
            wait_input(screen)
            wait = False
        pygame.display.flip()
        clock.tick(GAME_TICK_RATE)