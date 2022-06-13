import pygame

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, posX, posY, icon):
        super().__init__()
        self.x = posX
        self.y = posY
        self.image = icon
        self.rect = self.image.get_rect(center = (posX, posY))

    def update(self, bulletSpeed):
        self.rect.y += bulletSpeed
        if self.rect.y > 840:
            self.kill()