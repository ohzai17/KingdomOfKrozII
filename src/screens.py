from utils import *
from gameplay import levels

############################################################################################################################################################################################################################

def color(screen): # From KINGDOM4.INC (line 66)
    
    # Fonts
    title_font, heading_font = load_fonts([WIDTH // 50, WIDTH // 70])

    # Text rendering 
    title_text = render_text(title_font, "KINGDOM OF KROZ II", BLUE)
    heading_text = render_text(heading_font, "Is your screen color or monochrome (C/M)? C", WHITE)

    # Cursor setup
    cursor_visible, cursor_timer = setup_cursor()

    # Positioning
    title_text_x = center_text_x(WIDTH, title_text.get_width())
    title_text_y = position_text_y(HEIGHT, 0.25, title_font.get_height() * 8)

    heading_text_x = center_text_x(WIDTH, heading_text.get_width())
    heading_text_y = position_text_y(HEIGHT, 0.5, heading_font.get_height())
    
    # Cursor positioning
    cursor = render_text(heading_font, "C", BLACK)
    cursor = cursor.get_rect(topleft=(heading_text_x + heading_text.get_width() - heading_font.get_height(), heading_text_y))

    color_user_input = "C"
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
                        case pygame.K_m:
                            color_user_input = "M"
                            play_sound(500, 30)
                            running = False
                        case _:
                            play_sound(500, 30)                            
                            running = False
                    print("Color:" , color_user_input)
    return color_user_input

############################################################################################################################################################################################################################

def speed(screen, color_user_input): # From KINGDOM4.INC (line 87)
    

    # Fonts
    title_font, heading_font, subtext_font = load_fonts([WIDTH // 50, WIDTH // 70, WIDTH // 70])

    if color_user_input == "M":
        TITLE_COLOR = BLACK
    else:
        TITLE_COLOR = BLUE

    # Text rendering 
    title_text = render_text(title_font, "KINGDOM OF KROZ II", TITLE_COLOR)
    heading_text = render_text(heading_font, "Slow or Fast PC (S/F)? S", WHITE)
    subtext_1 = render_text(subtext_font, "If you have an older PC (like an XT model) choose \"S\" for Slow.", GRAY)
    subtext_2 = render_text(subtext_font, "If you have a PC AT, 80386 chip, etc., choose \"F\" for Fast.", GRAY)
    subtext_3 = render_text(subtext_font, "(Default = Slow)", GRAY)

    # Cursor setup
    cursor_visible, cursor_timer = setup_cursor()

    # Positioning
    title_text_x = center_text_x(WIDTH, title_text.get_width())
    title_text_y = position_text_y(HEIGHT, 0.25, title_font.get_height() * 8)

    heading_text_x = center_text_x(WIDTH, heading_text.get_width())
    heading_text_y = position_text_y(HEIGHT, 0.5, heading_font.get_height())

    subtext_1_x = center_text_x(WIDTH, subtext_1.get_width())
    subtext_1_y = position_subtext_y(heading_text_y, heading_font.get_height(), 2)

    subtext_2_x = center_text_x(WIDTH, subtext_2.get_width())
    subtext_2_y = position_subtext_y(subtext_1_y, subtext_font.get_height(), 1.5)

    subtext_3_x = center_text_x(WIDTH, subtext_3.get_width())
    subtext_3_y = position_subtext_y(subtext_2_y, subtext_font.get_height(), 1.5)
    
    # Cursor positioning
    cursor = render_text(heading_font, "S", BLACK)
    cursor = cursor.get_rect(topleft=(heading_text_x + heading_text.get_width() - heading_font.get_height(), heading_text_y))

    speed_user_input = "S"
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
                        case pygame.K_f:
                            speed_user_input = "F"
                            play_sound(300, 30)                            
                            running = False
                        case _:
                            play_sound(300, 30)                                                        
                            running = False
                    print("Speed:" , speed_user_input)
    return speed_user_input

############################################################################################################################################################################################################################

def title(screen, color_user_input): # From KINGDOM3.INC (line 64)


    # Logo setup
    logo = pygame.image.load("src/assets/kroz_logo.png").convert_alpha()
    logo_width = WIDTH // 1.1 
    aspect_ratio = logo.get_height() / logo.get_width()
    logo_height = int(logo_width * aspect_ratio)
    logo = pygame.transform.scale(logo, (logo_width, logo_height)) 

    heading_font, subtext_font, footer_font = load_fonts([WIDTH // 60, WIDTH // 70, WIDTH // 70])

    if color_user_input == "M":
        SUBTEXT_COLOR_1 = WHITE
        SUBTEXT_COLOR_2 = GRAY
        FOOTER_COLOR = GRAY
    else:
        SUBTEXT_COLOR_1 = YELLOW
        SUBTEXT_COLOR_2 = YELLOW
        FOOTER_COLOR = AQUA

    # Text rendering
    heading_text = render_text(heading_font, "Apogee Software Presents", WHITE)
    subtext_1 = render_text(subtext_font, "KINGDOM OF KROZ II -- UPDATED VOLUME THREE OF THE KROZ SERIES", SUBTEXT_COLOR_1)
    subtext_2 = render_text(subtext_font, "Copyright (C) 1990 Scott Miller", SUBTEXT_COLOR_2)
    subtext_3 = render_text(subtext_font, "User-Supported Software -- $7.50 Registration Fee Required", SUBTEXT_COLOR_2)
    footer_text = render_text(footer_font, "Press any key to continue.", FOOTER_COLOR)

    # Positioning

    heading_text_x = center_text_x(WIDTH, heading_text.get_width())
    heading_text_y = position_text_y(HEIGHT, 0.25, heading_font.get_height() * 8)

    subtext_1_x = center_text_x(WIDTH, subtext_1.get_width())
    subtext_1_y = position_text_y(HEIGHT, 0.7, subtext_font.get_height())

    subtext_2_x = center_text_x(WIDTH, subtext_2.get_width())
    subtext_2_y = position_subtext_y(subtext_1_y, subtext_font.get_height(), 2.5)

    subtext_3_x = center_text_x(WIDTH, subtext_3.get_width())
    subtext_3_y = position_subtext_y(subtext_2_y, subtext_font.get_height(), 2.5)

    footer_text_x = center_text_x(WIDTH, footer_text.get_width())
    footer_text_y = position_subtext_y(subtext_3_y, footer_font.get_height(), 2.5)

    time_elapsed = 0
    running = True
    
    while running:
        screen.fill(BLACK)

        time_elapsed += 1 

        colorized_logo = change_logo_color(logo, time_elapsed, color_user_input)
        logo_x = center_text_x(WIDTH, colorized_logo.get_width())
        logo_y = HEIGHT // 3 - 100  

        # Draw text
        screen.blit(colorized_logo, (logo_x, logo_y))
        screen.blit(heading_text, (heading_text_x, heading_text_y))
        screen.blit(subtext_1, (subtext_1_x, subtext_1_y))
        screen.blit(subtext_2, (subtext_2_x, subtext_2_y))
        screen.blit(subtext_3, (subtext_3_x, subtext_3_y))
        screen.blit(footer_text, (footer_text_x, footer_text_y))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    play_sound(220, 100)
                    running = False
                    
############################################################################################################################################################################################################################

def difficulty(screen, color_user_input): # From KINGDOM3.INC (line 86)
    

    # Fonts
    title_font, heading_font, subtext_font, footer_font = load_fonts([WIDTH // 50, WIDTH // 80, WIDTH // 80, WIDTH // 80])

    # Player icon setup
    player_icon = pygame.image.load("src/assets/player_icon.png").convert_alpha()
    player_icon_size = WIDTH // 40  # Scale the player icon size according to the screen width
    player_icon = pygame.transform.scale(player_icon, (player_icon_size, player_icon_size))

    if color_user_input == "M":
        player_icon = apply_grayscale(player_icon)
        BACKGROUND_COLOR = BLACK
        TITLE_TEXT_BOX_COLOR = GRAY
        SUBTEXT_COLOR_1 = WHITE
        SUBTEXT_COLOR_2 = GRAY
        HEADER_COLOR = GRAY
        CURSOR_COLOR = WHITE

    else:
        BACKGROUND_COLOR = BLUE
        TITLE_TEXT_BOX_COLOR = RED
        SUBTEXT_COLOR_1 = AQUA
        SUBTEXT_COLOR_2 = LIGHT_GREEN
        HEADER_COLOR = YELLOW
        CURSOR_COLOR = ORANGE

    # Text rendering 
    heading_text_1 = render_text(heading_font, "An Apogee Software Production", WHITE)
    heading_text_2 = render_text(heading_font, "Created by Scott Miller", WHITE)
    subtext_1 = render_text(subtext_font, "Kingdom of Kroz is a game of adventure, exploration and survival.   You are", SUBTEXT_COLOR_1)
    subtext_2 = render_text(subtext_font, "a fearless archaeologist in search of the Magical Amulet,  hidden somewhere", SUBTEXT_COLOR_1)
    subtext_3 = render_text(subtext_font, "deep in the vast and dangerous underground kingdom.   You enter the kingdom", SUBTEXT_COLOR_1)
    subtext_4 = render_text(subtext_font, "through a secret tunnel and ignite your brass lantern. Your only protection", SUBTEXT_COLOR_1)
    subtext_5 = render_text(subtext_font, "is a worn leather whip and your ingenuity.  Sweat beading on your forehead,", SUBTEXT_COLOR_1)
    subtext_6 = render_text(subtext_font, "             you embark on a journey that may be your last...             ", SUBTEXT_COLOR_1)
    subtext_7 = render_text(subtext_font, "Use the cursor keys to move yourself (  ) through the kingdom.", SUBTEXT_COLOR_2)
    subtext_8 = render_text(subtext_font, "Use your whip (press W) to destroy all nearby creatures.", SUBTEXT_COLOR_2)
    subtext_9 = render_text(subtext_font, "You are on your own to discover what other mysteries await--some", SUBTEXT_COLOR_2)
    subtext_10 = render_text(subtext_font, "helpful, others deadly...", SUBTEXT_COLOR_2)
    heading_text_3_1 = render_text(heading_font, "Are you a  ovice, an  xperienced, or an  dvanced player? ", HEADER_COLOR)
    heading_text_3_2 = render_text(heading_font, "          N          E                  A", WHITE)
    footer_text = render_text(footer_font, "Press any key. ", GRAY)

    # Cursor setup
    cursor_visible, cursor_timer = setup_cursor()

    # Blinking text setup
    blinking_text, blinking_text_timer = setup_blinking_text()

    # Positioning
    heading_text_1_x = center_text_x(WIDTH, heading_text_1.get_width())
    heading_text_1_y = position_text_y(HEIGHT, 0.2, heading_font.get_height())
    
    heading_text_2_x = center_text_x(WIDTH, heading_text_2.get_width())
    heading_text_2_y = position_subtext_y(heading_text_1_y, heading_font.get_height(), 1.5)

    subtext_1_x = center_text_x(WIDTH, subtext_1.get_width())
    subtext_1_y = position_subtext_y(heading_text_2_y, heading_font.get_height(), 3)

    subtext_2_x = center_text_x(WIDTH, subtext_2.get_width())
    subtext_2_y = position_subtext_y(subtext_1_y, subtext_font.get_height(), 1)

    subtext_3_x = center_text_x(WIDTH, subtext_3.get_width())
    subtext_3_y = position_subtext_y(subtext_2_y, subtext_font.get_height(), 1)

    subtext_4_x = center_text_x(WIDTH, subtext_4.get_width())
    subtext_4_y = position_subtext_y(subtext_3_y, subtext_font.get_height(), 1)

    subtext_5_x = center_text_x(WIDTH, subtext_5.get_width())
    subtext_5_y = position_subtext_y(subtext_4_y, subtext_font.get_height(), 1)

    subtext_6_x = center_text_x(WIDTH, subtext_6.get_width())
    subtext_6_y = position_subtext_y(subtext_5_y, subtext_font.get_height(), 1)

    subtext_7_x = center_text_x(WIDTH, subtext_7.get_width())
    subtext_7_y = position_subtext_y(subtext_6_y, subtext_font.get_height(), 3)

    subtext_8_x = center_text_x(WIDTH, subtext_8.get_width())
    subtext_8_y = position_subtext_y(subtext_7_y, subtext_font.get_height(), 1)

    subtext_9_x = center_text_x(WIDTH, subtext_9.get_width())
    subtext_9_y = position_subtext_y(subtext_8_y, subtext_font.get_height(), 1)

    subtext_10_x = center_text_x(WIDTH, subtext_10.get_width())
    subtext_10_y = position_subtext_y(subtext_9_y, subtext_font.get_height(), 1)

    # subtext 1-6 are together, subtext 7-10 are together

    heading_text_3_1_x = center_text_x(WIDTH, heading_text_3_1.get_width())
    heading_text_3_1_y = position_subtext_y(subtext_10_y, heading_font.get_height(), 3)

    heading_text_3_2_x = center_text_x(WIDTH, heading_text_3_1.get_width())
    heading_text_3_2_y = position_subtext_y(subtext_10_y, heading_font.get_height(), 3)

    # heading text 3 is split into two parts

    footer_text_x = center_text_x(WIDTH + 11, footer_text.get_width())
    footer_text_y = position_subtext_y(heading_text_3_2_y, footer_font.get_height(), 4)
    
    # Cursor positioning
    cursor = render_text(heading_font, "?", BLACK)
    cursor = cursor.get_rect(topleft=(heading_text_3_1_x + heading_text_3_1.get_width() - heading_font.get_height(), heading_text_3_2_y))

    time_elapsed = 0
    difficulty_user_input = "N"
    blinking_difficulty_text = ""
    running = True
    
    while running:
        screen.fill(BACKGROUND_COLOR)

        time_elapsed += 1

        # Title text rendering
        title_text = render_text(title_font, "KINGDOM OF KROZ II", change_title_color(time_elapsed, color_user_input))
        title_text_x = center_text_x(WIDTH, title_text.get_width())
        title_text_y = position_text_y(HEIGHT, 0.25, title_font.get_height() * 8)

        # Title text box
        title_text_box = pygame.Rect(title_text_x - 10, title_text_y - 10, title_text.get_width() + 20, title_text.get_height() + 20)
        pygame.draw.rect(screen, TITLE_TEXT_BOX_COLOR, title_text_box)
        screen.blit(title_text, (title_text_x, title_text_y))

        # Cursor blinking effect
        if cursor_visible and blinking_difficulty_text == "":
            pygame.draw.rect(screen, CURSOR_COLOR, cursor)

        # Handles difficulty selection
        if blinking_difficulty_text == "":
            screen.blit(heading_text_3_1, (heading_text_3_1_x, heading_text_3_1_y))
            screen.blit(heading_text_3_2, (heading_text_3_2_x, heading_text_3_2_y)) # Prompt is hidden after user input
        else:
            if blinking_text:
                blinking_difficulty_text_render = render_text(heading_font, blinking_difficulty_text, HEADER_COLOR)
            else:
                blinking_difficulty_text_render = render_text(heading_font, "", HEADER_COLOR)

            blinking_difficulty_text_x = center_text_x(WIDTH, blinking_difficulty_text_render.get_width())
            blinking_difficulty_text_y = position_subtext_y(subtext_10_y, heading_font.get_height(), 3)
            screen.blit(blinking_difficulty_text_render, (blinking_difficulty_text_x, blinking_difficulty_text_y)) # Display blinking difficulty text

            screen.blit(footer_text, (footer_text_x, footer_text_y)) # Display footer text after user input

        # Draw text
        screen.blit(heading_text_1, (heading_text_1_x, heading_text_1_y))
        screen.blit(heading_text_2, (heading_text_2_x, heading_text_2_y))
        screen.blit(subtext_1, (subtext_1_x, subtext_1_y))
        screen.blit(subtext_2, (subtext_2_x, subtext_2_y))
        screen.blit(subtext_3, (subtext_3_x, subtext_3_y))
        screen.blit(subtext_4, (subtext_4_x, subtext_4_y))
        screen.blit(subtext_5, (subtext_5_x, subtext_5_y))
        screen.blit(subtext_6, (subtext_6_x, subtext_6_y))
        screen.blit(subtext_7, (subtext_7_x, subtext_7_y))
        screen.blit(subtext_8, (subtext_8_x, subtext_8_y))
        screen.blit(subtext_9, (subtext_9_x, subtext_9_y))
        screen.blit(subtext_10, (subtext_10_x, subtext_10_y))

        # Draw player icon
        player_icon_x = subtext_7_x + subtext_7.get_width() // 2 + 69
        player_icon_y = subtext_7_y + subtext_7.get_height() // 2 - player_icon_size // 2
        screen.blit(player_icon, (player_icon_x, player_icon_y))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case _ if event.type == cursor_timer:
                    cursor_visible = not cursor_visible
                case _ if event.type == blinking_text_timer:
                    if blinking_difficulty_text:
                        blinking_text = not blinking_text
                case pygame.KEYDOWN:
                    if blinking_difficulty_text == "":
                        match event.key:
                            case pygame.K_e:
                                difficulty_user_input = 'E'
                                blinking_difficulty_text = "EXPERIENCED"
                                play_sound(300, 100)
                                play_sound(700, 100)
                            case pygame.K_a:
                                difficulty_user_input = 'A'
                                blinking_difficulty_text = "ADVANCED"
                                play_sound(300, 100)
                                play_sound(700, 100)                                
                            case pygame.K_x:
                                difficulty_user_input = 'X'
                                blinking_difficulty_text = "SECRET MODE"
                                play_sound(300, 100)
                                play_sound(700, 100)                                
                            case _:
                                blinking_difficulty_text = "NOVICE"
                                play_sound(300, 100)
                                play_sound(700, 100)                                
                        print("Difficulty:" , difficulty_user_input)
                    else:
                        return difficulty_user_input

############################################################################################################################################################################################################################

# START of shareware (info_screen)
def shareware(screen, color_user_input): # From KINGDOM3.INC (lines 495-541)
    
    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        FOOTER_COLOR = BLACK
        BODY_TEXT_COLOR_1 = GRAY
        BODY_TEXT_COLOR_2 = GRAY
        
    else:
        BACKGROUND = BLUE
        FOOTER_COLOR = WHITE        
        BODY_TEXT_COLOR_1 = WHITE
        BODY_TEXT_COLOR_2 = YELLOW
    
    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])

    title = title_font.render("KINGDOM OF KROZ II -  REGISTER", True, WHITE)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)
    
    title_rect = title.get_rect(center=(WIDTH // 2, 10))
    
    body_text_1 = render_text(body_font, "   This is not a shareware game, but it is user-supported. If you enjoy this", GRAY)
    body_text_2 = render_text(body_font, "game, you are asked by the author to please send a registration", GRAY)
    body_text_3 = render_text(body_font, "check in the amount of $7.50 to Apogee Software.", GRAY)
    body_text_4 = render_text(body_font, "   This registration fee will qualify you to order any of the other Kroz", GRAY)
    body_text_5 = render_text(body_font, "volumes available:", GRAY)
    
    body_text_6 = render_text(body_font, "Caverns of Kroz   - the first discovery of Kroz", BODY_TEXT_COLOR_1)
    body_text_7 = render_text(body_font, "Dungeons of Kroz  - the dark side of Kroz, fast-paced action", BODY_TEXT_COLOR_1)
    body_text_8 = render_text(body_font, "Kingdom of Kroz I - the national contest winner (\"Best Game\" in 1988)", BODY_TEXT_COLOR_1)
    body_text_9 = render_text(body_font, "Return of Kroz    - the discovery of entirely new underground chambers", BODY_TEXT_COLOR_1)
    body_text_10 = render_text(body_font, "Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems", BODY_TEXT_COLOR_1)
    body_text_11 = render_text(body_font, "The Final Crusade of Kroz - the surprising finish?", BODY_TEXT_COLOR_1)
   
    body_text_12 = render_text(body_font, "Each game is priced $7.50 each, any three for $20, or all six for only $35.", GRAY)
    body_text_13 = render_text(body_font, "You'll also get a secret code that makes this game easier to complete,", GRAY)
    body_text_14 = render_text(body_font, "Plus a Hints Tricks and Scoring Secrets guide and The Domain of Kroz map.", GRAY)
    body_text_15 = render_text(body_font, "Please make checks payable to:", GRAY)
    body_text_16 = render_text(body_font, "                                   apogee Software     (phone: 214/240-0614)", BODY_TEXT_COLOR_2)
    body_text_17 = render_text(body_font, "                                   4206 Mayflower", BODY_TEXT_COLOR_2)  
    body_text_18 = render_text(body_font, "Address is always valid!", WHITE)
    body_text_19 = render_text(body_font, "                                   Garland, TX 75045   (USA)", BODY_TEXT_COLOR_2)  
    body_text_20 = render_text(body_font, "Thank you and enjoy the game.  -- Scott Miller", WHITE)    
    
    # Adjust text alignment to be left-justified
    body_text_1_x = 10  # Left margin
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 1)

    body_text_2_x = 10
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = 10
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = 10
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = 10
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)
    
    # Positioning for body_text_6 to body_text_11
    bullet_x = 30  # Left margin for bullets
    text_indent_x = 50  # Indent for text after bullets
    bullet_size = 8  # Size of the square bullet

    body_text_6_x = text_indent_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 2)

    body_text_7_x = text_indent_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = text_indent_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = text_indent_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = text_indent_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = text_indent_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = 10
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 2)

    body_text_13_x = 10
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = 10
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = 10
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 2)

    body_text_16_x = 10
    body_text_16_y = position_subtext_y(body_text_14_y, body_font.get_height(), 2)

    body_text_17_x = 10
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = 10
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = 10
    body_text_19_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_20_x = 10
    body_text_20_y = position_subtext_y(body_text_19_y, body_font.get_height(), 2)


    running = True
    while running:

        screen.fill(BACKGROUND) 

        screen.blit(title, title_rect) # Title
        
        # Horizontal line under title
        line_y = title_rect.bottom + 8
        pygame.draw.line(screen, GRAY, (0, line_y), (WIDTH, line_y), 1)
        
        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))

        # Render body text with square bullets
        pygame.draw.rect(screen, WHITE, (bullet_x, body_text_6_y + body_font.get_height() // 4, bullet_size, bullet_size))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))

        pygame.draw.rect(screen, WHITE, (bullet_x, body_text_7_y + body_font.get_height() // 4, bullet_size, bullet_size))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))

        pygame.draw.rect(screen, WHITE, (bullet_x, body_text_8_y + body_font.get_height() // 4, bullet_size, bullet_size))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))

        pygame.draw.rect(screen, WHITE, (bullet_x, body_text_9_y + body_font.get_height() // 4, bullet_size, bullet_size))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))

        pygame.draw.rect(screen, WHITE, (bullet_x, body_text_10_y + body_font.get_height() // 4, bullet_size, bullet_size))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))

        pygame.draw.rect(screen, WHITE, (bullet_x, body_text_11_y + body_font.get_height() // 4, bullet_size, bullet_size))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))

        # Render remaining body text
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))
        screen.blit(body_text_20, (body_text_20_x, body_text_20_y))        

        # Random color rectangle
        pygame.draw.rect(screen, rand_color, (0, HEIGHT - 17, WIDTH, 17)) # (x, y, width, height)

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case pygame.KEYDOWN:
                    running = False
                    
############################################################################################################################################################################################################################                    

# START of instructions_1
def instructions_1(screen, color_user_input): #

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE                
        FOOTER_COLOR = BLACK
        BODY_TEXT_COLOR_1 = GRAY
        BODY_TEXT_COLOR_2 = GRAY
        
    else:
        BACKGROUND = BLUE
        TITLE_COLOR = YELLOW        
        FOOTER_COLOR = WHITE        
        BODY_TEXT_COLOR_1 = WHITE
        BODY_TEXT_COLOR_2 = YELLOW
        
    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])    

    title = title_font.render("THE INSTRUCTIONS", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)
    
    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   Kingdom of Kroz is a game of exploration and survival. Your journey will", BODY_TEXT_COLOR_1)
    body_text_2 = render_text(body_font, "take you through 25 very dangerous chambers, each riddled with diabolical", BODY_TEXT_COLOR_1)
    body_text_3 = render_text(body_font, "traps and hideous creatures. Hidden in the deepest chamber lies a hidden", BODY_TEXT_COLOR_1)
    body_text_4 = render_text(body_font, "treasure of immense value. Use the cursor pad to move 8 directions.", BODY_TEXT_COLOR_1)
    body_text_5 = render_text(body_font, "   The chambers contain dozens of treasures, spells, traps and other unknowns.", BODY_TEXT_COLOR_1)
    body_text_6 = render_text(body_font, "Touching an object for the first time will reveal a little of its identity,", BODY_TEXT_COLOR_1)
    body_text_7 = render_text(body_font, "but it will be left to you to decide how best to use it--or avoid it.", BODY_TEXT_COLOR_1)
    body_text_8 = render_text(body_font, "   When a creature touches you it will vanish, taking with it a few of your", BODY_TEXT_COLOR_1)
    body_text_9 = render_text(body_font, "gems that you have collected. If you have no gems then the creature will", BODY_TEXT_COLOR_1)
    body_text_10 = render_text(body_font, "instead take your life! Whips can be used to kill nearby creatures, but", BODY_TEXT_COLOR_1)
    body_text_11 = render_text(body_font, "they're better used to smash through \"breakable walls\" and other terrain.", BODY_TEXT_COLOR_1)
    body_text_12 = render_text(body_font, "   Laptop and PCjr players can", BODY_TEXT_COLOR_1)
    body_text_13 = render_text(body_font, "use the alternate cursor             U I O      ( NW N NE )", BODY_TEXT_COLOR_1)
    body_text_14 = render_text(body_font, "pad instead of the cursor             J K       (   W E   )", BODY_TEXT_COLOR_1)
    body_text_15 = render_text(body_font, "keys to move your man, plus          N M ,      ( SW S SE )", BODY_TEXT_COLOR_1)
    body_text_16 = render_text(body_font, "the four normal cursor keys.", BODY_TEXT_COLOR_1)
    body_text_17 = render_text(body_font, "  It's a good idea to save your game at every new level, therefore, if you die", BODY_TEXT_COLOR_1)
    body_text_18 = render_text(body_font, "you can easily restore the game at that level and try again.", BODY_TEXT_COLOR_1)
    body_text_19 = render_text(body_font, "Registered users will get a \"secret code\" that makes this game much easier!", BODY_TEXT_COLOR_1)


    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = body_text_1_x
    body_text_19_y = position_subtext_y(body_text_18_y, body_font.get_height(), 1)
    
    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y),(title_rect.right, line_y), 1)        

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instructions_1       

# START of instructions_2
def instructions_2(screen, color_user_input): #

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE                
        FOOTER_COLOR = BLACK
        BODY_TEXT_COLOR_1 = GRAY
        BODY_TEXT_COLOR_2 = GRAY
        
    else:
        BACKGROUND = BLUE
        TITLE_COLOR = YELLOW        
        FOOTER_COLOR = WHITE        
        BODY_TEXT_COLOR_1 = WHITE
        BODY_TEXT_COLOR_2 = YELLOW
        
    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])    

    title = title_font.render("THE INSTRUCTIONS", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)
    
    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   Kingdom of Kroz will present you with many challenges. You will venture deep", BODY_TEXT_COLOR_1)
    body_text_2 = render_text(body_font, "underground and probably not make it out alive!", BODY_TEXT_COLOR_1)
    
    body_text_3 = render_text(body_font, "Hints:    Don't forget to use the Home, End, PgUp, and PgDn keys to move your", BODY_TEXT_COLOR_1)
    body_text_4 = render_text(body_font, "          on-screen character diagonally (along with the marked cursor keys).", BODY_TEXT_COLOR_1)
    body_text_5 = render_text(body_font, "          Use your player to touch each new object to find out about it.  When", BODY_TEXT_COLOR_1)
    body_text_6 = render_text(body_font, "          you first touch an object a message appears at the bottom of the", BODY_TEXT_COLOR_1)
    body_text_7 = render_text(body_font, "          screen that describes it.", BODY_TEXT_COLOR_1)
    body_text_8 = render_text(body_font, "          Collect keys to unlock doors, which usually block the stairs.", BODY_TEXT_COLOR_1)
    body_text_9 = render_text(body_font, "          The faster monsters are the most dangerous to touch--they will knock", BODY_TEXT_COLOR_1)
    body_text_10 = render_text(body_font, "         off three of your valuable gems.  The slowest creatures only take a", BODY_TEXT_COLOR_1)
    body_text_11 = render_text(body_font, "         single gem from you, and the medium speed monsters take two.", BODY_TEXT_COLOR_1)
    
    body_text_12 = render_text(body_font, "   Some levels have a Magical Gravity that will pull you downward!  On these", BODY_TEXT_COLOR_1)
    body_text_13 = render_text(body_font, "levels the game is played as if viewing the level from a side angle.  On", BODY_TEXT_COLOR_1)
    body_text_14 = render_text(body_font, "these levels you can only move upward by using a rope, a secret tunnel, or", BODY_TEXT_COLOR_1)
    body_text_15 = render_text(body_font, "by using a teleport scroll.  These unique \"Sideways Levels\" may take a", BODY_TEXT_COLOR_1)
    body_text_16 = render_text(body_font, "little getting used to, but are well worth the effort.  At the beginning of", BODY_TEXT_COLOR_1)
    body_text_17 = render_text(body_font, "a \"sideways\" level a message at the bottom of the screen will alert you.", BODY_TEXT_COLOR_1)

    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 2)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 2)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 2)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 2)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)
    
    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15  # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y), (title_rect.right, line_y), 1)

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instructions_2

