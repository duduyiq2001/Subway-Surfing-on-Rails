import pygame


class Coin:
    def __format__(self, format_spec: str) -> str:
        return f"Coin(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self):
        return f"Coin(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __repr__(self):
        return f"Coin(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(
            self.x - self.width // 2, self.y - self.height // 2, self.width, self.height
        )

    def update(self, dt):
        self.y += dt
        self.rect.y = self.y - self.height // 2

    def draw(self, screen):
        screen.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
