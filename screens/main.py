import color
import speed
import title
import difficulty  # Import your information_screen function

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

if __name__ == "__main__":
    main()

