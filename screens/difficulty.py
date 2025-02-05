# Missing features:
# - orange blinking cursor
# - color cycling for title

import pygame

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    
    for word in words:
        test_line = current_line + ' ' + word if current_line else word
        test_width = font.size(test_line)[0]
        
        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

def information_screen(color_mode):
    pygame.init()
    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Colors based on color mode
    if color_mode == "M":
        BG_COLOR = (0, 0, 0)  # Background remains blue
        RECT_COLOR = (169, 169, 169)  # Gray rectangle
        TITLE_FLASH_COLOR = (0, 0, 0)  # Flashing title text in black
        TEXT_COLOR = (169, 169, 169)  # General text in gray
        LEVEL_PROMPT_COLOR = (169, 169, 169)  # "Are you a novice..." in gray
        DIFFICULTY_FLASH_COLOR = (169, 169, 169)  # Flashing difficulty in white
        INSTRUCTIONS_COLOR = (169, 169, 169)  # Instructions in gray
    else:
        BG_COLOR = (8, 4, 180)  # Background remains blue
        RECT_COLOR = (188, 4, 4)  # Red rectangle
        TITLE_FLASH_COLOR = (255, 255, 255)  # Flashing title in cycling colors
        TEXT_COLOR = (0, 255, 255)  # Cyan text
        LEVEL_PROMPT_COLOR = (255, 255, 0)  # "Are you a novice..." in gray
        DIFFICULTY_FLASH_COLOR = (255, 255, 0)  # Flashing difficulty in white
        INSTRUCTIONS_COLOR = (0, 255, 0)  # Instructions in gray


    title_font = pygame.font.Font("assets/PressStart2P.ttf", 12)
    text_font = pygame.font.Font("assets/PressStart2P.ttf", 12)
    info_font = pygame.font.Font("assets/PressStart2P.ttf", 10)
    
    subheading1 = text_font.render("An Apogee Software Production", True, (255, 255, 255))
    subheading2 = text_font.render("Created by Scott Miller", True, (255, 255, 255))
    
    description_text = "Kingdom of Kroz is a game of adventure, exploration and survival. You are a fearless archaeologist in search of the Magical Amulet, hidden somewhere deep in the vast and dangerous underground kingdom. You enter the kingdom through a secret tunnel and ignite your brass lantern. Your only protection is a worn leather whip and your ingenuity. Sweat beading on your forehead, you embark on a journey that may be your last..."
    instructions_lines = [
        "Use the cursor keys to move yourself through the kingdom.",
        "Use your whip (press W) to destroy all nearby creatures.",
        "You are on your own to discover what other mysteries await--some",
        "helpful, others deadly..."
    ]
    
    player_level_surface = info_font.render("Are you a Novice, an Experienced, or an Advanced player?", True, LEVEL_PROMPT_COLOR)
    
    max_width = WIDTH - 40
    description_lines = wrap_text(description_text, info_font, max_width)
    
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)
    cursor_visible = True
    
    flash_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(flash_timer, 250)
    show_text = True
    
    press_any_key_surface = info_font.render("Press any key.", True, (169, 169, 169))
    
    running = True
    player_input = ''
    difficulty_text = ""
    
    while running:
        screen.fill(BG_COLOR)
        
        title_text = title_font.render("KINGDOM OF KROZ II", True, TITLE_FLASH_COLOR)
        title_x = WIDTH // 2 - title_text.get_width() // 2
        title_rect = pygame.Rect(title_x - 10, 20 - 12, title_text.get_width() + 20, title_text.get_height() + 20)
        pygame.draw.rect(screen, RECT_COLOR, title_rect)
        
        screen.blit(title_text, (title_x, 20))
        screen.blit(subheading1, (WIDTH // 2 - subheading1.get_width() // 2, 100))
        screen.blit(subheading2, (WIDTH // 2 - subheading2.get_width() // 2, 130))
        
        y_offset = 180
        for line in description_lines:
            line_text = info_font.render(line, True, TEXT_COLOR)
            screen.blit(line_text, (WIDTH // 2 - line_text.get_width() // 2, y_offset))
            y_offset += 20
        
        for i, line in enumerate(instructions_lines):
            line_text = info_font.render(line, True, INSTRUCTIONS_COLOR)
            screen.blit(line_text, (WIDTH // 2 - line_text.get_width() // 2, y_offset + 30 + i * 20))
        
        if difficulty_text == "":
            screen.blit(player_level_surface, (WIDTH // 2 - player_level_surface.get_width() // 2, y_offset + 170))
        else:
            if show_text:
                difficulty_surface = info_font.render(difficulty_text, True, DIFFICULTY_FLASH_COLOR)
                screen.blit(difficulty_surface, (WIDTH // 2 - difficulty_surface.get_width() // 2, y_offset + 170))
            screen.blit(press_any_key_surface, (WIDTH // 2 - press_any_key_surface.get_width() // 2, y_offset + 240))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == flash_timer:
                if difficulty_text:
                    show_text = not show_text
            elif event.type == pygame.KEYDOWN:
                if difficulty_text == "":
                    if event.key == pygame.K_n:
                        player_input = 'N'
                        difficulty_text = "NOVICE"
                    elif event.key == pygame.K_e:
                        player_input = 'E'
                        difficulty_text = "EXPERIENCED"
                    elif event.key == pygame.K_a:
                        player_input = 'A'
                        difficulty_text = "ADVANCED"
                else:
                    running = False
    
    pygame.quit()
    return player_input
