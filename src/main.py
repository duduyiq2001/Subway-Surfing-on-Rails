# The entry point for running your game.
# Typically contains:
# Pygame (or other framework) initialization.
# Loading initial resources.
# Setting up the main window and passing control to game_loop.py.
# May also parse command-line arguments or handle environment settings if needed.


import pygame
import sys
from map_generator import draw_map

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
while True:
    draw_map(screen)
    pygame.display.flip()

# quit game
pygame.quit()