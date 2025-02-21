import pygame
import random

def level (screen):

    # Define tile dimensions
    TILE_WIDTH = 13
    TILE_HEIGHT = 13

    # Load tiles
    block    = pygame.image.load("assets/block.png")
    chest    = pygame.image.load("assets/chest.png")
    enemy1   = pygame.image.load("assets/enemy1.png")
    enemy2   = pygame.image.load("assets/enemy2.png")
    gem      = pygame.image.load("assets/gem.png")
    player   = pygame.image.load("assets/player.png")
    stairs   = pygame.image.load("assets/stairs.png")
    teleport = pygame.image.load("assets/teleport.png")
    trap     = pygame.image.load("assets/trap.png")
    wall     = pygame.image.load("assets/wall.png")
    whip     = pygame.image.load("assets/whip.png")

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

    # Main loop
    running = True
    clock = pygame.time.Clock()
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
        
        # Draw enemies with random movement
        for enemy in enemies:
            # Random chance to move per frame (10% chance)
            if random.random() < 0.1:
                delta_row = random.choice([-1, 0, 1])
                delta_col = random.choice([-1, 0, 1])
                new_enemy_row = enemy["row"] + delta_row
                new_enemy_col = enemy["col"] + delta_col
                # Ensure new position is within bounds and not collidable
                if (0 <= new_enemy_row < len(grid) and 
                    0 <= new_enemy_col < len(grid[new_enemy_row]) and 
                    grid[new_enemy_row][new_enemy_col] not in collidable_tiles):
                    enemy["row"], enemy["col"] = new_enemy_row, new_enemy_col
            
            # Draw enemy
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

    pygame.quit()
