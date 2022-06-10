import pygame
from pygame import mixer

class Bullet:
    def __init__(self, posX, posY, iconPath, bulletSpeed, soundPath):
        self.x = posX
        self.y = posY
        self.icon = pygame.image.load(iconPath)
        self.bulletSpeed = bulletSpeed
        self.sound = mixer.Sound(soundPath)