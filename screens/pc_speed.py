import pygame
from functions import *

# From KINGDOM4.INC (line 87)

def choose_pc_speed(color_mode): 
    pygame.init()

    # Screen setup
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Fonts
    title_font = pygame.font.Font("assets/PressStart2P - Regular.ttf", 16)
    heading_font = pygame.font.Font("assets/PressStart2P - Regular.ttf", 10)
    subtext_font = pygame.font.Font("assets/PressStart2P - Regular.ttf", 9)

    title_color = BLACK if color_mode == "M" else BLUE

    # Text rendering
    title_text = title_font.render("KINGDOM OF KROZ II", True, title_color)
    heading_text = heading_font.render("Slow or Fast PC (S/F)? S", True, WHITE)
    subtext_1 = subtext_font.render("If you have an older PC (like an XT model) choose \"S\" for Slow.", True, GRAY)
    subtext_2 = subtext_font.render("If you have a PC AT, 80386 chip, etc., choose \"F\" for Fast.", True, GRAY)
    subtext_3 = subtext_font.render("(Default = Slow)", True, GRAY)

    # Cursor setup
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)

    # Positioning
    title_text_x, title_text_y = WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4 - 120
    heading_text_x, heading_text_y = WIDTH // 2 - heading_text.get_width() // 2, HEIGHT // 2 - 60
    subtext_1_x, subtext_1_y = WIDTH // 2 - subtext_1.get_width() // 2, heading_text_y + heading_text.get_height() + 30
    subtext_2_x, subtext_2_y = WIDTH // 2 - subtext_2.get_width() // 2, subtext_1_y + subtext_1.get_height() + 15
    subtext_3_x, subtext_3_y = WIDTH // 2 - subtext_3.get_width() // 2, subtext_2_y + subtext_2.get_height() + 15

    # Cursor positioning
    cursor = heading_font.render("S", True, BLACK)
    cursor = cursor.get_rect(topleft=(heading_text_x + heading_text.get_width() - 10, heading_text_y))

    user_input = ""
    running = True

    while running:
        screen.fill(BLACK)

        # Draw text
        screen.blit(title_text, (title_text_x, title_text_y))
        screen.blit(heading_text, (heading_text_x, heading_text_y))
        screen.blit(subtext_1, (subtext_1_x, subtext_1_y))
        screen.blit(subtext_2, (subtext_2_x, subtext_2_y))
        screen.blit(subtext_3, (subtext_3_x, subtext_3_y))

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
                        case pygame.K_s:
                            user_input = "S"
                            running = False
                        case pygame.K_f:
                            user_input = "F"
                            running = False
    pygame.quit()
    return user_input