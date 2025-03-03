from title_screens import *

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((832, 624))
    run_all_title_screens(screen)
    # Removed level from main, now it's only called when user inputs "b" in load() function.
    Sign_Off(screen) # Ending credits
    pygame.quit()