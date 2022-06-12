import math
import pygame

class Enemy01(pygame.sprite.Sprite):
    def __init__(self, posX, posY, iconPath):
        super().__init__()
        self.x = posX
        self.y = posY
        self.phase = None
        self.image = pygame.image.load(iconPath)
        self.rect = self.image.get_rect(center=(posX, posY))
        self.rect.w -= 8
        self.rect.h -= 8

    def update(self):
        print('test')