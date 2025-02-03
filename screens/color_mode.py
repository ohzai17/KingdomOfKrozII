import pygame

def choose_color_mode():
    pygame.init()
    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ROYAL_BLUE = (65, 105, 225)  # Royal blue
    CURSOR_COLOR = WHITE

    # Font setup
    title_font = pygame.font.Font("assets/PressStart2P.ttf", 16)  # Larger font for title
    text_font = pygame.font.Font("assets/PressStart2P.ttf", 10)  # Default font

    # Text rendering
    title_text = title_font.render("KINGDOM OF KROZ II", True, ROYAL_BLUE)
    question_text = "Is your screen color or monochrome (C/M)? C"
    text_surface = text_font.render(question_text, True, WHITE)

    # Cursor properties
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

    # Get text positions
    title_x = WIDTH // 2 - title_text.get_width() // 2
    title_y = HEIGHT // 4 - 120  # Slightly above the center
    text_x = WIDTH // 2 - text_surface.get_width() // 2
    text_y = HEIGHT // 2 - 60

    # Get position of blinking cursor (over "C")
    c_surface = text_font.render("C", True, BLACK)  # "Erase" C when cursor is visible
    c_rect = c_surface.get_rect(topleft=(text_x + text_surface.get_width() - 10, text_y))  # Shifted 5px right

    # Variable to store user input
    user_input = None  # This will store "C" or "M"

    # Main loop
    running = True
    while running:
        screen.fill(BLACK)  # Set background to black

        # Draw title centered at the top
        screen.blit(title_text, (title_x, title_y))

        # Draw question text
        screen.blit(text_surface, (text_x, text_y))

        # Blinking cursor over "C"
        if cursor_visible:
            pygame.draw.rect(screen, CURSOR_COLOR, c_rect)  # Cover "C" with white block

        pygame.display.flip()  # Update the display

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  # Ensure program exits cleanly
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible  # Toggle cursor visibility
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    user_input = "C"  # Store user choice
                    running = False  # Exit loop
                elif event.key == pygame.K_m:
                    user_input = "M"
                    running = False

    pygame.quit()
    return user_input  # This was missing before!