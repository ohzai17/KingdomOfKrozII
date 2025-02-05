import pygame

<<<<<<< HEAD:Cycles/Arch Spike/screens/color.py
def choose_color_mode(screen):
    # Use the dimensions of the passed screen
    WIDTH, HEIGHT = screen.get_size()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ROYAL_BLUE = (65, 105, 225)
    CURSOR_COLOR = WHITE

    # Set up fonts
    set_title_font = WIDTH // 50
    set_text_font = WIDTH // 80
    title_font = pygame.font.Font("screens/assets/PressStart2P-Regular.ttf", set_title_font)
    text_font = pygame.font.Font("screens/assets/PressStart2P-Regular.ttf", set_text_font)

    # Render texts
=======
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
    title_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 16)  # Larger font for title
    text_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 10)  # Default font

    # Text rendering
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/color.py
    title_text = title_font.render("KINGDOM OF KROZ II", True, ROYAL_BLUE)
    question_text = "Is your screen color or monochrome (C/M)? C"
    text_surface = text_font.render(question_text, True, WHITE)

<<<<<<< HEAD:Cycles/Arch Spike/screens/color.py
    # Set up cursor properties and timer event for blinking
=======
    # Cursor properties
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/color.py
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

<<<<<<< HEAD:Cycles/Arch Spike/screens/color.py
    # Calculate positions for title and question
    title_x = WIDTH // 2 - title_text.get_width() // 2
    title_y = HEIGHT // 4 - 120
    text_x = WIDTH // 2 - text_surface.get_width() // 2
    text_y = HEIGHT // 2 - 60

    # Determine the position of the blinking cursor (over the "C")
    c_surface = text_font.render("C", True, BLACK)
    c_rect = c_surface.get_rect(topleft=(text_x + text_surface.get_width() - 10, text_y))

    user_input = None
    running = True
    clock = pygame.time.Clock()  # To control the frame rate

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                user_input = None  # Let the main function handle quitting if needed
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    user_input = "C"
                    running = False
=======
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
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/color.py
                elif event.key == pygame.K_m:
                    user_input = "M"
                    running = False

<<<<<<< HEAD:Cycles/Arch Spike/screens/color.py
        # Draw everything on the provided screen
        screen.fill(BLACK)
        screen.blit(title_text, (title_x, title_y))
        screen.blit(text_surface, (text_x, text_y))
        if cursor_visible:
            pygame.draw.rect(screen, CURSOR_COLOR, c_rect)
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    # Do not call pygame.quit() here; let the main program handle it.
    return user_input
=======
    pygame.quit()
    return user_input  # This was missing before!
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/color.py
