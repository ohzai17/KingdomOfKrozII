from screens import *

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((832, 624))
    pygame.display.set_caption("Kingdom of Kroz II")
    run_all_screens(screen)
    Sign_Off(screen)
    pygame.quit()