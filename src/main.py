# The entry point for running your game.
# Typically contains:
# Pygame (or other framework) initialization.
# Loading initial resources.
# Setting up the main window and passing control to game_loop.py.
# May also parse command-line arguments or handle environment settings if needed.


import pygame
import sys
from map_generator import draw_map
from player import Player
from game_loop import game_loop


def main():
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 1280, 720

    # Screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Subway Surfing on Rails")
    
    # Clock
    clock = pygame.time.Clock()
    fps = 60
    
    # Game Loop
    try:
        game_loop(screen, clock, fps)
    except Exception as e:
        print("Error in the game loop: ", e)
        pygame.quit()
        sys.exit()
        
    # exit
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()