import pygame
import button
pygame.init() #initialize pygame

#initialize a game window for display
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Title screen')

#game variables
game_paused = False

#define fonts
font = pygame.font.SysFont('arialblack', 40)

#define colours
TEXT_COL = (255, 255, 255) #white

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#game loop
run = True
while run:

    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused == True:
        pass
    
    #display menu
    else:
        draw_text('Press SPACE to pause game', font, TEXT_COL, 160, 250)   

    #event handler      
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = not game_paused
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()

'''    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
'''