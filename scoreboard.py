import pygame.font

class Scoreboard:
    """A class to report scoring information"""
    def __init__(self, ai_game):
        """Initialise scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font colours for scoring information
        self.text_colour = (66, 149, 245)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the scoreboard into a rendered image"""
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_colour, None)
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        self.new_highscore = False
    
    def prep_high_score(self):
        """Turn high score into rendered image"""
        if self.new_highscore == False:
            high_score_str = "{:,}".format(self.stats.high_score)
            self.high_score_image = self.font.render(high_score_str, True, self.text_colour,
            None)
        elif self.new_highscore:
            self.high_score_image = self.font.render("NEW HIGHSCORE!!!", True, 
            (140, 255, 122), None)

        # Center high score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def _check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.new_highscore = True
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.stats.write_high_score()

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)