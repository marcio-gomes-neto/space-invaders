from threading import Timer
import pygame, sys
from entities.player import Player
from entities.gamewindow import GameWindow
from services.button import Button
from services.alienselector import MenuAlien
from entities.stage import Stage
# initializing pygame

global newGame
global playerOne

newGame = GameWindow(800, 800, 'assets/icon/spaceship1.png', 'Space Invaders')
playerOne = Player(370, 723, "assets/icon/spaceship1.png")

newGame.playBackgroundMusic('assets/sound/menu.mp3', 'main-menu')
newGame.soundMixer.init()

def get_font(size):
    return pygame.font.Font("assets/font/font.ttf", size)

def mainMenu():
    newGame.prepareBackground('assets/background/menu.png')
    running = True
    menuAlien = MenuAlien(280, 480)

    alienSelector = pygame.sprite.Group(menuAlien)
    menuAlien.menuButton = "play"

    while running:

        alienSelector.update()
        alienSelector.draw(newGame.screen)

        newGame.clock.tick(5)

        playButton = Button(pos=(330, 460), textInput="PLAY", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")
        optionsButton = Button(pos=(330, 570), textInput="OPTIONS", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")
        quitButton = Button(pos=(330, 680), textInput="QUIT", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")

        for button in [playButton, optionsButton, quitButton]:
            button.update(newGame.screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pygame.draw.rect(newGame.screen, (0, 0, 0), menuAlien.rect)
                    menuAlien.moveDown()
                if event.key == pygame.K_UP:
                    pygame.draw.rect(newGame.screen, (0, 0, 0), menuAlien.rect)
                    menuAlien.moveUp()
                if event.key == pygame.K_SPACE:
                    if menuAlien.menuButton == "play":
                        newGame.stage = 1
                        play()
                    if menuAlien.menuButton == "options":
                        options()
                    if menuAlien.menuButton == "quit":
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

# game loop
def play():
    playerOne.selectShip()
    running = True

    stage = Stage()
    bulletGroup = pygame.sprite.Group()
    enemyGroup = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()
    x = 1
    spawnRate = 0


    newGame.status = 'running'
    playerOne.setWhichWeapon()


    while running:
        if stage.status == 'waiting':
            stage.prepareBackground(newGame, 'assets/background/background' + str(stage.level) + '.png')
            stage.status = 'ready'
        newGame.clock.tick(350)
        newGame.moveBackground()
        playerGroup.add(playerOne)
        if newGame.status == 'waiting':
            if newGame.music != 'waiting-menu':
                newGame.playBackgroundMusic('assets/sound/waiting-menu.wav', 'waiting-menu')
            if newGame.stage == 1:
                playerOne.setWhichWeapon()

            newGame.printText('LEVEL ' + str(stage.level), '#006600', 300, 300, 40)
            newGame.printText('PRESS ENTER', '#006600', 240, 400, 40)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        t = Timer(3, newGame.playFunction)
                        t.start()
                        newGame.playTime = 0
                        newGame.status = 'starting'

        elif newGame.status == 'starting':
            newGame.playTime += 1
            if newGame.playTime == 350:
                newGame.playSound('assets/sound/letsrock.wav')

            if newGame.playTime <= 400:
                newGame.printText('3', '#006600', 370, 325, 75)
            elif newGame.playTime <= 800:
                newGame.printText('2', '#006600', 370, 325, 75)
            elif newGame.playTime <= 1200:
                newGame.printText('1', '#006600', 370, 325, 75)

            playerOne.movement = 0
        elif newGame.status == 'running':
            if newGame.music != 'level':
                newGame.playBackgroundMusic('assets/sound/level' + str(stage.level) + '.wav', 'level')
            if newGame.playTime == 1234:
                pygame.event.clear()
            newGame.playTime += 1
            spawnRate += 1
            if newGame.playTime <= 2000:
                newGame.printText('LETS ROCK!', '#006600', 150, 325, 75)

            if playerOne.score < 25:
                stage.startStage(spawnRate, enemyGroup)
                enemyGroup.draw(newGame.screen)
                enemyGroup.update()
            if 25 <= playerOne.score < 86:
                stage.startStage(spawnRate, enemyGroup)
                enemyGroup.draw(newGame.screen)
                enemyGroup.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerOne.moveLeft()
                    if event.key == pygame.K_RIGHT:

                        playerOne.moveRight()
                    if event.key == pygame.K_SPACE:
                        if len(bulletGroup) <= 1:
                            playerOne.shooting = True
                            shot = playerOne.shot(newGame)
                            bulletGroup.add(shot)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        playerOne.stopLeft()
                    if event.key == pygame.K_RIGHT:
                        playerOne.stopRight()

            playerOne.x += playerOne.movement
            playerGroup.update()

            if playerOne.shooting:
                bulletGroup.draw(newGame.screen)
                bulletGroup.update(playerOne.weapon.bulletSpeed, shot)

                if len(bulletGroup) == 0:
                    playerOne.shooting = False

            # movement of the invader
            if pygame.sprite.groupcollide(playerGroup, enemyGroup, False, False):
                newGame.playSound('assets/sound/death.wav')
                # pygame.time.wait(3000000)
            if pygame.sprite.groupcollide(enemyGroup, bulletGroup, True, True):
                if stage.level == 1 or stage.level == 2:
                    playerOne.score += 1

            if playerOne.x <= 13:
                playerOne.x = 13
            elif playerOne.x >= 726:
                playerOne.x = 726

        if playerOne.score == newGame.nextLevel:
            newGame.updateNextLevelScore(stage.level + 1)
            stage.level += 1
            newGame.status = 'waiting'
            stage.status = 'waiting'
            playerOne.x = 370
            playerOne.y = 723

        newGame.simpleRenderer(playerOne.x, playerOne.y, playerOne.icon)
        newGame.updateScore(playerOne.score)
        newGame.updateLives(playerOne.lives, playerOne.icon)
        pygame.display.update()


def options():
    newGame.prepareBackground('assets/background/options.png')
    running = True
    menuAlien = MenuAlien(280, 180)
    alienSelector = pygame.sprite.Group(menuAlien)

    musicButton = Button(pos=(330, 160), textInput="MUSIC", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")
    soundFxButton = Button(pos=(330, 280), textInput="SFX", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")
    changeSpaceShip = Button(pos=(330, 400), textInput="SHIP", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")
    backButton = Button(pos=(330, 700), textInput="BACK", font=get_font(35), baseColor="#d7fcd4", hoverColor="White")

    menuAlien.menuButton = "music"

    while running:
        alienSelector.update()
        alienSelector.draw(newGame.screen)

        newGame.clock.tick(5)

        for button in [musicButton, soundFxButton, changeSpaceShip, backButton]:
            button.update(newGame.screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pygame.draw.rect(newGame.screen, (0, 0, 0), menuAlien.rect)
                    menuAlien.moveDownOption()

                if event.key == pygame.K_UP:
                    pygame.draw.rect(newGame.screen, (0, 0, 0), menuAlien.rect)
                    menuAlien.moveUpOption()

                if event.key == pygame.K_SPACE:
                    if menuAlien.menuButton == "music":
                        newGame.pausePlayMusic(musicButton)

                    if menuAlien.menuButton == "sfx":
                        newGame.pausePlaySFX(soundFxButton)

                    if menuAlien.menuButton == "ship":
                        changeShip()

                    if menuAlien.menuButton == "back":
                        mainMenu()

        pygame.display.update()


def changeShip():
    running = True
    ships = ['assets/icon/spaceship1.png', 'assets/icon/spaceship2.png', 'assets/icon/spaceship3.png', 'assets/icon/spaceship4.png']

    while running:
        newGame.clock.tick(5)
        newGame.prepareBackground('assets/background/options.png')

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if playerOne.ship == 1:
                        playerOne.ship = 0
                    if playerOne.ship == 3:
                        playerOne.ship = 2
                if event.key == pygame.K_RIGHT:
                    if playerOne.ship == 0:
                        playerOne.ship = 1
                    if playerOne.ship == 2:
                        playerOne.ship = 3
                if event.key == pygame.K_DOWN:
                    if playerOne.ship == 0:
                        playerOne.ship = 2
                    if playerOne.ship == 1:
                        playerOne.ship = 3
                if event.key == pygame.K_UP:
                    if playerOne.ship == 2:
                        playerOne.ship = 0
                    if playerOne.ship == 3:
                        playerOne.ship = 1
                if event.key == pygame.K_SPACE:
                    if not playerOne.ship == 3:
                        options()


        if (playerOne.ship == 0):
            pygame.draw.rect(newGame.screen, (0, 100, 255), (245, 245, 74, 74), 3)
        elif(playerOne.ship == 1):
            pygame.draw.rect(newGame.screen, (0, 100, 255), (445, 245, 74, 74), 3)
        elif(playerOne.ship == 2):
            pygame.draw.rect(newGame.screen, (0, 100, 255), (245, 445, 74, 74), 3)
        else:
            pygame.draw.rect(newGame.screen, (0, 100, 255), (445, 445, 74, 74), 3)
        pygame.display.update()

        playerOne.iconPath = ships[playerOne.ship]

        newGame.simpleRenderer(250, 250, pygame.image.load(ships[0]))
        newGame.simpleRenderer(450, 250, pygame.image.load(ships[1]))
        newGame.simpleRenderer(250, 450, pygame.image.load(ships[2]))
        newGame.simpleRenderer(450, 450, pygame.image.load(ships[3]))

        pygame.display.update()

mainMenu()