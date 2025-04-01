import os
import pygame
from os import listdir
from os.path import isfile, join
from src.config.settings import ASSETS_DIR, WIDTH, HEIGHT

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("src", ASSETS_DIR, dir1, dir2)
    try:
        images = [f for f in listdir(path) if isfile(join(path, f))]
    except FileNotFoundError:
        print(f"Warning: Could not find directory: {path}")
        return {}

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def get_block(size):
    path = join("src", ASSETS_DIR, "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(17, 4, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

def get_background():
    path = join("src", ASSETS_DIR, "Background", "space.jpg")
    background = pygame.image.load(path).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    return background 