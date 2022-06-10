import pygame


class Player:
    def __init__(self, posX, posY, iconPath, playerMovement):
        self.x = posX
        self.y = posY
        self.icon = pygame.image.load(iconPath)
        self.movement = playerMovement
        self.score = 0
    def moveLeft(self):
        self.movement += -0.3

    def moveRight(self):
        self.movement += 0.3

    def stopRight(self):
        self.movement += -0.3

    def stopLeft(self):
        self.movement += 0.3

