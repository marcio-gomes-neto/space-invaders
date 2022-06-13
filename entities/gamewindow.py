import pygame
from pygame import mixer
from threading import Timer

class GameWindow:
    def __init__(self, x, y, iconPath, description):
        pygame.init()
        self.started = False
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()
        img = pygame.image.load(iconPath)
        pygame.display.set_icon(img)
        pygame.display.set_caption(description)

        self.spawnedPower = 0
        self.firstWin = False
        self.winTextTimer = 0
        self.playTime = 0
        self.stage = 1
        self.status = 'waiting'
        self.music = 'none'
        self.musicPaused = False
        self.sfxPaused = False
        self.nextLevel = 25
        self.soundMixer = mixer
        self.screen = pygame.display.set_mode((self.x, self.y))
        self.clock = pygame.time.Clock()
        self.font = None
        self.gameOver = False

    def updateLives (self, lives, icon):
        for x in range(0, lives):
            self.screen.blit(icon, (650+ 40*x, 5))

        if lives == 0:
            self.gameOver = True

    def simpleRenderer(self, x, y, icon):
        self.screen.blit(icon, (x, y))

    def prepareBackground(self, bgPath):
        self.bg = pygame.image.load(bgPath).convert()
        self.bgHeigth = self.bg.get_height()
        self.scroll = 0
        self.simpleRenderer(0, 0, self.bg)

    def moveBackground(self):
        for i in range(0, 2):
            self.screen.blit(self.bg, (0, -i * self.bgHeigth + self.scroll))

        self.scroll += 0.3
        if abs(self.scroll) > self.bgHeigth:
            self.scroll = 0

    def playBackgroundMusic(self, musicPath, music):
        if not self.musicPaused:
            self.music = music
            self.soundMixer.music.stop()
            self.soundMixer.music.load(musicPath)

            self.soundMixer.music.play(-1)

    def playSound(self, path):
        if not self.sfxPaused:
            soundFx = self.soundMixer.Sound(path)
            self.soundMixer.Sound.play(soundFx)

    def pausePlayMusic(self, button):
        if not self.musicPaused:
            self.soundMixer.music.pause()
            self.musicPaused = True
            button.changeColor('#b02134')
            button.update(self.screen)
        else:
            self.soundMixer.music.unpause()
            self.musicPaused = False
            button.changeColor('#d7fcd4')
            button.update(self.screen)

    def pausePlaySFX(self, button):
        if not self.sfxPaused:
            self.sfxPaused = True
            button.changeColor('#b02134')
            button.update(self.screen)
        else:
            self.sfxPaused = False
            button.changeColor('#d7fcd4')
            button.update(self.screen)

    def printText(self, text, color, x, y, size):
        self.font = pygame.font.Font("assets/font/font.ttf", size)
        printText = self.font.render(text, True, color)
        self.screen.blit(printText, (x, y))

    def updateScore(self, score):
        self.printText("Points: " + str(score), '#FFFFFF', 5, 5, 20)

    def updateObjective(self):
        self.printText("OBJ: " + str(self.nextLevel), '#FFFFFF', 200, 5, 20)

    def playFunction(self):
        self.status = 'running'

    def updateNextLevelScore(self, level):
        if level == 2:
            self.nextLevel = 80
        if level == 3:
            self.nextLevel = 152
        if level == 4:
            self.nextLevel = 440
