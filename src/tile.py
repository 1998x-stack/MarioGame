import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


import pygame
from config.assets_config import TILE_IMAGE
from config.settings import TILE_WIDTH, TILE_HEIGHT

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initialize tile position and image"""
        super().__init__()
        self.image = pygame.image.load(TILE_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))