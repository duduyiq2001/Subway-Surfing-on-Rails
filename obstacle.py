import pygame
import random

class Obstacle:
    """
    Represents an obstacle that moves down the screen.
    """

    def __init__(self, track_index, y, track_position, width=100, height=30):
        """
        Initializes an obstacle in a random track.
        """
        self.track_index = track_index
        self.track_position = track_position
        self.x = track_position[self.track_index] - width // 2
        self.y = -height
        self.world_x = self.x
        self.world_y = y
        
        # random choose a type
        self.type = random.choice(["hurdle", "train"])
        self.height = height
        self.width = width

    def update(self, dt):
        """
        Moves the obstacle downward.
        """
        self.y += self.speed * dt
        self.rect.y = self.y

    def draw(self, screen):
        """
        Draws the obstacle as a black rectangle.
        """
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def check_collision(self, player):
        """
        Checks for collision with the player.
        """
        return self.rect.colliderect(player.get_rect())
