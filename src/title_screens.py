import random
from utils import *

############################################################################################################################################################################################################################

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
    logo = pygame.image.load("/KingdomOfKrozII/assets/kroz_logo.png").convert_alpha()
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
    player_icon = pygame.image.load("/KingdomOfKrozII/assets/player_icon.png").convert_alpha()
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

# START of info_screen1
def info_screen1(screen, color_user_input):

    WIDTH, HEIGHT = screen.get_size()

    if color_user_input == "M":  # Monochrome mode
        YELLOW = (255, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (0, 0, 0)
        OLD_BLUE = (0, 0, 0)
    else:
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        WHITE2 = (0, 0, 0)
        OLD_BLUE = (44, 0, 180)

    # Random rectangle Colors to cycle through 
    colors = rect_colors
    rand_color = random.choice(colors)

    # Font setup
    title_font = load_font(13)
    text_font = load_font(10)

    title = title_font.render("KINGDOM OF KROZ II -  REGISTER", True, WHITE)
    prompt_text = text_font.render("Press any key to continue", True, WHITE)
   
    paragraph1 = ["  This is not a shareware game, but it is user-supported. If you enjoy this",
        "game, you are asked by the author to please send a registration ",
        "check in the amount of $7.50 to Apogee Software.",
        "  This registration fee will qualify you to order any of the other Kroz",
        "volumes available:"]

    kroz_volumes = ["Caverns of Kroz   - the first discovery of Kroz",
        "Dungeons of Kroz  - the dark side of Kroz, fast-paced action", 
        "Kingdom of Kroz I - the national contest winner (\"Best Game\" in 1988)",
        "Return of Kroz    - the discovery of entirely  new underground chambers",
        "Temple of Kroz    - the bizarre side of Kroz, nothing is what is seems",
        "The Final Crusade of Kroz - the surprising finish?"]

    paragraph2 = ["Each gam is priced $7.50 each, any three for $20, or all six for only $35.",
        "You'll also get a secret code that makes this game easier to complete,",
        "Plus a \"Hints Tricks and Scoring Secrets\" guide and \"The Domain of Kroz\" map.",
        " ",
        " ",
        "Please make checks payable to:",
        " ",
        "Address is always valid!",
        " ",
        "Thank you and enjoy the game.  -- Scott Miller"] 

    check_info = ["apogee Software     (phone: 214/240-0614)",
        "4206 Mayflower",
        "Garland, TX 75045   (USA)"]

    # Atrributes for square bullet
    start_x, start_y = 30, 190
    line_spacing = 25
    bullet_size = 8

    title_rect = title.get_rect(center=(WIDTH // 2, 10))

    running = True
    clock = pygame.time.Clock()
    while running:

        screen.fill(OLD_BLUE) 

        screen.blit(title, title_rect) # Title
        
        # Horizontal line under title
        line_y = title_rect.bottom + 8
        pygame.draw.line(screen, GRAY, (0, line_y), (WIDTH, line_y), 1)
        
        # Paragraph 1
        y_offset = line_y + 10
        for line in paragraph1:
            rendered_line = text_font.render(line, True, GRAY)
            screen.blit(rendered_line, (2, y_offset))
            y_offset += 20

        # Paragraph of Kroz Volumes
        for i, name in enumerate(kroz_volumes):
            y_pos = start_y + i * line_spacing
            pygame.draw.rect(screen, WHITE, (start_x, y_pos, bullet_size, bullet_size))
            text_surface = text_font.render(name, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))

        # Paragraph 2
        y_offset = 380
        for index, line in enumerate(paragraph2):
            if index == 7:
                rendered_line = text_font.render(line, True, WHITE) # loop to single out a line
            else:
                rendered_line = text_font.render(line, True, GRAY)
            screen.blit(rendered_line, (2, y_offset))
            y_offset += 20
        
        # Check information
        y_offset = 480
        for line in check_info:
            rendered_line = text_font.render(line, True, YELLOW)
            screen.blit(rendered_line, (320, y_offset))
            y_offset += 20

        # Random color rectangle
        pygame.draw.rect(screen, rand_color, (0, HEIGHT - 17, WIDTH, 17)) # (x, y, width, height)

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                running = False
        clock.tick(60)
# END of info_screen1 

# START of instruction1
def instruction1(screen, color_user_input):

    WIDTH, HEIGHT = screen.get_size()

    if color_user_input == "M":  # change to grayscale
        YELLOW = (255, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
    else:
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)

    pygame.font.init()
    title_font = load_font(13)
    text_font = load_font(10)

    title = title_font.render("THE INSTRUCTIONS", True, YELLOW)
    prompt_text = text_font.render("Press any key to continue", True, WHITE2)

    paragraphs = [
    "   Kingdom of Kroz is a game of exploration and survival. Your journey will",
    "take you through 25 very dangerous chambers, each riddled with diabolical",
    "traps and hideous creatures. Hidden in the deepest chamber lies a hidden",
    "treasure of immense value. Use the cursor pad to move 8 directions.",
    "   The chambers contain dozens of treasures, spells, traps and other unknowns.",
    "Touching an object for the first time will reveal a little of its identity,",
    "but it will be left to you to decide how best to use it--or avoid it.",
    "   When a creature touches you it will vanish, taking with it a few of your",
    "gems that you have collected. If you have no gems then the creature will",
    "instead take your life! Whips can be used to kill nearby creatures, but",
    "they're better used to smash through \"breakable walls\" and other terrain.",
    "   Laptop and PCjr players can",
    "use the alternate cursor             U I O      ( NW N NE )",
    "pad instead of the cursor             J K       (   W E   )",
    "keys to move your man, plus          N M ,      ( SW S SE )",
    "the four normal cursor keys.",
    "  It's a good idea to save your game at every new level, therefore, if you die",
    "you can easily restore the game at that level and try again.",
    "Registered users will get a \"secret code\" that makes this game much easier!"
    ]

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    running = True
    while running:
        screen.fill(OLD_BLUE)

        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15  # Horizontal ine
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y), (title_rect.right, line_y), 1)
        
        # Paragraphs
        y_offset = 95
        for line in paragraphs:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (15, y_offset))
            y_offset += 23

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                    running = False
# END of instruction1       

