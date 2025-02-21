from title_screens import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    run_all_title_screens(screen) 
    pygame.quit()