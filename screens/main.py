import pygame
import color_mode
import pc_speed
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

    # Step 1: Choose Color Mode
    color = color_mode.choose_color_mode(screen)
    if color is None:
        return  

    # Step 2: Choose PC Speed
    speed = pc_speed.choose_pc_speed(screen, color)
    if speed is None:
        return  

    # Step 3: Display Title
    title.title(screen, color)  

    # Step 4: Choose Difficulty
    difficulty_level = difficulty.choose_difficulty(screen, color)  
    if difficulty_level is None:
        return  

    # Step 5: Display Game Info
    game_info.info_screen1(screen, color)

    # Step 6: Load Level
    choice = load_level.load(screen, color)
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
