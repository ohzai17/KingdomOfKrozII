import color_mode
import pc_speed
import main_menu

def main():
    color = color_mode.choose_color_mode()
    if color is None:
        return  # Exit if user quits

    speed = pc_speed.choose_pc_speed()
    if speed is None:
        return  # Exit if user quits

    main_menu.main_menu(color)  # Pass color mode to the menu

if __name__ == "__main__":
    main()
