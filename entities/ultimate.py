import pygame
from entities.ally import Ally

class Ultimate(pygame.sprite.Sprite):
    def __init__(self):
        self.fighters = 9

    def spawnFighters(self, allyGroup, iconPath):
        for x in range(0, 9):
            if x == 0 or x == 8:
                y = 885
            if x == 1 or x == 7:
                y = 870
            if x == 2 or x == 6:
                y = 855
            if x == 3 or x == 5:
                y = 840
            if x == 4:
                y = 825

            ally = Ally(55 + 84 * x, y, iconPath)
            allyGroup.add(ally)