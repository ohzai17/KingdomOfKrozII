import pygame

TILE_HEIGHT = 14
# START ****NEED TO ADD FUNCTIONS & COLORS FROM UTIL, importing is not working at the moment****
def init_screen(screen, WIDTH, HEIGHT, values=None):  # Modified to accept values parameter
    # Blue rectangle
    pygame.draw.rect(screen, (8, 4, 180), (0, (TILE_HEIGHT * 23) + 20, WIDTH, HEIGHT - (TILE_HEIGHT * 23)))

    # Use provided values if available, otherwise use defaults
    if values is None:
        # Default values (all zeros)
        Score = 0
        Level = 0
        Gems = 0
        Whips = 0
        Teleports = 0
        Keys = 0
        values = [Score, Level, Gems, Whips, Teleports, Keys]

    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Options"]
    option_list = ["Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]

    pygame.font.init()
    font = pygame.font.Font("src/assets/PressStart2P - Regular.ttf", 14)  
    
    word_x = 50  # Starting X position for the words
    word_y = (TILE_HEIGHT * 23) + 30  # Y position (intentional gap between map)

    rect_width = 80  # Fixed width of the gray rectangles
    rect_height = 30  # Height of the gray rectangle

    for i, word in enumerate(item_tracker):
        
        match(word): # Display items
            case ("Options"): # Rendered differently
                word_x += 40
                word_surface = font.render(word, True, (0, 255, 255))
                pygame.draw.rect(screen, (140, 0, 0), (word_x - 1, word_y - 8, word_surface.get_width() + 1, 30))
                screen.blit(word_surface, (word_x, word_y))
            case _: 
                word_surface = font.render(word, True, (254, 254, 6))
                screen.blit(word_surface, (word_x, word_y))

        if i < len(values): # Display values and gray box
            value_surface = font.render(str(values[i]), True, (140, 0, 0))
            value_x = word_x + (rect_width - value_surface.get_width()) // 2
            if item_tracker[i] == "Teleports":  # handled differently due to placement issues
                value_x = value_x + 25
                word_x = word_x + 25
                pygame.draw.rect(screen, (169, 169, 169), (word_x, word_y + word_surface.get_height() + 10, rect_width, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17)) # Value
                word_x = word_x - 25
            else:
                pygame.draw.rect(screen, (169, 169, 169), (word_x, word_y + word_surface.get_height() + 10, rect_width, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17)) # Value
        
        # Update word_x based on word width
        word_x += word_surface.get_width() + 30

    y_offset = word_y + 30  # Start position of the options_list (below "Options")
    for choice in option_list:
        first_letter_surface = font.render(choice[0], True, (254, 254, 254))
        rest_surface = font.render(choice[1:], True, (169, 169, 169))

        first_rect = first_letter_surface.get_rect(topleft=(word_x - 130, y_offset))
        rest_rect = rest_surface.get_rect(topleft=(first_rect.right, y_offset))

        screen.blit(first_letter_surface, first_rect)
        screen.blit(rest_surface, rest_rect)
        
        # Move the y_offset down
        y_offset += 20
# END of init_screen