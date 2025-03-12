import pygame
import time
import numpy as np

# Moving this into utils when changes are done

# Initialize Pygame
pygame.init()

def play_sound(frequency, duration, amplitude=4096):
    sample_rate = 44100
    n_samples = int(sample_rate * duration / 1000)
    t = np.linspace(0, duration / 1000, n_samples, False)
    wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    stereo_wave = np.column_stack((wave, wave))
    sound = pygame.sndarray.make_sound(stereo_wave.astype(np.int16))
    sound.play()
    time.sleep(duration / 1000)
    sound.stop()

# Play square wave sound for user selection
#play_sound(300, 30)
#play_sound(220, 100)
#play_sound(220, 100)

pygame.quit()