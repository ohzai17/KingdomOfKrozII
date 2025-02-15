import pygame

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
    title_font = pygame.font.Font("screens/assets/PressStart2P.ttf", set_title_font)
    text_font = pygame.font.Font("screens/assets/PressStart2P.ttf", set_text_font)

    # Render texts
    title_text = title_font.render("KINGDOM OF KROZ II", True, ROYAL_BLUE)
    question_text = "Is your screen color or monochrome (C/M)? C"
    text_surface = text_font.render(question_text, True, WHITE)

    # Set up cursor properties and timer event for blinking
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

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
                elif event.key == pygame.K_m:
                    user_input = "M"
                    running = False

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
