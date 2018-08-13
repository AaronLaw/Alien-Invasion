class GameStats():
    """Track statistics for Alien Invasion."""
    
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien invasion in an active state.
        # If ship got hit, its life -1 and check should we turn the game inactive.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit