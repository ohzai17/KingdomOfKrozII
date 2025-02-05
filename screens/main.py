import color_mode
import pc_speed
import title
import difficulty  

def main():
    color = color_mode.choose_color_mode()
    if color is None:
        return  # Exit if user quits

    speed = pc_speed.choose_pc_speed()
    if speed is None:
        return  # Exit if user quits

    title.title(color)  # Pass color mode to the title screen

    player_level = difficulty.information_screen(color)  # Call the function and store the result
    if player_level is None:
        return  # Exit if user quits

if __name__ == "__main__":
    main()