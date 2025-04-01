import pygame
from src.entities.object import Object
from src.utils.sprite_utils import load_sprite_sheets
from src.config.settings import PLAYER_ANIMATION_DELAY

class Fire(Object):
    ANIMATION_DELAY = PLAYER_ANIMATION_DELAY

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        
        if not self.fire or "on" not in self.fire:
            print(f"Warning: Failed to load fire sprites at {x}, {y}")
            self.fire = {
                "off": [pygame.Surface((width, height), pygame.SRCALPHA)],
                "on": [pygame.Surface((width, height), pygame.SRCALPHA)]
            }
            
            pygame.draw.rect(self.fire["off"][0], (255, 0, 0), pygame.Rect(0, 0, width, height))
            pygame.draw.rect(self.fire["on"][0], (255, 128, 0), pygame.Rect(0, 0, width, height))
        
        self.image = self.fire["on"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "on"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

    def draw(self, window, offset_x=0):
        window.blit(self.image, (self.rect.x - offset_x, self.rect.y)) 