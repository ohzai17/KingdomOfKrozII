import pygame
from utils import *

def pause(screen, quitting=False): # From KINGDOM3.INC (lines 495-541)
    paused = True

    while paused:
        # Choose text dynamically
        message = "Are you sure you want to quit (Y/N)?" if quitting else "Press any key to Resume"
        flash_color(screen, message)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if quitting:
                    if event.key == pygame.K_y: 
                        pygame.quit()
                        exit()
                    else:
                        paused = False  # Cancel quit prompt, stay in pause mode
                else:
                    paused = False  # Resume game