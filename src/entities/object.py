import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name="object"):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.rect) 