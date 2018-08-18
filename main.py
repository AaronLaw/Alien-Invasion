"""
A simple action game to learn OOP.

@Author: Aaronlaw
@Date: 2018-08-12
"""
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings ,screen)
    #alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, aliens)
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

def main():
    run_game()

if __name__ == "__main__":
    main()