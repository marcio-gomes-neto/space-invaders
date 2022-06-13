from entities.bullets.enemyBullet import EnemyBullet
from entities.weapon import Weapon
import pygame

class Enemy03(pygame.sprite.Sprite):
    def __init__(self, posX, posY, iconPath, line):
        super().__init__()
        self.x = posX
        self.y = posY
        self.line = line
        self.phase = 0
        self.image = pygame.image.load(iconPath)
        self.rect = self.image.get_rect(center=(posX, posY))
        self.initialRectX = self.rect.x
        self.initialRectY = self.rect.y

    def update(self):
        if self.rect.y != 250 and self.line == 1:
            self.rect.y += 2

        if self.rect.y != 150 and self.line == 2:
            self.rect.y += 2

        if self.rect.y != 50 and self.line == 3:
            self.rect.y += 2

        if self.initialRectX == self.rect.x and self.phase == 0:
            self.phase = 1
        if self.initialRectX == self.rect.x + 50:
            self.phase = 2
        if self.initialRectX == self.rect.x - 50:
            self.phase = 1

        if self.phase == 1 and (self.line == 1 or self.line == 3):
            self.rect.x -= 1
        if self.phase == 2 and (self.line == 1 or self.line == 3):
            self.rect.x += 1

    def shot(self):
        self.weapon = Weapon(self.rect.x + 31.5, self.rect.y + 20, 'assets/sound/enemy-shot.wav', 'assets/icon/enemy-shot.png', 1, 100)
        return EnemyBullet(self.weapon.x, self.weapon.y, self.weapon.icon)