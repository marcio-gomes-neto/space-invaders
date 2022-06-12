import pygame
from pygame import mixer

class Weapon:
    def __init__(self, posX, posY, soundPath, iconPath, bulletSpeed):
        self.x = posX
        self.y = posY
        self.sound = soundPath
        self.icon = pygame.image.load(iconPath)
        self.bulletSpeed = bulletSpeed

