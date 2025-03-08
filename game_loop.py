# For game loop
import pygame
import sys

from map_generator import draw_map
from player import Player
# obstacle
# collison

def game_loop(screen, clock, fps, update_func):
    # Constants
    WIDTH, HEIGHT = 1280, 720
    TRACK_COUNT = 5
    SIDE_WIDTH = 220
    TRACK_WIDTH = (WIDTH - 2 * SIDE_WIDTH) // TRACK_COUNT
    
    # First player
    player_x = SIDE_WIDTH + 2.5 * TRACK_WIDTH
    player_y = HEIGHT // 4 * 3

    # Initialize player
    player = Player(
        x=player_x,
        y=player_y,
        lane_positions= [SIDE_WIDTH + (i+0.5) * TRACK_WIDTH for i in range(TRACK_COUNT)],
    )

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw map
        draw_map(screen)

        # Draw player
        player.draw(screen)

        # Handle player movement
        update_func(player)
     
        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()


