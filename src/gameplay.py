import pygame
import os

pygame.init()

TILE_WIDTH, TILE_HEIGHT = 13, 13
screen = pygame.display.set_mode((832, 624))
pygame.display.set_caption("Level 1")

def level(screen):

    sprites = ["block", "chest", "enemy1", "enemy2", "enemy3", "gem", "player", "stairs", "teleport", 
               "trap", "wall", "whip", "slowTime", "invisible", "key", "door", "speedTime", "river", 
               "power", "forest", "tree", "bomb", "lava", "pit", "tome", "tunnel", "freeze", "nugget", 
               "quake", "iBlock", "iWall", "iDoor", "stop", "trap2", "zap", "create", "generator", 
               "trap3", "mBlock", "trap4", "showGems", "tablet", "zBlock", "blockSpell", "chance", 
               "statue", "wallVanish", "krozK", "krozR", "krozO", "krozZ", "oWall1", "oWall2", "oWall3", 
               "cWall1", "cWall2", "cWall3", "oSpell1", "oSpell2", "oSpell3", "cSpell1", "cSpell2", 
               "cSpell3", "gBlock", "rock", "eWall", "trap5", "tBlock", "tRock", "tGem", "tBlind", 
               "tWhip", "tGold", "tTree", "rope", "dropRope1", "dropRope2", "dropRope3", "dropRope4", 
               "dropRope5", "amulet", "shootRight", "shootLeft", "trap6", "trap7", "trap8", "trap9", 
               "trap10", "trap11", "trap12", "trap13", "message"]

    assets_path = os.path.join("src", "assets")
    images = {}

    special_cases = {
        "enemy1": "enemy1a",
        "enemy2": "enemy2a"
    }

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
        ".": images["trap"],
        "L": images["stairs"],
        "P": images["player"],
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
        "ⁿ": images["message"]
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
        "#       XX      1              +                 1   XXXX     1#",
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
        "@2#-;;##..#KK###RRRRR##7###11111111111## ###)##)##)#####--////J/",
        "@##-;;##..#KK##RRRRRRR#7###11111B11111----)))))))))))#####---///",
        "@2#;;;##22####RRRR#RRR##7##11111111111##############)########--/",
        "@##;;-##22###RRRR###RRR##7#11111111111#?#ò#---#*YYYY-63333####D#",
        "@2#;-;##22##RRRR##L##RRR#7#11111111111#O#T#-#-#*YYYY-63333---#D#",
        "@##;;;##22#RRRR##DD##RRR#7#11111111111#O#-4-#-#*YYYY-63333-#-4-#",
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
        "00000-00000000000000000---000-00000001110-000K--<000OO000OOOOO≤*",
        "--000-000000~~~0000000#---#00-00000000000-000000000000OOOO000000",
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

    collidable_tiles = {"X", "#", ";", "/", "J", "R", "4", "5", "6", "7", "8", "9"}

    dynamic_tiles = {"P", "1", "2", "3"}

    player_row, player_col = 0, 0
    found_player = False
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == "P":
                player_row, player_col = r, c
                found_player = True
                break
        if found_player:
            break

    enemies = []
    enemy_chars = {"1", "2"}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in enemy_chars:
                enemies.append({"row": r, "col": c, "type": char})

    def is_valid_move(row, col):
        return (0 <= row < len(grid) and 
                0 <= col < len(grid[row]) and 
                grid[row][col] not in collidable_tiles)

    def move_towards_player(enemy):
        if player_row < enemy["row"] and is_valid_move(enemy["row"] - 1, enemy["col"]):
            enemy["row"] -= 1
        elif player_row > enemy["row"] and is_valid_move(enemy["row"] + 1, enemy["col"]):
            enemy["row"] += 1
        elif player_col < enemy["col"] and is_valid_move(enemy["row"], enemy["col"] - 1):
            enemy["col"] -= 1
        elif player_col > enemy["col"] and is_valid_move(enemy["row"], enemy["col"] + 1):
            enemy["col"] += 1

    # Main loop
    running = True
    clock = pygame.time.Clock()
    frame_counter = 0  # Add a frame counter

    while running:
        screen.fill((0, 0, 0))
        
        # Draw the static grid
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char in tile_mapping and char not in dynamic_tiles:  # Skip dynamic tiles
                    x = col_index * TILE_WIDTH
                    y = row_index * TILE_HEIGHT
                    screen.blit(tile_mapping[char], (x, y))
        
        # Draw the player
        player_x = player_col * TILE_WIDTH
        player_y = player_row * TILE_HEIGHT
        screen.blit(images["player"], (player_x, player_y))
        
        # Move enemies every fourth frame
        if frame_counter % 4 == 0:
            for enemy in enemies:
                move_towards_player(enemy)
        
        # Draw enemies
        for enemy in enemies:
            enemy_x = enemy["col"] * TILE_WIDTH
            enemy_y = enemy["row"] * TILE_HEIGHT
            screen.blit(tile_mapping[enemy["type"]], (enemy_x, enemy_y))
        
        # Event handling for quitting and movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                new_row, new_col = player_row, player_col
                # TODO fix diagonal movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    new_row -= 1
                if keys[pygame.K_DOWN]:
                    new_row += 1
                if keys[pygame.K_LEFT]:
                    new_col -= 1
                if keys[pygame.K_RIGHT]:
                    new_col += 1
                
                # Ensure the new position is within bounds
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                    # Only move if the destination tile is not collidable
                    if grid[new_row][new_col] not in collidable_tiles:
                        player_row, new_row
                        player_col = new_col
                
                # Press TAB to switch to the next level
                if event.key == pygame.K_TAB:
                    current_level_index = (current_level_index + 1) % len(level_maps)
                    grid = [list(row) for row in level_maps[current_level_index]]
                    # Reinitialize player position
                    found_player = False
                    for r, row in enumerate(grid):
                        for c, tile in enumerate(row):
                            if tile == "P":
                                player_row, player_col = r, c
                                found_player = True
                                break
                        if found_player:
                            break
                    # Reinitialize enemy positions
                    enemies = []
                    for r, row in enumerate(grid):
                        for c, char in enumerate(row):
                            if char in enemy_chars:
                                enemies.append({"row": r, "col": c, "type": char})

        pygame.display.flip()
        clock.tick(18)
        frame_counter += 1  # Increment the frame counter

level(screen)
pygame.quit()
