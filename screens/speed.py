import pygame

def choose_pc_speed(screen):
    # Use the provided main window
    WIDTH, HEIGHT = screen.get_size()

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (169, 169, 169)
    ROYAL_BLUE = (65, 105, 225)

    # Font setup
    title_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 16)
    text_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 10)
    subtext_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 9)

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
    pygame.time.set_timer(cursor_timer, 150)

    # Get text positions
    title_x = WIDTH // 2 - title_text.get_width() // 2
    title_y = HEIGHT // 4 - 120
    text_x = WIDTH // 2 - text_surface.get_width() // 2
    text_y = HEIGHT // 2 - 60

    # Subtext positions
    subtext_1_x = WIDTH // 2 - subtext_1.get_width() // 2
    subtext_1_y = text_y + text_surface.get_height() + 30
    subtext_2_x = WIDTH // 2 - subtext_2.get_width() // 2
    subtext_2_y = subtext_1_y + subtext_1.get_height() + 15
    subtext_3_x = WIDTH // 2 - subtext_3.get_width() // 2
    subtext_3_y = subtext_2_y + subtext_2.get_height() + 15

    # Blinking cursor over "S"
    s_surface = text_font.render("S", True, BLACK)
    s_rect = s_surface.get_rect(topleft=(text_x + text_surface.get_width() - 10, text_y))

    user_input = ""

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(title_text, (title_x, title_y))
        screen.blit(text_surface, (text_x, text_y))
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, s_rect)
        screen.blit(subtext_1, (subtext_1_x, subtext_1_y))
        screen.blit(subtext_2, (subtext_2_x, subtext_2_y))
        screen.blit(subtext_3, (subtext_3_x, subtext_3_y))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    user_input = "S"
                    running = False
                elif event.key == pygame.K_f:
                    user_input = "F"
                    running = False

    return user_input
