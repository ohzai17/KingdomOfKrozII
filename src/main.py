from title_screens import *

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((832, 624))
    run_all_screens(screen)
    end_screen(screen)
    pygame.quit()