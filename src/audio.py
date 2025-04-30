from utils import *

pygame.mixer.init()

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
        
def play_wav(file_name):
    file_path = os.path.join(audio_dir, file_name)
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    while pygame.mixer.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.time.delay(100)              

def descent():
    play_wav('beginDescent.wav')
    
def footStep():
    sound_file = random.choice(['footStep_1.wav', 'footStep_2.wav'])
    play_wav(sound_file)
    
def enemyCollision():
    play_wav('enemyCollision.wav')
    
def electricWall():
    play_wav('electricWall.wav')
    
def teleport():
    play_wav('teleport.wav')
    
def teleportTrap():
    play_wav('teleportTrap.wav')
    
def whip():
    play_wav('whip.wav')
    
def zeroCollecible():
    play_wav('zeroCollectible.wav')
    
def chestPickup():
    play_wav('chestPickup.wav')