import pygame
from coin import Coin

import random


class CoinsManager:
    def __init__(self):
        self.coins = set()
        self.coins_pic = pygame.image.load("./resources/image/coin.png")
        self.coins_pic = pygame.transform.scale(
            self.coins_pic,
            (self.coins_pic.get_width() // 2, self.coins_pic.get_height() // 2),
        )

    def generate(self, lane_pos, obstacle_manager, HEIGHT):
        if len(self.coins) >= 5:
            return

        coin_x = random.choice(lane_pos)
        coin_y = -HEIGHT - random.randint(0, HEIGHT // 2)

        new_coin = Coin(
            coin_x,
            coin_y,
            self.coins_pic.get_height(),
            self.coins_pic.get_width(),
            self.coins_pic,
        )

        # two coins cannot be generated in the same time
        for coin in self.coins:
            if new_coin.rect.colliderect(coin.rect):
                return

        # two coins cannot be generated in the same time
        # for obstacle in obstacle_manager.obstacles:
        #     if new_coin.rect.colliderect(obstacle.rect):
        #         return

        self.coins.add(new_coin)

    def update(self, dt, HEIGHT):
        print(self.coins)
        for coin in self.coins:
            coin.update(dt)

        self.coins = {coin for coin in self.coins if coin.rect.y < HEIGHT}

        #

    #     for coin in self.coins:
    #         coin.update()

    def check_collision(self, player):
        for coin in self.coins:
            if coin.rect.colliderect(player.rect):
                player.score += player.score_per_coin

        self.coins = {
            coin for coin in self.coins if not coin.rect.colliderect(player.rect)
        }

    def draw(self, screen, player, HEIGHT):
        for coin in self.coins:
            pygame.draw.rect(screen, (255, 0, 0), coin.rect, 2)
            coin.draw(screen)
