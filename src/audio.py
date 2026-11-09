"""Missing audio hardware and optional sound effects must not stop gameplay."""
import pygame


def load_effect(path):
    if pygame.mixer.get_init() is None:
        return None
    try:
        return pygame.mixer.Sound(str(path))
    except (pygame.error, OSError):
        return None


def play_effect(path):
    sound = load_effect(path)
    if sound is not None:
        sound.play()


def start_music(path):
    if pygame.mixer.get_init() is None:
        return False
    try:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play(-1)
        return True
    except (pygame.error, OSError):
        return False
