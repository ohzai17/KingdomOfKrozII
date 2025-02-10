import pygame
from functions import *

# From KINGDOM3.INC (line 64)

def title(screen, color_mode): 

    # Use the dimensions of the passed screen
    WIDTH, HEIGHT = screen.get_size()

    # Logo setup
    logo = pygame.image.load("screens/assets/kroz_logo.png").convert_alpha()
    logo_width = 700
    aspect_ratio = logo.get_height() / logo.get_width()
    height = int(logo_width * aspect_ratio)
    logo = pygame.transform.scale(logo, (logo_width, height)) # Algorithm to keep aspect ratio

    # Fonts
    title_font = pygame.font.Font("screens/assets/PressStart2P - Regular.ttf", 12)
    text_font = pygame.font.Font("screens/assets/PressStart2P - Regular.ttf", 10)

    if color_mode == "M":
        subtext_color = WHITE
        footer_color = WHITE
    else:
        subtext_color = YELLOW
        footer_color = AQUA

    # Text rendering
    title_text = title_font.render("Apogee Software Presents", True, WHITE)
    subtext_1 = text_font.render("KINGDOM OF KROZ II -- UPDATED VOLUME THREE OF THE KROZ SERIES", True, subtext_color)
    subtext_2 = text_font.render("Copyright (C) 1990 Scott Miller", True, subtext_color)
    subtext_3 = text_font.render("User-Supported Software -- $7.50 Registration Fee Required", True, subtext_color)
    footer_text = text_font.render("Press any key to continue.", True, footer_color)

    # Positioning
    title_text_x, title_text_y = WIDTH // 2 - title_text.get_width() // 2, 30
    subtext_1_x, subtext_1_y = WIDTH // 2 - subtext_1.get_width() // 2, HEIGHT // 2 + 100
    subtext_2_x, subtext_2_y = WIDTH // 2 - subtext_2.get_width() // 2, subtext_1_y + subtext_1.get_height() + 40
    subtext_3_x, subtext_3_y = WIDTH // 2 - subtext_3.get_width() // 2, subtext_2_y + subtext_2.get_height() + 40
    footer_text_x, footer_text_y = WIDTH // 2 - footer_text.get_width() // 2, subtext_3_y + subtext_3.get_height() + 60

    time_elapsed = 0
    running = True
    
    while running:
        screen.fill(BLACK)

        time_elapsed += 1 

        # Logo positioning
        colorized_logo = change_logo_color(logo, time_elapsed, color_mode)
        logo_x, logo_y = WIDTH // 2 - colorized_logo.get_width() // 2, HEIGHT // 3 - 100

        # Draw text
        screen.blit(colorized_logo, (logo_x, logo_y))
        screen.blit(title_text, (title_text_x, title_text_y))
        screen.blit(subtext_1, (subtext_1_x, subtext_1_y))
        screen.blit(subtext_2, (subtext_2_x, subtext_2_y))
        screen.blit(subtext_3, (subtext_3_x, subtext_3_y))
        screen.blit(footer_text, (footer_text_x, footer_text_y))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    running = False
                    