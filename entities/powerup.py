import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, posX, posY, number, iconPath):
        super().__init__()
        self.x = posX
        self.y = posY
        self.image = pygame.image.load(iconPath)
        self.number = number
        self.rect = self.image.get_rect(center=(posX, posY))

    def update(self):
        self.rect.y += 1
        if self.rect.y > 840:
            self.kill()

