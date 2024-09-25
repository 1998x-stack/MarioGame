import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))

# assets_config.py

# Base Asset Paths
ASSETS_DIR = os.path.join("assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

# Image Paths
MARIO_IMAGE = os.path.join(IMAGES_DIR, "mario.png")
BACKGROUND_IMAGE = os.path.join(IMAGES_DIR, "background.png")
ENEMY_IMAGE = os.path.join(IMAGES_DIR, "enemy.png")
COIN_IMAGE = os.path.join(IMAGES_DIR, "coin.png")  # Coin image
TILE_IMAGE = os.path.join(IMAGES_DIR, "tile.png")  # Ground tile image

# Sound Paths
JUMP_SOUND = os.path.join(SOUNDS_DIR, "jump.wav")
BG_MUSIC = os.path.join(SOUNDS_DIR, "background.mp3")
COIN_SOUND = os.path.join(SOUNDS_DIR, "coin.wav")  # Coin collection sound