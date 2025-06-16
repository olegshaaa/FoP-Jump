import pygame
from settings import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = PLAYER_COLOR
        self.score = 0
        self.alive = True
        self.on_platform = None

    def jump_to_platform(self, platform):
        self.rect.midbottom = (platform.rect.centerx, platform.rect.top)
        self.on_platform = platform