# START of instructions_3
def instructions_3(screen, color_user_input): #

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE                
        FOOTER_COLOR = BLACK
        BODY_TEXT_COLOR_1 = GRAY
        BODY_TEXT_COLOR_2 = GRAY
        
    else:
        BACKGROUND = BLUE
        TITLE_COLOR = YELLOW        
        FOOTER_COLOR = WHITE        
        BODY_TEXT_COLOR_1 = WHITE
        BODY_TEXT_COLOR_2 = YELLOW
        
    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])    

    title = title_font.render("THE INSTRUCTIONS", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)
    
    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   Here are some brief descriptions of the most common objects that you are", BODY_TEXT_COLOR_1)
    body_text_2 = render_text(body_font, "likely to find in the Kingdom of Kroz:", BODY_TEXT_COLOR_1)
    body_text_3 = render_text(body_font, "       - this is you, a dauntless archaeologist without peer", BODY_TEXT_COLOR_1)
    body_text_4 = render_text(body_font, "       - red creatures move slow and only knock off 1 gem when touched", BODY_TEXT_COLOR_1)
    body_text_5 = render_text(body_font, "       - green creatures move faster and knock off 2 gems when touched", BODY_TEXT_COLOR_1)
    body_text_6 = render_text(body_font, "       - blue creatures move fastest and knock off 3 gems when touched", BODY_TEXT_COLOR_1)
    body_text_7 = render_text(body_font, "       - collect all the gems you can to survive creature attacks", BODY_TEXT_COLOR_1)
    body_text_8 = render_text(body_font, "       - whips are used to wipe out creatures and smash certain walls", BODY_TEXT_COLOR_1)
    body_text_9 = render_text(body_font, "       - teleport spells will magically transport you to a random place", BODY_TEXT_COLOR_1)
    body_text_10 = render_text(body_font, "       - chests contain a random number of gems and whips", BODY_TEXT_COLOR_1)
    body_text_11 = render_text(body_font, "       - collect keys to go through doors (')", BODY_TEXT_COLOR_1)
    body_text_12 = render_text(body_font, "       - collect these power rings to make your whips more powerful", BODY_TEXT_COLOR_1)
    body_text_13 = render_text(body_font, "       - these tablets will give you clues, advice and warnings", BODY_TEXT_COLOR_1)
    body_text_14 = render_text(body_font, "       - this might be anything, including a big pouch of gems!", BODY_TEXT_COLOR_1)
    body_text_15 = render_text(body_font, "       - stairs take you to the next level deeper in Kroz", BODY_TEXT_COLOR_1)
    body_text_16 = render_text(body_font, "   There are dozens and dozens of other objects to discover. The best way", BODY_TEXT_COLOR_1)
    body_text_17 = render_text(body_font, "to learn the usefulness of any new object is to touch it and read the brief", BODY_TEXT_COLOR_1)
    body_text_18 = render_text(body_font, "message that appears at the bottom of the screen.", BODY_TEXT_COLOR_1)

    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 2)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 2)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)
    
    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15  # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y), (title_rect.right, line_y), 1)

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)
        
        display_icons(screen)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instructions_3  

