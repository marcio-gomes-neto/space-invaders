import pygame
from entities.enemies.enemy01 import Enemy01
from entities.enemies.enemy02 import Enemy02
from entities.enemies.enemy03 import Enemy03

class Stage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.level = 2
        self.difficulty = 'normal'
        self.score = 0
        self.status = 'waiting'
        self.enemies = 0
        self.count = 0

    def prepareBackground(self, newGame, bgPath):
        newGame.prepareBackground(bgPath)
        self.enemies = 0

    def startStage(self, tick, enemyGroup):
        if self.level == 1:
            self.status = 'running'
            self.stageOne(tick, enemyGroup)
        if self.level == 2:
            self.status = 'running'
            self.stageTwo(tick, enemyGroup)
        if self.level == 3:
            self.status = 'running'
            self.stageTwo(tick, enemyGroup)

    def stageOne(self, tick, enemyGroup):
        if tick % 150 == 0 and self.enemies < 25:
            enemy = Enemy01(50, 50, 'assets/icon/enemy1.png')
            enemyGroup.add(enemy)
            self.enemies += 1

    def stageTwo(self, tick, enemyGroup):
        if tick % 150 == 0 and self.enemies < 61:
            if self.count % 2 == 0:
                enemy = Enemy02(50, 50, 'assets/icon/enemy2.png')
                enemyGroup.add(enemy)
                self.enemies += 1
            else:
                enemy = Enemy02(570, 50, 'assets/icon/enemy2.png')
                enemyGroup.add(enemy)
                self.enemies += 1
            self.count += 1

    def stageThree(self, tick, enemyGroup):
        if tick % 150 == 0 and self.enemies < 61:
            enemy = Enemy03(50, 50, 'assets/icon/enemy3.png')
            enemyGroup.add(enemy)
            self.enemies += 1
