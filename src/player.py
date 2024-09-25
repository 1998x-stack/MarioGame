import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pygame
from config.settings import (
    PLAYER_SPEED, PLAYER_JUMP_FORCE, GRAVITY, MARIO_WIDTH, MARIO_HEIGHT, PLAYER_MAX_JUMPS
)
from config.assets_config import MARIO_IMAGE, JUMP_SOUND, COIN_SOUND

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize player position, speed, and state"""
        super().__init__()
        self.image = pygame.image.load(MARIO_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (MARIO_WIDTH, MARIO_HEIGHT))
        self.rect = self.image.get_rect(topleft=(100, 400))

        # Movement attributes
        self.speed_x = 0
        self.speed_y = 0
        self.on_ground = False
        self.jump_count = 0  # To implement double jump
        self.space_pressed = False  # To prevent continuous jumping
        self.dead = False    # Player's alive status

        # Load sounds
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.coin_sound = pygame.mixer.Sound(COIN_SOUND)

    def handle_keys(self):
        """Handle keyboard input"""
        keys = pygame.key.get_pressed()

        # Move left/right
        self.speed_x = 0  # Reset horizontal speed each frame
        if keys[pygame.K_LEFT]:
            self.speed_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.speed_x = PLAYER_SPEED

        # Jump
        if keys[pygame.K_SPACE]:
            if not self.space_pressed:
                if self.jump_count < PLAYER_MAX_JUMPS:
                    self.speed_y = -PLAYER_JUMP_FORCE
                    self.jump_count += 1
                    self.jump_sound.play()  # Play jump sound effect
                self.space_pressed = True
        else:
            self.space_pressed = False

    def apply_gravity(self):
        """Apply gravity acceleration"""
        self.speed_y += GRAVITY
        if self.speed_y > PLAYER_JUMP_FORCE:
            self.speed_y = PLAYER_JUMP_FORCE  # Terminal velocity

    def update(self, tiles_group, enemies_group, coins_group, game):
        """Update player's logic"""
        self.handle_keys()
        self.apply_gravity()

        # Move horizontally and check for collisions
        self.rect.x += self.speed_x
        # Prevent moving beyond the left boundary
        if self.rect.x < 0:
            self.rect.x = 0

        self.check_collision(tiles_group, 'horizontal')

        # Move vertically and check for collisions
        self.rect.y += self.speed_y
        self.check_collision(tiles_group, 'vertical')

        # Check for collision with enemies
        enemy_hit_list = pygame.sprite.spritecollide(self, enemies_group, False)
        for enemy in enemy_hit_list:
            if self.speed_y > 0 and self.rect.bottom <= enemy.rect.bottom:  # Falling down, so defeat the enemy
                self.rect.bottom = enemy.rect.top
                self.speed_y = -PLAYER_JUMP_FORCE / 2  # Bounce up
                self.jump_sound.play()
                enemy.die(game.level, game)
            else:
                # Player dies if hit from the side or bottom
                self.die()

        # Check for collision with coins
        coin_hit_list = pygame.sprite.spritecollide(self, coins_group, True)
        for coin in coin_hit_list:
            self.coin_sound.play()
            game.score += 1

    def check_collision(self, group, direction):
        """Check collision with a group"""
        collisions = pygame.sprite.spritecollide(self, group, False)
        for sprite in collisions:
            if direction == 'horizontal':
                if self.speed_x > 0:  # Moving right
                    self.rect.right = sprite.rect.left
                if self.speed_x < 0:  # Moving left
                    self.rect.left = sprite.rect.right
            elif direction == 'vertical':
                if self.speed_y > 0:  # Falling down
                    self.rect.bottom = sprite.rect.top
                    self.speed_y = 0
                    self.on_ground = True
                    self.jump_count = 0  # Reset jump count when landing
                if self.speed_y < 0:  # Moving up
                    self.rect.top = sprite.rect.bottom
                    self.speed_y = 0

        if not collisions and direction == 'vertical':
            self.on_ground = False

    def die(self):
        """Handle player death"""
        self.dead = True