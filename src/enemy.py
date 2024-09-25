import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pygame
from config.assets_config import ENEMY_IMAGE, COIN_SOUND
from config.settings import ENEMY_HEIGHT, ENEMY_WIDTH
from src.coin import Coin

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_range):
        """Initialize enemy position and image"""
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.start_x = x
        self.move_range = move_range  # Tuple (min_x, max_x)
        self.speed = 2  # Enemy movement speed

    def update(self):
        """Enemy movement logic"""
        # Simple left-right movement within the move_range
        self.rect.x += self.speed
        if self.rect.x <= self.move_range[0]:
            self.rect.x = self.move_range[0]
            self.speed = -self.speed  # Reverse direction
        elif self.rect.x >= self.move_range[1]:
            self.rect.x = self.move_range[1]
            self.speed = -self.speed  # Reverse direction

    def die(self, level, game):
        """Handle enemy death, turning into a coin"""
        # Play coin sound
        pygame.mixer.Sound(COIN_SOUND).play()
        # Create a coin at enemy's position
        coin = Coin(self.rect.x, self.rect.y)
        level.coins_group.add(coin)
        # Remove enemy from all groups
        self.kill()
        # Update the score
        game.score += 1