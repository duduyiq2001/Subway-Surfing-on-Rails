# Generate Map for Subway Surfing Game
# There will be 5 tracks
import pygame

# Constants
TRACK_COUNT = 5
SIDE_WIDTH = 220

def draw_map(screen):
    #Draw 5 tracks on the screen
    screen.fill("gray")
    track_width = (screen.get_width()- 2 * SIDE_WIDTH) // (TRACK_COUNT)
    
    # Draw the tarck lines    
    for i in range(1, TRACK_COUNT):
        x_pos = SIDE_WIDTH + i * track_width
        pygame.draw.line(screen, "black", (x_pos, 0), (x_pos, screen.get_height()), 3)
        
    # Draw left side with white
    pygame.draw.rect(screen, "white", (0, 0, SIDE_WIDTH, screen.get_height()))
    
    # Draw right side with white
    pygame.draw.rect(screen, "white", (screen.get_width() - SIDE_WIDTH, 0, SIDE_WIDTH, screen.get_height()))