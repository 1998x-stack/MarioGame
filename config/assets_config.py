"""Absolute repo-relative paths to existing game assets."""
from pathlib import Path
_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = _ROOT / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"
MARIO_IMAGE = str(IMAGES_DIR / "mario.png")
BACKGROUND_IMAGE = str(IMAGES_DIR / "background.png")
ENEMY_IMAGE = str(IMAGES_DIR / "enemy.png")
COIN_IMAGE = str(IMAGES_DIR / "coin.png")
TILE_IMAGE = str(IMAGES_DIR / "tile.png")
JUMP_SOUND = str(SOUNDS_DIR / "jump.wav")
BG_MUSIC = str(SOUNDS_DIR / "background.mp3")
COIN_SOUND = str(SOUNDS_DIR / "coin.wav")
