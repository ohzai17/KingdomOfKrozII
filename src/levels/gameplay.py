import pygame

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
        "1": enemy1,
        "2": enemy2,
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

    # Extract enemy positions
    enemies = []
    enemy_chars = {"1", "2"}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in enemy_chars:
                enemies.append({"row": r, "col": c, "type": char})

    def is_valid_move(row, col):
        return (0 <= row < len(grid) and 
                0 <= col < len(grid[row]) and 
                grid[row][col] not in collidable_tiles)

    def move_towards_player(enemy):
        if player_row < enemy["row"] and is_valid_move(enemy["row"] - 1, enemy["col"]):
            enemy["row"] -= 1
        elif player_row > enemy["row"] and is_valid_move(enemy["row"] + 1, enemy["col"]):
            enemy["row"] += 1
        elif player_col < enemy["col"] and is_valid_move(enemy["row"], enemy["col"] - 1):
            enemy["col"] -= 1
        elif player_col > enemy["col"] and is_valid_move(enemy["row"], enemy["col"] + 1):
            enemy["col"] += 1

    # Main loop
    running = True
    clock = pygame.time.Clock()
    frame_counter = 0  # Add a frame counter

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
        
        # Move enemies every fourth frame
        if frame_counter % 4 == 0:
            for enemy in enemies:
                move_towards_player(enemy)
        
        # Draw enemies
        for enemy in enemies:
            enemy_x = enemy["col"] * TILE_WIDTH
            enemy_y = enemy["row"] * TILE_HEIGHT
            screen.blit(tile_mapping[enemy["type"]], (enemy_x, enemy_y))
        
        # Event handling for quitting and movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                new_row, new_col = player_row, player_col
                # TODO fix diagonal movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    new_row -= 1
                if keys[pygame.K_DOWN]:
                    new_row += 1
                if keys[pygame.K_LEFT]:
                    new_col -= 1
                if keys[pygame.K_RIGHT]:
                    new_col += 1
                
                # Ensure the new position is within bounds
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                    # Only move if the destination tile is not collidable
                    if grid[new_row][new_col] not in collidable_tiles:
                        player_row, player_col = new_row, new_col

        pygame.display.flip()
        clock.tick(18)
        frame_counter += 1  # Increment the frame counter

level(screen)
pygame.quit()
