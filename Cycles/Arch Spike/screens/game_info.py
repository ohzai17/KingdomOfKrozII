import pygame
import random
<<<<<<< HEAD:Cycles/Arch Spike/screens/game_info.py
from functions import *

def info_screen1(screen, color):
    # Use the provided screen
    WIDTH, HEIGHT = screen.get_size()

    if color == "M":  # Monochrome mode
        RED = (128, 128, 128)
        GREEN = (128, 128, 128)
        BLUE = (128, 128, 128)
        YELLOW = (255, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (0, 0, 0)
        BROWN = (128, 128, 128)
        OLD_BLUE = (0, 0, 0)
        ORANGE = (128, 128, 128)
        GRAY = (169, 169, 169)
    else:
        RED = (144, 13, 13)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
        BROWN = (139, 69, 19)
        OLD_BLUE = (44, 0, 180)
        ORANGE = (255, 165, 0)
        GRAY = (169, 169, 169)

    # Colors to cycle through (for title or cursor effects)
    colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BROWN]
    rand_color = random.choice(colors)

    # Font setup
    title_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 20)
    text_font = pygame.font.Font("screens/assets/PressStart2P-Regular.ttf", 10)

    title = title_font.render("KINGDOM OF KROZ II - HOW TO REGISTER", True, WHITE)
   
=======
from gen_functions import *

def info_screen1():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Colors to cycle through
    colors = [ RED,
              GREEN,
              BLUE,
              YELLOW,
              ORANGE,
              PINK,
              BROWN
    ]

    # Random color picker
    rand_color = random.choice(colors)

    # Font setup
    title_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 20)  # Larger font for title (Need to disable Italic)
    text_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 10)  # Default font

    # Text rendering
    title = title_font.render("KINGDOM OF KROZ II - HOW TO REGISTER", True, WHITE) # Antialias enable
   
    # Paragraph list1
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/game_info.py
    paragraph_text1 = [
        "  This is not a shareware game, but it is user-supported. If you enjoy this",
        "game, you are asked by the author to please send a registration ",
        "check in the amount of $7.50 to Apogee Software.",
        "  This registration fee will qualify you to order any of the other Kroz",
        "volumes available:"
    ]

