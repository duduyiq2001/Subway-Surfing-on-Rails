"""
player.py

Defines the Player class, which handles:
- Position, movement (left/right, jump)
- Collision boundaries
- Score tracking (for coin collection or other game points)
"""

import pygame


class Player:
    """
    Represents the main character in the infinite runner.

    Attributes:
        x (int): The x-coordinate of the player's position.
        y (int): The y-coordinate of the player's position.
        width (int): The width of the player's rectangle for collision.
        height (int): The height of the player's rectangle for collision.
        velocity_x (int): Horizontal speed.
        velocity_y (int): Vertical speed, important for jumping.
        score (int): The player's current score.
        on_ground (bool): True if the player is on the ground and can jump again.
        lane_positions (list): Possible x-coordinates or lanes if you want multi-lane movement.
        current_lane (int): Index of the lane the player is currently in.
    """

    def __init__(self, x, y, width=50, height=50, lane_positions=None):
        """
        Initialize the player.

        :param x: Initial x-position.
        :param y: Initial y-position.
        :param width: The width of the player's collision box.
        :param height: The height of the player's collision box.
        :param lane_positions: A list of valid x-coordinates or lanes the player can occupy.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Movement and physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5  # Gravity for jump logic
        self.jump_strength = (
            -10
        )  # Negative because up is typically negative in 2D coordinates
        self.on_ground = True  # If True, the player can jump

        # Lane system
        self.lane_positions = (
            lane_positions if lane_positions else [100, 200, 300, 400, 500]
        )
        # Start on a default lane (e.g., index 2 is middle)
        self.current_lane = 2
        # Make sure x matches the lane
        self.x = self.lane_positions[self.current_lane]

        # Score
        self.score = 0

        # For drawing or animations
        # self.image = pygame.image.load("path/to/player_sprite.png").convert_alpha()
        # Or a simple placeholder:
        self.color = (255, 0, 0)  # Red

        # smooth movement
        self.x_per_frame = []

    def move_left(self):
        """
        Move the player to the next lane on the left.
        """
        if self.current_lane > 0:
            self.current_lane -= 1
            # self.x = self.lane_positions[self.current_lane]
            self.x_per_frame = [
                -5,
                -10,
                -15,
                -20,
                -20,
                -15,
                -10,
                -5,
            ]  # maxhight = 10 + 2*delta

    def move_right(self):
        """
        Move the player to the next lane on the right.
        """
        if self.current_lane < len(self.lane_positions) - 1:
            self.current_lane += 1
            # self.x = self.lane_positions[self.current_lane]
            self.x_per_frame = [5, 10, 15, 20, 20, 15, 10, 5]  # maxhight = 10 + 2*delta

    def jump(self):
        """
        Make the player jump.
        Only works if the player is on the ground (on_ground == True).
        """
        if self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

    def update(self):
        """
        Update the player's position each frame.
        Handles gravity, vertical movement, and ground check.
        """

        # smooth movement
        if len(self.x_per_frame) > 0:
            self.x += (
                0.01
                * self.x_per_frame[-1]
                * (self.lane_positions[1] - self.lane_positions[0])
            )
            self.x_per_frame.pop()
        else:
            self.x_per_frame = [0, 0, 0, 0, 0, 0, 0, 0]

        # Apply gravity
        self.velocity_y += self.gravity

        # Update y-position
        self.y += self.velocity_y

        # Check if we've hit the 'ground'.
        # For a 2D runner, you might have a fixed ground level (e.g., y=500).
        # Adjust based on your game window size.
        ground_level = 500
        if self.y + self.height > ground_level:
            self.y = ground_level - self.height
            self.velocity_y = 0
            self.on_ground = True

    def increase_score(self, amount=1):
        """
        Increase the player's score by a certain amount.

        :param amount: The amount to add to the player's score.
        """
        self.score += amount

    def get_rect(self):
        """
        Returns the player's current collision rectangle.
        Useful for collision checks with obstacles or coins.
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        """
        Draw the player on the given surface.
        If you have a sprite/image, you can blit it. Otherwise, draw a rectangle as a placeholder.

        :param surface: The pygame surface to draw on.
        """
        # If you have an image:
        # surface.blit(self.image, (self.x, self.y))

        # Using a rectangle placeholder:
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
