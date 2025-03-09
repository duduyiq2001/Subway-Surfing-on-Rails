# Generate Map for Subway Surfing Game
# There will be 5 tracks
import pygame

# Constants
TRACK_COUNT = 5
SIDE_WIDTH = 220


# draw everything for the map
class Map:
    def __init__(self, screen, pos_y):
        # Draw 5 tracks on the screen
        self.track_width = (screen.get_width() - 2 * SIDE_WIDTH) // (TRACK_COUNT)
        self.pos_y = pos_y
        # Deal with the track image
        track_bg = pygame.image.load("./resources/image/track.png")
        self.track_image = pygame.transform.scale(
            track_bg, (self.track_width // 2, screen.get_height())
        )

    # draw once, update in the game loop
    def draw(self, screen):
        screen.fill((117, 110, 104))

        # Draw the tarck lines
        for i in range(0, TRACK_COUNT):
            x_pos = SIDE_WIDTH + i * self.track_width
            x_pos_for_track = (
                SIDE_WIDTH
                + i * self.track_width
                + (self.track_width - self.track_image.get_width()) // 2
            )
            pygame.draw.line(
                screen,
                "black",
                (x_pos, 0 + self.pos_y),
                (x_pos, screen.get_height() + self.pos_y),
                3,
            )
            screen.blit(self.track_image, (x_pos_for_track, 0 + self.pos_y))

        # Draw left side with white
        pygame.draw.rect(
            screen, "white", (0, 0 + self.pos_y, SIDE_WIDTH, screen.get_height())
        )

        # Draw right side with white
        pygame.draw.rect(
            screen,
            "white",
            (
                screen.get_width() - SIDE_WIDTH,
                0 + self.pos_y,
                SIDE_WIDTH,
                screen.get_height(),
            ),
        )

    def update(self, delta):
        self.pos_y += delta