# START of instruction2
def instruction2(screen, color_user_input):
    
    WIDTH, HEIGHT = screen.get_size()

    if color_user_input == "M":  # change to grayscale
        YELLOW = (255, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
    else:
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)

    # Font setup
    pygame.font.init()
    title_font = load_font(13)
    text_font = load_font(10)
    
    title = title_font.render("THE INSTRUCTIONS", True, YELLOW)
    prompt_text = text_font.render("Press any key to continue", True, WHITE2)

    paragraph1 = ["   Kingdom of Kroz will present you with many challenges. You will venture deep",
                  " underground and probably not make it out alive!"]

    paragraph2 = [" Hints:    Don't forget to use the Home, End, PgUp, and PgDn keys to move your",
                  "           on-screen character diagonally (along with the marked cursor keys)." ]

    paragraph3 = ["           Use your player to touch each new object to find out about it.  When",
                  "           you first touch an object a message appears at the bottom of the",
                  "           screen that describes it."]
    
    line1 =  "           Collect keys to unlock doors, which usually block the stairs."

    paragraph4 = ["           The faster monsters are the most dangerous to touch--they will knock",
                  "           off three of your valuable gems.  The slowest creatures only take a",
                  "           single gem from you, and the medium speed monsters take two."]

    paragraph5 = ["   Some levels have a Magical Gravity that will pull you downward!  On these",
                  " levels the game is played as if viewing the level from a side angle.  On",
                  " these levels you can only move upward by using a rope, a secret tunnel, or",
                  " by using a teleport scroll.  These unique \"Sideways Levels\" may take a",
                  " little getting used to, but are well worth the effort.  At the beginning of",
                  " a \"sideways\" level a message at the bottom of the screen will alert you."]

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    running = True
    while running:
        screen.fill(OLD_BLUE)  # Background color
        
        screen.blit(title, title_rect)  # Draw title

        line_y = title_rect.bottom + 15 # Draw line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y),(title_rect.right, line_y), 1)

        # Paragraph 1
        blit_x = 3
        blit_y = 95
        for line in paragraph1:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Paragraph 2
        blit_y = blit_y + 25
        for line in paragraph2:
            if line == paragraph2[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface,(blit_x, blit_y))
            blit_y += 23

        # Paragraph 3
        blit_y = blit_y + 15
        for line in paragraph3:
            if line == paragraph3[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        
        # line1
        blit_y += 15
        text_surface = text_font.render(line1, True, WHITE)
        pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size))
        screen.blit(text_surface,(blit_x, blit_y))
        blit_y += 23
        
        # Paragraph 5
        blit_y = blit_y + 15
        for line in paragraph4:
            if line == paragraph5[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size)) 
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Paragraph 6
        blit_y = blit_y + 25
        for line in paragraph5:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instruction2

