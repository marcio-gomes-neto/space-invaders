import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, posX, posY, icon):
        super().__init__()
        self.x = posX
        self.y = posY
        self.image = icon
        self.rect = self.image.get_rect(center = (posX, posY))

    def update(self, bulletSpeed, shot):
        self.rect.y -= bulletSpeed
        if self.rect.y < -32:
            self.kill()