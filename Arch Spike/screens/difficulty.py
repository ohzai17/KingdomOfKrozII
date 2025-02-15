import pygame
from functions import *

# From KINGDOM3.INC (line 86)

def choose_difficulty(screen, color_mode): 
    
    # Use the dimensions of the passed screen
    WIDTH, HEIGHT = screen.get_size()

    # Player icon setup
    player_icon = pygame.image.load("screens/assets/player_icon.png")
    player_icon = pygame.transform.scale(player_icon, (20, 20))

    # Fonts
    title_font = pygame.font.Font("screens/assets/PressStart2P - Regular.ttf", 16)
    heading_font = pygame.font.Font("screens/assets/PressStart2P - Regular.ttf", 10)
    subtext_font  = pygame.font.Font("screens/assets/PressStart2P - Regular.ttf", 10)
    footer_font = pygame.font.Font("screens/assets/PressStart2P - Regular.ttf", 10)

    player_icon = apply_grayscale(player_icon) if color_mode == "M" else player_icon

    if color_mode == "M":
        background_color = BLACK  
        subtext_color_1 = GRAY
        subtext_color_2 = GRAY
        header_color = GRAY
        cursor_color = WHITE
        title_text_box_color = GRAY

    else:
        background_color = BLUE  
        subtext_color_1 = AQUA
        subtext_color_2 = LIGHT_GREEN
        header_color = YELLOW
        cursor_color = ORANGE
        title_text_box_color = RED    

    # Text rendering
    heading_text_1 = heading_font.render("An Apogee Software Production", True, WHITE)
    heading_text_2 = heading_font.render("Created by Scott Miller", True, WHITE)
    subtext_1 = subtext_font.render("Kingdom of Kroz is a game of adventure, exploration and survival. You are", True, subtext_color_1 )
    subtext_2 = subtext_font.render("a fearless archaeologist in search of the Magical Amulet, hidden somewhere", True, subtext_color_1 )
    subtext_3 = subtext_font.render("deep in the vast and dangerous underground kingdom. You enter the kingdom", True, subtext_color_1 )
    subtext_4 = subtext_font.render("through a secret tunnel and ignite your brass lantern. Your only protection", True, subtext_color_1 )
    subtext_5 = subtext_font.render("is a worn leather whip and your ingenuity. Sweat beading on your forehead,", True, subtext_color_1 )
    subtext_6 = subtext_font.render("             you embark on a journey that may be your last...             ", True, subtext_color_1 )
    subtext_7 = subtext_font.render("Use the cursor keys to move yourself (  ) through the kingdom.", True, subtext_color_2)
    subtext_8 = subtext_font.render("Use your whip (press W) to destroy all nearby creatures.", True, subtext_color_2)
    subtext_9 = subtext_font.render("You are on your own to discover what other mysteries await--some", True, subtext_color_2)
    subtext_10 = subtext_font.render("helpful, others deadly...", True, subtext_color_2)
    heading_text_3 = heading_font.render("Are you a  ovice, an  xperienced, or an  dvanced player? ", True, header_color)
    heading_text_4 = heading_font.render("          N          E                  A", True, WHITE)
    footer_text = footer_font.render("Press any key. ", True, GRAY)

    # Positioning
    heading_text_1_x, heading_text_1_y = WIDTH // 2 - heading_text_1.get_width() // 2, HEIGHT // 2 - 60
    heading_text_2_x, heading_text_2_y = WIDTH // 2 - heading_text_2.get_width() // 2, heading_text_1_y + heading_text_1.get_height() + 15
    subtext_1_x, subtext_1_y = WIDTH // 2 - subtext_1.get_width() // 2, heading_text_2_y + heading_text_1.get_height() + 30
    subtext_2_x, subtext_2_y = WIDTH // 2 - subtext_2.get_width() // 2, subtext_1_y + subtext_1.get_height() + 15
    subtext_3_x, subtext_3_y = WIDTH // 2 - subtext_3.get_width() // 2, subtext_2_y + subtext_2.get_height() + 15
    subtext_4_x, subtext_4_y = WIDTH // 2 - subtext_4.get_width() // 2, subtext_3_y + subtext_3.get_height() + 15
    subtext_5_x, subtext_5_y = WIDTH // 2 - subtext_5.get_width() // 2, subtext_4_y + subtext_4.get_height() + 15
    subtext_6_x, subtext_6_y = WIDTH // 2 - subtext_6.get_width() // 2, subtext_5_y + subtext_5.get_height() + 15
    subtext_7_x, subtext_7_y = WIDTH // 2 - subtext_7.get_width() // 2, subtext_6_y + subtext_6.get_height() + 30
    subtext_8_x, subtext_8_y = WIDTH // 2 - subtext_8.get_width() // 2, subtext_7_y + subtext_7.get_height() + 15
    subtext_9_x, subtext_9_y = WIDTH // 2 - subtext_9.get_width() // 2, subtext_8_y + subtext_8.get_height() + 15
    subtext_10_x, subtext_10_y = WIDTH // 2 - subtext_10.get_width() // 2, subtext_9_y + subtext_9.get_height() + 15
    heading_text_3_x, heading_text_3_y = WIDTH // 2 - heading_text_3.get_width() // 2, subtext_3_y + subtext_3.get_height() + 30
    heading_text_4_x, heading_text_4_y = WIDTH // 2 - heading_text_4.get_width() // 2, heading_text_3_y + heading_text_3.get_height() + 15
    footer_text_x, footer_text_y = WIDTH // 2 - footer_text.get_width() // 2, subtext_10_y + subtext_10.get_height() + 30

    # Cursor setup
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)

    # Flashing text setup
    flashing_text = True
    flash_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(flash_timer, 250)

    # Cursor positioning
    cursor = footer_font.render("?", True, cursor_color)
    cursor = cursor.get_rect(topleft=(678, 470))
    
    time_elapsed = 0
    difficulty = 0
    difficulty_text = ""
    user_input = ""
    running = True

    while running:
        screen.fill(background_color)

        time_elapsed += 1

        # Title text rendering
        title_text = title_font.render("KINGDOM OF KROZ II", True, change_title_color(time_elapsed, color_mode))
        title_text_x, title_text_y = WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4 - 120
        
        # Title text box
        title_rect = pygame.Rect(title_text_x - 10, 20 - 12, title_text.get_width() + 20, title_text.get_height() + 20)
        pygame.draw.rect(screen, title_text_box_color, title_rect)

        # Cursor blinking effect
        if cursor_visible and difficulty_text == "":
            pygame.draw.rect(screen, cursor_color, cursor)

        # Handles difficulty selection
        if difficulty_text == "":
            screen.blit(heading_text_3, (WIDTH // 2 - heading_text_3.get_width() // 2, 470))
            screen.blit(heading_text_4, (WIDTH // 2 - 81 - heading_text_4.get_width() // 2, 470)) # Prompt is hidden after user input
        else:
            if flashing_text:
                difficulty_text_surface = heading_font.render(difficulty_text, True, background_color)
            else:
                difficulty_text_surface = heading_font.render(difficulty_text, True, header_color)
                difficulty_text_rect = difficulty_text_surface.get_rect(center=(WIDTH // 2, 476))
                screen.blit(difficulty_text_surface, difficulty_text_rect)
            screen.blit(footer_text, (WIDTH // 2 - footer_text.get_width() // 2 + 8, 560)) # Display footer text after user input
        
        # Draw text
        screen.blit(player_icon, (469, 345))
        screen.blit(title_text, (title_text_x, 20))
        screen.blit(heading_text_1, (WIDTH // 2 - heading_text_1.get_width() // 2, 100))
        screen.blit(heading_text_2, (WIDTH // 2 - heading_text_2.get_width() // 2, 130))
        screen.blit(subtext_1, (WIDTH // 2 - subtext_1.get_width() // 2, 190))
        screen.blit(subtext_2, (WIDTH // 2 - subtext_2.get_width() // 2, 210))
        screen.blit(subtext_3, (WIDTH // 2 - subtext_3.get_width() // 2, 230))
        screen.blit(subtext_4, (WIDTH // 2 - subtext_4.get_width() // 2, 250))
        screen.blit(subtext_5, (WIDTH // 2 - subtext_5.get_width() // 2, 270))
        screen.blit(subtext_6, (WIDTH // 2 - subtext_6.get_width() // 2, 290))
        screen.blit(subtext_7, (WIDTH // 2 - subtext_7.get_width() // 2, 350))
        screen.blit(subtext_8, (WIDTH // 2 - subtext_8.get_width() // 2, 370))
        screen.blit(subtext_9, (WIDTH // 2 - subtext_9.get_width() // 2, 390))
        screen.blit(subtext_10, (WIDTH // 2 - subtext_10.get_width() // 2, 410))

        pygame.display.flip()
        
        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case _ if event.type == cursor_timer:
                    cursor_visible = not cursor_visible
                case _ if event.type == flash_timer:
                    if difficulty_text:
                        flashing_text = not flashing_text
                case pygame.KEYDOWN:
                    if difficulty_text == "":
                        match event.key:
                            case pygame.K_n | pygame.K_SPACE | pygame.K_RETURN:
                                user_input = 'N'
                                difficulty_text = "NOVICE"
                                difficulty = 8
                            case pygame.K_e:
                                user_input = 'E'
                                difficulty_text = "EXPERIENCED" 
                                difficulty = 5                                
                            case pygame.K_a:
                                user_input = 'A'
                                difficulty_text = "ADVANCED"
                                difficulty = 2
                            case pygame.K_x:
                                user_input = 'X'
                                difficulty_text = "SECRET MODE"
                                difficulty = 9
                    else:
                        return difficulty
    return user_input
