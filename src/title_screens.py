from utils import *

def color(screen): # From KINGDOM4.INC (line 66)
    
    WIDTH, HEIGHT = screen.get_size()

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
                            running = False
                        case _:
                            running = False
                    print("Color:" , color_user_input)
    return color_user_input

############################################################################################################################################################################################################################

def speed(screen, color_user_input): # From KINGDOM4.INC (line 87)
    
    WIDTH, HEIGHT = screen.get_size()

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
                            running = False
                        case _:
                            running = False
                    print("Speed:" , speed_user_input)
    return speed_user_input

############################################################################################################################################################################################################################

def title(screen, color_user_input): # From KINGDOM3.INC (line 64)

    # Use the dimensions of the passed screen
    WIDTH, HEIGHT = screen.get_size()

    # Logo setup
    logo = pygame.image.load("assets/kroz_logo.png").convert_alpha()
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
                    running = False
                    
############################################################################################################################################################################################################################

def difficulty(screen, color_user_input): # From KINGDOM3.INC (line 86)
    
    WIDTH, HEIGHT = screen.get_size()

    # Fonts
    title_font, heading_font, subtext_font, footer_font = load_fonts([WIDTH // 50, WIDTH // 80, WIDTH // 80, WIDTH // 80])

    # Player icon setup
    player_icon = pygame.image.load("assets/player_icon.png").convert_alpha()
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
                            case pygame.K_a:
                                difficulty_user_input = 'A'
                                blinking_difficulty_text = "ADVANCED"
                            case pygame.K_x:
                                difficulty_user_input = 'X'
                                blinking_difficulty_text = "SECRET MODE"
                            case _:
                                blinking_difficulty_text = "NOVICE"
                        print("Difficulty:" , difficulty_user_input)
                    else:
                        return difficulty_user_input

############################################################################################################################################################################################################################


def run_all_title_screens(screen):
    color_user_input = color(screen)
    speed_user_input = speed(screen, color_user_input)
    title(screen, color_user_input)
    difficulty(screen, color_user_input)