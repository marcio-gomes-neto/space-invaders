import random

import pygame
from entities.enemies.enemy01 import Enemy01
from entities.enemies.enemy02 import Enemy02
from entities.enemies.enemy03 import Enemy03
from entities.enemies.enemy04 import Enemy04

class Stage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.difficulty = 'normal'
        self.score = 0
        self.line = 0
        self.status = 'waiting'
        self.stageTwoPower = False
        self.stageThreePower = False
        self.enemies = 0
        self.count = 0

    def prepareBackground(self, newGame, bgPath):
        newGame.prepareBackground(bgPath)
        self.line = 0
        self.enemies = 0

    def startStage(self, tick, enemyGroup, bulletGroup):
        if self.level == 1:
            self.status = 'running'
            self.stageOne(tick, enemyGroup, bulletGroup)
        if self.level == 2:
            self.status = 'running'
            self.stageTwo(tick, enemyGroup, bulletGroup)
        if self.level == 3:
            self.status = 'running'
            self.stageThree(tick, enemyGroup, bulletGroup)
        if self.level == 4:
            self.status = 'running'
            self.stageFour(tick, enemyGroup, bulletGroup)

    def stageOne(self, tick, enemyGroup, bulletGroup):
        if tick % 150 == 0 and self.enemies < 25:
            enemy = Enemy01(50, 50, 'assets/icon/enemy1.png')
            enemyGroup.add(enemy)
            self.enemies += 1

    def stageTwo(self, tick, enemyGroup, bulletGroup):
        if tick % 150 == 0 and self.enemies < 55:
            if self.count % 2 == 0:
                enemy = Enemy02(50, 50, 'assets/icon/enemy2.png')
                enemyGroup.add(enemy)
                self.enemies += 1
            else:
                enemy = Enemy02(570, 50, 'assets/icon/enemy2.png')
                enemyGroup.add(enemy)
                self.enemies += 1
            self.count += 1

    def stageThree(self, tick, enemyGroup, bulletGroup):
        if tick % 150 == 0 and self.enemies < 18:
            self.line += 1
            for x in range(0, 6):
                enemy = Enemy03(95 + 114*x, 0, 'assets/icon/enemy3.png', self.line)

                enemyGroup.add(enemy)
                self.enemies += 1

        for enemy in enemyGroup:
            if self.enemies == 18 and random.random() < 0.002 and len(bulletGroup) <= 15:
                shot = enemy.shot()
                bulletGroup.add(shot)

    def stageFour(self, tick, enemyGroup, bulletGroup):
        if tick % 150 == 0 and self.enemies < 18:
            enemy1 = Enemy04(50, 50, 'assets/icon/enemy4.png')
            enemyGroup.add(enemy1)

            enemy2 = Enemy04(200, 50, 'assets/icon/enemy4.png')
            enemyGroup.add(enemy2)
            self.enemies += 1

        for enemy in enemyGroup:
            if random.random() < 0.003 and len(bulletGroup) <= 20:
                shot = enemy.shot()
                bulletGroup.add(shot)
