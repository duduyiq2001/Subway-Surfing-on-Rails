import pygame

def music_play():
    # Initialize pygame mixer and settings
    pygame.mixer.init()

    # Load and play the background music in a loop
    mp3_file = r"resources/sound/funkysuspense.mp3"
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play(loops=-1)  # '-1' makes the music loop indefinitely