import pygame
from game_functions import *

# From KINGDOM4.INC (line 66)

def choose_color_mode(screen):
    
    # Use the dimensions of the passed screen
    WIDTH, HEIGHT = screen.get_size()

    # Fonts
    title_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 16)
    heading_font = pygame.font.Font("screens/assets/PressStart2P.ttf", 10)

    # Text rendering 
    title_text = title_font.render("KINGDOM OF KROZ II", True, BLUE)
    heading_text = heading_font.render("Is your screen color or monochrome (C/M)? C", True, WHITE)

    # Cursor setup
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)

    # Positioning
    title_text_x, title_text_y = WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4 - 120
    heading_text_x, heading_text_y = WIDTH // 2 - heading_text.get_width() // 2, HEIGHT // 2 - 60

    # Cursor positioning
    cursor = heading_font.render("C", True, BLACK)
    cursor = cursor.get_rect(topleft=(heading_text_x + heading_text.get_width() - 10, heading_text_y))

    user_input = ""
    running = True
    
    while running:
        screen.fill(BLACK)

        # Draw text
        screen.blit(title_text, (title_text_x, title_text_y))
        screen.blit(heading_text, (heading_text_x, heading_text_y))

        # Draw cursor
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, cursor)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case _ if event.type == cursor_timer:
                    cursor_visible = not cursor_visible
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_c:
                            user_input = "C"
                            running = False
                        case pygame.K_m:
                            user_input = "M"
                            running = False
    return user_input