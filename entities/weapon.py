import pygame
from pygame import mixer

class Weapon:
    def __init__(self, posX, posY, soundPath, iconPath, bulletSpeed, numberActive):
        self.x = posX
        self.y = posY
        self.sound = soundPath
        self.icon = pygame.image.load(iconPath)
        self.numberActive = numberActive
        self.bulletSpeed = bulletSpeed