# START of instructions_4
def instructions_4(screen, color_user_input): #

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE                
        FOOTER_COLOR = BLACK
        BODY_TEXT_COLOR_1 = GRAY
    else:
        BACKGROUND = BLUE
        TITLE_COLOR = YELLOW        
        FOOTER_COLOR = WHITE        
        BODY_TEXT_COLOR_1 = WHITE

    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])    

    title = title_font.render("MISCELLANEOUS", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)
    
    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "You can now save three different levels during a single game. When you", BODY_TEXT_COLOR_1)
    body_text_2 = render_text(body_font, "select the 'save' command you will also be asked to enter a letter, either", BODY_TEXT_COLOR_1)
    body_text_3 = render_text(body_font, "A, B or C. If you just hit the space bar then A is the default selection.", BODY_TEXT_COLOR_1)
    body_text_4 = render_text(body_font, "These letters do not refer to disk drives! They actually refer to the file", BODY_TEXT_COLOR_1)
    body_text_5 = render_text(body_font, "names used by the game. The restore command lets you pick from A, B or C.", BODY_TEXT_COLOR_1)

    body_text_6 = render_text(body_font, "Sideways levels can be recognized by the pause message that appears at", BODY_TEXT_COLOR_1)
    body_text_7 = render_text(body_font, "the bottom of the screen, which states that it's a 'sideways' level.", BODY_TEXT_COLOR_1)

    body_text_8 = render_text(body_font, "If you are tired of seeing the descriptions at the bottom of the screen", BODY_TEXT_COLOR_1)
    body_text_9 = render_text(body_font, "that appear whenever you touch a new object, you can disable most of the", BODY_TEXT_COLOR_1)
    body_text_10 = render_text(body_font, "messages by pressing the minus (-) key. The plus key (+) resets messages.", BODY_TEXT_COLOR_1)

    body_text_11 = render_text(body_font, "Kingdom of Kroz II is a completely updated and improved version over the", BODY_TEXT_COLOR_1)
    body_text_12 = render_text(body_font, "original version of Kingdom of Kroz. If you desire to play the original", BODY_TEXT_COLOR_1)
    body_text_13 = render_text(body_font, "Kingdom of Kroz, please send $7.50. Over 17 levels are different!", BODY_TEXT_COLOR_1)

    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 2)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 2)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 2)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)
    
    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15  # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y), (title_rect.right, line_y), 1)

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instructions_4 

