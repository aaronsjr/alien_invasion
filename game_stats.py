import os
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start alien invasion in an inactive state
        self.game_active = False

        if "highscore.txt" in os.listdir():
            # If the file exists read the high score from the file
            with open('highscore.txt', "r") as highscore:
                self.high_score = int(highscore.read())

        else:
            # If the file does not exist create the file and initialise the value
            # of highscore as 0 and write that to the file.
            with open('highscore.txt', 'w') as highscore:
                self.high_score = 0
                highscore.write(str(self.high_score))
                

    def reset_stats(self):
        """Initialise stats that can change during the game."""
        self.ships_left = self.settings.SHIP_LIMIT
        self.score = 0
    
    def write_high_score(self):
        with open("highscore.txt", 'w') as highscore:
            highscore.write(str(self.score))
