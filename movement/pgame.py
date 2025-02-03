# import pygame module in this program 
import pygame 

# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 

# create the display surface object 
# of specific dimension..e(500, 500). 
win = pygame.display.set_mode((800, 600)) 

# set the pygame window name 
pygame.display.set_caption("Moving rectangle") 

# object current co-ordinates 
x = 200
y = 200

# dimensions of the object 
width = 10
height = 10

# velocity / speed of movement 
vel = 4  # Adjusted to match the player's speed in KINGDOM5

# Indicates pygame is running 
run = True

# infinite loop 
#Procedure to handle player movement 
while run: 
	# creates time delay of 10ms 
	pygame.time.delay(10) 
	
	# iterate over the list of Event objects 
	# that was returned by pygame.event.get() method. 
	for event in pygame.event.get(): 
		
		# if event object type is QUIT 
		# then quitting the pygame 
		# and program both. 
		if event.type == pygame.QUIT: 
			
			# it will make exit the while loop 
			run = False
	# stores keys pressed 
	keys = pygame.key.get_pressed() 
	
	# if left arrow key is pressed 
	if keys[pygame.K_LEFT] and x>0: 
		
		# decrement in x co-ordinate 
		x -= vel 
		
	# if right arrow key is pressed 
	if keys[pygame.K_RIGHT] and x<800-width: 
		
		# increment in x co-ordinate 
		x += vel 
		
	# if up arrow key is pressed 
	if keys[pygame.K_UP] and y>0: 
		
		# decrement in y co-ordinate 
		y -= vel 
		
	# if down arrow key is pressed 
	if keys[pygame.K_DOWN] and y<600-height: 
		# increment in y co-ordinate 
		y += vel 
		

	# completely fill the surface object 
	# with black colour 
	win.fill((0, 0, 0)) 
	
	# drawing object on screen which is rectangle here 
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
	
	# it refreshes the window 
	pygame.display.update() 

# closes the pygame window 
pygame.quit()
