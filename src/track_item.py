import pygame
from utils import *

# START of init_screen
def Init_screen(screen, WIDTH, HEIGHT, values=None): # From KINGDOM4.INC (lines 96-183)

    pygame.draw.rect(screen, BLUE, (0, (TILE_HEIGHT * 23) + 20, WIDTH, HEIGHT - (TILE_HEIGHT * 23)))

    # Use provided values if available, otherwise use defaults
    if values is None:
        Score = 0
        Level = 0
        Gems = 0
        Whips = 0
        Teleports = 0
        Keys = 0
        values = [Score, Level, Gems, Whips, Teleports, Keys]

    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Options"]
    option_list = ["Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]

    font = load_font(14)  
    
    word_x = 50  # Starting X coordinate of words
    word_y = (TILE_HEIGHT * 23) + 30  # Y coordinate

    rect_width = 80  # Width of gray rec
    rect_height = 30  # Height of gray re

    for i, word in enumerate(item_tracker):
        
        match(word): # Display items
            case ("Options"): # Rendered differently
                word_x += 40
                word_surface = font.render(word, True, CYAN)
                pygame.draw.rect(screen, DARK_RED, (word_x - 1, word_y - 8, word_surface.get_width() + 1, 30))
                screen.blit(word_surface, (word_x, word_y))
            case _: 
                word_surface = font.render(word, True, (254, 254, 6))
                screen.blit(word_surface, (word_x, word_y))

        if i < len(values): # Values and gray box
            value_surface = font.render(str(values[i]), True, DARK_RED)
            value_x = word_x + (rect_width - value_surface.get_width()) // 2
            if item_tracker[i] == "Teleports":  # handled differently due to placement issues
                value_x = value_x + 25
                word_x = word_x + 25
                pygame.draw.rect(screen, LIGHT_GRAY, (word_x, word_y + word_surface.get_height() + 10, rect_width, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17)) # Value
                word_x = word_x - 25
            else:
                pygame.draw.rect(screen, LIGHT_GRAY, (word_x, word_y + word_surface.get_height() + 10, rect_width, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17)) # Value
        
        # Update word_x based on word width
        word_x += word_surface.get_width() + 30

    y_offset = word_y + 30  # Start position of the options_list (below "Options")
    for choice in option_list:
        first_letter_surface = font.render(choice[0], True, WHITE)
        rest_surface = font.render(choice[1:], True, GRAY)

        first_rect = first_letter_surface.get_rect(topleft=(word_x - 130, y_offset))
        rest_rect = rest_surface.get_rect(topleft=(first_rect.right, y_offset))

        screen.blit(first_letter_surface, first_rect)
        screen.blit(rest_surface, rest_rect)
        
        # Move the y_offset down
        y_offset += 20
# END of init_screen