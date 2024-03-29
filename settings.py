class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800
        self.BG_COLOR = (230, 230, 230)
        self.FPS = 60
        
        # Ship settings
        self.SHIP_LIMIT = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 20

        # Rate at which the game will increase in speed
        self.speedup_scale = 1.4
        self.score_scale = 1.4

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize the dynamic settings of the game."""
        self.ship_speed = 10
        self.bullet_speed = 18
        self.alien_speed = 5.0
        
        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)