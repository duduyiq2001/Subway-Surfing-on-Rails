import pygame
import os

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
FPS = 10  # Adjust for animation speed

# Abosulute path to the sprite sheet
img_path = os.path.abspath("./resources/image/walk_Up.png")

# Load sprite sheet
sprite_sheet = pygame.image.load(img_path)

# Get sprite dimensions
SPRITE_WIDTH = sprite_sheet.get_width() // 8  # Assuming 8 frames
SPRITE_HEIGHT = sprite_sheet.get_height()

# Extract frames
frames = []
for i in range(8):
    frame = sprite_sheet.subsurface(pygame.Rect(i * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
    frames.append(frame)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation")

# Main loop
running = True
clock = pygame.time.Clock()
frame_index = 0
x, y = WIDTH // 2, HEIGHT // 2  # Initial position

while running:
    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(frames[frame_index], (x, y))  # Draw current frame

    frame_index = (frame_index + 1) % len(frames)  # Loop animation

    pygame.display.flip()
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()