<<<<<<< HEAD:Cycles/Arch Spike/screens/game_info.py
    kroz_volumes = [
        "Caverns of Kroz   - the first discovery of Kroz",
        "Dungeons of Kroz  - the dark side of Kroz, fast-paced action", 
        "Kingdom of Kroz I - the national contest winner (\"Best Game\" in 1988)",
=======
    # Kroz volumes list
    kroz_volumes = [
        "Caverns of Kroz   - the first discovery of Kroz",
        "Dungeons of Kroz  - the dark side of Kroz, fast-paced action", 
        "Kingdom of Kroz I - the national contest winner (""Best Game"" in 1988)",
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/game_info.py
        "Return of Kroz    - the discovery of entirely  new underground chambers",
        "Temple of Kroz    - the bizarre side of Kroz, nothing is what is seems",
        "The Final Crusade of Kroz - the surprising finish?"
    ]
<<<<<<< HEAD:Cycles/Arch Spike/screens/game_info.py
    start_x, start_y = 30, 190
    line_spacing = 25
    bullet_size = 8

    paragraph_text2 = [
        "Each gam is priced $7.50 each, any three for $20, or all six for only $35.",
        "You'll also get a secret code that makes this game easier to complete,",
=======
    start_x, start_y = 30, 190  # Starting position
    line_spacing = 25           # Spacing between lines
    bullet_size = 8             # Size of the square bullet

    # Paragraph list2
    paragraph_text2 = [
        "Each gam is priced $7.50 each, any three for $20, or all six for only $35.",
        "You'll also get a secret code that this game easier to complete,",
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/game_info.py
        "Plus a \"Hints Tricks and Scoring Secrets\" guide and \"The Domain of Kroz\" map.",
        " ",
        " ",
        "Please make checks payable to:",
        " ",
        " ",
        " ",
        "Thank you and enjoy the game.  -- Scott Miller"
<<<<<<< HEAD:Cycles/Arch Spike/screens/game_info.py
    ] 

=======

    ] 

    # yellow paragraph
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/game_info.py
    check_info = [
        "apogee Software     (phone: 214/240-0614)",
        "4206 Mayflower",
        "Garland, TX 75045   (USA)"
    ]

<<<<<<< HEAD:Cycles/Arch Spike/screens/game_info.py
    prompt_text = text_font.render("Press any key to continue", True, WHITE2)
    title_rect = title.get_rect(center=(WIDTH // 2, 15))

    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill(OLD_BLUE)
        screen.blit(title, title_rect)
        
        # Draw horizontal line under title
        line_y = title_rect.bottom + 8
        pygame.draw.line(screen, GRAY, (0, line_y), (WIDTH, line_y), 1)
        
        y_offset = line_y + 10
        for line in paragraph_text1:
            rendered_line = text_font.render(line, True, GRAY)
            screen.blit(rendered_line, (2, y_offset))
            y_offset += 20

        for i, name in enumerate(kroz_volumes):
            y_pos = start_y + i * line_spacing
            pygame.draw.rect(screen, WHITE, (start_x, y_pos, bullet_size, bullet_size))
            text_surface = text_font.render(name, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))

        y_offset = 380
        for line in paragraph_text2:
            rendered_line = text_font.render(line, True, GRAY)
            screen.blit(rendered_line, (2, y_offset))
            y_offset += 20
        
        y_offset = 480
        for line in check_info:
            rendered_line = text_font.render(line, True, YELLOW)
            screen.blit(rendered_line, (320, y_offset))
            y_offset += 20
        
        single_line = text_font.render("Address is always valid!", True, WHITE)
        screen.blit(single_line, (0, y_offset - 20))
        
        pygame.draw.rect(screen, rand_color, (0, 580, WIDTH, 200))

        if (pygame.time.get_ticks() // 20) % 2 == 0:
=======
    # Flashing prompt render
    prompt_text = text_font.render("Press any key to continue", True, WHITE)

    # Get title rectangle and center it
    title_rect = title.get_rect(center=(WIDTH // 2, 15))

    running = True
    while running:
        screen.fill(OLD_BLUE)  # Set background to dark blue

        # Draw title
        screen.blit(title, title_rect)
        
         # Draw a horizontal line under the title
        line_y = title_rect.bottom + 8  # 8 pixels below the title
        pygame.draw.line(screen, GRAY, (0, line_y), (WIDTH, line_y), 1) # Syntax: surface, color, start_pos, end_pos, width

         # Draw paragraph 1
        y_offset = line_y + 10  # Start text below the line
        for line in paragraph_text1:
            rendered_line = text_font.render(line, True, GRAY)
            screen.blit(rendered_line, (2, y_offset))  # Start text at x=2
            y_offset += 20  # Move down for the next line

        # Draw volumes with square bullets
        for i, name in enumerate(kroz_volumes):
            y_pos = start_y + i * line_spacing
            pygame.draw.rect(screen, WHITE, (start_x, y_pos , bullet_size, bullet_size))  # parameters: location, colour, x, y, width, height
            text_surface = text_font.render(name, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))  # Adjust text position

        # Draw paragraph 2
        y_offset = 380  # Start text below list of volumes
        for line in paragraph_text2:
            rendered_line = text_font.render(line, True, GRAY)
            screen.blit(rendered_line, (2, y_offset))  # Start text at x=2, y_offset
            y_offset += 20  # Move down for the next line
        
        # Yellow paragraph
        y_offset = 480
        for line in check_info:
            rendered_line = text_font.render(line, True, YELLOW)
            screen.blit(rendered_line, (320, y_offset))  # Start text at x=320, y_offset
            y_offset += 20  # Move down for the next line

        # White text
        single_line = text_font.render("Address is always valid!", True, WHITE) # Antialias enable
        screen.blit(single_line, (0, y_offset-20))  # Start text at x=0, y_offset

        pygame.draw.rect(screen, rand_color, (0, 580, WIDTH, 200)) # Red rectangle on bottom of screen

        # Flashing prompt logic
        if (pygame.time.get_ticks() // 500) % 2 == 0: # Alternate between even and odd every 0.5 seconds
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/game_info.py
            screen.blit(prompt_text, (WIDTH // 2 - 120, HEIGHT - 15))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
<<<<<<< HEAD:Cycles/Arch Spike/screens/game_info.py
                return
            elif event.type == pygame.KEYDOWN:
                running = False

        clock.tick(60)
    # Do not call pygame.quit() here; main will handle quitting.
=======
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
    pygame.quit()
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/game_info.py