############################################################################################################################################################################################################################

def marketing(screen, color_user_input): # From KINGDOM3.INC (line 348)

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE
        FOOTER_COLOR = WHITE
    else:
        TITLE_COLOR = YELLOW
        FOOTER_COLOR = WHITE
        BACKGROUND = BLUE

    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])
    
    # Font render
    title = title_font.render("THE MARKETING OF KROZ", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   Kingdom of Kroz II is a user-supported game.  This means that the creator of", WHITE)
    body_text_2 = render_text(body_font, " this program relies on the appreciation of honest players to pay the game's", WHITE)
    body_text_3 = render_text(body_font, " registration fee--$7.50.", WHITE)
    body_text_4 = render_text(body_font, "   Payment of this fee entitles you to all the free help and hints you might", WHITE)
    body_text_5 = render_text(body_font, " need to enjoy the game.  All letters from registered users are answered", WHITE)
    body_text_6 = render_text(body_font, " within two days.  (Try to get this kind of support from commercial games!)", WHITE)
    body_text_7 = render_text(body_font, "   Also, players can order the other Kroz sequels ONLY if this registration", WHITE)
    body_text_8 = render_text(body_font, " fee is paid.  ($7.50 each or $20 for The Lost Adventures of Kroz.)", WHITE)
    body_text_9 = render_text(body_font, "   Everyone who orders (or registers) any of the other six Kroz games will also", WHITE)
    body_text_10 = render_text(body_font, ' get a "Hints, Tricks and Scoring Secrets" guide, and "The Domain of Kroz" map.', WHITE)
    body_text_11 = render_text(body_font, "   A single Kroz game takes several months to create, up to 200 hours per game!", WHITE)
    body_text_12 = render_text(body_font, " I can't afford to devote this much time without receiving something in return.", WHITE)
    body_text_13 = render_text(body_font, " That is why I ask for this small fee, which is only necessary if you enjoy", WHITE)
    body_text_14 = render_text(body_font, " this game.  In other words, try before you buy.", WHITE)
    body_text_15 = render_text(body_font, "   Even if you buy this game from a public domain or shareware library, I don't", WHITE)
    body_text_16 = render_text(body_font, ' receive any of that money.  You\'re simply paying for "storage, distribution,', WHITE)
    body_text_17 = render_text(body_font, ' disk, and handling."', WHITE)
    body_text_18 = render_text(body_font, "   Note:  The current Apogee Software address will ALWAYS BE VALID.  Foreign", WHITE)
    body_text_19 = render_text(body_font, " orders are always welcome, please send U.S. funds/money orders only.", WHITE)
    body_text_20 = render_text(body_font, "Press any key to continue.", WHITE)


    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = body_text_1_x
    body_text_19_y = position_subtext_y(body_text_18_y, body_font.get_height(), 1)

    body_text_20_x = body_text_1_x
    body_text_20_y = position_subtext_y(body_text_19_y, body_font.get_height(), 1)


    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y),(title_rect.right, line_y), 1)        

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))
        screen.blit(body_text_20, (body_text_20_x, body_text_20_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False

############################################################################################################################################################################################################################

def story_1(screen, color_user_input): # From KINGDOM4.INC (line 379)

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
    else:
        TITLE_COLOR = YELLOW
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
        BACKGROUND = BLUE

    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])
    
    # Font render
    title = title_font.render("THE STORY BEHIND KROZ", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   The original Kroz Trilogy (consisting of Caverns of Kroz, Dungeons of Kroz,", WHITE)
    body_text_2 = render_text(body_font, " and Kingdom of Kroz) was developed after I spent many hours playing another", WHITE)
    body_text_3 = render_text(body_font, " explore-the-levels type game titled Rogue.  I never could finish Rogue,", WHITE)
    body_text_4 = render_text(body_font, " though, because the game relied too much on luck and random occurrences.", WHITE)
    body_text_5 = render_text(body_font, "   The name 'Kroz' is actually Zork (an Infocom text adventure) spelled in", WHITE)
    body_text_6 = render_text(body_font, " reverse.  Many players still inquire about this bit of trivia.  The game was", WHITE)
    body_text_7 = render_text(body_font, " first designed without predefined level layouts, meaning every level was a", WHITE)
    body_text_8 = render_text(body_font, " random placement of creatures and play field objects.  New objects, like", WHITE)
    body_text_9 = render_text(body_font, " spells, lava, doors, etc., were added quickly as the first Kroz game took", WHITE)
    body_text_10 = render_text(body_font, " shape, including the ability to have predefined level floor plans.", WHITE)
    body_text_11 = render_text(body_font, "   My main objective was to create a game that wasn't all fast paced action,", WHITE)
    body_text_12 = render_text(body_font, " but also included strategy and puzzle solving.  Kingdom of Kroz was entered", WHITE)
    body_text_13 = render_text(body_font, " in a national programming contest in 1988 and took top honors in the game", WHITE)
    body_text_14 = render_text(body_font, " category, and number two overall (beaten by a spreadsheet program.)", WHITE)
    body_text_15 = render_text(body_font, "   The latest Kroz games have been greatly re-designed and re-programmed, but", WHITE)
    body_text_16 = render_text(body_font, " the familiar appearance has been mostly maintained.  You will discover new", WHITE)
    body_text_17 = render_text(body_font, " dangers, creatures and objects in your adventures below.", WHITE)
    body_text_18 = render_text(body_font, "   Thanks to all the players of Kroz who contributed dozens of suggestions,", WHITE)
    body_text_19 = render_text(body_font, " ideas and improvements that were incorporated in later versions of Kroz.", WHITE)
    body_text_20 = render_text(body_font, "Press any key to continue.", WHITE)


    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = body_text_1_x
    body_text_19_y = position_subtext_y(body_text_18_y, body_font.get_height(), 1)

    body_text_20_x = body_text_1_x
    body_text_20_y = position_subtext_y(body_text_19_y, body_font.get_height(), 1)


    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y),(title_rect.right, line_y), 1)        

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))
        screen.blit(body_text_20, (body_text_20_x, body_text_20_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False

############################################################################################################################################################################################################################

def story_2(screen, color_user_input): # From KINGDOM4.INC (line 379)

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
    else:
        TITLE_COLOR = YELLOW
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
        BACKGROUND = BLUE

    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])
    
    # Font render
    title = title_font.render("THE STORY BEHIND KROZ", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   Kroz is a hobby that's gotten out of control!", WHITE)
    body_text_2 = render_text(body_font, "   Kroz is truly a phenomenon in the user-supported software market.  The", WHITE)
    body_text_3 = render_text(body_font, " overwhelming success of the original Kroz games was completely unexpected.", WHITE)
    body_text_4 = render_text(body_font, " Most (probably 99%) of all 'shareware' games are not profitable for their", WHITE)
    body_text_5 = render_text(body_font, " creator.  This is a well-known fact among the community of shareware game", WHITE)
    body_text_6 = render_text(body_font, " authors, and one that I've verified by speaking to many other games de-", WHITE)
    body_text_7 = render_text(body_font, " signers.  Most people simply don't register games.", WHITE)
    body_text_8 = render_text(body_font, "   Through my research the Kroz games are the only user-supported games that", WHITE)
    body_text_9 = render_text(body_font, " generate a substantial amount of registrations and orders for its creator,", WHITE)
    body_text_10 = render_text(body_font, " namely, Scott Miller (me).  I don't know what cord I've struck with players,", WHITE)
    body_text_11 = render_text(body_font, " but everyday I receive fascinating and appreciative letters from players", WHITE)
    body_text_12 = render_text(body_font, " telling me how much they enjoy the Kroz games.", WHITE)
    body_text_13 = render_text(body_font, "   Thanks to Kroz I now know what a mutual fund is, but on the downside my", WHITE)
    body_text_14 = render_text(body_font, " taxes require a book two inches thick to figure out.", WHITE)
    body_text_15 = render_text(body_font, "   Will Kroz ever end?  I thought that THE FINAL CRUSADE would be the closing", WHITE)
    body_text_16 = render_text(body_font, " chapter--but a flood of letters demanding more proved that I'm a pushover.", WHITE)
    body_text_17 = render_text(body_font, " I guess as long as the letters keep coming, I'll continue to make Kroz games.", WHITE)
    body_text_18 = render_text(body_font, " After all, Kroz is like my second home now, one that I like to visit often...", WHITE)
    body_text_19 = render_text(body_font, "                                                        -- Scott Miller", WHITE)


    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = body_text_1_x
    body_text_19_y = position_subtext_y(body_text_18_y, body_font.get_height(), 1)

    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y),(title_rect.right, line_y), 1)        

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False

