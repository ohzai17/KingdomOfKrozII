import pygame

from game_functions import *

# START of load
color = "M"
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
def load(screen, color):
    # Use the existing main window
    WIDTH, HEIGHT = screen.get_size()

    if color == "M":  # change to grayscale
        RED = (128, 128, 128)
        BLUE = (128, 128, 128)
        YELLOW = (255, 255, 255)
        CYAN = (128, 128, 128)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
        BROWN = (128, 128, 128)
        GREEN = (128, 128, 128)
    else:
        RED = (144, 13, 13)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        CYAN = (0, 255, 255)
        WHITE = (255, 255, 255)
        WHITE2 = (255, 255, 255)
        BROWN = (139, 69, 19)
        GREEN = (0, 128, 0)

    # Store user input
    user_input2 = ""

    # Font setup
    pygame.font.init()
    title_font = pygame.font.Font("C:/KingdomOfKrozII/screens/assets/RobotoMono-Regular.ttf", 20)  # Larger font for title
    text_font = pygame.font.Font("C:/KingdomOfKrozII/screens/assets/RobotoMono-Regular.ttf", 16)   # Default font

    # Paragraph 
    para1 = [
        "THIS GAME MAY BE DISTRIBUTED BY SHAREWARE OR PUBLIC DOMAIN LIBRARIES,",
        " OR BULLETING BOARD SYSTEMS. NO NEED TO INQUIRE FOR WRITTEN PERMISSION."
    ]
    
    # List of choices
    choice_list = [
        "Begin your descent into Kroz...",
        "Instructions",
        "Marketing Kroz",
        "Story behind Kroz",
        "Original Kroz Games",
        "About the Author"
    ]

    # Font render
    title_surface = title_font.render("KINGDOM OF KROZ II", True, WHITE)
    subtext1 = text_font.render("Copyright (c) 1990 Apogee Softwate Productions", True, BROWN)
    subtext2 = text_font.render("Version 2.0 -- by Scott Miller", True, BROWN)
    selector = text_font.render("Your choice (B, I, M, O, A)?", True, WHITE)

    # Center all the text on screen
    title_rect = title_surface.get_rect(midtop=(WIDTH // 2, 20))
    subtext1_rect = subtext1.get_rect(midtop=(WIDTH // 2, 75))
    subtext2_rect = subtext2.get_rect(midtop=(WIDTH // 2, 115))
    selector_x = WIDTH // 2 - 130  # For blinking cursor mechanics
    selector_y = 550

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

    # Main loop
    running = True
    while running:
        screen.fill((0, 0, 0))

        # Draw title and subtext
        screen.blit(title_surface, title_rect)
        screen.blit(subtext1, subtext1_rect)
        screen.blit(subtext2, subtext2_rect)

        # Position and draw paragraphs
        y_offset1 = 160  # Start after subtext1
        for line in para1:
            line_surface = text_font.render(line, True, GREEN)
            line_rect = line_surface.get_rect(midtop=(WIDTH // 2, y_offset1))
            screen.blit(line_surface, line_rect)
            y_offset1 += 20

        # Draw a horizontal line under the paragraphs
        line_y = y_offset1 + 8
        pygame.draw.line(screen, RED, (0, line_y), (WIDTH, line_y), 1)

        # Draw list of choices
        y_offset2 = y_offset1 + 65
        for choice in choice_list:
            first_letter_surface = text_font.render(choice[0], True, YELLOW)
            rest_surface = text_font.render(choice[1:], True, CYAN)
            first_rect = first_letter_surface.get_rect(bottomleft=(WIDTH // 2 - 100, y_offset2))
            rest_rect = rest_surface.get_rect(bottomleft=(first_rect.right, y_offset2))
            screen.blit(first_letter_surface, first_rect)
            screen.blit(rest_surface, rest_rect)
            y_offset2 += 50

        # Draw elongated blue rectangle and selector text
        pygame.draw.rect(screen, BLUE, (selector_x, selector_y, 300, 22))
        screen.blit(selector, (selector_x, selector_y))

        # Draw blinking "B"
        if cursor_visible:
            pygame.draw.rect(screen, WHITE, (selector_x + selector.get_width() + 4, selector_y, 16, 22))
            blinking_b = text_font.render("B", True, BLUE)
        else:
            blinking_b = text_font.render("B", True, WHITE)
        screen.blit(blinking_b, (selector_x + selector.get_width() + 8, selector_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE: 
                WIDTH, HEIGHT = event.size
                # Update text scaling if needed using your scale functions.
                title_surface = scale_title(title_surface, WIDTH, HEIGHT)
                subtext1 = scale_text(subtext1, WIDTH, HEIGHT)
            elif event.type == cursor_timer:
                cursor_visible = not cursor_visible
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    user_input2 = key_map[event.key]
                    return user_input2

        pygame.display.update()
# END of load


# START of instruction1
def instruction1(screen, color):
    # Font setup
    WIDTH, HEIGHT = 800, 600
    pygame.font.init()
    title_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 13)
    text_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 10)

    clock = pygame.time.Clock()  # Create the clock object

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
        screen.fill(OLD_BLUE)  # Background color

        screen.blit(title, title_rect)  # Draw title

        line_y = title_rect.bottom + 15  # Draw line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y), (title_rect.right, line_y), 1)

        # Draw paragraphs
        y_offset = 95
        for line in paragraphs:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (15, y_offset))
            y_offset += 23

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                    running = False
# END of instruction1       


# START of instruction2
def instruction2(screen, color):
    clock = pygame.time.Clock()  # Create the clock object
    WIDTH, HEIGHT = screen.get_size()

    # Font setup
    pygame.font.init()
    title_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 13)
    text_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 10)
    
    title = title_font.render("THE INSTRUCTIONS", True, YELLOW)
    prompt_text = text_font.render("Press any key to continue", True, WHITE2)

    paragraph1 = [
    "   Kingdom of Kroz will present you with many challenges. You will venture deep",
    " underground and probably not make it out alive!"
]
    paragraph2 = [" Hints:    Don't forget to use the Home, End, PgUp, and PgDn keys to move your",
                  "           on-screen character diagonally (along with the marked cursor keys)." ]

    paragraph3 = ["           Use your player to touch each new object to find out about it.  When",
                  "           you first touch an object a message appears at the bottom of the",
                  "           screen that describes it."]
    
    paragraph4 = "           Collect keys to unlock doors, which usually block the stairs."

    paragraph5 = ["           The faster monsters are the most dangerous to touch--they will knock",
                  "           off three of your valuable gems.  The slowest creatures only take a",
                  "           single gem from you, and the medium speed monsters take two."]

    paragraph6 = ["   Some levels have a Magical Gravity that will pull you downward!  On these",
                  " levels the game is played as if viewing the level from a side angle.  On",
                  " these levels you can only move upward by using a rope, a secret tunnel, or",
                  " by using a teleport scroll.  These unique \"Sideways Levels\" may take a",
                  " little getting used to, but are well worth the effort.  At the beginning of",
                  " a \"sideways\" level a message at the bottom of the screen will alert you."]

    title_rect = title.get_rect(center=(WIDTH // 2, 30))
    square_size = 8

    running = True
    while running:
        screen.fill(OLD_BLUE)  # Background color
        
        screen.blit(title, title_rect)  # Draw title

        line_y = title_rect.bottom + 15 # Draw line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y),(title_rect.right, line_y), 1)

        # Draw paragraph 1
        blit_x = 3
        blit_y = 95
        for line in paragraph1:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 2
        blit_y = blit_y + 25
        for line in paragraph2:
            if line == paragraph2[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface,(blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 3
        blit_y = blit_y + 15
        for line in paragraph3:
            if line == paragraph3[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        
        # Draw paragraph 4(no for loop, single line)
        blit_y += 15
        text_surface = text_font.render(paragraph4, True, WHITE)
        pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size))
        screen.blit(text_surface,(blit_x, blit_y))
        blit_y += 23
        
        # Draw paragraph 5
        blit_y = blit_y + 15
        for line in paragraph5:
            if line == paragraph5[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 93, blit_y + 2, square_size, square_size)) 
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 6
        blit_y = blit_y + 25
        for line in paragraph6:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instruction2


# START of instruction3
def instruction3(screen, color):
    clock = pygame.time.Clock()  # Create the clock object
    WIDTH, HEIGHT = screen.get_size()

    # Font setup
    pygame.font.init()
    title_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 13)
    text_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 10)
    
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
        screen.fill(OLD_BLUE)  # Background color
        
        screen.blit(title, title_rect)  # Draw title

        line_y = title_rect.bottom + 15 # Draw line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y),(title_rect.right, line_y), 1)

        # Draw paragraph 1
        blit_x = 3
        blit_y = 95
        for line in paragraph1:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 2
        blit_y = blit_y + 25
        for line in paragraph2:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface,(blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 3
        blit_y = blit_y + 20
        for line in paragraph3:
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        
        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instruction3  


# START of instruction4
def instruction4(screen, color):
    clock = pygame.time.Clock()  # Create the clock object
    WIDTH, HEIGHT = screen.get_size()

    # Font setup
    pygame.font.init()
    title_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 13)
    text_font = pygame.font.Font("assets/PressStart2p-Regular.ttf", 10)
    
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


    title_rect = title.get_rect(center=(WIDTH // 2, 40))
    square_size = 8

    running = True
    while running:
        screen.fill(OLD_BLUE)  # Background color
        
        screen.blit(title, title_rect)  # Draw title

        line_y = title_rect.bottom + 5 # Draw line
        pygame.draw.line(screen, YELLOW, (title_rect.left, line_y),(title_rect.right, line_y), 1)

        # Draw paragraph 1
        blit_x = 3
        blit_y = 110
        for line in paragraph1:
            if line == paragraph1[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 2
        blit_y = blit_y + 30
        for line in paragraph2:
            if line == paragraph2[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface,(blit_x, blit_y))
            blit_y += 23

        # Draw paragraph 3
        blit_y = blit_y + 30
        for line in paragraph3:
            if line == paragraph3[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        
        # Draw paragraph 4(no for loop, single line)
        blit_y = blit_y + 30
        for line in paragraph4:
            if line == paragraph4[0]:
                pygame.draw.rect(screen, WHITE, (blit_x + 5, blit_y + 2, square_size, square_size))
            text_surface = text_font.render(line, True, WHITE)
            screen.blit(text_surface, (blit_x, blit_y))
            blit_y += 23
        

        flash(screen, prompt_text, WIDTH, HEIGHT)

        pygame.display.update()  # Refresh the screen
        clock.tick(60)  # Limit to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                running = False
# END of instruction4  

running = True
while running:
    choice = load(screen, color)
    
    match(choice):
        case "b":
            print("Start Game!!")
        case "i":
            instruction1(screen, color)
            instruction2(screen, color)
            instruction3(screen, color)
            instruction4(screen, color)
        case "m":
            print("Marketing")
        case "o":
            print("Story")
        case "a":
            print("Author")