# START of instruction3
def instruction3(screen, color_user_input):

    WIDTH, HEIGHT = screen.get_size()

    if color_user_input == "M":  # change to grayscale
        YELLOW = (255, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
    else:
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)

    # Font setup
    pygame.font.init()
    title_font = load_font(13)
    text_font = load_font(10)
    
    title = title_font.render("THE INSTRUCTIONS", True, YELLOW)
    prompt_text = text_font.render("Press any key to continue", True, WHITE2)

    paragraph1 = [ "   Here are some brief descriptions of the most common objects that you are",
    " likely to find in the Kingdom of Kroz:" ]

    paragraph2 = ["       - this is you, a dauntless archaeologist without peer",
                  "       - red creatures move slow and only knock off 1 gem when touched",
                  "       - green creatures move faster and knock off 2 gems when touched",
                  "       - blue creatures move fastest and knock off 3 gems when touched",
                  "       - collect all the gems you can to survive creature attacks",
                  "       - whips are used to wipe out creatures and smash certain walls",
                  "       - teleport spells will magically transport you to a random place",
                  "       - chests contain a random number of gems and whips",
                  "       - collect keys to go through doors (')",
                  "       - collect these power rings to make your whips more powerful",
                  "       - these tablets will give you clues, advice and warnings",
                  "       - this might be anything, including a big pouch of gems!",
                  "       - stairs take you to the next level deeper in Kroz" ]
    
    paragraph3 = ["   There are dozens and dozens of other objects to discover.  The best way",
                  " to learn the usefulness of any new object is to touch it and read the brief",
                  " message that appears at the bottom of the screen."]

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    running = True
    while running:

        screen.fill(OLD_BLUE)  # 
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y),(title_rect.right, line_y), 1)

        # Paragraph 1
        blit_x = 3
        blit_y = 95
        for line in paragraph1:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Paragraph 2
        blit_y = blit_y + 25
        for line in paragraph2:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface,(blit_x, blit_y))
            blit_y += 23

        # Paragraph 3
        blit_y = blit_y + 20
        for line in paragraph3:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Display all the image icons
        display_icons(screen)

        # Flashing text
        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instruction3  

# START of instruction4
def instruction4(screen, color_user_input):

    WIDTH, HEIGHT = screen.get_size()

    if color_user_input == "M":  # change to grayscale
        YELLOW = (255, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
    else:
        YELLOW = (255, 255, 0)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)

    # Font setup
    title_font = load_font(13)
    text_font = load_font(10)
    
    # Font render
    title = title_font.render("MISCELLANEOUS", True, YELLOW)
    prompt_text = text_font.render("Press any key to continue", True, WHITE2)

    paragraph1 = [ "  You can now save three different levels during a single game. When you",
    "  select the 'save' command you will also be asked to enter a letter, either",
    "  A, B or C. If you just hit the space bar then A is the default selection.",
    "  These letters do not refer to disk drives! They actually refer to the file",
    "  names used by the game. The restore command lets you pick from A, B or C." ]

    paragraph2 = [ "  Sideways levels can be recognized by the pause message that appears at",
    "  the bottom of the screen, which states that it's a 'sideways' level." ]

    paragraph3 = [ "  If you are tired of seeing the descriptions at the bottom of the screen",
    "  that appear whenever you touch a new object, you can disable most of the",
    "  messages by pressing the minus (-) key. The plus key (+) resets messages." ]

    paragraph4 = [ "  Kingdom of Kroz II is a completely updated and improved version over the",
    "  original version of Kingdom of Kroz. If you desire to play the original",
    "  Kingdom of Kroz, please send $7.50. Over 17 levels are different!" ]

    title_rect = title.get_rect(center=(WIDTH // 2, 30))

    running = True
    while running:
        screen.fill(OLD_BLUE)
        
        screen.blit(title, title_rect)  # Title

        line_y = title_rect.bottom + 15 # Line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y),(title_rect.right, line_y), 1)

        # Paragraph 1
        blit_x = 3
        blit_y = 110
        for line in paragraph1:
            if line == paragraph1[0]: # Adds a square bullet to 1st line
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Paragraph 2
        blit_y = blit_y + 30
        for line in paragraph2:
            if line == paragraph2[0]: # Adds a square bullet to 1st line
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface,(blit_x, blit_y))
            blit_y += 23

        # Paragraph 3
        blit_y = blit_y + 30
        for line in paragraph3:
            if line == paragraph3[0]: # Adds a square bullet to 1st line
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        
        # Paragraph 4
        blit_y = blit_y + 30
        for line in paragraph4:
            if line == paragraph4[0]: # Adds a square bullet to 1st line
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instruction4 

# START of load
def load(screen, color_user_input):

    WIDTH, HEIGHT = screen.get_size()

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
    user_input2 = ""

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
            if event.type == pygame.QUIT:
                running = False
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    user_input2 = key_map[event.key]
                    print(f"Key pressed: {user_input2}")
                    return user_input2
        pygame.display.update()
# END of load 

# START of ending_creds
def ending_creds(screen):
    # Use the provided screen
    WIDTH, HEIGHT = screen.get_size()

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
        "   An epic adventure rated by Shareware Magazine as one of the best games",
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
                pygame.draw.rect(screen, WHITE, (start_x, y_pos, bullet_size, bullet_size))
            text_surface = text_font.render(text, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))
        
        # Paragraph 2
        for i, text in enumerate(paragraphs2):
            y_pos = start_y + i * line_spacing
            if i == 1:
                pygame.draw.rect(screen, GRAY, (start_x, y_pos, bullet_size, bullet_size))
            text_surface = text_font.render(text, False, GRAY)
            screen.blit(text_surface, (start_x + 20, y_pos))
        
        # Paragraph 3
        y_pos = 500
        for text in paragraphs3:
            y_pos += 20
            if paragraphs3[0]:
                pygame.draw.rect(screen, WHITE, (start_x, y_pos, bullet_size, bullet_size))
            text_surface = text_font.render(text, False, WHITE)
            screen.blit(text_surface, (start_x + 20, y_pos))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
# END of ending_creds

def run_all_title_screens(screen):
    color_user_input = color(screen)
    speed_user_input = speed(screen, color_user_input)
    title(screen, color_user_input)
    difficulty(screen, color_user_input)
    info_screen1(screen, color_user_input)
    user_choice = load(screen, color_user_input)
    
    # This runs and proccess the loading screen along with screens in load()
    run = True
    while run: 
        match(user_choice):
            case "b":
                print(f"Choice: {user_choice}")
                run = False
            case "i":
                print(f"Choice: {user_choice}")
                instruction1(screen, color_user_input)
                instruction2(screen, color_user_input)
                instruction3(screen, color_user_input)
                instruction4(screen, color_user_input)
                user_choice = load(screen, color_user_input) # return to load() until "b" is pressed
            case "m":
                print(f"Choice: {user_choice}")
                user_choice = load(screen, color_user_input) # return to load() until "b" is pressed
            case "s":
                print(f"Choice: {user_choice}")
                user_choice = load(screen, color_user_input) # return to load() until "b" is pressed
            case "a":
                print(f"Choice: {user_choice}")
                user_choice = load(screen, color_user_input) # return to load() until "b" is pressed