############################################################################################################################################################################################################################

def original(screen, color_user_input): # From KINGDOM4.INC (line 438)

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
    else:
        TITLE_COLOR = YELLOW
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
        BACKGROUND = BLUE

    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])
    
    # Font render
    title = title_font.render("THE ORIGINAL KROZ GAMES", True, TITLE_COLOR)
    prompt_text = body_font.render("Press any key to continue", True, FOOTER_COLOR)

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   The Lost Adventures of Kroz is the latest addition to the Kroz family of", WHITE)
    body_text_2 = render_text(body_font, " games.  Before this game there are six more Kroz volumes, separated into two", WHITE)
    body_text_3 = render_text(body_font, " trilogies:  The Kroz Trilogy and The Super Kroz Trilogy.", WHITE)
    body_text_4 = render_text(body_font, "   The original Kroz Trilogy was such a surprising success that I decided to", WHITE)
    body_text_5 = render_text(body_font, " created a second 'Super Kroz' trilogy.  The first three original Kroz", WHITE)
    body_text_6 = render_text(body_font, " games are:     Kingdom of Kroz     Caverns of Kroz     Dungeons of Kroz.", WHITE)  # Replace � with spaces
    body_text_7 = render_text(body_font, " All three are still available and are constantly being updated and improved.", WHITE)
    body_text_8 = render_text(body_font, "   The original Kroz Trilogy games can be purchased for $7.50 each, or all 3", WHITE)
    body_text_9 = render_text(body_font, " for $20 (these prices include postage, disks, and handling).", WHITE)
    body_text_10 = render_text(body_font, "   Only Kingdom of Kroz can be placed in a shareware library for distribution,", WHITE)
    body_text_11 = render_text(body_font, " and the other two can only be ordered from Apogee Software Productions.", WHITE)
    body_text_12 = render_text(body_font, "   The Super Kroz Trilogy volumes are revamped and greatly improved.  They are", WHITE)
    body_text_13 = render_text(body_font, "     Return to Kroz     Temple of Kroz     The Final Crusade of Kroz.  The last", WHITE)  # Replace � with spaces
    body_text_14 = render_text(body_font, " three volumes were supposed to be the end of Kroz, but the mail kept coming", WHITE)
    body_text_15 = render_text(body_font, " and again I was impelled to create another Kroz adventure.", WHITE)
    body_text_16 = render_text(body_font, "   All Kroz games work on all monitors, either graphics or monochrome systems.", WHITE)
    body_text_17 = render_text(body_font, " Plus, they only rely on keyboard control, and have slow-down routines that", WHITE)
    body_text_18 = render_text(body_font, " permit them to function correctly on any speed IBM PC compatible computer.", WHITE)
    body_text_19 = render_text(body_font, "Press any key to continue.", WHITE)

    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = body_text_1_x
    body_text_19_y = position_subtext_y(body_text_18_y, body_font.get_height(), 1)

    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y),(title_rect.right, line_y), 1)        

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))  

        square_size = 8
        square_color = WHITE
        pygame.draw.rect(screen, square_color, (body_text_6_x + 140, body_text_6_y, square_size, square_size))
        pygame.draw.rect(screen, square_color, (body_text_6_x + 340, body_text_6_y, square_size, square_size))
        pygame.draw.rect(screen, square_color, (body_text_6_x + 540, body_text_6_y, square_size, square_size))
        pygame.draw.rect(screen, square_color, (body_text_13_x + 30, body_text_13_y, square_size, square_size))
        pygame.draw.rect(screen, square_color, (body_text_13_x + 220, body_text_13_y, square_size, square_size))
        pygame.draw.rect(screen, square_color, (body_text_13_x + 410, body_text_13_y, square_size, square_size))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
