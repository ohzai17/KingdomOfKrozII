import color_mode
import pc_speed
import title
import difficulty
import functions  

def main():

    color = color_mode.choose_color_mode()
    if color is None:
        return  

    speed = pc_speed.choose_pc_speed(color)
    if speed is None:
        return  

    title.title(color)  

    difficulty_level = difficulty.choose_difficulty(color)  
    if difficulty_level is None:
        return  

if __name__ == "__main__":
    main()