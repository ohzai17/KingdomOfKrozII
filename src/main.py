from title_screens import *
from levels.gameplay import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((832, 624))
    run_all_title_screens(screen)
    level(screen)
    pygame.quit()