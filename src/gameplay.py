import pygame
import os
import random
from utils import *

def pause_quit(screen, quitting=False): # From KINGDOM.PAS (lines 49-69)
    paused = True

    while paused:
        message = "Are you sure you want to quit (Y/N)?" if quitting else "Press any key to Resume"
        flash_c(screen, message)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if quitting:
                    if event.key == pygame.K_y:
                        from screens import Sign_Off 
                        Sign_Off(screen)
                        return True
                    else:
                        paused = False
                else:
                    paused = False  # Resume game
                    
    return False  # User didn't quit

def player_death(screen):
    """Handle player death when out of gems"""
    print("you have died")
    
    # Display death message on screen
    draw_text(1, "YOU HAVE DIED!!!", BLACK, True, False, LIGHT_GRAY)
    draw_text(3, "Press any key to continue...", WHITE, False, True, None) # Add prompt
    pygame.display.flip()
    
    # Wait for user input
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting_for_input = False # Exit loop on any key press
                
    # Go to sign-off screen
    from screens import sign_off
    sign_off(screen)
    pygame.quit()
    exit()
                    
def hud(screen, WIDTH, HEIGHT, values=None): # From KINGDOM4.INC (lines 96-183)
    
    pygame.draw.rect(screen, BLUE, (0, (TILE_HEIGHT * 23) + 20, WIDTH, HEIGHT - (TILE_HEIGHT * 23)))


    item_tracker = ["Score", "Level", "Gems", "Whips", "Teleports", "Keys", "Cloaks", "Options"]
    option_list = ["Cloaks", "Whip", "Teleport", "Pause", "Quit", "Save", "Restore"]

    font = load_font(13)  
    
    word_x = 5  # Starting X coordinate of words
    word_y = (TILE_HEIGHT * 23) + 30  # Y coordinate

    rect_width = 78  # Width of gray rec
    rect_height = 30  # Height of gray re

    for i, word in enumerate(item_tracker):
        
        match(word): # Display items
            case ("Options"): # Rendered differently
                word_x += 5
                word_surface = font.render(word, True, CYAN)
                pygame.draw.rect(screen, DARK_RED, (word_x - 1, word_y - 8, word_surface.get_width() + 1, 30))
                screen.blit(word_surface, (word_x, word_y)) 
            case _: 

                word_surface = font.render(word, True, (YELLOW))
                screen.blit(word_surface, (word_x, word_y))

        if i < len(values): # Values and gray box
            if item_tracker[i] == "Teleports":  # handled differently due to placement issues
                value_surface = font.render(str(values[i]), True, DARK_RED)
                box_x = word_x + ((word_surface.get_width() // 2) - (rect_width // 2) - 18)
                value_x = (box_x + ((rect_width - value_surface.get_width()) // 2) + 16)
                pygame.draw.rect(screen, LIGHT_GRAY, (box_x, word_y + word_surface.get_height() + 10, rect_width + 35, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17))
            else:
                value_surface = font.render(str(values[i]), True, DARK_RED)
                box_x = (word_x + (word_surface.get_width() // 2) - (rect_width // 2) + 5)
                value_x = box_x + (rect_width - value_surface.get_width()) // 2
                pygame.draw.rect(screen, LIGHT_GRAY, (box_x, word_y + word_surface.get_height() + 10, rect_width, rect_height))
                screen.blit(value_surface, (value_x, word_y + word_surface.get_height() + 17))

        # Update word_x based on word width
        word_x += word_surface.get_width() + 30

    y_offset = word_y + 30  # Start position of the options_list (below "Options")
    for choice in option_list:
        first_letter_surface = font.render(choice[0], True, WHITE)
        rest_surface = font.render(choice[1:], True, GRAY)

        first_rect = first_letter_surface.get_rect(topleft=(word_x - 120, y_offset))
        rest_rect = rest_surface.get_rect(topleft=(first_rect.right, y_offset))

        screen.blit(first_letter_surface, first_rect)
        screen.blit(rest_surface, rest_rect)
        
        # Move the y_offset down
        y_offset += 20

def levels(screen, difficulty_input, mixUp=False):

    WIDTH, HEIGHT = screen.get_size()
    
    screen.fill(BLACK)

    sprites = ["block", "chest", "enemy1", "enemy2", "enemy3", "gem", "player", "teleport_player","stairs", "teleport", 
               "trap", "wall", "whip", "slowTime", "invisible", "key", "door", "speedTime", "river", 
               "power", "forest", "tree", "bomb", "lava", "pit", "tome", "tunnel", "freeze", "nugget", 
               "quake", "iBlock", "iWall", "iDoor", "stop", "trap2", "zap", "create", "generator", 
               "trap3", "mBlock", "trap4", "showGems", "tablet", "zBlock", "blockSpell", "chance", 
               "statue", "wallVanish", "krozK", "krozR", "krozO", "krozZ", "oWall1", "oWall2", "oWall3", 
               "cWall1", "cWall2", "cWall3", "oSpell1", "oSpell2", "oSpell3", "cSpell1", "cSpell2", 
               "cSpell3", "gBlock", "rock", "eWall", "trap5", "tBlock", "tRock", "tGem", "tBlind", 
               "tWhip", "tGold", "tTree", "rope", "dropRope1", "dropRope2", "dropRope3", "dropRope4", 
               "dropRope5", "amulet", "shootRight", "shootLeft", "trap6", "trap7", "trap8", "trap9", 
               "trap10", "trap11", "trap12", "trap13", "message", "whip1", "whip2", "whip3", "whip4",]

    assets_path = os.path.join("src", "assets")
    images = {}

    special_cases = {
        "enemy1": "enemy1a",
        "enemy2": "enemy2a"
    }
    
    TILE_WIDTH, TILE_HEIGHT = 13, 17

    for sprite in sprites:
        filename = special_cases.get(sprite, sprite) + ".png"
        full_path = os.path.join(assets_path, filename)

        img = pygame.image.load(full_path)
        images[sprite] = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))

    tile_mapping = {
        "X": images["block"],
        "#": images["wall"],
        "C": images["chest"],
        "W": images["whip"],
        "1": images["enemy1"],
        "2": images["enemy2"],
        "3": images["enemy3"],
        "+": images["gem"],
        "T": images["teleport"],
        "_": images["teleport_player"],
        ".": images["trap"],
        "L": images["stairs"],
        "P": images["player"],
        "TP": images["teleport_player"],
        "S": images["slowTime"],
        "I": images["invisible"],
        "K": images["key"],
        "D": images["door"],
        "F": images["speedTime"],
        "R": images["river"],
        "Q": images["power"],
        "/": images["forest"],
        "J": images["tree"],
        "B": images["bomb"],
        "V": images["lava"],
        "=": images["pit"],
        "A": images["tome"],
        "U": images["tunnel"],
        "Z": images["freeze"],
        "*": images["nugget"],
        "E": images["quake"],
        ";": images["iBlock"],
        ":": images["iWall"],
        "`": images["iDoor"],
        "-": images["stop"],
        "@": images["trap2"],
        "%": images["zap"],
        "]": images["create"],
        "G": images["generator"],
        ")": images["trap3"],
        "M": images["mBlock"],
        "(": images["trap4"],
        "&": images["showGems"],
        "!": images["tablet"],
        "O": images["zBlock"],
        "H": images["blockSpell"],
        "?": images["chance"],
        ">": images["statue"],
        "N": images["wallVanish"],
        "<": images["krozK"],
        "[": images["krozR"],
        "|": images["krozO"],
        ",": images["krozZ"],
        "4": images["oWall1"],
        "5": images["oWall2"],
        "6": images["oWall3"],
        "7": images["cWall1"],
        "8": images["cWall2"],
        "9": images["cWall3"],
        "±": images["oSpell1"],
        "≥": images["oSpell2"],
        "≤": images["oSpell3"],
        "⌠": images["cSpell1"],
        "⌡": images["cSpell2"],
        "÷": images["cSpell3"],
        "Y": images["gBlock"],
        "0": images["rock"],
        "~": images["eWall"],
        "$": images["trap5"],
        "æ": images["tBlock"],
        "Æ": images["tRock"],
        "ô": images["tGem"],
        "ö": images["tBlind"],
        "ò": images["tWhip"],
        "û": images["tGold"],
        "ù": images["tTree"],
        "¿": images["rope"],
        "┤": images["dropRope1"],
        "│": images["dropRope2"],
        "┐": images["dropRope3"],
        "┘": images["dropRope4"],
        "╜": images["dropRope5"],
        "â": images["amulet"],
        "»": images["shootRight"],
        "«": images["shootLeft"],
        "α": images["trap6"],
        "β": images["trap7"],
        "┌": images["trap8"],
        "π": images["trap9"],
        "∑": images["trap10"],
        "σ": images["trap11"],
        "μ": images["trap12"],
        "τ": images["trap13"],
        "ⁿ": images["message"],
        "whip1": images["whip1"],
        "whip2": images["whip2"],
        "whip3": images["whip3"],
        "whip4": images["whip4"]
    }

    level1_map = [
        "W W W W             2 2 2 2 2  C  2 2 2 2 2              W W W W",
        "XXXXXXXXXXXXXXXXXXX###########   ###########XXXXXXXXXXXXXXXXXXXX",
        " 1           1                               1                  ",
        "                                    1            XX         1   ",
        "       1            1                           XXXX            ",
        "#        XX                    +                 XX            #",
        "##      XXXX  1                +          1          1        ##",
        "T##      XX               2    +    2                        ##T",
        "T1##                       W   +   W                        ##1T",
        "T########X                 WX     XW             1    X########T",
        ".        X                2WX  P  XW2                 X        .",
        "T########X         1       WX     XW                  X########T",
        "T1##                       W   +   W         1              ##1T",
        "T##                       2    +    2                        ##T",
        "##   1                         +                      XX      ##",
        "#       XX      1      _       +                 1   XXXX     1#",
        "       XXXX                 ##   ##                   XX        ",
        "1       XX                 ##     ##     1        1           1 ",
        "                    1#######       ########                     ",
        "    1         ########11111  +++++  111111########              ",
        "WW     ########+++++        #######         WWWWW########1    WW",
        "########»                    2 2 2                     C########",
        "L2  +  X      ####################################      X  +  2L",
    ]
    level2_map = [
        "Æ                                                           .   ",
        "  2#############################K############################   ",
        "   ##æ  2    2   2 2    2   2  ###  2  2   2    2    2    2##   ",
        "  2##+#2   2   2    2  2 2   2  2 2  2   2 2   2   2    2  ##   ",
        "   ##+#   2  2    2   2   2   2    2    2  2    2    2   2 ##   ",
        "  2##+# 2    2  2   2  2 2 2 2  2 2  2 2 2   2    2   2   2##   ",
        "   ##+#2   2  2   2                            2   2   2   ## W ",
        "  2##+#  2   2   2   XXXXXXXXXXXXXXXXXXXXXXX  2    2  2   2##@@@",
        "   ##+#2   2  2   2  XXXXXXXXXXXXXXXXXXXXXXX    2   2  2   ##   ",
        "  2##+# 2   2  2 2   XXXXXXXXXXXXXXXXXXXXXXX   2  2   2  2 ##   ",
        "   ##+#   2 2 2   2  XXXXXX    -+-    XXXXXX  2 2    2  2  ##   ",
        "  2##+#2   2   2 2   XXXXXX1   -P-   1XXXXXX  2  2 2   2 2 ##   ",
        "   ##+#  2  2  2  2  XXXXXX    -+-    XXXXXX   2  2 2     2##   ",
        "  2##+# 2 2  2  2    XXXXXXXXXXXXXXXXXXXXXXX  2   2   2 2  ##   ",
        "   ##+#2 2    2   2  XXXXXXXXXXXXXXXXXXXXXXX    2  2   2 2 ##   ",
        "  2##+# 2  2  2  2   XXXXXXXXXXXXXXXXXXXXXXX   2    2 2 2  ##   ",
        "   ##+#  2  2 2   2                           2  2   2   2 ##   ",
        "  2##+#2   2    2   2 2  2  2  2 2  2 2  2  2   2   2  2  2##   ",
        "   ##+# 2    2  2  2 2  2   2   2   2  2  2    2    2   2  ##   ",
        "  2##3#   2   2   2   2   2   2   2   2 2    2    2   2   2##@@@",
        "   ##T#2   2     2  2  2 2   2 ###   2   2 2  2    2   2   ##222",
        "   #############################S#######################XXX##@@@",
        "                                                          I##LLL",
    ]
    level4_map = [
        "-..............................3#1#2#3##------;------------;----",
        "-##############################-##1#2#3#-######################-",
        "-#.....----......- I#S###### ##K###1#2#3-#///////1///////////1//",
        "-#.-..-....-....-.# # I####1# ######1#2#-#J1JJJJJJJJJJJJJ1JJJJJJ",
        "-#-.-..-..-.....-.# # # ### ## ##1###1#2-#/////1////////////////",
        "-#-.-.-..-..---..-# # ## # ##1## # ###1#-#CCCJJJJJJJJJ1JJJJJJ1JJ",
        "-#-.-..-.-.-..-..-# # ### ####  ### K##1-#CCC/////1//////1/////K",
        "-#-..--...-....--.# # ##################-#######################",
        "-#-################                                           α ",
        "---3333333333-CC### #F######################XXXXXXXX###α####-##+",
        "################## ###------------------«###############2###-##+",
        "big#######     ## ####22222222222222222#-##-----------###2##-##K",
        "trouble## RRRRR  #######################-##-####U####-####2####+",
        "######## RRRKRRRR #########$;$$$$$$3$T##-##-----------#####2###3",
        "+++++### RR 2 2 RR ####Z###$############-############æ##Q###2###",
        "++T++## RR 2 P  2RR ### #-U--------------###TT.TT####----####2##",
        "+++++## RR2   2 RR ####1#-####################;###############2#",
        "#O#O#### RR 2  2RR #3## #C####3#3#3#3#3#3#3#3#3#3#3#3#3#3#3#3##D",
        "#X#X##### RRR2CRR ##3## # ###@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@###D",
        "#X#X###### RRRRRR ##3## #3##@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##K#D",
        "-----; #### RRR  ### ## ###@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#D",
        "-----# #####   # ##W W# ##@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##@#D",
        "22222#      #####       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#L",
    ]
    level6_map = [
        "---###########RRRRR##W        ############W////1/C//J//JJJJJJJJJ",
        "-U---------Z###RRRRR##7######   ##KK⌠   Z##-//////J///1/JJJJJJUJ",
        "---###########RRRRR##7####### P ######## ###-////////J///JJ1JJJJ",
        "@#############RRRRR#7####                ####-///J/////////JJJJJ",
        "@2#------.###RRRRR##7#W3; ############## #####-////1//J//1///JJJ",
        "@##;-;###.##RRRRR##7##W3; #WWWWWWWWWWW## #2####--//////////J///J",
        "@2#-;;##..##RRRRR##7##W3; ######-####### ##2#####-/////J/////1//",
        "@##;-;##..-##RRRRR##7#### #11111111111## ###2##2##-/////1/////J/",
        "@2#;;-##..#D##RRRRR##7##T #11111111111## #2##2##2##--///////J///",
        "@##;;;##..#D###RRRRR##7####11111111111## ##2##2##2###---///////1",
        "@2#-;;##..#KK###RRRRR##7###11111B11111----)))))))))))#####---///",
        "@##-;;##..#KK##RRRRRRR#7###11111111111##############)########--/",
        "@2#;;;##22####RRRR#RRR##7##11111111111#?#ò#---#*YYYY-63333####D#",
        "@##;;-##22###RRRR###RRR##7#11111111111#O#T#-#-#*YYYY-63333---#D#",
        "@2#;-;##22##RRRR##L##RRR#7#11111111111#O#-4-#-#*YYYY-63333-#-4-#",
        "@##;;;##22#RRRR##DD##RRR#7#11111111111#O#-#-#-#*YYYY-63333-#-#-#",
        "@2#;-;##-##RRRR#DDD#RRR##7###########-#O#-#-#-#*YYYY-63333-#-#-#",
        "@##;;-##C#RRRR##DDD##RRR##7###+++++##-#O#-#-#-#*YYYY-63333-#-#-#",
        "@2#;;;##H##RRRR#DDDD##RRR##7##+++++##-#O#-#-#-#*YYYY-63333-#-#-#",
        "@##;-;####RRRR##44444##RRR##7###.####-#O#-#-#-#*YYYY-63333-#-#-#",
        "@2#-;;###RRRR##±±±±±±±##RRR#7###.#K-#-#O#-#-#-#*YYYY-63333-#-#-#",
        "@###-###RRRR##X--------#RRR##⌠##.#--#-#-#---#-######-#####-#---#",
        "-----##RRRR##%X---U----##RRR#K##--------#111#--------------#111#",
    ]
    level8_map = [
        "-------┘--------44---¿¿¿¿¿¿¿¿¿¿¿¿│---│¿¿¿¿¿¿¿¿¿¿¿------K---┤;-U-",
        "XXXXXXX-XXX-----44---      -----------------    ----#######-;---",
        "--------------71#####       ---------------      #####┤-----;;;;",
        "K------------71###           -------------          #####¿##; P ",
        "#17---------71####****        -----------       ****##----æW;   ",
        "##17-------71#####*###         ----K----        ###*##¿#####;   ",
        "###17-----71######*#             #####            #*## 1   7;   ",
        "####17---71#######*;     W    W    W    W    W    :*#######¿;   ",
        "#####17-71########*#444444444444444444444444444444#*##±     ;   ",
        "######---#########*#                              #*##444¿##;   ",
        "#######∑##########U#                              #!##æ     ;   ",
        "----------------####                              ######¿###;   ",
        "----------------##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV## ò    ;   ",
        "----------------##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV###¿####;   ",
        "┐∑-------------≥######################################      ;   ",
        "5555555555555555#############the#lava#pit#################¿#;   ",
        "            -------         ------------***********-##+Æ   C;   ",
        "              000            ---┐######-###########-####¿###;   ",
        "                                ------7æ##LL-D-D-D-¿##      ;   ",
        "                                     ##-###########¿#######¿;   ",
        "                                     ##-7  1   TTT7¿##     æ;   ",
        "┘       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1##--#########æ¿###¿####;   ",
        "###this#is#the#first#sideways#level####111111111  ∑C##ò       æ ",
    ]
    level10_map = [
        "!+-----+----+------+##%VVOOOOO44U44OOOOVV%##3333333333333333333K",
        "-----+--+-----+-----##VVVOOOOO44444OOOOVVV##66666666666666666663",
        "+--+------+--------+##OOOOOOOO##5##OOOOOOO##                  63",
        "-----+-------+----+-##OOOOOOOO##?##OOOOOOO##                  63",
        "---+-----+------+---##VVVOOOOOO###OOOOOVVV##XXXXX             63",
        "-+----+-------+-----##CVVOOOOOOO#OOOOOOVVC##XXXXX             63",
        "+-------+--------+-U##CVVOOOOOOOOOOOOOOVVC##UXXXX             63",
        "###############################OOO##############################",
        "MMMMMMMMMMMMMMMMMMMM##S                  S##11111111111111111111",
        "MMMMMMMMMMMMMMMMMMMM##                    ##11111111111111111111",
        "@@@@@@@@@@@@@@@@@@@@##         000        ##11111111111111111111",
        "K@@@@@@@@@@@@W                 0P0        HB11111111111B1111111±",
        "@@@@@@@@@@@@@@@@@@@@##         000        ##11111111111111111111",
        "MMMMMMMMMMMMMMMMMMMM##                    ##11111111111111111111",
        "MMMMMMMMMMMMMMMMMMMM##S                  S##11111111111111111111",
        "###############################~~~##############################",
        "111111111111111111-U##C00000000---0-000---##U-))I)))))))333))))-",
        "1(((((((((((((((((--##-0000H---0000---0-0-##--)I)))))))333))))-*",
        "1(((((((TTT((((((((1##00000000 00000000000##))I)))))))333))))-*I",
        "1(((((((TTT((((((((1##-0-00000000000000-00##)I)))))))333))))-*I*",
        "1(((((((TTT((((((((1##00-0-----0000000<[|,##I)))))))333))))-*I*I",
        "1((((((((((((((((((1##-#####################)))))))333))))-*I*I*",
        "≤1111111111111111111##C-------D-D-D]]E≥&LL##K)))))333))))-*I*I*C",
    ]
    level12_map = [
        "LLL##U##@@@@@@@@@@@|000---0000000000000000-0--00000000VVV000Y-0V",
        "```##-##@00000000000000---0000222222220---0000-00000000000--Y-0V",
        "```##K##@@022222222K000---0000-0000000000-0000-0)))))YYYW-W0Y-0V",
        "```##6##@@@222222222000---000U*******00000000000)))0000000000-00",
        "```##6##@@@222222222000---000000000000000000000000222222--000---",
        "```##6##@@0222222222000---(((((((((((((((±(((((000222222-C00000-",
        "333##6##@00000000000000---00004444444444444444(0000000000000000-",
        "333##6##3CCC....0---------00022222222222222222(K(---------------",
        "$$$##6##000000000000000---00000000000000000000000000000000000000",
        "   0--00000000000000000---000000000000000000000===============--",
        " P 00-00+02222222220--------------------------0=,===-=--===-==-=",
        "$$$00-00+02222222220-00---0000000000000000000-0==I=-=-==-=-=-==-",
        " ! 00-00+02222222220-00-Z-0000000000000000000-0=H==-===T==-==--=",
        "00000-00[02222B22220-00---00----03333333CC----0==I==-===-==-====",
        "0--00-00+02222222220-00---00-0000000000000000-0===--==-==-==--==",
        "-0000-00+02222222220-00---00-0000000000000000-0==-===-=-=-====-=",
        "00000-00+02222222220W00---00-----0--------000-0=-==--==-=-=--=T=",
        "0--00-00000000000000000---000000000001110-000-0==T-===-===-==-==",
        "00000-00000000000000000---000000000001110-00000=======-=========",
        "--000----------------- ---0WWWWWWWWK01110-000-000000000000000000",
        "00000-000000~~~0000000#---#00-00000001110-000K--<000OO000OOOOO≤*",
        "00C000000********3000##VVV##0-------------00000000boulderville├0", # INVESTIGATE ├ symbol
    ]
    level14_map = [
        "###<@@@@@@@@@@@@@@@@@@@@@@@@@#one#@@@@@@@@@@@@@@@@@@@@@@@@@FK###",
        "K÷###@@@@@@@@@@@@@@@@@@@@@@@@@;!:@@@@@@@@@@@@@@@@@@@@@@@@@@###$[",
        "÷÷((###@@@@@@@@@@@@@@@@@@@@@@@:::@@@@@@@@@@@@@@@@@@@@@@@@###$$$$",
        "((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$",
        "(((((((2###222222222222222222222222222222222222222222###2$$$$$$$",
        "(((((((2((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$2$$$$$$$",
        "(((((((2((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$2$$$$$$$",
        "(((((((2((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$2$$$$$$$",
        "DD##(((2((((((((###@@@@@@@@@@@@@@@@@@@@@@@@@@###$$$$$$$$2$$$####",
        "DD#f(((2(((((((((##############77##############$$$$$$$$$2$$$##CC",
        "DD#o(((2((((((((÷##2------------------------2##⌠$$$$$$$$2$$$t#αα",
        "DD#u(((2((((((((÷----------F---P----S--------88⌠$$$$$$$$2$$$w#MM",
        "&&#r(((2((((((((÷##2------------------------2##⌠$$$$$$$$2$$$o#MM",
        "LL##(((2(((((((((##############99##############$$$$$$$$$2$$$##MM",
        "####(((2((((((((###)))))))))))⌡⌡⌡⌡)))))))))))###$$$$$$$$2$$$##αα",
        "(((((((2((((((###))))))))))))))))))))))))))))))###$$$$$$2$$$$$$$",
        "(((((((2((((###))))))))))))))))))))))))))))))))))###$$$$2$$$$$$$",
        "(((((((2((###))))))))))))))))))))))))))))))))))))))###$$2$$$$$$$",
        "(((((((2###))))))))))))))))))))))))))))))))))))))))))###2$$$$$$$",
        "((((((###2222222222222222222222222222222222222222222222###$$$$$$",
        "((((###))))))))))))))))))))))))))))))))))))))))))))))))))###$$⌠⌠",
        ",(###))))))))))))))))))))))))))))))))))))))))))))))))))))))###⌠K",
        "###K⌡)))))))))))))))))))))))#three#))))))))))))))))))))))))F|###",
    ]
    level16_map = [
        "##tunnels#of#kroz###########-P--################################",
        "########################X###----######X##-------æ--------##X####",
        "############################----#########----------------#######",
        "L---N----H######≥  ≥ ≥######-----------------########----#######",
        "L---N-----##X###  CC  555555-----------------#####X##1111#######",
        "######----######≥ ≥  ≥###############################----#####X#",
        "######1111###########################################1111#######",
        "#X####----##############X#######magic#####X##########----#######",
        "######1111####################ô-ò-û-ò-ô##############----N-----#",
        "######----####################----K----##############----N-----#",
        "######1111#######X############æ-æ-æ-æ-æ#########X##########----#",
        "######----########################-########################1111#",
        "######1111################X#######-########################----#",
        "######----########################---------N-------------------#",
        "###X##----##########################################-----------#",
        "######---------------7±########################X####----########",
        "######---------------7-444444444444444444###########1111########",
        "#####O#############--77##################444########----#####X##",
        "####O##############1111#############X#######4⌠%-####1111########",
        "###O#####XXX#######----#############################----########",
        "##O#####X###Q######-------N------`----------------------########",
        "##O##OOO###########-------N------`--------æ-------------##X#####",
        "###OO###########################################################",
    ]
    level18_map = [
        "###########klose#enkounters#of#the#krazy#kubikal#kind├##########",
        "3                               P                              3",
        "##-##############:########:#######:###########:##############:##",
        "XXXXXXXXX##~W~W~W~W~##æ-M----M.--$$$$$$$$$-9/-/J--J-|##---Æ≥Æ---",
        "---------##*~*~*~*~*##-æ.-öM-ö-##$$$$$$$$$##J--/-J-/J##YYYYYYYYY",
        "MMMMMMMMM##~W~W~W~W~##M--æ-.-M-##111111111##-/-J/--/-##(((((((((",
        ")))))))))##*~*~*~*~*##.ö-.-ö-.ö##222222222##/J--J-J-/##(((((((((",
        "C))))))))--~W~W~W~W~##≤.-ö--æ-M##333333333##ⁿ-//-J-/-9-(((((((((",
        "###################-################################9##55555555-",
        "ô-ô-ô-ô-ô##YYYYYYYYY##222222222------0---W##RRRRRRRRR##MMMMMMMMM",
        "-----------YYYYYYYYY##@@@@@@@@@##---000---##RXXXXXXXR##MMMMMMMMM",
        "XXXXXXXXX##YYYYYYYYY##@@@@@@@@@##--00G00--##RXXXKXXXR##MMMMMMMMM",
        "---------##YYYYYYYYY##@@XXX@@@@##---000---##RXXXXXXXR##MMMMMMMMM",
        "ÆÆÆÆÆÆÆÆÆ##YYYYYYYYK##@@XZX@@@@##----0---W##RRRRRRRRR##MMMMMMMMK",
        "-#####################-##########⌠##################H##Z########",
        "~-~[~-~-~##WWW......α1:1:1:1:1:##-773C7--7##=--=I==-=##ββββββY0,",
        "-~-~-~-~-##WWW......##1:1:1:1:1##7-777-77-##!==-=--==##ββββββY00",
        "~-~-~-~-~##.........##:1:1:1:1:##-77--77-7##=======-=##ββββββYYY",
        "-~-~-~-~-##.........##1:1:1:1:1##7-7-77-77##-==-=-==I##βββββββββ",
        "K-~-~-~-~-α..<......##:1:1:1:1±##77-7777---I=--=-=--=##222222222", # INVESTIGATE < SYMBOL
        "############################################################44##",
        "LL---V--V-VV-V--VV---D-----D--Æ--D--ö--D--66333333333333333-WWWW",
        "LL--V-VV-V--V-VV--V--D-----D--ö--D--Æ--D--66YYYYYYYYYYYYYYYYYYYY",
    ]
    level20_map = [
        "###key#shop###MTMMMMMMMMMMMMMMMMMMMMM-----MMMMMMMMMMMM-MM--!##LL",
        "##Kβα44@@@@@##MMMMMMMMMMMMMMMMMMMMMM-MMMMM-MMMMMMMMMM-M-M-P-##LL",
        "##Kβ3##@@@@@@DMMMMMMCMMMMMMMMMMMMMM-MMMMMMM-MMM<MMMM-MMM----##DD",
        "##Kβα##@@@@@##M-MMMMMMMMMMMMMMMM---MMMMMMMM-MMMMMMM-MMMMMMMM##DD",
        "#######X######MM-MMMMMMMMMMM----MMMMMMMMMMMM-MMMMM-MMMMMMMMM##DD",
        "##±-----##MMMMMMM-MMMMM-----MMMMMMMMMMMKMMMMM-MMM-MMMMMMMMMM##DD",
        "##########MMMMMMTMMMMM-MMMMMMMMMMMMMMMMMMMMMMM-M-MMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMM-MMMMMMMMMMMMMMMMMMMMMMMMM-MMMMMMCMMMMMM-MM",
        "MMMMMMMM-----MMMM----MMMMMMMM[MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MMM",
        "MMMM----MMMMM----MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTMMMMMMMMMMM-MMMM",
        "MMM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MMM",
        "MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM",
        "MM-MMMMMMCMMMMMMMMMMMMMMMBWWWWWWWWWW-------------------------MMM",
        "MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM",
        "MM-MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTMMMMMMMMMMMMMMM-M",
        "MMM-------MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-MM",
        "MMMMMMMMMM-----MMMMMMMMMMMMMMMM]MMMMMMMMM-M-MMMMMMMMMMMMMMMM-MMM",
        ")))))))))MMMMMM-MMMMMMMMMMMMMMMMMMMMMM-M-M-M-MMMMMMMMCMMMMM-MMMM",
        "22222222)MMTMMM-MMMMMCMMMMMMMMMMMMMMM-M-MMMMM-MMM-MMMMMMMM-MMMMM",
        "22222222)MMMMMM-MMMMMMMMMMMMMMM------MMMMMMM-MMM-M-MMMMMM-MMMMMM",
        "22222222)MMMMMM-MMMMMMMMMM-----MMMMMMMMMMMM-MMM-MM-MMMMM-MMMMMMM",
        "--222222)MMMMMM-----------MMMMMMMMMMMMMMMM-MM-M-MMM-M-M-MMMMM,MM",
        "K-222222)MMMMMMMMMMMMMMMMMMMMMMMMMM|MMMMMMM--M-MMMMM-M-MMMMMMMMM",
    ]
    level22_map = [
        "1111144       ##C######locksmith#shoppe######C##         RRRRRRR",
        "1111144       ##]##K#K#K#K#K#-3-3#K#K#K#K#K##]##        RRRRRRRv",
        "1111144          ##:::::::::######::::::::;##         RRRRRRRCYY",
        "1111144          ##------------------------##     666RRRRRRRR66 ",
        "1111144          #############--#############     6666666666666 ",
        "1111144                                           HOOOOOOOOH    ",
        "1111144                                        6666666666666    ",
        "1111144                                        66RRRRRRR6666    ",
        "1111144                                        RRRRRRR          ",
        "1111144                                      RRRRRR           YY",
        "1111144               P                    RRRRRR             YZ",
        "1111144                                 RRRRRRRRRR            YY",
        "1111144                              RRRRR333RRRRR              ",
        "1111144                             RRR3333333RRRRR             ",
        "@@@@@##                           RRR3333333333RRRRR            ",
        "MMMMM##                           RRR333333333RRRRR             ",
        "))))##                          RRR33333333RRRRR               ",
        "MMMMM##                        RRRR333333RRRRRRR        DDDDDDDD",
        "(((((##                       RRRR3LL3RRRRRRRR          DDDDDDDD",
        "MMMMM##                      RRRRRRRRRRRRRR             DDDDDDDD",
        "$$$$$##                     RRRRRRRRRRRR                DDDD7777",
        "MMMMM##                     RRRRRRRR                    DDDD77⌠⌠",
        "]]K]]##ô                   RRRRRRK]                     DDDD77⌠!",
    ]
    level24_map = [
        "T    P  #the#step#of#faith#-----Æ-~K±-------U-----#---D-D-D-D-LL",
        "######----------------------│44444444-------┐-KÆ--#┘############",
        "-----------------------------#       ------#####┐-#-----¿-------",
        "-----------------------------#        -----:------#----¿-¿------",
        "------###--------------------#        -----:------#--¿¿---¿-----",
        "--------#--------------------#        -----:------#-#------┘----",
        "--------#--------------------#        -----#####--#-#-----------",
        "--------#--------------------#        -----#---;--#-#------┘----",
        "--------#--------------------#        -----#<###--#-#-----------",
        "--------#---------⌡---------¿#         ----#[#----#-#-----¿-----",
        "--K-----#┤########88888888888#         ----#|#----#-#----¿--W---",
        "-XXX----#      #             #         ----#,#----#-#-------W---",
        "        #      #             #          ---#-#----#-#---¿---W---",
        "        # ô    #             #          ----------#-##-¿----W---",
        "        #      #             #             ;;;;;- #┘K#¿-----W---",
        "        #      #             #                 +-+####------W---",
        "        #      #             #                 +-+----¿-----W---",
        "    XXXX#      #             #                 +-+---¿------W---",
        "         ┤     #             #                 +-+###-----------",
        "       ###     #             #    U            +-+#--------7----",
        "               #             #                 + +#   ##C.!.C## ",
        "               #             #                 + +#   ######### ",
        "VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV",
    ]
    level25_map = [
        "K»    -++++++++++++++++#the#sacred#temple#+++++++++++++++-    «K",
        " VVVVVV11111111111111111111111111111111111111111111111111JJJJJJ ",
        " VVVV;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;JJJJ ",
        " VV1111111111;:::-:::111111111#####111111111::-:::::111111111JJ ",
        " V11         :-:-:-::        ###A###        :-:-:--:        11J ",
        "X 1          ::-:::B:        RR#`#RR        :B::-::;         1 X",
        "X  22####-####-------------RRRR#D#RRRR-------------####-####22 X",
        "X  22##3@-@3##;3;3;3;3;3;3RRRRR#`#RRRRR3;3;3;3;3;3;##~~~~~##22 X",
        "X  22##3@-@3##3;3;3;3;3;3RR1ÆC##D##CÆ1RR3;3;3;3;3;3##~~~~~##22 X",
        "X  22##3@-@3##;3;3;3;3;3RR11ÆÆ##`##ÆÆ11RR3;3;3;3;3;##~~~~~##22 X",
        "X--####3@-@3####3;3;3;3RR11#####D#####11RR3;3;3;3####~~~~~####-X",
        "X   U##3@@@3##U ;3;3;3RRB11-+T1   1T+-11BRR3;3;3; U##~~~~~##U  X",
        "X--####3@@@3####3;3;3;3RR11#####P#####11RR3;3;3;3####~~~~~####-X",
        "X  22##3@@@3##;3;3;3;3;3RR1111##U##1111RR3;3;3;3;3;##~~~~~##22 X",
        "X  22##3@@@3##3;3;3;3;3;3RR111#####111RR3;3;3;3;3;3##~~~~~##22 X",
        "X  22##3@K@3##;3;3;3;3;3;3RR111∑∑∑111RR3;3;3;3;3;3;##~~K~~##22 X",
        "X  22#########-----B-------RRRR∑C∑RRRR-------B-----#########22 X",
        "X 1  ##|0<0                   RRRRR                   0[0,## 1 X",
        " R11 #######  11111111111111;--->---;11111111111111  #######11= ",
        " RR111111111111-VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV-11111111111== ",
        " RRRR111111111-V V V-V V V-2-V*VCV*V-2-V V-V-V V V-11111111==== ",
        "βRRRRRR111111-V V V-2-V V V-V*V*V*V*V-V V V-2-V V V-11111======┌",
        "KββββββββββββVGVæV V V V VæV*V*V*V*V*VæV V V V VæVGV┌┌┌┌┌┌┌┌┌┌┌K",
    ]

    level_maps = [level1_map, level2_map, level4_map, level6_map, level8_map, level10_map,
                  level12_map, level14_map, level16_map, level18_map, level20_map, level22_map,
                  level24_map, level25_map]
    current_level_index = 0
    grid = [list(row) for row in level_maps[current_level_index]]

    collidable_tiles = {"X", "#", ";", "/", "J", "R", "4", "5", "6", "8", "9"}

    dynamic_tiles = {"P", "1", "2", "3"}
    # Game state
    grid = [list(row) for row in level1_map]
    collidable_tiles = {"X", "#"}
    slow_enemies = []
    medium_enemies = []
    keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, 
                    pygame.K_LEFT: False, pygame.K_RIGHT: False,
                    pygame.K_w: False}
    
    # Find player and enemies
    player_row, player_col = 0, 0
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == "P":
                player_row, player_col = r, c
            elif tile == "1":
                slow_enemies.append({"row": r, "col": c})
            elif tile == "2":
                medium_enemies.append({"row": r, "col": c})  # Fixed: added colon after "col"

    # Initialize score tracking variables *Based off difficulty*
    match(difficulty_input):
        case "E":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        case "A":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 2, 0, 0, 0, 0
        case "N", " ":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        case "X":
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 250, 100, 50, 0, 0
        case _:
            score, level_num, gems, whips, teleports, keys, cloaks = 0, 1, 20, 10, 0, 0, 0
        
    if mixUp:
        score, level_num, gems, whips, teleports, keys = 0, 1, gems + 60, whips + 30, teleports + 15, 2
    
    values = [score, level_num, gems, whips, teleports, keys, cloaks]
    hud(screen, WIDTH, HEIGHT, values)
        
    # Function to change to the next level
    def change_level(next_level_index):
        nonlocal grid, player_row, player_col, slow_enemies, medium_enemies, level_num
        
        # Check if level index is valid
        if next_level_index >= len(level_maps):
            next_level_index = 0  # Loop back to first level
        
        # Update level number
        level_num = next_level_index + 1
        
        # Reset level grid
        grid = [list(row) for row in level_maps[next_level_index]]
        
        # Reset enemies
        slow_enemies = []
        medium_enemies = []
        
        # Find new player position and enemies
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == "P":
                    player_row, player_col = r, c
                elif tile == "1":
                    slow_enemies.append({"row": r, "col": c})
                elif tile == "2":
                    medium_enemies.append({"row": r, "col": c})

    # Core functions
    def has_line_of_sight(from_row, from_col, to_row, to_col):
        """Check if there's a direct line of sight between two positions"""
        # Bresenham's line algorithm for line of sight
        points = []
        dx, dy = abs(to_col - from_col), abs(to_row - from_row)
        sx = 1 if from_col < to_col else -1
        sy = 1 if from_row < to_row else -1
        err = dx - dy
        
        x, y = from_col, from_row
        while True:
            points.append((x, y))
            if x == to_col and y == to_row:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
                
        # Check if any solid walls block the line of sight
        # Enemies can now see through breakable blocks ("X")
        for col, row in points[1:-1]:  # Skip start and end points
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == "#":  # Only solid walls block vision
                    return False
        return True

    def move_enemy(enemy, enemy_type, move_prob):
        if is_cloaked:
            pass
        else:
            """Move an enemy toward the player if they can see the player"""
            row, col = enemy["row"], enemy["col"]
            
            # Check if enemy was removed
            if grid[row][col] != enemy_type:
                return True  # Remove enemy
            
            # Random chance for player move
            if random.randint(0, move_prob-1) == 0:
                player_input()
            
            # Check if enemy can see player
            if not has_line_of_sight(row, col, player_row, player_col):
                return False  # Stay still if can't see player
            
            # Clear current position
            grid[row][col] = " "
            
            # Calculate move direction toward player
            new_row, new_col = row, col
            x_dir, y_dir = 0, 0
            
            if player_col < col:
                new_col -= 1
                x_dir = 1
            elif player_col > col:
                new_col += 1
                x_dir = -1
            
            if player_row < row:
                new_row -= 1
                y_dir = 1
            elif player_row > row:
                new_row += 1
                y_dir = -1
        
        # If no movement was determined, try the other axis
        if new_row == row and new_col == col:
            if player_col < col:
                new_col -= 1
                x_dir = 1
            elif player_col > col:
                new_col += 1
                x_dir = -1
            elif player_row < row:
                new_row -= 1
                y_dir = 1
            elif player_row > row:
                new_row += 1
                y_dir = -1
        
        # Handle movement and collisions
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # Breaking X blocks
            if grid[new_row][new_col] == "X":
                grid[new_row][new_col] = " "  # Break the block
                # Award points based on enemy type
                if enemy_type == "1": score += 1
                elif enemy_type == "2": score += 2
                elif enemy_type == "3": score += 3
                return True  # Enemy dies when breaking block
            
            # Handle collision with gems, whips, teleports
            elif grid[new_row][new_col] == "+":  # Gem
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3
                
                if gems < 0:
                    player_death(screen)  # Call player_death when out of gems
                
                # Update display
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False
                
            # Collide with an item (whip, teleport)
            elif grid[new_row][new_col] in {"W", "T"}:
                # Destroy the item and move the enemy
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False
                
            # Empty space - move there
            elif grid[new_row][new_col] == " ":
                enemy["row"], enemy["col"] = new_row, new_col
                grid[new_row][new_col] = enemy_type
                return False

            # Hit player
            elif grid[new_row][new_col] == "P":
                # Attack player by taking gems
                if enemy_type == "1": gems -= 1
                elif enemy_type == "2": gems -= 2
                elif enemy_type == "3": gems -= 3
                
                if gems < 0:
                    player_death(screen)  # Call player_death when out of gems
                    
                return True  # Enemy dies
                
                # Blocked - try to find another way
                else:
                    grid[row][col] = enemy_type  # Stay in place
            else:
                grid[row][col] = enemy_type  # Stay in place
    
    def use_whip(screen, grid, player_row, player_col, whips, slow_enemies, medium_enemies, images, tile_mapping, TILE_WIDTH, TILE_HEIGHT):
        """Handle the whip animation and enemy interactions"""
        # Access game state variables from enclosing scope
        nonlocal score, level_num, gems, teleports, keys, WIDTH, HEIGHT
        
        # Check if player has whips
        if whips <= 0:
            return 0, [], []  # No whips to use
        whips -= 1
        
        # Define the whip animation positions (counter-clockwise)
        whip_positions = [
            {"row": -1, "col": -1, "sprite": "whip1"},  # Top-left
            {"row": -1, "col":  0, "sprite": "whip3"},  # Top
            {"row": -1, "col":  1, "sprite": "whip2"},  # Top-right
            {"row":  0, "col":  1, "sprite": "whip4"},  # Right
            {"row":  1, "col":  1, "sprite": "whip1"},  # Bottom-right
            {"row":  1, "col":  0, "sprite": "whip3"},  # Bottom
            {"row":  1, "col": -1, "sprite": "whip2"},  # Bottom-left
            {"row":  0, "col": -1, "sprite": "whip4"},  # Left
        ]
        
        # Track affected enemies
        enemies_hit = []
        
        # Timing values
        delay = 25  # milliseconds per frame
        
        # Original grid state before whip animation
        original_grid = [row[:] for row in grid]
        
        # Whip animation loop
        for position in whip_positions:
            # Calculate target position
            whip_row = player_row + position["row"]
            whip_col = player_col + position["col"]
            
            # Check if position is in bounds
            if not (0 <= whip_row < len(grid) and 0 <= whip_col < len(grid[0])):
                continue
            
            # Original tile at this position
            original_tile = grid[whip_row][whip_col]
            
            # Check for enemy hits at this position
            if original_tile in ["1", "2", "3"]:
                enemies_hit.append((whip_row, whip_col, original_tile))
            
            # Place whip sprite
            grid[whip_row][whip_col] = position["sprite"]
            
            # Render the grid
            screen.fill((BLACK))
            for r_idx, row in enumerate(grid):
                for c_idx, tile in enumerate(row):
                    if tile in tile_mapping:
                        screen.blit(tile_mapping[tile], (c_idx * TILE_WIDTH, r_idx * TILE_HEIGHT))
                        
            pygame.display.flip()
            pygame.time.wait(delay)
            
            # Restore original tile at this position
            grid[whip_row][whip_col] = original_tile

            # Draw HUD with updated whip count (show whip being used)
            hud(screen, WIDTH, HEIGHT, values)
        
        # Process enemy hits and update game state
        kills = 0
        new_slow_enemies = []
        new_medium_enemies = []
        
        # Clear enemies hit by whip from both grid and enemy lists
        for r, c, enemy_type in enemies_hit:
            grid[r][c] = " "  # Clear enemy from grid
            kills += 1
            
        # Rebuild enemy lists excluding the killed ones
        for enemy in slow_enemies:
            if grid[enemy["row"]][enemy["col"]] == "1":
                new_slow_enemies.append(enemy)
                
        for enemy in medium_enemies:
            if grid[enemy["row"]][enemy["col"]] == "2":
                new_medium_enemies.append(enemy)
        
        return kills, new_slow_enemies, new_medium_enemies
    
    cloaks = 0
    is_cloaked = False
    cloak_start_time = 0
    CLOAK_DURATION = 8000

    def cloak(): 
        """ Handles cloak pickup, activation, and duration. """
        nonlocal cloaks, is_cloaked, cloak_start_time, values, CLOAK_DURATION
        
        cloak_start_time = pygame.time.get_ticks()
        is_cloaked = True
        cloaks -= 1
        print(f"{cloaks}")

    def teleport2(grid, player_row, player_col, tile_mapping, screen):  
        """Teleports the player to a random empty space on the grid with a flickering effect before and after teleporting."""
    
        if teleports <= 0:
            return player_row, player_col

        # Find all empty spaces
        empty_spaces = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == ' ']

        if not empty_spaces:
            return player_row, player_col

        # Flicker at the original position 
        for _ in range(20):  
            random_color = random.choice(blinking_text_color_list)

            # Fill original position with random color
            screen.fill(random_color, (player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

            # Draw the player sprite at the original location
            screen.blit(tile_mapping['P'], (player_col * TILE_WIDTH, player_row * TILE_HEIGHT))

            pygame.display.update(pygame.Rect(player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.time.delay(40)

        # Clear the player's original position
        screen.fill((BLACK), (player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
        pygame.display.update([pygame.Rect(player_col * TILE_WIDTH, player_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)])

        for _ in range(250): 
            # Select a random empty space
            new_row, new_col = random.choice(empty_spaces)

            # Flicker at the intermediate locations with only the TP icon (no random colors)
            screen.fill((BLACK), (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))  # Clear previous

            # Draw the TP icon at the new location
            screen.blit(tile_mapping['TP'], (new_col * TILE_WIDTH, new_row * TILE_HEIGHT))

            pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.time.delay(8)
            screen.fill((BLACK), (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

        # Flicker at the final destination (10 times)
        for _ in range(20):  
            random_color = random.choice(blinking_text_color_list)

            # Fill final position with random color
            screen.fill(random_color, (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))

            # Draw the player sprite at the final location
            screen.blit(tile_mapping['P'], (new_col * TILE_WIDTH, new_row * TILE_HEIGHT))

            pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            pygame.time.delay(40)

        # Clear the final position before placing the player
        screen.fill((BLACK), (new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
        pygame.display.update(pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))


        # Clear old player position from the grid
        grid[player_row][player_col] = ' '

        # Update the grid with new player position
        grid[new_row][new_col] = 'P'

        # Ensure final player placement is visible
        screen.blit(tile_mapping['P'], (new_col * TILE_WIDTH, new_row * TILE_HEIGHT))
        pygame.display.update([pygame.Rect(new_col * TILE_WIDTH, new_row * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)])

        # Return new player position
        return new_row, new_col

    # Movement settings - simplified for consistent movement
    movement_cooldown = 100  # ms between moves (one space per 100ms)
    last_move_time = 0
    keys_held_time = {
        pygame.K_UP: 0,
        pygame.K_DOWN: 0, 
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0
    }
    momentum = {
        pygame.K_UP: 0,
        pygame.K_DOWN: 0, 
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0
    }
    
    # How long a key needs to be held to generate momentum (in ms)
    MOMENTUM_THRESHOLD = 300
    # Maximum momentum value (number of extra moves)
    MAX_MOMENTUM = 5

    def player_input():
        """Handle player movement with consistent rate and momentum"""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys
        nonlocal slow_enemies, medium_enemies, last_move_time, cloaks, is_cloaked
        
        current_time = pygame.time.get_ticks()
        current_keys = pygame.key.get_pressed()
        action_performed = False
        
        # Handle whip activation with the 'W' key
        if current_keys[pygame.K_w]:
            if not keys_pressed[pygame.K_w]:  # Key just pressed
                keys_pressed[pygame.K_w] = True
                if whips > 0:
                    kills, slow_enemies, medium_enemies = use_whip(
                        screen, grid, player_row, player_col, whips, 
                        slow_enemies, medium_enemies, images, tile_mapping, 
                        TILE_WIDTH, TILE_HEIGHT
                    )
                    whips -= 1
                    score += kills * 150  # Award points for kills
                    action_performed = True
        else:
            keys_pressed[pygame.K_w] = False

        # Handle Teleport activation with the 't' key
        if current_keys[pygame.K_t]:
            if not keys_pressed[pygame.K_t]:
                keys_pressed[pygame.K_t] = True
                if teleports > 0:
                    player_row, player_col = teleport2(grid, player_row, player_col, tile_mapping, screen)
                    teleports -= 1
                action_performed = True
        else:
            keys_pressed[pygame.K_t] = False

        # Handle cloak activation with the 'c' key
        # Activate cloak if 'c' is pressed
        if current_keys[pygame.K_c]:
            if not keys_pressed[pygame.K_c]:
                keys_pressed[pygame.K_c] = True
                if cloaks > 0 and not is_cloaked:
                    cloak()  
                action_performed = True
        else:
            keys_pressed[pygame.K_c] = False


        # Check if enough time has passed since last move
        time_since_last_move = current_time - last_move_time
        if time_since_last_move < movement_cooldown:
            return action_performed  # Not time to move yet
        
        # Ready to make a move
        move_made = False
        active_direction = None
        
        # Direction priority: UP, DOWN, LEFT, RIGHT
        direction_keys = [
            (pygame.K_UP, (-1, 0)),
            (pygame.K_DOWN, (1, 0)),
            (pygame.K_LEFT, (0, -1)),
            (pygame.K_RIGHT, (0, 1))
        ]
        
        # First check keys being held down
        for key, (delta_row, delta_col) in direction_keys:
            if current_keys[key]:
                if not keys_pressed[key]:  # Key just pressed
                    keys_pressed[key] = True
                    keys_held_time[key] = current_time
                
                # This is our active direction
                active_direction = key
                move_made = process_move(player_row + delta_row, player_col + delta_col)
                if move_made:
                    last_move_time = current_time
                    break
            else:
                # Key released
                if keys_pressed[key]:
                    hold_duration = current_time - keys_held_time[key]
                    if hold_duration > MOMENTUM_THRESHOLD:
                        # Add momentum based on hold duration
                        momentum[key] = min(MAX_MOMENTUM, int((hold_duration - MOMENTUM_THRESHOLD) / 100))
                    keys_pressed[key] = False
        
        # If no key is pressed but we have momentum, apply it
        if not move_made:
            for key, (delta_row, delta_col) in direction_keys:
                if momentum[key] > 0:
                    move_made = process_move(player_row + delta_row, player_col + delta_col)
                    if move_made:
                        momentum[key] -= 1
                        last_move_time = current_time
                        break
        
        return action_performed or move_made
    
    def process_move(new_row, new_col):
        """Process a player movement to a new position"""
        nonlocal player_row, player_col, score, gems, whips, teleports, keys, level_num, cloaks
        
        # Check if position is valid
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        
        # Check if destination is not a wall
        if grid[new_row][new_col] not in collidable_tiles:
            # Collect items
            if grid[new_row][new_col] == "+":  # Gem
                gems += 1
                score += 100
            elif grid[new_row][new_col] == "W":  # Whip
                whips += 1
                score += 50
            elif grid[new_row][new_col] == "T":  # Teleport
                teleports += 1
                score += 75
            elif grid[new_row][new_col] == "K":  # Key
                keys += 1
                score += 125
            elif grid[new_row][new_col] == "L":  # Stairs to next level
                level_num += 1
                score += 1000
            elif grid[new_row][new_col] == "_":  # Cloak
                cloaks += 1
                score += 60  # optional, just for fun
                # Could add level change logic here
            
            # Move player
            grid[player_row][player_col] = " "
            player_row, player_col = new_row, new_col
            grid[player_row][player_col] = "P"
            return True
        
        # Movement was blocked
        return False
    
    # Game constants
    SLOW_TIMER = 5
    MEDIUM_TIMER = 6
    GAME_TICK_RATE = 12.0
    
     # Game loop
    running = True
    clock = pygame.time.Clock()
    tick_counter = 0

    wait = True

    # Ensure the "saves" directory exists
    saves_dir = os.path.join("src", "saves")
    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)

    def save_game(state, slot):
        """Save the game state to a JSON file."""
        save_path = os.path.join(saves_dir, f"KINGDOM{slot}.json")  # Use saves_dir from utils
        with open(save_path, "w") as save_file:
            json.dump(state, save_file, indent=4)  # Save only the player state
        print(f"Saving to file {slot}...")
        pygame.time.wait(2000)  # Wait for 2 seconds

    def restore_game(slot):
        """Restore the game state from a JSON file."""
        save_path = os.path.join(saves_dir, f"KINGDOM{slot}.json")  # Use saves_dir from utils
        if os.path.exists(save_path):
            with open(save_path, "r") as save_file:
                state = json.load(save_file)
            print(f"Restoring from file {slot}...")
            pygame.time.wait(2000)  # Wait for 2 seconds
            return state  # Return the restored state
        else:
            print(f"No save file found for slot {slot}.")
            return None

    def handle_save(screen, state):
        """Handle the save process."""
        paused = True
        print("\nGame is PAUSED.\n")  # Output when the game is paused for saving
        print("Are you sure you want to SAVE (Y/N)?")
        while paused:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        paused = False
                        save_slot = prompt_save_restore(screen, "SAVE")
                        if save_slot:
                            save_game({
                                "player_row": state["player_row"],
                                "player_col": state["player_col"],
                                "Score": state["Score"],
                                "level_num": state["level_num"],  # Save the level number
                                "gems": state["gems"],
                                "whips": state["whips"],
                                "teleports": state["teleports"],
                                "keys": state["keys"]
                            }, save_slot)
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        paused = False
        print("\nGame RESUMED.\n")  # Output when the game resumes after saving

    def handle_restore(screen):
        """Handle the restore process."""
        paused = True
        print("\nGame is PAUSED.\n")  # Output when the game is paused for restoring
        print("Are you sure you want to RESTORE (Y/N)?")
        while paused:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        paused = False
                        restore_slot = prompt_save_restore(screen, "RESTORE")
                        if restore_slot:
                            restored_state = restore_game(restore_slot)
                            if restored_state:
                                # Regenerate the grid based on the saved level number
                                grid = generate_grid_for_level(restored_state["level_num"])
                                return {
                                    "grid": grid,  # Regenerated grid
                                    "player_row": restored_state["player_row"],
                                    "player_col": restored_state["player_col"],
                                    "Score": restored_state["Score"],
                                    "level_num": restored_state["level_num"],
                                    "gems": restored_state["gems"],
                                    "whips": restored_state["whips"],
                                    "teleports": restored_state["teleports"],
                                    "keys": restored_state["keys"]
                                }
                    elif event.key in (pygame.K_n, pygame.K_ESCAPE):
                        paused = False
        print("\nGame RESUMED.\n")  # Output when the game resumes after restoring
        return None

    def prompt_save_restore(screen, action):
        """Prompt the user to pick a save/restore slot."""
        slot = None
        print(f"Pick which letter to {action} to/from: A, B, or C? A")  # Print the prompt once
        while slot not in {"A", "B", "C"}:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_a, pygame.K_b, pygame.K_c):
                        slot = chr(event.key).upper()
                        return slot
                    
    def generate_grid_for_level(level_num):
        """Generate the grid for the given level number."""
        # Ensure the level number is valid
        if 1 <= level_num <= len(level_maps):
            return [list(row) for row in level_maps[level_num - 1]]  # Convert strings to lists of characters
        else:
            raise ValueError(f"Level {level_num} is not defined in level_maps.")

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # ASCII value 80 
                    pause_quit(screen, quitting=False)
                elif event.key in (pygame.K_q, pygame.K_ESCAPE): # ASCII value # 81 & 27
                    if pause_quit(screen, quitting=True):
                        running = False   
                elif event.key == pygame.K_TAB:
                    # Go to next level when Tab is pressed
                    current_level_index = (current_level_index + 1) % len(level_maps)
                    change_level(current_level_index)
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False
        
        # Process player input
        player_input()

         # Auto-deactivate cloak after duration
        if is_cloaked and pygame.time.get_ticks() - cloak_start_time > 5000:
            is_cloaked = False

        # Draw the grid
        screen.fill(BLACK)
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char == "P":
                    if is_cloaked: # Changed player icon
                        screen.blit(tile_mapping['TP'], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT)) 
                    else:
                        screen.blit(tile_mapping['P'], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT))
                elif char in tile_mapping:
                    screen.blit(tile_mapping[char], (col_index * TILE_WIDTH, row_index * TILE_HEIGHT))

        # Update the item tracking UI with current values
        values = [score, level_num, gems, whips-1, teleports, keys, cloaks]
        hud(screen, WIDTH, HEIGHT, values)
        
        # Update game state
        tick_counter += 1
        
        # Move enemies on their respective timers
        if tick_counter % SLOW_TIMER == 0:
            # Move slow enemies
            for i in range(len(slow_enemies)-1, -1, -1):
                if move_enemy(slow_enemies[i], "1", 8):
                    del slow_enemies[i]
        
        if tick_counter % MEDIUM_TIMER == 0:
            # Move medium enemies
            for i in range(len(medium_enemies)-1, -1, -1):
                if move_enemy(medium_enemies[i], "2", 7):
                    del medium_enemies[i]

        if wait:
            wait_input(screen)
            wait = False
        pygame.display.flip()
        clock.tick(GAME_TICK_RATE)
levels(screen, difficulty_input, mixUp = False)