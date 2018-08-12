"""
A simple RPG game to learn OOP.

@Author: Aaronlaw
@Date: 2018-08-12
"""
import sys
import pygame
from settings import Settings

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    screen.fill(ai_settings.bg_color)
    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

    pygame.display.flip()


def main():
    run_game()

if __name__ == "__main__":
    main()