# Missing features:
# - title monochrome mode

import pygame

def choose_pc_speed():
    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (169, 169, 169)  # Gray for subtext
    ROYAL_BLUE = (65, 105, 225)  # Royal blue

    # Font setup
    title_font = pygame.font.Font("screens_ohzai/assets/PressStart2P.ttf", 16)  # Larger font for title
    text_font = pygame.font.Font("screens_ohzai/assets/PressStart2P.ttf", 10)  # Default font for question
    subtext_font = pygame.font.Font("screens_ohzai/assets/PressStart2P.ttf", 9)  # Smaller font for subtext

    # Text rendering
    title_text = title_font.render("KINGDOM OF KROZ II", True, ROYAL_BLUE)
    question_text = "Slow or Fast PC (S/F)? S"
    text_surface = text_font.render(question_text, True, WHITE)

    # Subtext rendering
    subtext_1 = subtext_font.render("If you have an older PC (like an XT model) choose \"S\" for Slow.", True, GRAY)
    subtext_2 = subtext_font.render("If you have a PC AT, 80386 chip, etc., choose \"F\" for Fast.", True, GRAY)
    subtext_3 = subtext_font.render("(Default = Slow)", True, GRAY)

    # Cursor properties
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

    # Get text positions
    title_x = WIDTH // 2 - title_text.get_width() // 2
    title_y = HEIGHT // 4 - 120  # Slightly above the center
    text_x = WIDTH // 2 - text_surface.get_width() // 2
    text_y = HEIGHT // 2 - 60

    # Subtext positions (centered under the main question)
    subtext_1_x = WIDTH // 2 - subtext_1.get_width() // 2
    subtext_1_y = text_y + text_surface.get_height() + 30
    subtext_2_x = WIDTH // 2 - subtext_2.get_width() // 2
    subtext_2_y = subtext_1_y + subtext_1.get_height() + 15
    subtext_3_x = WIDTH // 2 - subtext_3.get_width() // 2
    subtext_3_y = subtext_2_y + subtext_2.get_height() + 15

    # Get position of blinking cursor (over "S")
    s_surface = text_font.render("S", True, BLACK)  # "Erase" S when cursor is visible
    s_rect = s_surface.get_rect(topleft=(text_x + text_surface.get_width() - 10, text_y))  # Shifted 5px right

    # Variable to store user input
    user_input = ""

    # Main loop
    running = True
    while running:
        screen.fill(BLACK)  # Set background to black

        # Draw title centered at the top
        screen.blit(title_text, (title_x, title_y))

        # Draw question text
        screen.blit(text_surface, (text_x, text_y))

        # Blinking "S" over the question text
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, s_rect)  # Cover "S" with white block

        # Draw subtext centered below the question
        screen.blit(subtext_1, (subtext_1_x, subtext_1_y))
        screen.blit(subtext_2, (subtext_2_x, subtext_2_y))
        screen.blit(subtext_3, (subtext_3_x, subtext_3_y))

        pygame.display.flip()  # Update the display

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible  # Toggle cursor visibility
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    user_input = "S"  # Set the user input to 'S'
                    running = False  # Exit loop after valid input
                elif event.key == pygame.K_f:
                    user_input = "F"  # Set the user input to 'F'
                    running = False  # Exit loop after valid input

        # Only accept S or F, nothing else is processed

    pygame.quit()
    return user_input  
