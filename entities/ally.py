import math
import pygame
from entities.weapon import Weapon
from entities.bullets.bullet01 import Bullet01

class Ally(pygame.sprite.Sprite):
    def __init__(self, posX, posY, iconPath):
        super().__init__()
        self.x = posX
        self.y = posY
        self.fired = False
        self.image = pygame.image.load(iconPath)
        self.rect = self.image.get_rect(center=(posX, posY))
        self.rect.w -= 4
        self.rect.h -= 4

    def update(self, allyBulletGroup):
        self.rect.y -= 2
        if self.rect.y <= 700 and self.fired == False:
            self.fired = True
            self.weapon = Weapon(self.x + 31.5, 720, 'assets/sound/bullet.wav', 'assets/icon/bullet.png', 2, 2)
            self.shot = self.shot()

            allyBulletGroup.add(self.shot)

        if self.rect.y < -20:
            self.kill()

    def shot(self):
        return Bullet01(self.x , self.weapon.y, self.weapon.icon)