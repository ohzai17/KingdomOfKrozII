import pygame
<<<<<<< HEAD:Cycles/Arch Spike/screens/load_level.py
import color_mode
from functions import *

def load(screen, color):
    # Use the existing main window
    WIDTH, HEIGHT = screen.get_size()

    if color == "M":  # change to grayscale
        RED = (128, 128, 128)
        GREEN = (128, 128, 128)
        BLUE = (128, 128, 128)
        YELLOW = (255, 255, 255)
        CYAN = (128, 128, 128)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BROWN = (128, 128, 128)
    else:
        RED = (144, 13, 13)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        CYAN = (0, 255, 255)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BROWN = (139, 69, 19)

    # Store user input
    user_input2 = ""

    # Font setup
    title_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 20)  # Larger font for title
    text_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 16)   # Default font

    # Paragraph 
    para1 = [
        "THIS GAME MAY BE DISTRIBUTED BY SHAREWARE OR PUBLIC DOMAIN LIBRARIES,",
        " OR BULLETING BOARD SYSTEMS. NO NEED TO INQUIRE FOR WRITTEN PERMISSION."
=======
from gen_functions import *

def load():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Store user input
    user_input = ""

    # Font setup
    title_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 20)  # Larger font for title
    text_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 16)  # Default font


    # Paragraph 
    para1 = ["THIS GAME MAY BE DISTRIBUTED BY SHAREWARE OR PUBLIC DOMAIN LIBRARIES,",
    " OR BULLETING BOARD SYSTEMS. NO NEED TO INQUIRE FOR WRITTEN PERMISSION."
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/load_level.py
    ]
    
    # List of choices
    choice_list = [
        "Begin your descent into Kroz...",
        "Instructions",
        "Marketing Kroz",
        "Story behind Kroz",
        "Original Kroz Games",
        "About the Author"
    ]

<<<<<<< HEAD:Cycles/Arch Spike/screens/load_level.py
    # Font render
    title_surface = title_font.render("KINGDOM OF KROZ II", True, WHITE)
=======

    # Font render
    title = title_font.render("KINGDOM OF KROZ II", True, WHITE)
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/load_level.py
    subtext1 = text_font.render("Copyright (c) 1990 Apogee Softwate Productions", True, BROWN)
    subtext2 = text_font.render("Version 2.0 -- by Scott Miller", True, BROWN)
    selector = text_font.render("Your choice (B, I, M, O, A)?", True, WHITE)

    # Center all the text on screen
