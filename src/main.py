from screens import *

if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((832, 468))
    pygame.display.set_caption("Kingdom of Kroz II")
    run_all_screens(screen)
    pygame.quit()