from entities.bullets.enemyBullet import EnemyBullet
from entities.weapon import Weapon
import pygame

class Enemy04(pygame.sprite.Sprite):
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
        if self.rect.y == 18 and self.rect.x == 18:
            self.phase = 1
        if self.rect.y == 350 and self.rect.x == 18:
            self.phase = 2
        if self.rect.y == 18 and self.rect.x == 350 and not self.phase == 8:
            self.phase = 3
        if self.rect.y == 350 and self.rect.x == 682:
            self.phase = 4
        if self.rect.y == 18 and self.rect.x == 682:
            self.phase = 5
        if self.rect.y == 350 and self.rect.x == 350 and not self.phase == 7:
            self.phase = 6

        if self.rect.y == 18 and self.rect.x == 168:
            self.phase = 1
        if self.rect.y == 350 and self.rect.x == 168:
            self.phase = 7
        if self.rect.y == 350 and self.rect.x == 540:
            self.phase = 4
        if self.rect.y == 18 and self.rect.x == 540:
            self.phase = 8

        if self.phase == 1:
            self.rect.y += 2

        if self.phase == 2:
            self.rect.x += 2
            self.rect.y -= 2

        if self.phase == 3:
            self.rect.x += 2
            self.rect.y += 2

        if self.phase == 4:
            self.rect.y -= 2

        if self.phase == 5:
            self.rect.y += 2
            self.rect.x -= 2

        if self.phase == 6:
            self.rect.y -= 2
            self.rect.x -= 2

        if self.phase == 7:
            self.rect.x += 2

        if self.phase == 8:
            self.rect.x -= 2

    def shot(self):
        self.weapon = Weapon(self.rect.x + 31.5, self.rect.y + 20, 'assets/sound/enemy-shot.wav', 'assets/icon/enemy-shot.png', 1, 100)
        return EnemyBullet(self.weapon.x, self.weapon.y, self.weapon.icon)
