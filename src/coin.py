import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pygame
from config.assets_config import COIN_IMAGE
from config.settings import COIN_WIDTH, COIN_HEIGHT

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initialize coin position and image"""
        super().__init__()
        self.image = pygame.image.load(COIN_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (COIN_WIDTH, COIN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))