<<<<<<< HEAD:Cycles/Arch Spike/screens/main.py
import pygame
import color_mode
import pc_speed
import title
import difficulty
=======
import color
import speed
import title
import difficulty  # Import your information_screen function
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/main.py
import game_info
import ending_credits
import load_level

def main():
<<<<<<< HEAD:Cycles/Arch Spike/screens/main.py
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
    print(difficulty_level)
    if difficulty_level is None:
        return  

    # Step 5: Display Game Info
    game_info.info_screen1(screen, color)

    # Step 6: Load Level
    choice = load_level.load(screen, color)
=======
    colorFunc = color.choose_color_mode()
    if color is None:
        return  # Exit if user quits

    speedFunc = speed.choose_pc_speed()
    if speed is None:
        return  # Exit if user quits

    title.title(color)  # Pass color mode to the title screen

    player_level = difficulty.information_screen(color)  # Call the function and store the result
    if player_level is None:
        return  # Exit if user quits
    
    infoFunc = game_info.info_screen1() # General info, displayes after choosing the difficulty

    choice = load_level.load()
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/main.py
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

<<<<<<< HEAD:Cycles/Arch Spike/screens/main.py
    # Step 7: Show Ending Credits
    ending_credits.ending_creds(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
=======
    endingFunc = ending_credits.ending_creds() # ENDING CREDITS, this function is placed here temporarily
    
if __name__ == "__main__":
    main()
>>>>>>> df025a4 (Revert "Moving files due to merge conflict"):screens/main.py
