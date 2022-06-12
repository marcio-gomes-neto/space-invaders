import math
import pygame

class Enemy02(pygame.sprite.Sprite):
    def __init__(self, posX, posY, iconPath):
        super().__init__()
        self.x = posX
        self.y = posY
        self.phase = None
        self.image = pygame.image.load(iconPath)
        self.rect = self.image.get_rect(center=(posX, posY))

    def update(self):
        if self.rect.y == 18 and self.rect.x == 18:
            self.phase = 1
        if self.rect.y == 720 and self.rect.x == 18:
            self.phase = 2
        if self.rect.y == 46 and self.rect.x == 355:
            self.phase = 3
        if self.rect.y == 720 and self.rect.x == 355:
            self.phase = 4
        if self.rect.y == 50 and self.rect.x == 690:
            self.phase = 5
        if self.rect.y == 720 and self.rect.x == 690:
            self.phase = 6
        if self.rect.x == 18 and self.phase == 6:
            self.rect.x = 18
            self.rect.y = 18
            self.phase = 1

        if self.rect.y == 18 and self.rect.x == 538:
            self.phase = 1
        if self.rect.y == 720 and self.rect.x == 538:
            self.phase = 7
        if self.rect.y == 18 and self.rect.x == 187:
            self.phase = 1
        if self.rect.y == 720 and self.rect.x == 187:
            self.phase = 2

        if self.phase == 1:
            self.rect.y += 2

        if self.phase == 2:
            self.rect.x += 1
            self.rect.y -= 2

        if self.phase == 3:
            self.rect.y += 2

        if self.phase == 4:
            self.rect.y -= 2
            self.rect.x += 1

        if self.phase == 5:
            self.rect.y += 2

        if self.phase == 6:
            self.rect.y -= 2
            self.rect.x -= 2

        if self.phase == 7:
            self.rect.y -= 2
            self.rect.x -= 1