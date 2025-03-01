import pygame
import random

pygame.init()

# Initiate Screen
WIDTH, HEIGHT = 896, 504
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level 1")

# Define tile dimensions
TILE_WIDTH = 14
TILE_HEIGHT = 14

# Load tiles
block    = pygame.image.load("src/assets/block.png")
chest    = pygame.image.load("src/assets/chest.png")
enemy1   = pygame.image.load("src/assets/enemy1.png")
enemy2   = pygame.image.load("src/assets/enemy2.png")
gem      = pygame.image.load("src/assets/gem.png")
player   = pygame.image.load("src/assets/player.png")
stairs   = pygame.image.load("src/assets/stairs.png")
teleport = pygame.image.load("src/assets/teleport.png")
trap     = pygame.image.load("src/assets/trap.png")
wall     = pygame.image.load("src/assets/wall.png")
whip     = pygame.image.load("src/assets/whip.png")
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

def level(screen):
    # Level map as a list of strings
    level_map = [
        "W W W W             2 2 2 2 2  C  2 2 2 2 2              W W W W",
        "XXXXXXXXXXXXXXXXXXX###########   ###########XXXXXXXXXXXXXXXXXXXX",
        " 1           1                               1                  ",
        "                                    1            XX         1   ",
        "       1            1                           XXXX            ",
        "#        XX                    +                 XX            #",
        "##      XXXX  1                +          1          1        ##",
        "T##      XX               2    +    2                        ##T",
        "T1##                       W   +   W                        ##1T",
        "T########X                 WX     XW             1    X########T",
        ".        X                2WX  P  XW2                 X        .",
        "T########X         1       WX     XW                  X########T",
        "T1##                       W   +   W         1              ##1T",
        "T##                       2    +    2                        ##T",
        "##   1                         +                      XX      ##",
        "#       XX      1              +                 1   XXXX     1#",
        "       XXXX                 ##   ##                   XX        ",
        "1       XX                 ##     ##     1        1           1 ",
        "                    1#######       ########                     ",
        "    1         ########11111  +++++  111111########              ",
        "WW     ########+++++        #######         WWWWW########1    WW",
        "########C                    2 2 2                     C########",
        "L2  +  X      ####################################      X  +  2L",
    ]

    # Map char to tile
    tile_mapping = {
        "X": block,
        "#": wall,
        "C": chest,
        "W": whip,
        "1": enemy1,  # Slow enemy
        "2": enemy2,  # Medium/Fast enemy
        "+": gem,
        "T": teleport,
        ".": trap,
        "L": stairs,
        "P": player
    }

    # Initiate grid
    grid = [list(row) for row in level_map]

    # Define collidable tiles and function to check if a tile is collidable
    collidable_tiles = {"X", "#"}

    # Define dynamic tiles
    dynamic_tiles = {"P", "1", "2"}

    # Find the player's starting position
    player_row, player_col = 0, 0
    found_player = False
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == "P":
                player_row, player_col = r, c
                found_player = True
                break
        if found_player:
            break

    # Extract enemy positions with types and timers - exactly matching KROZ format
    enemies = []
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "1":  # Slow enemy (matching Slow in KROZ)
                enemies.append({
                    "row": r, 
                    "col": c, 
                    "type": char,
                    "timer": 0,
                    "move_rate": 5  # T[1] in KINGDOM.PAS
                })
            elif char == "2":  # Medium/Fast enemy (matching Medium/Fast in KROZ)
                enemies.append({
                    "row": r, 
                    "col": c, 
                    "type": char, 
                    "timer": 0,
                    "move_rate": 3  # T[2]/T[3] in KINGDOM.PAS
                })

    def is_valid_move(row, col):
        return (0 <= row < len(grid) and 
                0 <= col < len(grid[row]) and 
                grid[row][col] not in collidable_tiles)

    def move_enemy(enemy):
        """Move enemy toward player exactly like in KINGDOM.PAS"""
        # Reset the current grid position
        current_row, current_col = enemy["row"], enemy["col"]
        grid[current_row][current_col] = " "  # Clear current position
        
        # Determine direction toward player (X movement takes priority like in KROZ)
        x_dir, y_dir = 0, 0
        
        # Determine direction directly toward player
        if player_col < current_col:
            x_dir = -1
        elif player_col > current_col:
            x_dir = 1
            
        if player_row < current_row:
            y_dir = -1
        elif player_row > current_row:
            y_dir = 1
        
        # Try X movement first (as in original KROZ)
        if x_dir != 0:
            new_row, new_col = current_row, current_col + x_dir
            if is_valid_move(new_row, new_col):
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy["type"]
                return
        
        # If X movement not possible or not needed, try Y movement
        if y_dir != 0:
            new_row, new_col = current_row + y_dir, current_col
            if is_valid_move(new_row, new_col):
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy["type"]
                return
        
        # If no move was possible, stay in place
        grid[current_row][current_col] = enemy["type"]

    # Main loop
    running = True
    clock = pygame.time.Clock()
    frame_counter = 0
    slow_time_active = False
    slow_time_counter = 0
    speed_time_active = False  
    speed_time_counter = 0
    freeze_active = False
    freeze_counter = 0

    while running:
        screen.fill((0, 0, 0))
        
        # Draw the static grid
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char in tile_mapping and char not in dynamic_tiles:  # Skip dynamic tiles
                    x = col_index * TILE_WIDTH
                    y = row_index * TILE_HEIGHT
                    screen.blit(tile_mapping[char], (x, y))
        
        # Draw the player
        player_x = player_col * TILE_WIDTH
        player_y = player_row * TILE_HEIGHT
        screen.blit(player, (player_x, player_y))
        
        player_moved = False  # Flag to check if the player has moved

        # Event handling for quitting and movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                new_row, new_col = player_row, player_col
                keys = pygame.key.get_pressed()
                
                # Support both diagonal and cardinal movements like in KROZ
                if keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    new_row -= 1  # North
                elif keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    new_row += 1  # South
                elif keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    new_col -= 1  # West
                elif keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    new_col += 1  # East
                elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                    new_row -= 1  # Northwest
                    new_col -= 1
                elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                    new_row -= 1  # Northeast
                    new_col += 1
                elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                    new_row += 1  # Southwest
                    new_col -= 1
                elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                    new_row += 1  # Southeast
                    new_col += 1
                
                # Ensure the new position is within bounds
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                    # Only move if the destination tile is not collidable
                    if grid[new_row][new_col] not in collidable_tiles:
                        # Clear the player's current position in the grid
                        grid[player_row][player_col] = " "
                        player_row, player_col = new_row, new_col
                        grid[player_row][player_col] = "P"
                        player_moved = True

        # Handle enemy movement exactly as in KINGDOM.PAS
        if frame_counter % 4 == 0:  # Basic timing factor
            # Update spell counters
            if slow_time_counter > 0:
                slow_time_counter -= 1
                slow_time_active = True
            else:
                slow_time_active = False
            
            if speed_time_counter > 0:
                speed_time_counter -= 1
                speed_time_active = True
            else:
                speed_time_active = False
                
            if freeze_counter > 0:
                freeze_counter -= 1
                freeze_active = True
            else:
                freeze_active = False
                
            # Process enemy movement if not frozen
            if not freeze_active:
                for enemy in enemies:
                    # Adjust movement rate based on active spells (just like in KROZ)
                    if speed_time_active:
                        actual_move_rate = max(1, enemy["move_rate"] // 2)
                    elif slow_time_active:
                        actual_move_rate = enemy["move_rate"] * 2
                    else:
                        actual_move_rate = enemy["move_rate"]
                    
                    # Update timer
                    enemy["timer"] += 1
                    if enemy["timer"] >= actual_move_rate:
                        enemy["timer"] = 0
                        
                        # In original KROZ, enemies sometimes move even if player moved
                        # This simulates the random movement checks in the original game
                        if not player_moved or random.random() < 0.25:
                            move_enemy(enemy)
        
        # Draw enemies
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char in ["1", "2"]:  # Draw any enemies in the grid
                    x = col_index * TILE_WIDTH
                    y = row_index * TILE_HEIGHT
                    screen.blit(tile_mapping[char], (x, y))
        
        pygame.display.flip()
        clock.tick(18.2)  # Match KROZ framerate (18.2Hz)
        frame_counter += 1

level(screen)
pygame.quit()
