import pygame

# Initialize Pygame
pygame.init()

# Set the initial window size and make it resizable
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Text Adjustment Example")

# Load the font
title_font = pygame.font.Font("screens/assets/RobotoMono-Regular.ttf", 20)

# Render the text to a surface with the initial font size
text_surface = title_font.render("Your Title", True, (255, 255, 255))  # White color
original_width, original_height = text_surface.get_size()

# Set the position for the text
x_pos = 100
y_pos = 50

# Function to scale text based on window size (both width and height)
def scale_text(window_width, window_height):
    # Scale based on the initial window size
    scale_factor_width = window_width / 800  # Original window width (800 is the starting width)
    scale_factor_height = window_height / 600  # Original window height (600 is the starting height)
    
    # New width and height based on the scale factors
    new_width = int(original_width * scale_factor_width)
    new_height = int(original_height * scale_factor_height)
    
    return pygame.transform.scale(text_surface, (new_width, new_height))

# Initial scaling based on the initial window size
scaled_surface = scale_text(window_width, window_height)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            # Update the window size when resized
            window_width, window_height = event.size
            screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

            # Update the scaled text when the window size changes
            scaled_surface = scale_text(window_width, window_height)

    # Fill the screen with a background color
    screen.fill((0, 0, 0))  # Black background

    # Place the scaled text surface on the screen
    screen.blit(scaled_surface, (x_pos, y_pos))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
