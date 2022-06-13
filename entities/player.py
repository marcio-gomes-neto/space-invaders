import pygame
from entities.weapon import Weapon
from entities.bullets.bullet01 import Bullet01

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
        self.playerUltimate = 0

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
            self.weapon = Weapon(self.x + 31.5, 720, 'assets/sound/bullet.wav', 'assets/icon/bullet.png', 2,  2)

        if self.playerWeapon == 2:
            self.weapon = Weapon(self.x + 31.5, 720, 'assets/sound/bullet1.wav', 'assets/icon/bullet1.png', 2, 1)

        if self.playerWeapon == 3:
            self.weapon = Weapon(self.x + 31.5, 720, 'assets/sound/bullet2.wav', 'assets/icon/bullet2.png', 2, 5)

    def update(self):
        self.rect.x = self.x+24

    def drawUltimate(self, newGame):
        if self.playerUltimate == 0:
            newGame.printText('Ultimate:', '#CF000F', 5, 775, 20)
        if self.playerUltimate == 1:
            newGame.printText('Ultimate:', '#CF000F', 5, 775, 20)
            newGame.printText('I', '#CF000F', 135, 775, 20)
        if self.playerUltimate == 2:
            newGame.printText('Ultimate:', '#CF000F', 5, 775, 20)
            newGame.printText('I', '#CF000F', 135, 775, 20)
            newGame.printText('I', '#CF000F', 145, 775, 20)
        if self.playerUltimate == 3:
            newGame.printText('Ultimate:', '#006600', 5, 775, 20)
            newGame.printText('I', '#006600', 135, 775, 20)
            newGame.printText('I', '#006600', 145, 775, 20)
            newGame.printText('I', '#006600', 155, 775, 20)
            newGame.printText('  -  PRESS E', '#006600', 165, 775, 20)

    def shot(self, newGame):
        newGame.playSound(self.weapon.sound)
        return Bullet01(self.x + 31.5, self.weapon.y, self.weapon.icon)