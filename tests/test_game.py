"""Real Pygame geometry, explicit match restart and headless window boot."""
import os
os.environ.setdefault("SDL_VIDEODRIVER","dummy")
os.environ.setdefault("SDL_AUDIODRIVER","dummy")

import unittest
from unittest.mock import patch
import pygame
from src.game import Game
from src.audio import load_effect, start_music
from main import main
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT


class GameTests(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.event.clear()

    def tearDown(self):
        if pygame.get_init():
            pygame.event.clear()
        pygame.quit()

    def test_game_starts_with_real_assets_and_level(self):
        g = Game(self.screen)
        self.assertEqual((g.score,g.lives,g.level_number),(0,3,1))
        self.assertGreater(len(g.level.tiles_group),0)
        g.render()

    def test_restart_rebuilds_first_level_and_score(self):
        g = Game(self.screen)
        g.score=42
        g.lives=0
        g.game_over=True
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_r))
        self.assertTrue(g.update())
        self.assertEqual((g.score,g.lives,g.level_number),(0,3,1))
        self.assertFalse(g.game_over)

    def test_escape_quits_and_does_not_kill_interpreter(self):
        g = Game(self.screen)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_ESCAPE))
        self.assertFalse(g.update())

    def test_missing_audio_does_not_crash(self):
        with patch("pygame.mixer.get_init",return_value=None):
            self.assertIsNone(load_effect("nonexistent.wav"))
            self.assertFalse(start_music("nonexistent.mp3"))
            g=Game(self.screen)
            self.assertIsNone(g.player.jump_sound)
            g.render()

    def test_virtual_display_main_smoke(self):
        main(max_frames=1)

if __name__ == "__main__":
    unittest.main()
