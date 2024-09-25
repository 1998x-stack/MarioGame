import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

# settings.py

# Window Settings
WINDOW_WIDTH = 800    # Game window width
WINDOW_HEIGHT = 600   # Game window height
FPS = 60              # Frames per second

# Level Settings
LEVEL_WIDTH = 3000    # Total width of the level
LEVEL_HEIGHT = WINDOW_HEIGHT

# Player Settings
PLAYER_SPEED = 5          # Mario's movement speed
PLAYER_JUMP_FORCE = 15    # Mario's jump force
GRAVITY = 1               # Gravity acceleration
PLAYER_MAX_JUMPS = 2      # Number of allowed jumps (double jump)

# Enemy Settings
ENEMY_MOVEMENT_RANGE = 200  # Enemies move within this range

# Game Settings
TILE_SIZE = 50        # Size of platforms or objects (e.g., ground tiles)

# Image Sizes (in pixels)
MARIO_WIDTH = 40      # Mario's width
MARIO_HEIGHT = 60     # Mario's height
ENEMY_WIDTH = 40      # Enemy's width
ENEMY_HEIGHT = 60     # Enemy's height
BACKGROUND_WIDTH = LEVEL_WIDTH  # Background image width adjusted to cover entire level
BACKGROUND_HEIGHT = WINDOW_HEIGHT  # Background image height
TILE_WIDTH = TILE_SIZE             # Ground tile width
TILE_HEIGHT = TILE_SIZE            # Ground tile height
COIN_WIDTH = 30      # Coin width
COIN_HEIGHT = 30     # Coin height