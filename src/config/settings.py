import os
import pygame

WIDTH = 1920
HEIGHT = 1080
FPS = 60

PLAYER_VEL = 5
PLAYER_GRAVITY = 0.8
PLAYER_ANIMATION_DELAY = 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FONT_SIZE = 36
FONT_COLOR = BLACK
HEALTH_BAR_COLOR = GREEN
HEALTH_BAR_BG_COLOR = RED

ASSETS_DIR = "assets"
SPRITES_DIR = os.path.join(ASSETS_DIR, "sprites")

PLAYER_DIR = os.path.join(ASSETS_DIR, "Player")
ANIMATIONS_DIR = os.path.join(PLAYER_DIR, "Animations")

TRAPS_DIR = os.path.join(ASSETS_DIR, "Traps")
FIRE_DIR = os.path.join(TRAPS_DIR, "Fire")

def load_player_sprites():
    sprites = {}
    for animation in ["idle", "run", "jump", "fall"]:
        path = os.path.join("src", ANIMATIONS_DIR, f"{animation}.png")
        sprite_sheet = pygame.image.load(path).convert_alpha()
        width = sprite_sheet.get_width() // 3
        height = sprite_sheet.get_height()
        
        sprites[f"{animation}_right"] = []
        for i in range(3):
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            scaled_surface = pygame.transform.scale(surface, (width * 2, height * 2))
            sprites[f"{animation}_right"].append(scaled_surface)
        
        sprites[f"{animation}_left"] = []
        for i in range(3):
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            scaled_surface = pygame.transform.scale(surface, (width * 2, height * 2))
            flipped_surface = pygame.transform.flip(scaled_surface, True, False)
            sprites[f"{animation}_left"].append(flipped_surface)
    
    return sprites 