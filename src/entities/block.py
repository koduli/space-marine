import pygame
from src.entities.object import Object
from src.utils.sprite_utils import get_block

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, "block")
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, window, offset_x=0):
        window.blit(self.image, (self.rect.x - offset_x, self.rect.y)) 