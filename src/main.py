from screens import *

if __name__ == "__main__":

    pygame.init()
<<<<<<< HEAD
    pygame.mixer.init()
=======
>>>>>>> 55b80a57edd6b6c2126747f03c98113db20fd74a
    screen = pygame.display.set_mode((832, 624))
    pygame.display.set_caption("Kingdom of Kroz II")
    run_all_screens(screen)
    end_screen(screen)
    pygame.quit()