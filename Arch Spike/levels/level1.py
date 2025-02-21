import pygame

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level 1")

# Load images into variables
block = pygame.image.load("levels/tiles/block.png")
chest = pygame.image.load("levels/tiles/chest.png")
enemy1 = pygame.image.load("levels/tiles/enemy1.png")
enemy2 = pygame.image.load("levels/tiles/enemy2.png")
gem = pygame.image.load("levels/tiles/gem.png")
player = pygame.image.load("levels/tiles/player.png")
stairs = pygame.image.load("levels/tiles/stairs.png")
teleport = pygame.image.load("levels/tiles/teleport.png")
trap = pygame.image.load("levels/tiles/trap.png")
wall = pygame.image.load("levels/tiles/wall.png")
whip = pygame.image.load("levels/tiles/whip.png")

# Optional: Scale images if needed
TILE_SIZE = 30  # Adjust size as needed
block = pygame.transform.scale(block, (TILE_SIZE, TILE_SIZE))
chest = pygame.transform.scale(chest, (TILE_SIZE, TILE_SIZE))
enemy1 = pygame.transform.scale(enemy1, (TILE_SIZE, TILE_SIZE))
enemy2 = pygame.transform.scale(enemy2, (TILE_SIZE, TILE_SIZE))
gem = pygame.transform.scale(gem, (TILE_SIZE, TILE_SIZE))
player = pygame.transform.scale(player, (TILE_SIZE, TILE_SIZE))
stairs = pygame.transform.scale(stairs, (TILE_SIZE, TILE_SIZE))
teleport = pygame.transform.scale(teleport, (TILE_SIZE, TILE_SIZE))
trap = pygame.transform.scale(trap, (TILE_SIZE, TILE_SIZE))
wall = pygame.transform.scale(wall, (TILE_SIZE, TILE_SIZE))
whip = pygame.transform.scale(whip, (TILE_SIZE, TILE_SIZE))

# Tile settings
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

# Map character to tile
tile_mapping = {
    "X": block,
    "#": wall,
    "P": player,
    "C": chest,
    "W": whip,
    "1": enemy1,
    "2": enemy2,
    "+": gem,
    "T": teleport,
    ".": trap,
}

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Draw tiles
    for row_index, row in enumerate(level_map):
        for col_index, char in enumerate(row):
            if char in tile_mapping:
                screen.blit(tile_mapping[char], (col_index * TILE_SIZE, row_index * TILE_SIZE))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
