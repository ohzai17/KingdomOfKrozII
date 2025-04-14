from utils import screen, pygame
from screens import run_all_screens, sign_off
from gameplay import levels

if __name__ == "__main__":

    run_all_screens(screen)
    levels(screen)
    sign_off(screen)
    pygame.quit()