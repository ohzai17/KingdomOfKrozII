import pygame
import color
import speed
import title
import difficulty
import game_info
import ending_credits
import load_level

def main():
    pygame.init()

    # Create a single window that will be shared across modules
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Kingdom of Kroz II")

    # Step 1: Choose Color Mode (using the single window)
    color_choice = color.choose_color_mode(screen)
    if color_choice is None:
        pygame.quit()
        return

    # Step 2: Choose PC Speed
    speed_choice = speed.choose_pc_speed(screen)
    if speed_choice is None:
        pygame.quit()
        return

    # Step 3: Display Title
    title.title(screen, color_choice)

    # Step 4: Choose Difficulty
    player_level = difficulty.information_screen(screen, color_choice)
    if player_level is None:
        pygame.quit()
        return

    # Step 5: Display Game Info
    game_info.info_screen1(screen, color_choice)

    # Step 6: Load Level
    choice = load_level.load(screen, color_choice)
    if choice == "b":
        print("Start Game!!")
    elif choice == "i":
        print("Instructions")
    elif choice == "m":
        print("Marketing")
    elif choice == "o":
        print("Story")
    elif choice == "a":
        print("Author")

    # Step 7: Show Ending Credits
    ending_credits.ending_creds(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
