import pygame
import random

class Obstacle:
    """
    Represents an obstacle that moves down the screen.
    """

    def __init__(self, track_index, track_position, width=100, height=30, speed=200):
        """
        Initializes an obstacle in a random track.
        
        :param track_positions: List of x-positions for each track.
        :param width: Width of the obstacle.
        :param height: Height of the obstacle.
        :param speed: Speed at which the obstacle moves downward.
        """
        self.track_index = track_index
        self.track_position = track_position
        self.x = track_position[self.track_index] - width // 2
        
        # random choose a type
        self.type = random.choice(["hurdle", "train"])
        
        if self.type == "train":
            # train size is different
            self.height = 200
        else:
            self.height = height
        
        self.width = width
        self.y = -height  # Start above the screen
        self.speed = speed  # Speed at which the obstacle moves
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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
