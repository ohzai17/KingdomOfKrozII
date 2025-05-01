import utils
from utilities.texts import *
from audio import *
from utilities.draw_text import draw_text
import gameplay as gp
from utilities.game_text import scale_loaded_sprites

############################################################################################################################################################################################################################

def color(): # From KINGDOM4.INC (line 66)

    color_input = "C"
    running = True
    
    while running:
        screen.fill(BLACK)

        draw_text(2, game_title, LIGHT_BLUE)
        draw_text(10, color_heading)
        draw_text(10, color_cursor, None, True)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_m:
                            color_input = "M"
                            set_monochrome_palette()
                            play_sound(500, 30)
                            running = False
                        case _:
                            play_sound(500, 30)                            
                            running = False
                    print("Color:" , color_input)

    return color_input

############################################################################################################################################################################################################################

def speed(color_input): # From KINGDOM4.INC (line 87)

    speed_user_input = "S"
    running = True
    
    while running:
        screen.fill(BLACK)

        if color_input == "C":
            draw_text(2, game_title, LIGHT_BLUE)
        
        draw_text(14, speed_heading_1)
        draw_text(14, speed_cursor, None, True)
        draw_text(17, speed_subtext_1, LIGHT_GRAY)
        draw_text(19, speed_subtext_2, LIGHT_GRAY)
        draw_text(21, speed_subtext_3, LIGHT_GRAY)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
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

def title(color_input): # From KINGDOM3.INC (line 64)

    logo = pygame.image.load(logo_path).convert_alpha()
    aspect_ratio = logo.get_height() / logo.get_width()
    logo_height = CHAR_HEIGHT * 13
    logo_width = logo_height / aspect_ratio
    logo = pygame.transform.scale(logo, (logo_width, logo_height))

    time_elapsed = 0
    running = True
    
    while running:
        screen.fill(BLACK)

        time_elapsed += 1 

        colorized_logo = change_logo_color(logo, time_elapsed, color_input)
        logo_x = ((GRID_WIDTH * CHAR_WIDTH) - logo_width) // 2
        logo_y = 4 * CHAR_HEIGHT
        screen.blit(colorized_logo, (logo_x, logo_y))

        draw_text(2, title_heading_1)
        draw_text(19, title_subtext_1, YELLOW)
        draw_text(21, title_subtext_2, YELLOW)
        draw_text(23, title_subtext_3, YELLOW)
        draw_text(25, press_any_key_dot, LIGHT_CYAN)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case pygame.KEYDOWN:
                    play_sound(220, 100)
                    running = False
                    
############################################################################################################################################################################################################################

def difficulty(BACKGROUND): # From KINGDOM3.INC (line 86)

    blinking_difficulty_text = ""
    running = True
    
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, difficulty_title, "CHANGING", False, True, RED, True)
        draw_text(5, difficulty_heading_1)
        draw_text(7, difficulty_heading_2)
        draw_text(9, difficulty_subtext_1, LIGHT_CYAN)
        draw_text(10, difficulty_subtext_2, LIGHT_CYAN)
        draw_text(11, difficulty_subtext_3, LIGHT_CYAN)
        draw_text(12, difficulty_subtext_4, LIGHT_CYAN)
        draw_text(13, difficulty_subtext_5, LIGHT_CYAN)
        draw_text(14, difficulty_subtext_6, LIGHT_CYAN)
        draw_text(17, difficulty_subtext_7, LIGHT_GREEN)
        draw_text(17, difficulty_subtext_7a)
        draw_text(18, difficulty_subtext_8, LIGHT_GREEN)
        draw_text(19, difficulty_subtext_9, LIGHT_GREEN)
        draw_text(20, difficulty_subtext_10, LIGHT_GREEN)
        if blinking_difficulty_text == "":
            draw_text(22, difficulty_heading_3_1, YELLOW)
            draw_text(22, difficulty_heading_3_2)
            draw_text(22, difficulty_cursor, BROWN, True)
        else:
            draw_text(22, blinking_difficulty_text, YELLOW, True)
            draw_text(25, difficulty_footer, LIGHT_GRAY)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    return None
                case pygame.KEYDOWN:
                    if blinking_difficulty_text == "":
                        match event.key:
                            case pygame.K_e:
                                difficulty_input = 'E'
                                blinking_difficulty_text = "EXPERIENCED"
                                play_sound(300, 100)
                                play_sound(700, 100)
                            case pygame.K_a:
                                difficulty_input = 'A'
                                blinking_difficulty_text = "ADVANCED"
                                play_sound(300, 100)
                                play_sound(700, 100)                                
                            case pygame.K_x:
                                difficulty_input = 'X'
                                blinking_difficulty_text = "SECRET MODE  "
                                play_sound(300, 100)
                                play_sound(700, 100)                                
                            case _:
                                difficulty_input = 'N'
                                blinking_difficulty_text = "NOVICE"
                                play_sound(300, 100)
                                play_sound(700, 100)
                        print("Difficulty:" , difficulty_input)
                    else:
                        return difficulty_input

