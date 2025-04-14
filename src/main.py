from screens import *
from gameplay import *

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Kingdom of Kroz II")
    run_all_screens(screen)
    pygame.quit()