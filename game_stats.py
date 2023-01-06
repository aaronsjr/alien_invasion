class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start alien invasion in an inactive state
        self.game_active = False
    
    def reset_stats(self):
        """Initialise stats that can change during the game."""
        self.ships_left = self.settings.SHIP_LIMIT
        self.score = 0