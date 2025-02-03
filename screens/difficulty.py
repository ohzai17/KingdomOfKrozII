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

def information_screen():
    pygame.init()
    
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kingdom of Kroz II")

    # Colors
    BLUE = (8, 4, 180)
    RED = (188, 4, 4)
    WHITE = (255, 255, 255)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 65, 76)

    title_colors = [WHITE, CYAN, GREEN, YELLOW]  # Colors for cycling
    
    title_font = pygame.font.Font("assets/PressStart2P.ttf", 12)
    text_font = pygame.font.Font("assets/PressStart2P.ttf", 12)
    info_font = pygame.font.Font("assets/PressStart2P.ttf", 10)
    
    subheading1 = text_font.render("An Apogee Software Production", True, WHITE)
    subheading2 = text_font.render("Created by Scott Miller", True, WHITE)
    
    description_text = "Kingdom of Kroz is a game of adventure, exploration and survival. You are a fearless archaeologist in search of the Magical Amulet, hidden somewhere deep in the vast and dangerous underground kingdom. You enter the kingdom through a secret tunnel and ignite your brass lantern. Your only protection is a worn leather whip and your ingenuity. Sweat beading on your forehead, you embark on a journey that may be your last..."
    
    instructions_lines = [
        "Use the cursor keys to move yourself through the kingdom.",
        "Use your whip (press W) to destroy all nearby creatures.",
        "You are on your own to discover what other mysteries await--some",
        "helpful, others deadly..."
    ]
    
    player_level_text = "Are you a Novice, an Experienced, or an Advanced player?"
    player_level_surface = info_font.render(player_level_text, True, YELLOW)
    
    title_y = 20
    subheading1_y = 100
    subheading2_y = subheading1_y + 30
    
    max_width = WIDTH - 40
    description_lines = wrap_text(description_text, info_font, max_width)
    
    description_y = subheading2_y + 50
    instructions_y = description_y + len(description_lines) * 15 + 90
    player_level_y = instructions_y + len(instructions_lines) * 15 + 110
    
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)
    cursor_visible = True
    cursor_x = WIDTH // 2 + player_level_surface.get_width() // 2 + 3
    cursor_y = player_level_y - 2
    
    running = True
    player_input = ''
    while running:
        screen.fill(BLUE)
        
        time = pygame.time.get_ticks()
        color_index = (time // 50) % len(title_colors)
        title_color = title_colors[color_index]
        
        title_text = title_font.render("KINGDOM OF KROZ II", True, title_color)
        title_x = WIDTH // 2 - title_text.get_width() // 2
        
        title_rect = pygame.Rect(title_x - 10, title_y - 12, title_text.get_width() + 20, title_text.get_height() + 20)
        pygame.draw.rect(screen, RED, title_rect)
        
        screen.blit(title_text, (title_x, title_y))
        screen.blit(subheading1, (WIDTH // 2 - subheading1.get_width() // 2, subheading1_y))
        screen.blit(subheading2, (WIDTH // 2 - subheading2.get_width() // 2, subheading2_y))
        
        for i, line in enumerate(description_lines):
            line_text = info_font.render(line, True, CYAN)
            screen.blit(line_text, (WIDTH // 2 - line_text.get_width() // 2, description_y + i * 20))
        
        for i, line in enumerate(instructions_lines):
            line_text = info_font.render(line, True, GREEN)
            screen.blit(line_text, (WIDTH // 2 - line_text.get_width() // 2, instructions_y + i * 20))
        
        screen.blit(player_level_surface, (WIDTH // 2 - player_level_surface.get_width() // 2, player_level_y))
        
        if cursor_visible:
            pygame.draw.rect(screen, ORANGE, (cursor_x, cursor_y, 8, 15))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  # Return None if the user quits the game
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    player_input = 'N'
                    running = False
                elif event.key == pygame.K_e:
                    player_input = 'E'
                    running = False
                elif event.key == pygame.K_a:
                    player_input = 'A'
                    running = False
    pygame.quit()
    return player_input # Return the player's input