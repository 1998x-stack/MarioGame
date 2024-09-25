import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

import pygame
import random
from src.enemy import Enemy
from src.tile import Tile
from src.coin import Coin
from config.assets_config import BACKGROUND_IMAGE
from config.settings import TILE_SIZE, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, LEVEL_WIDTH, COIN_HEIGHT, COIN_WIDTH

class Level:
    def __init__(self, level_number):
        """Initialize level and background"""
        self.level_number = level_number
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.tiles_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()

        # Generate level based on level_number
        if self.level_number == 1:
            self.create_level_1()
        elif self.level_number == 2:
            self.create_level_2()
        elif self.level_number == 3:
            self.create_level_3()
        else:
            # Optional: Handle levels beyond those defined
            self.create_default_level()
        
        # # Generate level using the generalized create_level method
        # self.create_level(self.level_number)
            
    def create_level(self, level):
        """Generalized function to create levels based on level parameter"""
        if level == 1:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=40, 
                floating_tile_pattern=[(10, 400), (20, 300)], 
                enemy_positions=[(600, 450, 500, 700), (1200, 450, 1100, 1300)], 
                coin_probability=0.3
            )
        elif level == 2:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=50, 
                floating_tile_pattern=[(5, 400), (20, 300), (35, 200)], 
                enemy_positions=[(10 * TILE_SIZE, 350, 10 * TILE_SIZE, 19 * TILE_SIZE), 
                                 (22 * TILE_SIZE, 250, 22 * TILE_SIZE, 30 * TILE_SIZE)], 
                coin_probability=0.4
            )
        elif level == 3:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=60, 
                floating_tile_pattern=[(12, 400), (22, 300), (34, 200)], 
                enemy_positions=[(12 * TILE_SIZE, 350, 10 * TILE_SIZE, 20 * TILE_SIZE), 
                                 (24 * TILE_SIZE, 250, 22 * TILE_SIZE, 30 * TILE_SIZE)], 
                coin_probability=0.5
            )
        elif level == 4:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=70, 
                floating_tile_pattern=[(15, 400), (25, 350)], 
                enemy_positions=[(15 * TILE_SIZE, 350, 15 * TILE_SIZE, 24 * TILE_SIZE), 
                                 (27 * TILE_SIZE, 300, 25 * TILE_SIZE, 35 * TILE_SIZE)], 
                coin_probability=0.6
            )
        elif level == 5:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=80, 
                floating_tile_pattern=[(10, 400), (30, 350), (50, 300)], 
                enemy_positions=[(12 * TILE_SIZE, 350, 10 * TILE_SIZE, 20 * TILE_SIZE), 
                                 (32 * TILE_SIZE, 250, 30 * TILE_SIZE, 40 * TILE_SIZE)], 
                coin_probability=0.7
            )
        elif level == 6:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=90, 
                floating_tile_pattern=[(20, 400), (40, 350), (60, 300)], 
                enemy_positions=[(22 * TILE_SIZE, 350, 20 * TILE_SIZE, 30 * TILE_SIZE), 
                                 (42 * TILE_SIZE, 300, 40 * TILE_SIZE, 50 * TILE_SIZE)], 
                coin_probability=0.75
            )
        elif level == 7:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=100, 
                floating_tile_pattern=[(15, 400), (35, 350), (55, 300)], 
                enemy_positions=[(17 * TILE_SIZE, 350, 15 * TILE_SIZE, 25 * TILE_SIZE), 
                                 (37 * TILE_SIZE, 300, 35 * TILE_SIZE, 45 * TILE_SIZE)], 
                coin_probability=0.8
            )
        elif level == 8:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=110, 
                floating_tile_pattern=[(20, 400), (50, 350), (70, 300)], 
                enemy_positions=[(22 * TILE_SIZE, 350, 20 * TILE_SIZE, 30 * TILE_SIZE), 
                                 (52 * TILE_SIZE, 300, 50 * TILE_SIZE, 60 * TILE_SIZE)], 
                coin_probability=0.85
            )
        elif level == 9:
            self.create_level_with_tiles_and_enemies(
                ground_tile_count=120, 
                floating_tile_pattern=[(25, 400), (60, 350), (80, 300)], 
                enemy_positions=[(27 * TILE_SIZE, 350, 25 * TILE_SIZE, 35 * TILE_SIZE), 
                                 (62 * TILE_SIZE, 300, 60 * TILE_SIZE, 70 * TILE_SIZE)], 
                coin_probability=0.9
            )
        else:
            # Optional: Handle levels beyond those defined
            self.create_default_level()

    def create_level_with_tiles_and_enemies(self, ground_tile_count, floating_tile_pattern, enemy_positions, coin_probability):
        """
        Creates the level layout with tiles, enemies, and coins.
        
        Parameters:
        ground_tile_count (int): The number of ground tiles.
        floating_tile_pattern (list of tuples): Each tuple contains (x_tile_index, y_position) for floating tiles.
        enemy_positions (list of tuples): Each tuple contains (x, y, patrol_start_x, patrol_end_x) for enemies.
        coin_probability (float): The probability of placing a coin on a tile.
        """

        # Generate ground tiles across the level
        for i in range(ground_tile_count):
            tile = Tile(i * TILE_SIZE, 500)
            self.tiles_group.add(tile)

        # Generate floating platforms based on the pattern
        for pattern in floating_tile_pattern:
            tile_x_index, tile_y = pattern
            tile = Tile(tile_x_index * TILE_SIZE, tile_y)
            self.tiles_group.add(tile)

        # Spawn enemies with patrol ranges based on the positions provided
        for enemy_pos in enemy_positions:
            enemy_x, enemy_y, patrol_start_x, patrol_end_x = enemy_pos
            enemy = Enemy(enemy_x, enemy_y, move_range=(patrol_start_x, patrol_end_x))
            self.enemies_group.add(enemy)

        # Place coins on top of tiles with a certain probability
        for tile in self.tiles_group:
            if random.random() < coin_probability:
                coin = Coin(tile.rect.x + (TILE_SIZE - COIN_WIDTH) // 2, tile.rect.y - COIN_HEIGHT)
                self.coins_group.add(coin)

    def create_level_1(self):
        """Create Level 1"""
        # Generate ground tiles across the entire level width
        for i in range(0, LEVEL_WIDTH, TILE_SIZE):
            tile = Tile(i, 500)
            self.tiles_group.add(tile)

        # Randomly place floating platforms
        self.generate_floating_tiles()

        # Initialize enemies
        self.spawn_enemies()

        # Generate coins on tiles
        self.generate_coins()

    def create_level_2(self):
        """Create Level 2 with consecutive tiles in the air and enemy patrols"""
        # Generate ground tiles
        for i in range(0, LEVEL_WIDTH, TILE_SIZE):
            tile = Tile(i, 500)
            self.tiles_group.add(tile)

        # Create consecutive floating platforms
        for i in range(5, 15):
            tile = Tile(i * TILE_SIZE, 400)
            self.tiles_group.add(tile)

        for i in range(20, 30):
            tile = Tile(i * TILE_SIZE, 300)
            self.tiles_group.add(tile)

        # Spawn enemies patrolling on floating platforms
        enemy1 = Enemy(5 * TILE_SIZE, 350, move_range=(5 * TILE_SIZE, 14 * TILE_SIZE))
        enemy2 = Enemy(20 * TILE_SIZE, 250, move_range=(20 * TILE_SIZE, 29 * TILE_SIZE))
        self.enemies_group.add(enemy1, enemy2)

        # Generate coins on floating platforms
        for i in range(5, 15):
            if random.random() < 0.5:
                coin = Coin(i * TILE_SIZE + (TILE_SIZE - COIN_WIDTH) // 2, 400 - COIN_HEIGHT)
                self.coins_group.add(coin)
        for i in range(20, 30):
            if random.random() < 0.5:
                coin = Coin(i * TILE_SIZE + (TILE_SIZE - COIN_WIDTH) // 2, 300 - COIN_HEIGHT)
                self.coins_group.add(coin)

    def create_level_3(self):
        """Create Level 3 with unique design"""
        # Generate ground tiles across the entire level width
        for i in range(0, LEVEL_WIDTH, TILE_SIZE):
            tile = Tile(i, 500)
            self.tiles_group.add(tile)

        # Create challenging platform layout
        for i in range(10, 20):
            tile = Tile(i * TILE_SIZE, 400)
            self.tiles_group.add(tile)
        for i in range(22, 32):
            tile = Tile(i * TILE_SIZE, 300)
            self.tiles_group.add(tile)
        for i in range(34, 44):
            tile = Tile(i * TILE_SIZE, 200)
            self.tiles_group.add(tile)

        # Spawn enemies with patrol ranges on platforms
        enemy1 = Enemy(12 * TILE_SIZE, 350, move_range=(10 * TILE_SIZE, 19 * TILE_SIZE))
        enemy2 = Enemy(24 * TILE_SIZE, 250, move_range=(22 * TILE_SIZE, 31 * TILE_SIZE))
        enemy3 = Enemy(36 * TILE_SIZE, 150, move_range=(34 * TILE_SIZE, 43 * TILE_SIZE))
        self.enemies_group.add(enemy1, enemy2, enemy3)

        # Generate coins on platforms
        for tile in self.tiles_group:
            if random.random() < 0.5:
                coin = Coin(tile.rect.x + (TILE_SIZE - COIN_WIDTH) // 2, tile.rect.y - COIN_HEIGHT)
                self.coins_group.add(coin)
                
    def create_default_level(self):
        """Create a default level or loop back to Level 1"""
        self.level_number = 1  # Reset to Level 1
        self.create_level_1()

    def generate_coins(self):
        """Generate coins on top of tiles"""
        for tile in self.tiles_group:
            # 30% chance to have a coin on a tile
            if random.random() < 0.3:
                coin = Coin(tile.rect.x + (TILE_SIZE - COIN_WIDTH) // 2, tile.rect.y - COIN_HEIGHT)
                self.coins_group.add(coin)

    def spawn_enemies(self):
        """Spawn enemies"""
        # Spawn enemies with specific movement ranges
        enemy1 = Enemy(600, 450, move_range=(500, 700))
        enemy2 = Enemy(1200, 450, move_range=(1100, 1300))
        self.enemies_group.add(enemy1, enemy2)

    def generate_floating_tiles(self):
        """Generate random floating platforms"""
        num_floating_tiles = 10  # Generate 10 random platforms
        for _ in range(num_floating_tiles):
            tile_x = random.randint(5, (LEVEL_WIDTH // TILE_SIZE) - 5) * TILE_SIZE  # Random horizontal position
            tile_y = random.randint(200, 400)  # Random vertical position, ensuring platforms are in the air
            tile = Tile(tile_x, tile_y)
            self.tiles_group.add(tile)

    def update(self):
        """Update level elements"""
        self.enemies_group.update()

    def draw(self, screen, camera_x):
        """Draw level background and ground"""
        # Draw background
        screen.blit(self.background, (-camera_x, 0))

        # Draw tiles
        for tile in self.tiles_group:
            screen.blit(tile.image, (tile.rect.x - camera_x, tile.rect.y))

        # Draw enemies
        for enemy in self.enemies_group:
            screen.blit(enemy.image, (enemy.rect.x - camera_x, enemy.rect.y))

        # Draw coins
        for coin in self.coins_group:
            screen.blit(coin.image, (coin.rect.x - camera_x, coin.rect.y))