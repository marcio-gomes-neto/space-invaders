import pygame
from pygame import mixer
from entities.weapon import Weapon
from entities.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY, iconPath):
        super().__init__()
        self.x = posX
        self.y = posY
        self.icon = None
        self.iconPath = iconPath
        self.movement = 0
        self.shooting = False
        self.score = 0
        self.ship = 0
        self.lives = 3
        self.playerWeapon = 1

    def selectShip(self):
        self.icon = pygame.image.load(self.iconPath)
        if (self.ship == 0):
            hitBox = self.icon.get_rect(center=(self.x, self.y))
            hitBox.w -= 48
            hitBox.h -= 20
            hitBox.y += 40
            self.rect = hitBox

    def moveLeft(self):
        self.movement += -0.5

    def moveRight(self):
        self.movement += 0.5

    def stopRight(self):
        self.movement += -0.5

    def stopLeft(self):
        self.movement += 0.5

    def setWhichWeapon(self):
        if self.playerWeapon == 1:
            self.weapon = Weapon(self.x + 31.5, 720, 'assets/sound/bullet.wav', 'assets/icon/bullet.png', 2)

    def update(self):
        self.rect.x = self.x+24

    def shot(self, newGame):
        newGame.playSound(self.weapon.sound)
        return Bullet(self.x + 31.5, self.weapon.y, self.weapon.icon)