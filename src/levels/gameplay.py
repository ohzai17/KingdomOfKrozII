import pygame
import random

pygame.init()

# Basic setup
WIDTH, HEIGHT = 896, 504
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kingdom of Kroz II")

# Tile dimensions
TILE_WIDTH = 14
TILE_HEIGHT = 14

# Load and scale tiles
block    = pygame.transform.scale(pygame.image.load("src/assets/block.png"), (TILE_WIDTH, TILE_HEIGHT))
chest    = pygame.transform.scale(pygame.image.load("src/assets/chest.png"), (TILE_WIDTH, TILE_HEIGHT))
enemy1   = pygame.transform.scale(pygame.image.load("src/assets/enemy1.png"), (TILE_WIDTH, TILE_HEIGHT))
enemy2   = pygame.transform.scale(pygame.image.load("src/assets/enemy2.png"), (TILE_WIDTH, TILE_HEIGHT))
gem      = pygame.transform.scale(pygame.image.load("src/assets/gem.png"), (TILE_WIDTH, TILE_HEIGHT))
player   = pygame.transform.scale(pygame.image.load("src/assets/player.png"), (TILE_WIDTH, TILE_HEIGHT))
stairs   = pygame.transform.scale(pygame.image.load("src/assets/stairs.png"), (TILE_WIDTH, TILE_HEIGHT))
teleport = pygame.transform.scale(pygame.image.load("src/assets/teleport.png"), (TILE_WIDTH, TILE_HEIGHT))
trap     = pygame.transform.scale(pygame.image.load("src/assets/trap.png"), (TILE_WIDTH, TILE_HEIGHT))
wall     = pygame.transform.scale(pygame.image.load("src/assets/wall.png"), (TILE_WIDTH, TILE_HEIGHT))
whip     = pygame.transform.scale(pygame.image.load("src/assets/whip.png"), (TILE_WIDTH, TILE_HEIGHT))

def level(screen):
    # Level map
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

    # Map characters to tiles
    tile_mapping = {
        "X": block, "#": wall, "C": chest, "W": whip,
        "1": enemy1, "2": enemy2, "+": gem, "T": teleport,
        ".": trap, "L": stairs, "P": player
    }
    
    # Game state
    grid = [list(row) for row in level_map]
    collidable_tiles = {"X", "#"}
    slow_enemies = []
    medium_enemies = []
    keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, 
                    pygame.K_LEFT: False, pygame.K_RIGHT: False}
    
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
        
        # Handle movement and collisions
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # Breaking X blocks
            if grid[new_row][new_col] == "X":
                grid[new_row][new_col] = " "  # Break the block
                return True  # Enemy dies when breaking block
                
            # Empty space - move there
            elif grid[new_row][new_col] == " ":
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                
            # Hit player
            elif grid[new_row][new_col] == "P":
                return True  # Enemy dies
                
            # Blocked - try to find another way
            else:
                grid[row][col] = enemy_type  # Stay in place
        else:
            grid[row][col] = enemy_type  # Stay in place
            
        return False

    def player_input():
        """Handle player movement with key press tracking"""
        nonlocal player_row, player_col
        
        # Get current key states
        current_keys = pygame.key.get_pressed()
        
        # Calculate new position based on key presses
        new_row, new_col = player_row, player_col
        moved = False
        
        # Cardinal directions (no diagonals for simplicity)
        if current_keys[pygame.K_UP] and not keys_pressed[pygame.K_UP]:
            new_row -= 1
            moved = True
            keys_pressed[pygame.K_UP] = True
        elif current_keys[pygame.K_DOWN] and not keys_pressed[pygame.K_DOWN]:
            new_row += 1
            moved = True
            keys_pressed[pygame.K_DOWN] = True
        elif current_keys[pygame.K_LEFT] and not keys_pressed[pygame.K_LEFT]:
            new_col -= 1
            moved = True
            keys_pressed[pygame.K_LEFT] = True
        elif current_keys[pygame.K_RIGHT] and not keys_pressed[pygame.K_RIGHT]:
            new_col += 1
            moved = True
            keys_pressed[pygame.K_RIGHT] = True
        
        # Reset keys that have been released
        for key in keys_pressed:
            if not current_keys[key]:
                keys_pressed[key] = False
        
        # Move player if valid
        if moved and (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                     grid[new_row][new_col] not in collidable_tiles):
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            return True
            
        return False

    # Game constants
    SLOW_TIMER = 5
    MEDIUM_TIMER = 6
    GAME_TICK_RATE = 12.0
    
    # Game loop
    running = True
    clock = pygame.time.Clock()
    tick_counter = 0
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False
        
        # Process player input
        player_input()
        
        # Draw the grid
        screen.fill((0, 0, 0))
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char in tile_mapping:
                    screen.blit(tile_mapping[char], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT))
        
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
        
        pygame.display.flip()
        clock.tick(GAME_TICK_RATE)

level(screen)
pygame.quit()
