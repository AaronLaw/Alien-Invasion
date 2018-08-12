"""
A simple RPG game to learn OOP.

@Author: Aaronlaw
@Date: 2018-08-12
"""
import sys
import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

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