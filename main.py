# The entry point for running your game.
# Typically contains:
# Pygame (or other framework) initialization.
# Loading initial resources.
# Setting up the main window and passing control to game_loop.py.
# May also parse command-line arguments or handle environment settings if needed.


import pygame
import sys
from game_loop import game_loop
from hand_gestures.model import run_model_on_cam
from helpers import create_gesture_update, keyboard_update
from start_scene import start_screen
import threading
from queue import Queue
from play_music import music_play

mapping = {"Thumb_Up": "left", "Open_Palm": "right"}


def main():
    # Initialize Pygame
    pygame.init()
    # Initialize Queue
    gesture_queue = Queue(maxsize=1)
    logfile = "log.txt"
    # . launch thread for webcam
    threading.Thread(
        target=run_model_on_cam, args=(gesture_queue, logfile), daemon=True
    ).start()
    ### creating callback function
    gest_update = create_gesture_update(gesture_queue, mapping)

    # Constants
    WIDTH, HEIGHT = 1280, 720

    # Screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Subway Surfing on Rails")

    # Clock
    clock = pygame.time.Clock()
    fps = 120
    
    # Start Scene
    playerid, state = start_screen(screen, fps, clock)

    # Add music
    threading.Thread(
        target=music_play, daemon=True
    ).start()

    # Game Loop
    try:
        game_loop(screen, clock, fps, gest_update, playerid)
    except Exception as e:
        print("Error in the game loop: ", e)
        pygame.quit()
        sys.exit()

    # exit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
