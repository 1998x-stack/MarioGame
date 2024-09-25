import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pygame
from src.player import Player
from src.level import Level
from src.ui import UI
from config.assets_config import BG_MUSIC
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, LEVEL_WIDTH, MARIO_WIDTH

class Game:
    def __init__(self, screen: pygame.Surface):
        """Initialize the game, including player and level"""
        self.screen = screen
        self.ui = UI()
        self.camera_x = 0  # Horizontal scroll camera offset

        # Game variables
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.level_number = 1  # Start at level 1

        # Initialize the first level
        self.load_level(self.level_number)

        # Load and play background music
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.play(-1)  # Loop indefinitely

        # Timer for displaying level number
        self.level_display_time = 2000  # Display level number for 2 seconds
        self.level_display_timer = pygame.time.get_ticks()

    def load_level(self, level_number):
        """Load a level"""
        self.level = Level(level_number)
        self.player = Player()

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.level.tiles_group)
        self.all_sprites.add(self.level.enemies_group)
        self.all_sprites.add(self.level.coins_group)

        # Reset camera
        self.camera_x = 0

        # Reset level display timer
        self.level_display_timer = pygame.time.get_ticks()

    def update(self) -> bool:
        """Update game state and handle events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if not self.game_over:
            # Update player and level
            self.player.update(self.level.tiles_group, self.level.enemies_group, self.level.coins_group, self)
            self.level.update()

            # Check for player death
            if self.player.dead:
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over = True
                else:
                    # Reset player position and state
                    self.player.rect.topleft = (100, 400)
                    self.player.speed_x = 0
                    self.player.speed_y = 0
                    self.player.dead = False
                    self.player.jump_count = 0

            # Check if level is completed
            if self.player.rect.x >= LEVEL_WIDTH - MARIO_WIDTH:
                # Move to the next level
                self.level_number += 1
                self.load_level(self.level_number)

            # Adjust camera to keep the player in view
            self.update_camera()

        return True

    def update_camera(self):
        """Update camera based on player's position"""
        # Start scrolling when the player exceeds 40% of the screen width
        self.camera_x = max(0, self.player.rect.x - WINDOW_WIDTH * 0.4)
        # Ensure camera doesn't go beyond level bounds
        max_camera_x = LEVEL_WIDTH - WINDOW_WIDTH
        if self.camera_x > max_camera_x:
            self.camera_x = max_camera_x

    def render(self):
        """Render the game screen"""
        self.screen.fill((0, 0, 0))  # Clear screen

        # Draw level elements
        self.level.draw(self.screen, self.camera_x)

        # Draw player
        self.screen.blit(self.player.image, (self.player.rect.x - self.camera_x, self.player.rect.y))

        # Draw UI elements
        self.ui.draw_score(self.screen, self.score)
        self.ui.draw_lives(self.screen, self.lives)

        # Display Level Number at the beginning of the level
        current_time = pygame.time.get_ticks()
        if current_time - self.level_display_timer < self.level_display_time:
            self.ui.draw_text(self.screen, f"Level {self.level_number}", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, centered=True)
        if self.game_over:
            self.ui.draw_text(self.screen, "Game Over", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, centered=True)

        pygame.display.flip()  # Update display