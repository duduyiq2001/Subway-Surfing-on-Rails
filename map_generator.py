# Generate Map for Subway Surfing Game
# There will be 5 tracks
import pygame

# Constants
TRACK_COUNT = 5
SIDE_WIDTH = 220


class MapGenerator:
    def __init__(self, screen):
        #Draw 5 tracks on the screen
        self.track_width = (screen.get_width()- 2 * SIDE_WIDTH) // (TRACK_COUNT)

        # Deal with the track image    
        track_bg = pygame.image.load("./resources/image/track.png")
        self.track_image = pygame.transform.scale(track_bg, (self.track_width // 2, screen.get_height()))
    
    def draw_map(self, screen):
        screen.fill("gray")        
        
        # Draw the tarck lines    
        for i in range(0, TRACK_COUNT):
            x_pos = SIDE_WIDTH + i * self.track_width
            x_pos_for_track = SIDE_WIDTH + i * self.track_width + (self.track_width - self.track_image.get_width()) // 2
            pygame.draw.line(screen, "black", (x_pos, 0), (x_pos, screen.get_height()), 3)
            screen.blit(self.track_image, (x_pos_for_track, 0))
                    
        # Draw left side with white
        pygame.draw.rect(screen, "white", (0, 0, SIDE_WIDTH, screen.get_height()))
        
        # Draw right side with white
        pygame.draw.rect(screen, "white", (screen.get_width() - SIDE_WIDTH, 0, SIDE_WIDTH, screen.get_height()))


