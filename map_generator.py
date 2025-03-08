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
        track_bg = pygame.image.load("./resources/image/track.jpeg")
        TRACK_X = track_bg.get_width() // 2 - 25
        TRACK_Y = 0
        TRACK_WIDTH = 50
        TRACK_HEIGHT = track_bg.get_height()
        self.track_image = track_bg.subsurface(pygame.Rect(TRACK_X, TRACK_Y, TRACK_WIDTH, TRACK_HEIGHT))


    
    def draw_map(self, screen):
        screen.fill("gray")        
        
        # Draw the tarck lines    
        for i in range(1, TRACK_COUNT):
            x_pos = SIDE_WIDTH + i * self.track_width
            pygame.draw.line(screen, "black", (x_pos, 0), (x_pos, screen.get_height()), 3)
            screen.blit(self.track_image, (x_pos, 0))
                    
        # Draw left side with white
        pygame.draw.rect(screen, "white", (0, 0, SIDE_WIDTH, screen.get_height()))
        
        # Draw right side with white
        pygame.draw.rect(screen, "white", (screen.get_width() - SIDE_WIDTH, 0, SIDE_WIDTH, screen.get_height()))


