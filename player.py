"""
player.py

Defines the Player class, which handles:
- Position, movement (left/right, jump)
- Collision boundaries
- Score tracking (for coin collection or other game points)
"""

import pygame

# SMOOTH1 = [5, 10, 15, 20, 20, 15, 10, 5]
# SMOOTH2 = [3, 9, 16, 22, 22, 16, 9, 3]
# SMOOTH3 = [1, 8, 17, 24, 24, 17, 8, 1]

# Accelerating increase
SMOOTH1 = [
    0.0,
    0.01111111111111111,
    0.02222222222222222,
    0.03333333333333333,
    0.04444444444444444,
    0.05555555555555556,
    0.06666666666666667,
    0.07777777777777777,
    0.08888888888888888,
    0.1,
    0.1,
    0.08888888888888888,
    0.07777777777777777,
    0.06666666666666667,
    0.05555555555555556,
    0.04444444444444444,
    0.03333333333333333,
    0.02222222222222222,
    0.01111111111111111,
    0.0,
]


class Player:
    """
    Represents the main character in the infinite runner.

    Attributes:
        x (int): The x-coordinate of the player's position.
        y (int): The y-coordinate of the player's position.
        width (int): The width of the player's rectangle for collision.
        height (int): The height of the player's rectangle for collision.
        velocity_x (int): Horizontal speed.
        velocity_y (int): Vertical speed.
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
        self.world_x = x
        self.world_y = y
        self.width = width
        self.height = height

        # Movement and physics
        self.velocity_x = 0
        self.velocity_y = 5
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
        self.image = pygame.image.load("resources/image/player.png").convert_alpha()
        
        # Frame
        self.frames = []
        SPRITE_WIDTH = self.image.get_width() // 8
        SPRITE_HEIGHT = self.image.get_height()
        
        for i in range(8):
            frame = self.image.subsurface(pygame.Rect(i * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
            frame = pygame.transform.scale(frame, (SPRITE_WIDTH * 4, SPRITE_HEIGHT * 4))
            self.frames.append(frame)
        
        # Animation
        self.current_frame = 0
        self.animation_speed = 5
        self.frame_counter = 0
        
        self.rect = self.frames[0].get_rect(center = (self.x, self.y))
        
        
        # Or a simple placeholder:
        #self.color = (255, 0, 0)  # Red

        # smooth movement
        self.x_per_frame = []
        self.x_smooth_dist = 0

    def update_animation(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_counter = 0
    
    def move_left(self):
        """
        Move the player to the next lane on the left.
        """
        if self.current_lane > 0:
            self.current_lane -= 1
            # self.x = self.lane_positions[self.current_lane]
            self.x_per_frame = [
                -x for x in SMOOTH1.copy()
            ]  # reverse the list and multiply by -1
            self.x_smooth_dist = self.x - self.lane_positions[self.current_lane]

    def move_right(self):
        """
        Move the player to the next lane on the right.
        """
        if self.current_lane < len(self.lane_positions) - 1:
            self.current_lane += 1
            # self.x = self.lane_positions[self.current_lane]
            self.x_per_frame = SMOOTH1.copy()
            self.x_smooth_dist = self.lane_positions[self.current_lane] - self.x


    # def jump(self):
    #     """
    #     Make the player jump.
    #     Only works if the player is on the ground (on_ground == True).
    #     """
    #     if self.on_ground:
    #         self.velocity_y = self.jump_strength
    #         self.on_ground = False

    def update(self):
        """
        Update the player's position each frame.
        Handles gravity, vertical movement, and ground check.
        """

        # smooth movement
        if len(self.x_per_frame) > 0:
            self.x += self.x_per_frame[-1] * self.x_smooth_dist

            self.world_x = self.x
            self.x_per_frame.pop()
        else:
            self.x_per_frame = [0, 0, 0, 0, 0, 0, 0, 0]
            

        self.rect.center = (self.x, self.y)

        # Update y-position

        self.world_y += self.velocity_y
        
        # # Check if we've hit the 'ground'.
        # # For a 2D runner, you might have a fixed ground level (e.g., y=500).
        # # Adjust based on your game window size.
        # ground_level = 500
        # if self.y + self.height > ground_level:
        #     self.y = ground_level - self.height
        #     self.velocity_y = 0
        #     self.on_ground = True=

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
        return pygame.Rect(
            self.x - self.width / 2, self.y - self.height / 2, self.width, self.height
        )

    def draw(self, surface):
        """
        Draw the player on the given surface.
        If you have a sprite/image, you can blit it. Otherwise, draw a rectangle as a placeholder.

        :param surface: The pygame surface to draw on.
        """
        # If you have an image:
        self.update_animation()
        surface.blit(self.frames[self.current_frame], (self.rect.topleft))

        # Using a rectangle placeholder:
        # pygame.draw.rect(
        #     surface,
        #     self.color,
        #     (
        #         self.x - self.width / 2,
        #         self.y - self.height / 2,
        #         self.width,
        #         self.height,
        #     ),
        # )

        # draw collision box
        # pygame.draw.rect(
        #     surface,
        #     (0, 255, 0),
        #     (
        #         self.x - self.width / 2,
        #         self.y - self.height / 2,
        #         self.width,
        #         self.height,
        #     ),
        #     1,
        # )
