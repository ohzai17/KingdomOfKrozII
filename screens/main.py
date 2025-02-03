import color
import speed
import title
import difficulty  # Import your information_screen function
import game_info
import ending_credits

def main():
    colorFunc = color.choose_color_mode()
    if color is None:
        return  # Exit if user quits

    speedFunc = speed.choose_pc_speed()
    if speed is None:
        return  # Exit if user quits

    title.title(color)  # Pass color mode to the title screen

    player_level = difficulty.information_screen()  # Call the function and store the result
    if player_level is None:
        return  # Exit if user quits
    
    infoFunc = game_info.info_screen1() # General info, displayes after choosing the difficulty
    
    
    endingFunc = ending_credits.ending_creds() # ENDING CREDITS, this function is placed here temporarily
 
if __name__ == "__main__":
    main()

