import pygame

# Initialize pygame mixer and settings
pygame.mixer.init()

# Load and play the background music in a loop
mp3_file = r"funkysuspense.mp3"
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.play(loops=-1)  # '-1' makes the music loop indefinitely

print("Background music is playing!")

# Game loop (replace this with your actual game logic)
try:
    while True:
        # Your game logic goes here

        pass
except KeyboardInterrupt:
    pygame.mixer.music.stop()  # Stop the music when the game ends or is interrupted
    print("Music stopped.")