############################################################################################################################################################################################################################

def about(screen, color_user_input): # From KINGDOM4.INC (line 467)

    if color_user_input == "M":  # change to grayscale
        BACKGROUND = BLACK
        TITLE_COLOR = WHITE
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
    else:
        TITLE_COLOR = YELLOW
        FOOTER = WHITE
        FOOTER_COLOR = WHITE
        BACKGROUND = BLUE

    title_font, body_font = load_fonts([WIDTH // 60, WIDTH // 80])
    
    # Font render
    title = title_font.render("ABOUT THE AUTHOR", True, YELLOW)
    prompt_text = body_font.render("Press any key to continue", True, TITLE_COLOR)

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    body_text_1 = render_text(body_font, "   Scott Miller, the creator of all the Kroz games, along with Supernova, Trek", WHITE)
    body_text_2 = render_text(body_font, " Trivia and Beyond the Titanic (all shareware games) began programming in high", WHITE)
    body_text_3 = render_text(body_font, " school in 1975.  Since then he's created over 100 games and has had dozens", WHITE)
    body_text_4 = render_text(body_font, " publishered by BIG BLUE DISK, I.B.Magazette and Keypunch Software.", WHITE)
    body_text_5 = render_text(body_font, "", WHITE)
    body_text_6 = render_text(body_font, "   For over three years he wrote two weekly computer columns for the Dallas", WHITE)
    body_text_7 = render_text(body_font, " Morning News, one of the nation's largest newspapers.  He also co-authored", WHITE)
    body_text_8 = render_text(body_font, ' a video game strategy book titled, "Shootout: Beating the Video Games."', WHITE)
    body_text_9 = render_text(body_font, " Scott has written articles for COMPUTE!'s PC and PCjr Magazine and is a", WHITE)
    body_text_10 = render_text(body_font, " software reviewer with COMPUTE! Publications.", WHITE)
    body_text_11 = render_text(body_font, "", WHITE)
    body_text_12 = render_text(body_font, "   Hobbies include softball, running, tennis, karate (1st degree black belt),", WHITE)
    body_text_13 = render_text(body_font, " drumming, rock music, science fiction, and creating new computer games.", WHITE)
    body_text_14 = render_text(body_font, " Favorite computer games are M.U.L.E., Jumpman, Planetfall, Enchanter, Zork,", WHITE)
    body_text_15 = render_text(body_font, " Spelunker, and Archon.  All are games of strategy, with action secondary.", WHITE)
    body_text_16 = render_text(body_font, "", WHITE)
    body_text_17 = render_text(body_font, "   Scott creates all Apogee Software programs on an AST Premium 80386 (20 Mhz)", WHITE)
    body_text_18 = render_text(body_font, " equipped with VGA graphics, a NEC MultiSync II and an HP LaserJet series II.", WHITE)
    body_text_19 = render_text(body_font, " The cost to market each Kroz game to the many shareware libraries and BBS's", WHITE)
    body_text_20 = render_text(body_font, " is over $2000 per game.  All of the appreciative letters make it worth it!", WHITE)
    body_text_21 = render_text(body_font, "Press any key to continue.", WHITE)

    body_text_1_x = center_text_x(WIDTH, body_text_1.get_width())
    body_text_1_y = position_subtext_y(title_rect.bottom, body_font.get_height(), 2)

    body_text_2_x = body_text_1_x
    body_text_2_y = position_subtext_y(body_text_1_y, body_font.get_height(), 1)

    body_text_3_x = body_text_1_x
    body_text_3_y = position_subtext_y(body_text_2_y, body_font.get_height(), 1)

    body_text_4_x = body_text_1_x
    body_text_4_y = position_subtext_y(body_text_3_y, body_font.get_height(), 1)

    body_text_5_x = body_text_1_x
    body_text_5_y = position_subtext_y(body_text_4_y, body_font.get_height(), 1)

    body_text_6_x = body_text_1_x
    body_text_6_y = position_subtext_y(body_text_5_y, body_font.get_height(), 1)

    body_text_7_x = body_text_1_x
    body_text_7_y = position_subtext_y(body_text_6_y, body_font.get_height(), 1)

    body_text_8_x = body_text_1_x
    body_text_8_y = position_subtext_y(body_text_7_y, body_font.get_height(), 1)

    body_text_9_x = body_text_1_x
    body_text_9_y = position_subtext_y(body_text_8_y, body_font.get_height(), 1)

    body_text_10_x = body_text_1_x
    body_text_10_y = position_subtext_y(body_text_9_y, body_font.get_height(), 1)

    body_text_11_x = body_text_1_x
    body_text_11_y = position_subtext_y(body_text_10_y, body_font.get_height(), 1)

    body_text_12_x = body_text_1_x
    body_text_12_y = position_subtext_y(body_text_11_y, body_font.get_height(), 1)

    body_text_13_x = body_text_1_x
    body_text_13_y = position_subtext_y(body_text_12_y, body_font.get_height(), 1)

    body_text_14_x = body_text_1_x
    body_text_14_y = position_subtext_y(body_text_13_y, body_font.get_height(), 1)

    body_text_15_x = body_text_1_x
    body_text_15_y = position_subtext_y(body_text_14_y, body_font.get_height(), 1)

    body_text_16_x = body_text_1_x
    body_text_16_y = position_subtext_y(body_text_15_y, body_font.get_height(), 1)

    body_text_17_x = body_text_1_x
    body_text_17_y = position_subtext_y(body_text_16_y, body_font.get_height(), 1)

    body_text_18_x = body_text_1_x
    body_text_18_y = position_subtext_y(body_text_17_y, body_font.get_height(), 1)

    body_text_19_x = body_text_1_x
    body_text_19_y = position_subtext_y(body_text_18_y, body_font.get_height(), 1)

    body_text_20_x = body_text_1_x
    body_text_20_y = position_subtext_y(body_text_19_y, body_font.get_height(), 1)

    body_text_21_x = body_text_1_x
    body_text_21_y = position_subtext_y(body_text_20_y, body_font.get_height(), 1)


    running = True
    while running:
        screen.fill(BACKGROUND)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, TITLE_COLOR, (title_rect.left, line_y),(title_rect.right, line_y), 1)        

        screen.blit(body_text_1, (body_text_1_x, body_text_1_y))
        screen.blit(body_text_2, (body_text_2_x, body_text_2_y))
        screen.blit(body_text_3, (body_text_3_x, body_text_3_y))
        screen.blit(body_text_4, (body_text_4_x, body_text_4_y))
        screen.blit(body_text_5, (body_text_5_x, body_text_5_y))
        screen.blit(body_text_6, (body_text_6_x, body_text_6_y))
        screen.blit(body_text_7, (body_text_7_x, body_text_7_y))
        screen.blit(body_text_8, (body_text_8_x, body_text_8_y))
        screen.blit(body_text_9, (body_text_9_x, body_text_9_y))
        screen.blit(body_text_10, (body_text_10_x, body_text_10_y))
        screen.blit(body_text_11, (body_text_11_x, body_text_11_y))
        screen.blit(body_text_12, (body_text_12_x, body_text_12_y))
        screen.blit(body_text_13, (body_text_13_x, body_text_13_y))
        screen.blit(body_text_14, (body_text_14_x, body_text_14_y))
        screen.blit(body_text_15, (body_text_15_x, body_text_15_y))
        screen.blit(body_text_16, (body_text_16_x, body_text_16_y))
        screen.blit(body_text_17, (body_text_17_x, body_text_17_y))
        screen.blit(body_text_18, (body_text_18_x, body_text_18_y))
        screen.blit(body_text_19, (body_text_19_x, body_text_19_y))
        screen.blit(body_text_20, (body_text_20_x, body_text_20_y))
        screen.blit(body_text_21, (body_text_21_x, body_text_21_y))

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
                
############################################################################################################################################################################################################################

# START of ending_creds
def sign_off(screen): # From KINGDOM1.INC (lines 471-493)

    # Font setup
    text_font = load_font(10)
    
    # Render text elements
    title = text_font.render("KINGDOM OF KROZ II", True, GRAY)
    subtitle = text_font.render("An Apogee Software Production", True, GRAY)
    subtitle2 = text_font.render("Other great games available from Scott Miller:", True, GRAY)
    
    paragraphs1 = ["Six more Kroz games! KINGDOM OF KROZ I, CAVERNS OF KROZ, DUNGEONS OF KROZ,",
        "   RETURN OF KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.",
        "   Each volume is just $7.50, or order all six for $35",]
    
    paragraphs2 = ["SUPERNOVA - Explore a galaxy and save a planet from an exploding star!",
        "   An epic adventure rated by shareware Magazine as one of the best games",
        "   ever! Highly advanced game has graphics, sound effects galore, clue",
        "   command, and dozens of unique features. ($10)",
        "",
        "BEYOND THE TITANIC - A fantastic adventure of exploration and survival.",
        "   What really happened? Sound effects and 16 color screens. ($8)",
        "",
        "WORD WHIZ - New game that challenges your knowledge of the English",
        "   language. Fun to play, yet very educational, too. ($5)"]
    
    paragraphs3 = ["THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best",
        "   levels yet! Built-in contest! New features galore. ($20)"]
    
    # Square bullet logic
    start_x, start_y = 30, 240
    line_spacing = 25
    bullet_size = 8
    
    text_rect = title.get_rect(center=(WIDTH // 2, 30))
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(title, text_rect)
        screen.blit(subtitle, (250, 50))
        screen.blit(subtitle2, (0, 110))
        
        # Paragraph 1
        y_pos = 130
        for text in paragraphs1:
            y_pos += 20
            if paragraphs1[0]:
                pygame.draw.rect(screen, WHITE, (start_x + 5, y_pos + 2, bullet_size, bullet_size))
            text_surface = text_font.render(text, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))
        
        # Paragraph 2
        for i, text in enumerate(paragraphs2):
            y_pos = start_y + i * line_spacing
            if i == 1:
                pygame.draw.rect(screen, GRAY, (start_x + 5, y_pos + 2, bullet_size, bullet_size))
            text_surface = text_font.render(text, False, GRAY)
            screen.blit(text_surface, (start_x + 20, y_pos))
        
        # Paragraph 3
        y_pos = 500
        for text in paragraphs3:
            y_pos += 20
            if paragraphs3[0]:
                pygame.draw.rect(screen, WHITE, (start_x + 5, y_pos + 2, bullet_size, bullet_size))
            text_surface = text_font.render(text, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    running = False
                    pygame.quit()  # Terminate pygame
                    exit()  # Immediately exit the program after sign_off
                    

############################################################################################################################################################################################################################

# START of load
def load(screen, color_user_input): # From KINGDOM3.INC (lines 141-495) includes other screens


    if color_user_input == "M":  # change to grayscale
        RED = (128, 128, 128)
        BLUE = (128, 128, 128)
        YELLOW = (255, 255, 255)
        CYAN = (128, 128, 128)
        WHITE = (255, 255, 255)
        BROWN = (128, 128, 128)
        GREEN = (128, 128, 128)
    else:
        RED = (144, 13, 13)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        CYAN = (0, 255, 255)
        WHITE = (255, 255, 255)
        BROWN = (139, 69, 19)
        GREEN = (0, 128, 0)

    # Store user input
    load_selection = ""

    # Font setup
    title_font = load_font(13)  # Larger font for title
    text_font = load_font(10)   # Default font

    # Paragraph 
    para1 = ["THIS GAME MAY BE DISTRIBUTED BY SHAREWARE OR PUBLIC DOMAIN LIBRARIES,",
        " OR BULLETING BOARD SYSTEMS. NO NEED TO INQUIRE FOR WRITTEN PERMISSION."]
    
    # List of choices
    choice_list = ["Begin your descent into Kroz...",
        "Instructions",
        "Marketing Kroz",
        "Story behind Kroz",
        "Original Kroz Games",
        "About the Author"]

    # Font render
    title_surface = title_font.render("KINGDOM OF KROZ II", True, WHITE)
    subtext1 = text_font.render("Copyright (c) 1990 Apogee Softwate Productions", True, BROWN)
    subtext2 = text_font.render("Version 2.0 -- by Scott Miller", True, BROWN)
    selector = text_font.render("Your choice (B, I, M, O, A)?", True, WHITE)

    # Center all the text on screen
    title_rect = title_surface.get_rect(midtop=(WIDTH // 2, 20))
    subtext1_rect = subtext1.get_rect(midtop=(WIDTH // 2, 75))
    subtext2_rect = subtext2.get_rect(midtop=(WIDTH // 2, 115))
    selector_x = WIDTH // 2 - 140  # For blinking cursor mechanics
    selector_y = HEIGHT / 1.114 # (624(height) / 560) 

    # Keymap to prevent a long list of elif statements
    key_map = {
        pygame.K_b: "b",
        pygame.K_i: "i",
        pygame.K_m: "m",
        pygame.K_s: "s",
        pygame.K_o: "o",
        pygame.K_a: "a"
    }

    # Cursor properties
    cursor_visible = True
    cursor_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cursor_timer, 150)  # Toggle every 150ms

    # Event Handling
    running = True
    while running:
        screen.fill((0, 0, 0))

        # Title and subtext
        screen.blit(title_surface, title_rect)
        screen.blit(subtext1, subtext1_rect)
        screen.blit(subtext2, subtext2_rect)

        # Paragraph 1
        y_offset1 = 160  # Start after subtext1
        for line in para1:
            line_surface = text_font.render(line, True, GREEN)
            line_rect = line_surface.get_rect(midtop=(WIDTH // 2, y_offset1))
            screen.blit(line_surface, line_rect)
            y_offset1 += 20

        # Horizontal line below paragraph 1
        line_y = y_offset1 + 8
        pygame.draw.line(screen, RED, (0, line_y), (WIDTH, line_y), 1)

        # List of choices
        y_offset2 = y_offset1 + 65
        for choice in choice_list:
            first_letter_surface = text_font.render(choice[0], True, YELLOW)
            rest_surface = text_font.render(choice[1:], True, CYAN)
            first_rect = first_letter_surface.get_rect(bottomleft=(WIDTH // 2 - 100, y_offset2))
            rest_rect = rest_surface.get_rect(bottomleft=(first_rect.right, y_offset2))
            screen.blit(first_letter_surface, first_rect)
            screen.blit(rest_surface, rest_rect)
            y_offset2 += 50

        # Elongated blue rectangle and selector text
        pygame.draw.rect(screen, BLUE, (selector_x, selector_y - 3, selector.get_width() + 20, 16))

        screen.blit(selector, (selector_x, selector_y))

        # Draw blinking "B"
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, (selector_x  + selector.get_width() + 4, selector_y - 3, 16, 16))
            blinking_b = text_font.render("B", True, BLUE)
        else:
            blinking_b = text_font.render("B", True, WHITE)
        screen.blit(blinking_b, (selector_x + selector.get_width() + 8, selector_y))

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_b:
                            return "b"
                        case pygame.K_i:
                            return "i"
                        case pygame.K_m:
                            return "m"
                        case pygame.K_s:
                            return "s"
                        case pygame.K_o:
                            return "o"
                        case pygame.K_a:
                            return "a"
                        case pygame.K_r:
                            return "r"
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
        pygame.display.update()
# END of load                

def run_all_screens(screen):
    color_user_input = color(screen)
    # speed_user_input = speed(screen, color_user_input)
    # title(screen, color_user_input)
    # difficulty(screen, color_user_input)
    # shareware(screen, color_user_input)
    user_choice = load(screen, color_user_input)
    
    # This runs and proccess the loading screen along with screens in load()
    startGame = True
    while startGame: 
        match(user_choice): 
            case "b":
                print(f"Choice: B")
                descent()                
                levels(screen)
                startGame = False
            case "i":
                print(f"Choice: I")
                instructions_1(screen, color_user_input)
                instructions_2(screen, color_user_input)
                instructions_3(screen, color_user_input)
                instructions_4(screen, color_user_input)
                user_choice = load(screen, color_user_input) # return to load() until "b" is pressed
            case "m":
                print(f"Choice: M")
                marketing(screen, color_user_input)
                user_choice = load(screen, color_user_input) 
            case "s":
                print(f"Choice: S")
                story_1(screen, color_user_input)
                story_2(screen, color_user_input)
                user_choice = load(screen, color_user_input) 
            case "o":
                print(f"Choice: O")
                original(screen, color_user_input)
                user_choice = load(screen, color_user_input)
            case "a":
                print(f"Choice: A")
                about(screen, color_user_input)
                user_choice = load(screen, color_user_input)