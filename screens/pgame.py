import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 20
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 50

# Load player image
player_image = pygame.image.load('KingdomOfKrozII/movement/player.png')
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Enemy settings
enemy_size = 20
enemy_speed = 2

# Create a list of enemies
enemies = []
for _ in range(1):  # Spawn 5 enemies
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)
    enemies.append([enemy_x, enemy_y])

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

	#line 130
    # Get player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

	#line 133 134
	# Ensure player stays within screen bounds
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))
    
    # Draw player image
    screen.blit(player_image, (player_x, player_y))
    
     # Update enemy positions to chase the player
    for enemy in enemies:
        enemy_x, enemy_y = enemy

        # Calculate direction toward player
        dx, dy = player_x - enemy_x, player_y - enemy_y

        # Move enemy toward player
        distance = math.hypot(dx, dy)
        dx, dy = dx / distance, dy / distance
        enemy_x += dx * enemy_speed
        enemy_y += dy * enemy_speed

        # Draw enemy
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))

        # Update enemy position in the list
        enemy[0], enemy[1] = enemy_x, enemy_y

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(18.2)

pygame.quit()
