import pygame
pygame.init()

# Initialize the game window
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Title screen')

# Define colors
BLACK = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Load the button image
button_img = pygame.image.load('C:/KingdomOfKrozII/Title-screen/Images/coffeeCup.png')  # Replace with your image path
button_img = pygame.transform.scale(button_img, (200, 200))  # Resize the image if needed

# Define button area (the rect where the button will be clickable)
button_rect = button_img.get_rect()
button_rect.topleft = (350, 250)  # Position the button at (350, 250)

# Define fonts for text
font = pygame.font.SysFont('Orbitron', 50)
TEXT_COL = (0, 191, 255)  # Deep Sky Blue
TEXT_SHADOW = (12, 103, 137) # Dark blue

# Game variables
game_paused = False

# Define screen states
MAIN_MENU = 0
NEW_SCREEN = 1
GAME_SCREEN = 2
current_screen = MAIN_MENU  # Start at the main menu

# Function to draw text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen

    # Get the mouse position to check if it's hovering over the button
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # If the mouse is hovering over the button, make it semi-transparent
    if button_rect.collidepoint(mouse_x, mouse_y):
        button_img.set_alpha(128)  # Set the alpha to 128 (semi-transparent)
    else:
        button_img.set_alpha(255)  # Set the alpha back to 255 (fully opaque)

    # Display the correct screen based on current_screen
    if current_screen == MAIN_MENU:
        draw_text('KINGDOM OF KROZ II', font, TEXT_SHADOW, 253, 53)
        draw_text('KINGDOM OF KROZ II', font, TEXT_COL, 250, 50)
        draw_text('Click the button below', font, TEXT_COL, 220, 150)
        
        # Draw the button image
        screen.blit(button_img, button_rect)

    elif current_screen == NEW_SCREEN:
        draw_text('This is the New Screen', font, TEXT_COL, 350, 50)
        draw_text('Press B to go back', font, TEXT_COL, 220, 250)

    elif current_screen == GAME_SCREEN:
        draw_text('Game Screen - Playing', font, TEXT_COL, 350, 50)
        draw_text('Press P to pause', font, TEXT_COL, 220, 250)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click on the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_x, mouse_y):  # If the click is inside the button area
                print('Button clicked!')
                current_screen = NEW_SCREEN  # Switch to another screen, for example

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b and current_screen == NEW_SCREEN:  # Go back to main menu
                current_screen = MAIN_MENU
            elif event.key == pygame.K_p and current_screen == GAME_SCREEN:  # Pause game (optional)
                game_paused = not game_paused

    pygame.display.update()  # Update the display

pygame.quit()
