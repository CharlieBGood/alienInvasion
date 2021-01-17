class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, main_settings):
        """Initialize statistics."""
        self.main_settings = main_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.main_settings.ship_limit