############################################################################################################################################################################################################################

# START of shareware (info_screen)
def shareware(BACKGROUND): # From KINGDOM3.INC (lines 495-541)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(1, shareware_title)
        draw_text(2, "—" * 82)
        draw_text(22, shareware_line22, None, False, False)

        for i, line in enumerate(shareware_paragraph_1):
            row = 3 + i
            draw_text(row, line, LIGHT_GRAY, False, False)

        for i, line in enumerate(shareware_kroz_volumes):
            row = 9 + i
            draw_text(row, line, None, False, False)

        for i, line in enumerate(shareware_paragraph_2):
            row = 16 + i
            draw_text(row, line, LIGHT_GRAY, False, False)

        for i, line in enumerate(shareware_check_info):
            row = 20 + i
            draw_text(row, line, YELLOW, False, False)

        draw_text(25, "█" * 82, rand_color)
        draw_text(25, press_any_key_dot, BLACK, True)

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
def instructions_1(BACKGROUND): #
    
    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, instructions_title, YELLOW)
        draw_text(3, instructions_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(instruction1_paragraphs):
            row = 5 + i
            draw_text(row, line, None, False, False)

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
def instructions_2(BACKGROUND): #

        
    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, instructions_title, YELLOW)
        draw_text(3, instructions_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(instruction2_paragraphs):
            row = 5 + i
            draw_text(row, line, None, False, False)

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
def instructions_3(BACKGROUND):

    running = True
    while running:
        screen.fill(BACKGROUND)
        
        draw_text(2, instructions_title, YELLOW)
        draw_text(3, instructions_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(instruction3_paragraphs):
            row = 4 + i
            draw_text(row, line, None, False, False)

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
def instructions_4(BACKGROUND): #

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, instruction4_title, YELLOW)
        draw_text(3, instruction4_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(instruction4_paragraphs):
            row = 6 + i
            draw_text(row, line, None, False, False)

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

def marketing(BACKGROUND): # From KINGDOM3.INC (line 348)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, marketing_title, YELLOW)
        draw_text(3, marketing_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(marketing_paragraphs):
            row = 5 + i
            draw_text(row, line, None, False, False)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False

############################################################################################################################################################################################################################

def story_1(BACKGROUND): # From KINGDOM4.INC (line 379)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, story_title, YELLOW)
        draw_text(3, story_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(story1_paragraphs):
            row = 5 + i
            draw_text(row, line, None, False, False)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False

############################################################################################################################################################################################################################

def story_2(BACKGROUND): # From KINGDOM4.INC (line 379)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, story_title, YELLOW)
        draw_text(3, story_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(story2_paragraphs):
            row = 5 + i
            draw_text(row, line, None, False, False)

        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False

############################################################################################################################################################################################################################

def original(BACKGROUND): # From KINGDOM4.INC (line 438)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, original_title, YELLOW)
        draw_text(3, original_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(original_paragraphs):
            row = 5 + i
            draw_text(row, line, None, False, False)
        
        pygame.display.update()  # Refresh the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
############################################################################################################################################################################################################################

def about(BACKGROUND): # From KINGDOM4.INC (line 467)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, about_title, YELLOW)
        draw_text(3, about_subtitle, YELLOW)
        draw_text(25, press_any_key_dot, "CHANGING")

        for i, line in enumerate(about_paragraphs):
            row = 4 + i
            draw_text(row, line, None, False, False)

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
def sign_off(): # From KINGDOM1.INC (lines 471-493)
    
    running = True
    while running:
        screen.fill(BLACK)

        draw_text(2, game_title, LIGHT_GRAY)
        draw_text(3, ending_subtitle_1, LIGHT_GRAY)
        draw_text(5, ending_subtitle_2, LIGHT_GRAY, False, False)


        for i, line in enumerate(ending_paragraphs_1):
            row = 7 + i
            draw_text(row, line, None, False, False)

        for i, line in enumerate(ending_paragraphs_2):
            row = 11 + i
            draw_text(row, line, LIGHT_GRAY, False, False)

        for i, line in enumerate(ending_paragraphs_3):
            row = 22 + i
            draw_text(row, line, None, False, False)
        
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

def hud_selector(): # Returns "O" or "R", which maps to bottom or right HUD
    global TILE_HEIGHT, TILE_WIDTH
    screen.fill(BLACK)
    draw_text(4, "SELECT HUD STYLE", text_color=YELLOW, center=True)

    # Load HUD preview images
    bottom_hud_image = pygame.image.load(os.path.join("src", "assets", "original_hud.png")).convert_alpha()
    right_hud_image = pygame.image.load(os.path.join("src", "assets", "right_hud.png")).convert_alpha()

    # Resize images
    image_width, image_height = 400, 280
    bottom_hud_image = pygame.transform.scale(bottom_hud_image, (image_width, image_height))
    right_hud_image = pygame.transform.scale(right_hud_image, (image_width, image_height))

    # Define positions
    left_x = 70
    right_x = WIDTH - image_width - 70
    image_y = 150

    # Blit images
    screen.blit(bottom_hud_image, (left_x, image_y))
    screen.blit(right_hud_image, (right_x, image_y))

    # Approximate row to be below the images (based on your layout)
    draw_text(23, "       ]O] UPDATED UI(BOTTOM)", text_color=WHITE, center=False)
    draw_text(23, "                                             ]R] ORIGINAL UI(SIDEBAR)", text_color=WHITE, center=True)

    pygame.display.flip()

    selecting = True

    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    hud_input = "O"
                    utils.TILE_WIDTH, utils.TILE_HEIGHT = WIDTH // 66, WIDTH // 66
                    gp.GP_TILE_WIDTH, gp.GP_TILE_HEIGHT = utils.TILE_WIDTH, utils.TILE_HEIGHT
                    selecting = False
                elif event.key == pygame.K_r:
                    hud_input = "R"
                    utils.TILE_HEIGHT = HEIGHT // 25
                    utils.TILE_WIDTH = int(utils.TILE_HEIGHT / (16 / 9))
                    gp.GP_TILE_WIDTH, gp.GP_TILE_HEIGHT = utils.TILE_WIDTH, utils.TILE_HEIGHT
                    selecting = False

    return hud_input


# START of load
def load(): # From KINGDOM3.INC (lines 141-495) includes other screens

    # Store user input
    load_selection = ""

    # Keymap to prevent a long list of elif statements
    key_map = {
        pygame.K_b: "b",
        pygame.K_i: "i",
        pygame.K_m: "m",
        pygame.K_s: "s",
        pygame.K_o: "o",
        pygame.K_a: "a",
        pygame.K_r: "r"
    }

    # Event Handling
    running = True
    while running:
        screen.fill(BLACK)

        draw_text(2, game_title)
        draw_text(4, load_subtext_1, BROWN)
        draw_text(6, load_subtext_2, BROWN)
        draw_text(10, "—" * 82, RED)
        draw_text(24, load_selector, None, False, False, BLUE)
        draw_text(24, load_cursor, None, True, False) #investigate cursor size
        draw_text(24, load_pad, BLACK, False, False)

        for i, line in enumerate(load_paragraph):
            row = 8 + i
            draw_text(row, line, GREEN)

        for i, line in enumerate(load_choice_list): #investigate color
            row = 12 + i
            draw_text(row, line, (85, 255, 255))

        for i, line in enumerate(load_choice_list2):
            row = 12 + i
            draw_text(row, line, YELLOW)


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


############################################################################################################################################################################################################################

def leaderboard_screen(score, level_num):
    """Displays the leaderboard screen."""
    leaderboard = load_leaderboard()
    user_input = ""  # Initialize user input
    leaderboard_pad = "█████████████"  # Initial pad
    backspace_held = False  # Track if backspace is held
    backspace_timer = 0  # Timer for backspace hold
    running = True

    # Determine the position of the current run
    current_run_position = None
    for i, entry in enumerate(leaderboard):
        if entry["name"] == "Adventurer" and entry["score"] == score and entry["level"] == level_num:
            current_run_position = i + 1  # 1-based index
            break

    while running:
        screen.fill(BLACK)

        draw_text(2, game_title, LIGHT_BLUE)  # Display the game title
        draw_text(4, leaderboard_headers, LIGHT_CYAN)
        draw_text(22, leaderboard_prompt, RED, False, True, LIGHT_GRAY)

        # Draw leaderboard entries with aligned numbers
        for i, entry in enumerate(leaderboard):
            row = 6 + i
            color = LIGHT_RED if i % 2 == 0 else LIGHT_MAGENTA
            number = f"{i + 1:>2}"  # Right-align numbers to ensure proper spacing
            draw_text(row, f"{number} {entry['name']:<20}{entry['score']:<15}{entry['level']:<5}", color)

            # Adjust the pad position based on the current run position
            if current_run_position:
                if current_run_position <= 6 and i == 5:  # Move pad below the 6th player
                    draw_text(row + 1, 21 * " " + leaderboard_pad, LIGHT_RED, False, False, None)
                elif current_run_position > 6 and i == current_run_position - 1:  # Move pad above the current run
                    draw_text(row - 1, 21 * " " + leaderboard_pad, LIGHT_RED, False, False, None)

        # Adjust cursor position based on user input length
        cursor_position = 21 + len(user_input)
        draw_text(11, 21 * " " + leaderboard_pad, RED, False, False, None)
        draw_text(11, cursor_position * " " + leaderboard_cursor, LIGHT_RED, True, False, None)
        
        # Display user input and dynamic pad
        if len(user_input) > 13:
            leaderboard_pad = "█" * (len(user_input) + 1)
        draw_text(11, 21 * " " + user_input, WHITE, False, False, None)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Exit on Enter key
                        running = False
                    elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                        backspace_held = True
                        backspace_timer = pygame.time.get_ticks()
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode  # Append typed character
                case pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        backspace_held = False

        # Handle continuous backspace when held
        if backspace_held and pygame.time.get_ticks() - backspace_timer > 100:
            user_input = user_input[:-1]
            backspace_timer = pygame.time.get_ticks()

    # Update leaderboard with the new score
    leaderboard = update_leaderboard(leaderboard, user_input.strip() or "Adventurer", score, level_num)
    save_leaderboard(leaderboard)

    # Blinking popup for another game at the bottom of the leaderboard
    popup_running = True
    while popup_running:
        draw_text(24, leaderboard_transtion, WHITE, True, True)  # Bottom message
        pygame.display.flip()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_y:  # User wants to play again
                        popup_running = False
                        user_choice = load()  # Return to load screen
                        process_user_choice(user_choice)  # Reuse the function
                    elif event.key == pygame.K_n:  # User does not want to play again
                        popup_running = False
                        sign_off() 
                    
                    
def load_leaderboard():
    """Load the leaderboard from a file."""
    if os.path.exists(leaderboard_path):
        with open(leaderboard_path, "r") as file:
            return json.load(file)
    return [{"name": "Scott Miller", "score": 136400, "level": 16},
            {"name": "I. Jones", "score": 85740, "level": 14},
            {"name": "Terry Nagy", "score": 69950, "level": 11},
            {"name": "Neil Peart", "score": 35010, "level": 8},
            {"name": "Banzai Boyd", "score": 12280, "level": 5}] + [{"name": "Adventurer", "score": 0, "level": 0} for _ in range(10)]

def save_leaderboard(leaderboard):
    """Save the leaderboard to a file."""
    with open(leaderboard_path, "w") as file:
        json.dump(leaderboard, file, indent=1)  # Compact format

def update_leaderboard(leaderboard, name, score, level):
    """Update the leaderboard with the player's score."""
    leaderboard.append({"name": name, "score": score, "level": level})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)  # Sort by score descending
    return leaderboard[:15]  # Keep only the top 15 entries

############################################################################################################################################################################################################################                    

def process_user_choice(user_choice, hud_input, difficulty_input, color_input):
    """Handle user choices and navigate through the game screens."""
    startGame = True
    while startGame:
        match user_choice:
            case "b":
                print(f"Choice: B")
                descent()
                gp.levels(difficulty_input, color_input, hud_input, mixUp=False)
                startGame = False
            case "i":
                print(f"Choice: I")
                instructions_1(BACKGROUND)
                instructions_2(BACKGROUND)
                instructions_3(BACKGROUND)
                instructions_4(BACKGROUND)
                user_choice = load()
            case "m":
                print(f"Choice: M")
                marketing(BACKGROUND)
                user_choice = load()
            case "s":
                print(f"Choice: S")
                story_1(BACKGROUND)
                story_2(BACKGROUND)
                user_choice = load()
            case "o":
                print(f"Choice: O")
                original(BACKGROUND)
                user_choice = load()
            case "a":
                print(f"Choice: A")
                about(BACKGROUND)
                user_choice = load()
            case "r":
                print(f"Choice: R")
                descent()
                gp.levels(difficulty_input, color_input, hud_input, mixUp=True)
                startGame = False
    sign_off()

def run_all_screens():
    color_input = color()
    speed_user_input = speed(color_input)
    title(color_input)
    difficulty(BACKGROUND)
    shareware(BACKGROUND)
    utils.hud_input = hud_selector()
    scale_loaded_sprites()
    gp.scale_gameplay_sprites((TILE_WIDTH, TILE_HEIGHT), color_input)
    user_choice = load()
    process_user_choice(user_choice, utils.hud_input, difficulty_input, color_input)