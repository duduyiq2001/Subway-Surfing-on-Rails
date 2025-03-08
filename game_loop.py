# For game loop
import pygame
import sys
import time

from map_generator import draw_map
from player import Player
from obstacle import Obstacle
# collison


def game_loop(screen, clock, fps, update_func):
    # Constants
    WIDTH, HEIGHT = 1280, 720
    TRACK_COUNT = 5
    SIDE_WIDTH = 220
    TRACK_WIDTH = (WIDTH - 2 * SIDE_WIDTH) // TRACK_COUNT
    MOVE_COOLDOWN = 0.5

    # First player
    player_x = SIDE_WIDTH + 2.5 * TRACK_WIDTH
    player_y = HEIGHT // 4 * 3

    # Initialize player
    player = Player(
        x=player_x,
        y=player_y,
        lane_positions=[
            SIDE_WIDTH + (i + 0.5) * TRACK_WIDTH for i in range(TRACK_COUNT)
        ],
    )
    prev_time = time.time()
    
    # Initialize obstacles
    obstacles = []
    obstacle_spawn_time = 0

    # Main loop
    running = True
    while running:
        dt = clock.tick(fps) / 1000
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                print("key pressed", event.key)
                if event.key == pygame.K_a:
                    player.move_left()
                elif event.key == pygame.K_d:
                    player.move_right()

        # Draw map
        draw_map(screen)

        # Draw player
        player.draw(screen)
              
        # Handle player movement
        # print(time.time() - prev_time)
        if time.time() - prev_time > MOVE_COOLDOWN:
            update_func(player)
            prev_time = time.time()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_d]:
            player.move_right()
            
        # Obstacle spawning
        obstacle_spawn_time += dt
        if obstacle_spawn_time > 1.5:  # Spawn every second
            obstacles.append(Obstacle(player.lane_positions))
            obstacle_spawn_time = 0

        for obstacle in obstacles:
            obstacle.update(dt)

        for obstacle in obstacles:
            if obstacle.check_collision(player):
                print("Collision detected!")
                running = False
                return

        # Remove off-screen obstacles
        obstacles = [ob for ob in obstacles if ob.y < HEIGHT]
        
        # Draw obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)
        
        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()
