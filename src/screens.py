from utils import *
from texts import *
from draw_text import draw_text
from gameplay import levels

############################################################################################################################################################################################################################

def color(screen): # From KINGDOM4.INC (line 66)

    color_user_input = "C"
    running = True
    
    while running:
        screen.fill(BLACK)

        draw_text(2, game_title, BLUE)
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
                            color_user_input = "M"
                            set_monochrome_palette()
                            play_sound(500, 30)
                            running = False
                        case _:
                            play_sound(500, 30)                            
                            running = False
                    print("Color:" , color_user_input)

    return color_user_input

############################################################################################################################################################################################################################

def speed(screen, color_user_input): # From KINGDOM4.INC (line 87)

    speed_user_input = "S"
    running = True
    
    while running:
        screen.fill(BLACK)

        if color_user_input == "C":
            draw_text(2, game_title, BLUE)
        
        draw_text(14, speed_heading_1)
        draw_text(14, speed_cursor, None, True)
        draw_text(17, speed_subtext_1, GRAY)
        draw_text(19, speed_subtext_2, GRAY)
        draw_text(21, speed_subtext_3, GRAY)

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

def title(screen, color_user_input): # From KINGDOM3.INC (line 64)

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

        colorized_logo = change_logo_color(logo, time_elapsed, color_user_input)
        logo_x = ((GRID_WIDTH * CHAR_WIDTH) - logo_width) // 2
        logo_y = 4 * CHAR_HEIGHT
        screen.blit(colorized_logo, (logo_x, logo_y))

        draw_text(2, title_heading_1)
        draw_text(19, title_subtext_1, YELLOW)
        draw_text(21, title_subtext_2, YELLOW)
        draw_text(23, title_subtext_3, YELLOW)
        draw_text(25, press_any_key_dot, AQUA)

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

def difficulty(screen, BACKGROUND): # From KINGDOM3.INC (line 86)

    difficulty_user_input = "N"
    blinking_difficulty_text = ""
    running = True
    
    while running:
        screen.fill(BACKGROUND)

        draw_text(2, difficulty_title, "CHANGING", False, True, RED, True)
        draw_text(5, difficulty_heading_1)
        draw_text(7, difficulty_heading_2)
        draw_text(9, difficulty_subtext_1, AQUA)
        draw_text(10, difficulty_subtext_2, AQUA)
        draw_text(11, difficulty_subtext_3, AQUA)
        draw_text(12, difficulty_subtext_4, AQUA)
        draw_text(13, difficulty_subtext_5, AQUA)
        draw_text(14, difficulty_subtext_6, AQUA)
        draw_text(17, difficulty_subtext_7, LIGHT_GREEN)
        draw_text(17, difficulty_subtext_7a)
        draw_text(18, difficulty_subtext_8, LIGHT_GREEN)
        draw_text(19, difficulty_subtext_9, LIGHT_GREEN)
        draw_text(20, difficulty_subtext_10, LIGHT_GREEN)
        if blinking_difficulty_text == "":
            draw_text(22, difficulty_heading_3_1, YELLOW)
            draw_text(22, difficulty_heading_3_2)
            draw_text(22, difficulty_cursor, ORANGE, True)
        else:
            draw_text(22, blinking_difficulty_text, YELLOW, True)
            draw_text(25, difficulty_footer, GRAY)

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
                                blinking_difficulty_text = "SECRET MODE  "
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
def shareware(screen, BACKGROUND): # From KINGDOM3.INC (lines 495-541)

    running = True
    while running:
        screen.fill(BACKGROUND)

        draw_text(1, shareware_title)
        draw_text(2, "—" * 80)
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

        draw_text(25, "█" * 80, rand_color)
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
def instructions_1(screen, BACKGROUND): #
    
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
def instructions_2(screen, BACKGROUND): #

        
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
def instructions_3(screen, BACKGROUND):

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
def instructions_4(screen, BACKGROUND): #

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

def marketing(screen, BACKGROUND): # From KINGDOM3.INC (line 348)

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

def story_1(screen, BACKGROUND): # From KINGDOM4.INC (line 379)

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

def story_2(screen, BACKGROUND): # From KINGDOM4.INC (line 379)

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

def original(screen, BACKGROUND): # From KINGDOM4.INC (line 438)

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

def about(screen, BACKGROUND): # From KINGDOM4.INC (line 467)

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
def sign_off(screen): # From KINGDOM1.INC (lines 471-493)
    
    running = True
    while running:
        screen.fill(BLACK)

        draw_text(2, game_title, GRAY)
        draw_text(3, ending_subtitle_1, GRAY)
        draw_text(5, ending_subtitle_2, GRAY, False, False)


        for i, line in enumerate(ending_paragraphs_1):
            row = 7 + i
            draw_text(row, line, None, False, False)

        for i, line in enumerate(ending_paragraphs_2):
            row = 11 + i
            draw_text(row, line, GRAY, False, False)

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

# START of load
def load(screen): # From KINGDOM3.INC (lines 141-495) includes other screens

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
        draw_text(10, "—" * 80, RED)
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

def run_all_screens(screen):
    #color_user_input = "C"
    color_user_input = color(screen)
    speed_user_input = speed(screen, color_user_input)
    title(screen, color_user_input)
    difficulty(screen, BACKGROUND)
    shareware(screen, BACKGROUND)
    user_choice = load(screen)
    
    # This runs and proccess the loading screen along with screens in load()
    startGame = True
    while startGame: 
        match(user_choice): 
            case "b":
                print(f"Choice: B")
                descent()                
                #levels(screen, difficulty_input)
                startGame = False
            case "i":
                print(f"Choice: I")
                instructions_1(screen, BACKGROUND)
                instructions_2(screen, BACKGROUND)
                instructions_3(screen, BACKGROUND)
                instructions_4(screen, BACKGROUND)
                user_choice = load(screen) # return to load() until "b" is pressed
            case "m":
                print(f"Choice: M")
                marketing(screen, BACKGROUND)
                user_choice = load(screen) 
            case "s":
                print(f"Choice: S")
                story_1(screen, BACKGROUND)
                story_2(screen, BACKGROUND)
                user_choice = load(screen) 
            case "o":
                print(f"Choice: O")
                original(screen, BACKGROUND)
                user_choice = load(screen)
            case "a":
                print(f"Choice: A")
                about(screen, BACKGROUND)
                user_choice = load(screen)
            case "r":
                print(f"Choice: R")
                descent()                
                levels(screen, difficulty_input, mixUp=True)
                startGame = False
    sign_off(screen)