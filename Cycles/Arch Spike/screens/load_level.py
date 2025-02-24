import pygame
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

    # Font render
    title_surface = title_font.render("KINGDOM OF KROZ II", True, WHITE)
    subtext1 = text_font.render("Copyright (c) 1990 Apogee Softwate Productions", True, BROWN)
    subtext2 = text_font.render("Version 2.0 -- by Scott Miller", True, BROWN)
    selector = text_font.render("Your choice (B, I, M, O, A)?", True, WHITE)

    # Center all the text on screen
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
    }

    # Cursor properties
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

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
            screen.blit(first_letter_surface, first_rect)
            screen.blit(rest_surface, rest_rect)
            y_offset2 += 50

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
