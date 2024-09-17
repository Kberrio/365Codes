import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Define the notes and their corresponding frequencies
notes = {
    'a': 262,  # C4
    's': 294,  # D4
    'd': 330,  # E4
    'f': 349,  # F4
    'g': 392,  # G4
    'h': 440,  # A4
    'j': 494,  # B4
    'k': 523,  # C5
}

# Create sound objects for each note
sounds = {key: pygame.mixer.Sound(pygame.sndarray.make_sound(pygame.sndarray.array(pygame.mixer.Sound.from_file('data:audio/wav;base64,')))) for key in notes}

for key, freq in notes.items():
    arr = pygame.sndarray.array(sounds[key])
    arr[:] = (pygame.sndarray.make_sound(pygame.sndarray.array(pygame.mixer.Sound.from_file('data:audio/wav;base64,'))).get_raw())
    arr *= 32767 * pygame.sndarray.make_sound(pygame.sndarray.array(pygame.mixer.Sound.from_file('data:audio/wav;base64,'))).get_length() * freq / 44100
    sounds[key] = pygame.sndarray.make_sound(arr.astype('int16'))

print("Welcome to the Python Kalimba!")
print("Use the keys A-S-D-F-G-H-J-K to play notes.")
print("Press 'q' to quit.")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.unicode.lower() in sounds:
                sounds[event.unicode.lower()].play()
    
    time.sleep(0.01)

pygame.quit()