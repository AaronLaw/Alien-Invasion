import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
            # When the player holds down the right arrow key, we want the ship to continue moving right until the player releases the key. We’ll have our game detect a pygame.KEYUP event so we’ll know when the right arrow key is released; then we’ll use the KEYDOWN and KEYUP events together with a flag called moving_right to implement continuous motion.
        self.moving_right = False

    def update(self):
        """Update the ships's position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)