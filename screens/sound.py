import pygame
import array

# Initialize pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=1)

def generate_sound(frequency=440, duration=1.0, volume=0.5):
    sample_rate = 44100  # 44.1 kHz standard sample rate
    num_samples = int(sample_rate * duration)

    # Generate a sine wave (manual method without NumPy)
    wave = array.array("h", [
        int(volume * 32767 * (i % (sample_rate // frequency) < (sample_rate // (2 * frequency))) * 2 - 1)
        for i in range(num_samples)
    ])

    return pygame.sndarray.make_sound(wave)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Press any key to play sound")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Generate and play a 440 Hz beep sound for 1 second
            sound = generate_sound(440, 0.05)
            sound.play()

    # Keep the program running to allow the sound to play
    pygame.time.delay(100)  # Small delay to prevent high CPU usage

pygame.quit()