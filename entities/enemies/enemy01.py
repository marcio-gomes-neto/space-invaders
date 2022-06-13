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
        self.rect.w -= 4
        self.rect.h -= 4

    def update(self):
        if self.rect.y == 18 and self.rect.x == 18:
            self.phase = 1
        if self.rect.y == 720 and self.rect.x == 18:
            self.phase = 2
        if self.rect.y == 46 and self.rect.x == 355:
            self.phase = 3
        if self.rect.y == 720 and self.rect.x == 692:
            self.phase = 4
        if self.rect.y == 50 and self.rect.x == 692:
            self.phase = 5
        if self.rect.y == 720 and self.rect.x == 357:
            self.phase = 6
        if self.rect.y == 38 and self. rect.x == 16:
            self.rect.x = 18
            self.rect.y = 18
            self.phase = 1

        if self.phase == 1:
            self.rect.y += 2

        if self.phase == 2:
            self.rect.x +=1
            self.rect.y -=2

        if self.phase == 3:
            self.rect.x += 1
            self.rect.y += 2

        if self.phase == 4:
            self.rect.y -= 2

        if self.phase == 5:
            self.rect.y += 2
            self.rect.x -= 1

        if self.phase == 6:
            self.rect.y -= 2
            self.rect.x -= 1