<<<<<<< HEAD:Cycles/Arch Spike/screens/load_level.py
    title_rect = title_surface.get_rect(midtop=(WIDTH // 2, 20))
    subtext1_rect = subtext1.get_rect(midtop=(WIDTH // 2, 75))
    subtext2_rect = subtext2.get_rect(midtop=(WIDTH // 2, 115))
    selector_x = WIDTH // 2 - 130  # For blinking cursor mechanics
    selector_y = 550

    # Keymap to prevent a long list of elif statements
    key_map = {
        pygame.K_b: "b",
        pygame.K_i: "i",
        pygame.K_m: "m",
        pygame.K_o: "o",
        pygame.K_a: "a"
=======
    title_rect = title.get_rect(midtop=(WIDTH // 2, 20))
    subtext1_rect = subtext1.get_rect(midtop=(WIDTH // 2, 75))
    subtext2_rect = subtext2.get_rect(midtop=(WIDTH // 2, 115))
    selector_x = WIDTH // 2 - 130 # Different mechanics, to have it work with blinking cursor
    selector_y = 550

    # Keymap to prevent a long line of elif statements
    key_map = {
    pygame.K_b: "b",
    pygame.K_i: "i",
    pygame.K_m: "m",
    pygame.K_o: "o",
    pygame.K_a: "a"
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/load_level.py
    }

    # Cursor properties
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

<<<<<<< HEAD:Cycles/Arch Spike/screens/load_level.py
    # Main loop
    running = True
    while running:
        screen.fill((0, 0, 0))

        # Draw title and subtext
        screen.blit(title_surface, title_rect)
        screen.blit(subtext1, subtext1_rect)
        screen.blit(subtext2, subtext2_rect)

        # Position and draw paragraphs
        y_offset1 = 160  # Start after subtext1
        for line in para1:
            line_surface = text_font.render(line, True, (0, 255, 0))  # GREEN
            line_rect = line_surface.get_rect(midtop=(WIDTH // 2, y_offset1))
            screen.blit(line_surface, line_rect)
            y_offset1 += 20

        # Draw a horizontal line under the paragraphs
        line_y = y_offset1 + 8
        pygame.draw.line(screen, RED, (0, line_y), (WIDTH, line_y), 1)

        # Draw list of choices
        y_offset2 = y_offset1 + 65
        for choice in choice_list:
            first_letter_surface = text_font.render(choice[0], True, YELLOW)
            rest_surface = text_font.render(choice[1:], True, CYAN)
            first_rect = first_letter_surface.get_rect(bottomleft=(WIDTH // 2 - 100, y_offset2))
            rest_rect = rest_surface.get_rect(bottomleft=(first_rect.right, y_offset2))
=======
    # Get position of blinking cursor (over "B")
    s_surface = text_font.render("B", True, BLACK)  
    s_rect = s_surface.get_rect(topleft=(selector_x + selector.get_width() + 8, selector_y))


    # Main loop
    running = True
    while running:

        screen.fill(BLACK)

        # Draw title , and subtext
        screen.blit(title, title_rect)
        screen.blit(subtext1, subtext1_rect)
        screen.blit(subtext2, subtext2_rect)

        # loop to position paragraphs on screen
        y_offset1 = 160 # used for placing paragraph after subtext1
        for line in para1:
           line_surface = text_font.render(line, True, GREEN)
           line_rect = line_surface.get_rect(midtop=(WIDTH // 2, y_offset1))
           screen.blit(line_surface, line_rect)
           y_offset1 += 20

        # Draw a horizontal line under the paragraphs
        line_y = y_offset1 + 8  # 8 pixels below the paragraph
        pygame.draw.line(screen, RED, (0, line_y), (WIDTH, line_y), 1) # Syntax: surface, color, start_pos, end_pos, width

        # Loop to display list of choices
        y_offset2 = y_offset1 + 65
        for choice in choice_list:
            first_letter_surface = text_font.render(choice[0], True, YELLOW)  # Render first letter in yellow
            rest_surface = text_font.render(choice[1:], True, CYAN)  # Render the rest in cyan
            
            first_rect = first_letter_surface.get_rect(bottomleft=(WIDTH // 2 - 100, y_offset2))
            rest_rect = rest_surface.get_rect(bottomleft=(first_rect.right, y_offset2))  # Position after the first letter
            
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/load_level.py
            screen.blit(first_letter_surface, first_rect)
            screen.blit(rest_surface, rest_rect)
            y_offset2 += 50

<<<<<<< HEAD:Cycles/Arch Spike/screens/load_level.py
        # Draw elongated blue rectangle and selector text
        pygame.draw.rect(screen, BLUE, (selector_x, selector_y, 300, 22))
        screen.blit(selector, (selector_x, selector_y))

        # Draw blinking "B"
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, (selector_x + selector.get_width() + 4, selector_y, 16, 22))
            blinking_b = text_font.render("B", True, BLUE)
        else:
            blinking_b = text_font.render("B", True, WHITE)
        screen.blit(blinking_b, (selector_x + selector.get_width() + 8, selector_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.VIDEORESIZE: 
                WIDTH, HEIGHT = event.size
                # Update text scaling if needed using your scale functions.
                title_surface = scale_title(title_surface, WIDTH, HEIGHT)
                subtext1 = scale_text(subtext1, WIDTH, HEIGHT)

            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    user_input2 = key_map[event.key]
                    running = False

        pygame.display.update()

    return user_input2
=======
        # Elongated blue rectangle
        pygame.draw.rect(screen, BLUE, (selector_x, selector_y, 300, 22)) # Red rectangle on bottom of screen
        
        # Display choice options
        screen.blit(selector,(selector_x,selector_y))

        # Alternate between white and blue for the rectangle and text
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, (selector_x + selector.get_width() + 4, selector_y, 16, 22))  # White rectangle
            blinking_b = text_font.render("B", True, BLUE)  # "B" turns blue
        else:
            blinking_b = text_font.render("B", True, WHITE)  # "B" turns white

        # Draw blinking "B"
        screen.blit(blinking_b, (selector_x + selector.get_width() + 8, selector_y))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible  # Toggle cursor visibility
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    user_input = key_map[event.key]  # Set user input based on the key pressed
                    running = False  # Exit loop after valid input
    pygame.quit()
    return user_input # Return the user input
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/load_level.py
