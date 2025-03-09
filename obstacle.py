import pygame


WIDTH = 128
HEIGHT = 720


class Obstacle:
    """
    Represents an obstacle that moves down the screen.
    """

    def __init__(
        self, track_index, y, track_position, type, seg_length, width=100, height=30
    ):
        """
        Initializes an obstacle in a random track.
        """
        self.track_index = track_index
        self.track_position = track_position
        self.x = track_position[self.track_index] - width // 2
        ## will be updated in the first iteration
        self.y = -height
        # 0,0 128,0 0,760 128,760
        self.world_x = self.x

        if y < 0 or y >= seg_length:
            raise Exception("y has be lower than seg_length")
        # mod value of y
        self.world_y = y

        # random choose a type
        self.type = type
        self.height = height
        self.width = width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, p_world, p_canva, seg_length):
        """
        Updating the canva position based on player world and player canvas
        """
        # 1 index is y
        self.y = p_canva[1] - (self.world_y - (p_world[1] % seg_length))
        self.rect.y = self.y

    def draw(self, screen):
        """
        Draws the obstacle as a black rectangle.
        """
        if self.y + self.height >= 0 and self.y <= HEIGHT:
            pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def check_collision(self, player):
        """
        Checks for collision with the player.
        """
        if self.y >= 0 and self.y <= HEIGHT:
            return self.rect.colliderect(player.get_rect())
