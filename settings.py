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
        self.ship_speed = 7
        self.SHIP_LIMIT = 3

        # Bullet settings
        self.bullet_speed = 9
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 20
        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1