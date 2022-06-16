import pygame

class Sounds:
    def __init__(self):
        self.bullet_sound = pygame.mixer.Sound("sounds/bullet_sound.wav")
        self.alien_explosion = pygame.mixer.Sound("sounds/alien_explosion.wav")