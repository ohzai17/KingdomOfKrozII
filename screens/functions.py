# Colors used in the game

BLACK = (0, 0, 0)
BLUE = (8,4,180)
DARK_BLUE = (3, 3, 178)
GREEN = (0, 128, 0)
AQUA = (0, 242, 250)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 66, 77)
YELLOW = (254, 254, 6)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (0, 241, 54)
LIGHT_AQUA = (224, 255, 255)
LIGHT_RED = (255, 182, 193) 
LIGHT_PURPLE = (221, 160, 221)
LIGHT_YELLOW = (255, 255, 224)

color_list = [RED, AQUA, PURPLE, YELLOW, GRAY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
logo_color_list = [RED, AQUA, PURPLE, YELLOW, LIGHT_BLUE, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]
title_color_list = [AQUA, PURPLE, YELLOW, GRAY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_AQUA, LIGHT_RED, LIGHT_PURPLE, LIGHT_YELLOW]

import pygame
import color_mode
import array

# functions

def apply_grayscale(image):
    grayscale_image = pygame.Surface(image.get_size(), pygame.SRCALPHA) # Create alpha channel over image
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r, g, b, a = image.get_at((x, y))
            gray_formula = int(0.299 * r + 0.587 * g + 0.114 * b) # Standard grayscale formula
            gray = min(255, gray_formula + 70) # Increase brightness
            grayscale_image.set_at((x, y), (gray, gray, gray, a))
    return grayscale_image

def change_logo_color(image, time, color_mode):
    if color_mode == "M":
        return apply_grayscale(image)
    else:
        color_index = (time // 150) % len(logo_color_list)
        current_color = logo_color_list[color_index] 
        color_filter = pygame.Surface(image.get_size()) # Create imaging surface
        color_filter.fill(current_color) 
        colorized_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        colorized_image.blit(image, (0, 0)) 
        colorized_image.blit(color_filter, (0, 0), special_flags=pygame.BLEND_RGB_MULT) # Apply color filter
        return colorized_image

def change_title_color(time, color_mode):
    if color_mode == "M":
        return BLACK
    else:
        color_index = (time // 50) % len(title_color_list)
        return title_color_list[color_index]