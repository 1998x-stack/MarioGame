import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

# ui.py
import pygame
from config.colors import WHITE

class UI:
    def __init__(self, font_size=30):
        """Initialize UI font"""
        self.font = pygame.font.SysFont('Arial', font_size)

    def draw_text(self, screen, text, x, y, centered=False):
        """Draw text on the screen"""
        label = self.font.render(text, True, WHITE)
        if centered:
            rect = label.get_rect(center=(x, y))
            screen.blit(label, rect)
        else:
            screen.blit(label, (x, y))

    def draw_score(self, screen, score):
        """Draw the score"""
        self.draw_text(screen, f"Score: {score}", 10, 10)

    def draw_lives(self, screen, lives):
        """Draw remaining lives"""
        self.draw_text(screen, f"Lives: {lives}", 10, 40)