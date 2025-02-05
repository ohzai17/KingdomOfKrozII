import pygame
<<<<<<< HEAD:Cycles/Arch Spike/screens/title.py
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
=======

def title(color_mode):
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Load the Kroz logo with transparency
    logo = pygame.image.load("screens/assets/kroz_logo.png").convert_alpha()

    # Resize the logo before applying color change (to desired width and height)
    desired_width = 700  # Set your desired width here
    aspect_ratio = logo.get_height() / logo.get_width()
    desired_height = int(desired_width * aspect_ratio)

    # Resize the logo to keep the aspect ratio
    logo = pygame.transform.scale(logo, (desired_width, desired_height))

    # Colors to cycle through (only used in color mode)
    color_list = [
        (255, 0, 0),      # Red
        (255, 255, 255),  # White
        (169, 169, 169),  # Grey
        (255, 0, 255),    # Magenta
        (173, 216, 230),  # Light Blue
        (0, 255, 255),    # Cyan
        (0, 0, 255),      # Blue
        (255, 165, 0)     # Orange
    ]

    time_elapsed = 0

    # Function to apply a static bright grayscale filter to the image
    def apply_grayscale(image):
        grayscale_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        for x in range(image.get_width()):
            for y in range(image.get_height()):
                r, g, b, a = image.get_at((x, y))
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                gray = min(255, gray + 100)
                grayscale_image.set_at((x, y), (gray, gray, gray, a))
        return grayscale_image

    # Function to change the color of the image by cycling through the colors
    def change_color(image, time):
        if color_mode == "M":
            return apply_grayscale(image)
        else:
            color_index = (time // 100) % len(color_list)
            current_color = color_list[color_index]
            color_filter = pygame.Surface(image.get_size())
            color_filter.fill(current_color)
            colorized_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
            colorized_image.blit(image, (0, 0))
            colorized_image.blit(color_filter, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            return colorized_image

    # Load custom fonts
    font_white = pygame.font.Font("screens/assets/PressStart2P.ttf", 12)
    font_yellow = pygame.font.Font("screens/assets/PressStart2P.ttf", 10)
    font_cyan = pygame.font.Font("screens/assets/PressStart2P.ttf", 10)

    # Text to display
    text_white = "Apogee Software Presents"
    text_yellow_1 = "KINGDOM OF KROZ II -- UPDATED VOLUME THREE OF THE KROZ SERIES"
    text_yellow_2 = "Copyright (C) 1990 Scott Miller"
    text_yellow_3 = "User-Supported Software -- $7.50 Registration Fee Required"
    text_cyan = "Press any key to continue."

    # Adjust text color based on mode
    if color_mode == "M":
        yellow_color = (255, 255, 255)
        cyan_color = (255, 255, 255)
    else:
        yellow_color = (255, 255, 0)
        cyan_color = (0, 255, 255)

    # Render the text surfaces
    text_white_surface = font_white.render(text_white, True, (255, 255, 255))
    text_yellow_1_surface = font_yellow.render(text_yellow_1, True, yellow_color)
    text_yellow_2_surface = font_yellow.render(text_yellow_2, True, yellow_color)
    text_yellow_3_surface = font_yellow.render(text_yellow_3, True, yellow_color)
    text_cyan_surface = font_cyan.render(text_cyan, True, cyan_color)

    # Main loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        time_elapsed += 1
        colorized_logo = change_color(logo, time_elapsed)

        # Get logo position
        logo_rect = colorized_logo.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 40))
        screen.blit(colorized_logo, logo_rect)

        # Draw text
        text_white_rect = text_white_surface.get_rect(center=(WIDTH // 2, 30))
        screen.blit(text_white_surface, text_white_rect)
        text_yellow_1_rect = text_yellow_1_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        text_yellow_2_rect = text_yellow_2_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
        text_yellow_3_rect = text_yellow_3_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 180))
        screen.blit(text_yellow_1_surface, text_yellow_1_rect)
        screen.blit(text_yellow_2_surface, text_yellow_2_rect)
        screen.blit(text_yellow_3_surface, text_yellow_3_rect)
        text_cyan_rect = text_cyan_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 240))
        screen.blit(text_cyan_surface, text_cyan_rect)
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/title.py

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
<<<<<<< HEAD:Cycles/Arch Spike/screens/title.py
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    running = False
                    
=======
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False

    pygame.quit()
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/title.py
