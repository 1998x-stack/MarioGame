# main.py
import pygame
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from src.game import Game

def main():
    """Main function: initialize game window and run the game loop"""
    # Initialize pygame
    pygame.init()

    # Create game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Super Mario Game")

    # Create game instance
    game = Game(screen)

    # Game main loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Frame rate limit
        clock.tick(FPS)

        # Handle events and update game state
        running = game.update()

        # Render game screen
        game.render()

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()