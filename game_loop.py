# For game loop
import pygame
import sys
import time
import random

# from map_manager import MapManager
from player import Player
from obstacle import Obstacle
from obstacle_manager import ObstacleManager
from map import Map
# collison


def game_loop(screen, clock, fps, update_func):
    # Constants
    WIDTH, HEIGHT = 1280, 720
    TRACK_COUNT = 5
    SIDE_WIDTH = 220
    TRACK_WIDTH = (WIDTH - 2 * SIDE_WIDTH) // TRACK_COUNT
    MOVE_COOLDOWN = 0.5
    SEG_LENGTH = 7200
    GAME_LENGTH = 30000
    GAME_SPEED = 10
    # NUM OF objects per type
    OBJ_NUM = 10
    LANE_POS = [SIDE_WIDTH + (i + 0.5) * TRACK_WIDTH for i in range(TRACK_COUNT)]

    # First player
    player_x = SIDE_WIDTH + 2.5 * TRACK_WIDTH
    player_y = HEIGHT // 4 * 3

    # Initialize player
    player = Player(
        x=player_x,
        y=player_y,
        lane_positions=LANE_POS,
        speed=GAME_SPEED,
    )
    prev_time = time.time()

    # Initialize obstacles
    objs = []

    interval = SEG_LENGTH / OBJ_NUM
    # 90 + i*5, 25 + i
    for i in range(OBJ_NUM):
        objs.append(
            Obstacle(
                i % TRACK_COUNT,
                i * interval,
                LANE_POS,
                "hurdle",
                SEG_LENGTH,
                90 + i * 5,
                80 + i * 5,
            )
        )

    print("swdwjqdbwqd")

    obstacle_manager = ObstacleManager(LANE_POS, SEG_LENGTH, objs)

    # Initialize font
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)

    # Initialize map
    # map_manager = MapManager(screen)
    map_pos_y = 0
    static_map = pygame.surface.Surface((WIDTH, HEIGHT))
    map = Map(screen=static_map, pos_y=0)
    # draw everything in the background here
    map.draw(static_map)

    static_map_2 = pygame.surface.Surface((WIDTH, HEIGHT * 2))
    static_map_2.blit(static_map, (0, 0))
    static_map_2.blit(static_map, (0, HEIGHT))

    screen.blit(static_map_2, (0, -HEIGHT))

    while player.world_y <= GAME_LENGTH:
        dt = clock.tick(fps) / 1000

        ####### Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                print("key pressed", event.key)
                if event.key == pygame.K_a:
                    player.move_left()
                elif event.key == pygame.K_d:
                    player.move_right()

        #### rendering
        # Draw map
        screen.blit(static_map_2, (0, -HEIGHT + map_pos_y))
        # Draw player
        player.draw(screen)

        # Draw other players

        # Draw obstacles
        obstacle_manager.draw(screen)

        ##### updating
        player.update()
        # map_manager.update(player.velocity_y)
        map_pos_y += player.velocity_y
        if map_pos_y > HEIGHT:
            map_pos_y = 0

        # Handle player movement
        # print(time.time() - prev_time)
        if time.time() - prev_time > MOVE_COOLDOWN:
            update_func(player)
            prev_time = time.time()

        # Update other players

        # Update obstacles

        obstacle_manager.update(
            (player.world_x, player.world_y), (player.x, player.y), SEG_LENGTH
        )

        # Check for collisions
        if obstacle_manager.check_collision(player):
            print("Collision detected!")
            player.velocity_y = 0
            continue
        else:
            player.velocity_y = GAME_SPEED

        # running = False
        # return

        # Calculate and display FPS
        fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
        progress_text = font.render(
            f"Progress: {int(player.world_y / GAME_LENGTH * 100)}%",
            True,
            (0, 0, 0),
        )

        score_text = font.render(f"Score: {player.score}", True, (0, 0, 0))
        screen.blit(fps_text, (10, 10))
        screen.blit(progress_text, (10, 30))
        screen.blit(score_text, (10, 50))
        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    pygame.quit()
    sys.exit()
