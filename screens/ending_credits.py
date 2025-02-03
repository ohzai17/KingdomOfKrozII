import pygame

def ending_creds():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Colors
    GREY = (200, 200, 200)
    WHITE = (255, 255, 255)

    # Font setup
    text_font = pygame.font.Font("assets/PressStart2P.ttf", 10)  # Default font

    # font render
    title = text_font.render("KINGDOM OF KROZ II", True, GREY)
    subtitle = text_font.render("An Apogee Software Production", True, GREY)
    subtitle2 = text_font.render("Other great games available from Scott Miller:", True, GREY)

    # list of paragraphs
    paragraphs_1 = [
        "Six more Kroz games! KINGDOM OF KROZ I, CAVERNS OF KROZ, DUNGEONS OF KROZ,",
        "   RETURN OF KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.",
        "   Each volume is just $7.50, or order all six for $35",     
    ]

    paragraphs_2 = [
        "SUPERNOVA - Explore a galaxy and save a planet from an exploding star!",
        "   An epic adventure rated by Shareware Magazine as one of the best games",
        "   ever! Highly advanced game has graphics, sound effects galore, clue",
        "   command, and dozens of unique features. ($10)",
        "",
        "BEYOND THE TITANIC - A fantastic adventure of exploration and survival.",
        "   What really happened? Sound effects and 16 color screens. ($8)",
        "",
        "WORD WHIZ - New game that challenges your knowledge of the English",
        "   language. Fun to play, yet very educational, too. ($5)",
    ]

    paragraphs_3 = [
        "THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best",
        "   levels yet! Built-in contest! New features galore. ($20)"        
    ]

    start_x, start_y = 30, 240  # Starting position
    line_spacing = 25           # Spacing between lines
    bullet_size = 8             # Size of the square bullet

    # Get title rectangle and center it
    text_rect = title.get_rect(center=(WIDTH // 2, 30))

    # Event loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(title, text_rect)  # Draw the title
        screen.blit(subtitle, (250, 50)) 
        screen.blit(subtitle2, (0, 110)) 
        
        # Draw volumes with square bullets
        y_pos = 130
        for text in paragraphs_1:
            y_pos += 20
            if text and not text.startswith(' '):
                pygame.draw.rect(screen, WHITE, (start_x, y_pos , bullet_size, bullet_size))  # parameters: location, colour, x, y, width, height
            text_surface = text_font.render(text, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))

        for i, text in enumerate(paragraphs_2):
            y_pos = start_y + i * line_spacing # Square, y coordinate
            if text and not text.startswith(' '):
                pygame.draw.rect(screen, GREY, (start_x, y_pos , bullet_size, bullet_size))  # parameters: location, colour, x, y, width, height
            text_surface = text_font.render(text, False, GREY)
            screen.blit(text_surface, (start_x + 20, y_pos))

        y_pos = 500
        for text in paragraphs_3:
            y_pos += 20
            if text and not text.startswith(' '):
                pygame.draw.rect(screen, WHITE, (start_x, y_pos , bullet_size, bullet_size))  # parameters: location, colour, x, y, width, height
            text_surface = text_font.render(text, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))

        pygame.display.flip()  # Update the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit loop if user closes the window

    pygame.quit()

# Run the function
ending_creds()
