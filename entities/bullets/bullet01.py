import pygame

class Bullet01(pygame.sprite.Sprite):
    def __init__(self, posX, posY, icon):
        super().__init__()
        self.x = posX
        self.y = posY
        self.image = icon
        self.rect = self.image.get_rect(center=(posX, posY))
        self.collision = 0

    def update(self, bulletSpeed, collision):
        self.collision += collision
        self.rect.y -= bulletSpeed
        if self.rect.y < -32 or self.collision >= 2:
            self.collision = 0
            self.kill()