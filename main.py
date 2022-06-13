import random
from threading import Timer
import pygame, sys
from entities.player import Player
from entities.gamewindow import GameWindow
from services.button import Button
from services.alienselector import MenuAlien
from entities.stage import Stage
from entities.powerup import PowerUp
from services.explosion import Explosion
from entities.ultimate import Ultimate
# initializing pygame


global newGame
global playerOne

newGame = GameWindow(800, 800, 'assets/icon/spaceship1.png', 'Space Invaders')
playerOne = Player(370, 723, "assets/icon/spaceship1.png")


def get_font(size):
    return pygame.font.Font("assets/font/font.ttf", size)

def mainMenu():
    if newGame.music != 'main-menu':
        newGame.playBackgroundMusic('assets/sound/menu.mp3', 'main-menu')

    newGame.prepareBackground('assets/background/menu.png')
    newGame.soundMixer.init()
    running = True
    menuAlien = MenuAlien(280, 480)

    alienSelector = pygame.sprite.Group(menuAlien)
    menuAlien.menuButton = "play"

    while running:

        alienSelector.draw(newGame.screen)
        alienSelector.update()

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
                    menuAlien.moveDown(newGame)
                if event.key == pygame.K_UP:
                    pygame.draw.rect(newGame.screen, (0, 0, 0), menuAlien.rect)
                    menuAlien.moveUp(newGame)
                if event.key == pygame.K_SPACE:
                    newGame.playSound('assets/sound/menu-change.wav')
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
    enemyBulletGroup = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()
    powerUpGroup = pygame.sprite.Group()
    allyGroup = pygame.sprite.Group()
    allyBulletGroup = pygame.sprite.Group()
    explosionGroup = pygame.sprite.Group()
    x = 1
    spawnRate = 0


    # newGame.status = 'running'
    # playerOne.setWhichWeapon()


    while running:
        if stage.status == 'waiting':
            stage.prepareBackground(newGame, 'assets/background/background' + str(stage.level) + '.png')
            stage.status = 'ready'
        newGame.clock.tick(350)
        playerGroup.add(playerOne)
        if newGame.status == 'waiting':
            newGame.moveBackground()
            if newGame.music != 'waiting-menu':
                newGame.playBackgroundMusic('assets/sound/waiting-menu.wav', 'waiting-menu')
            if stage.level == 1:
                playerOne.playerWeapon = 1
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

            newGame.simpleRenderer(playerOne.x, playerOne.y, playerOne.icon)
        elif newGame.status == 'starting':
            newGame.moveBackground()
            newGame.playTime += 1
            if newGame.playTime == 350:
                bulletGroup.empty()
                enemyGroup.empty()
                enemyBulletGroup.empty()
                newGame.playSound('assets/sound/letsrock.wav')

            if newGame.playTime <= 400:
                newGame.printText('3', '#006600', 370, 325, 75)
            elif newGame.playTime <= 800:
                newGame.printText('2', '#006600', 370, 325, 75)
            elif newGame.playTime <= 1200:
                newGame.printText('1', '#006600', 370, 325, 75)

            newGame.simpleRenderer(playerOne.x, playerOne.y, playerOne.icon)
            playerOne.movement = 0
        elif newGame.status == 'running':
            newGame.moveBackground()
            playerOne.setWhichWeapon()
            if newGame.music != 'level':
                newGame.playBackgroundMusic('assets/sound/level' + str(stage.level) + '.wav', 'level')
            if newGame.playTime == 1234:
                pygame.event.clear()
            newGame.playTime += 1
            spawnRate += 1
            if newGame.playTime <= 2000:
                newGame.printText('LETS ROCK!', '#006600', 150, 325, 75)

            stage.startStage(spawnRate, enemyGroup, enemyBulletGroup)
            enemyGroup.draw(newGame.screen)
            enemyGroup.update()

            enemyBulletGroup.draw(newGame.screen)
            enemyBulletGroup.update(1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerOne.moveLeft()
                    if event.key == pygame.K_RIGHT:

                        playerOne.moveRight()
                    if event.key == pygame.K_SPACE:
                        if len(bulletGroup) < playerOne.weapon.numberActive:
                            playerOne.shooting = True
                            shot = playerOne.shot(newGame)
                            bulletGroup.add(shot)

                    if event.key == pygame.K_e:
                        if playerOne.playerUltimate == 3:
                            newGame.playSound('assets/sound/ultimate.wav')
                            ultimate = Ultimate()
                            ultimate.spawnFighters(allyGroup, playerOne.iconPath)

                            playerOne.playerUltimate = 0
                            playerOne.shooting = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        playerOne.stopLeft()
                    if event.key == pygame.K_RIGHT:
                        playerOne.stopRight()

            playerOne.x += playerOne.movement
            playerGroup.update()

            if playerOne.shooting:
                bulletGroup.draw(newGame.screen)
                bulletGroup.update(playerOne.weapon.bulletSpeed, 0)

                if len(bulletGroup) == 0:
                    playerOne.shooting = False

            if playerOne.score == 70 and not stage.stageTwoPower:
                newGame.spawnedPower = 2
                powerUpGroup.add(PowerUp(random.randint(50, 750), 0, 0,  'assets/icon/box1.png'))
                stage.stageTwoPower = True

            if playerOne.score == 132 and not stage.stageThreePower:
                newGame.spawnedPower = 3
                powerUpGroup.add(PowerUp(random.randint(50, 750), 0, 0, 'assets/icon/box2.png'))
                stage.stageThreePower = True


            # collisions
            pygame.sprite.groupcollide(allyGroup, enemyBulletGroup, False, True)

            if pygame.sprite.groupcollide(allyBulletGroup, enemyGroup, True, True):
                if stage.level == 1 or stage.level == 2:
                    playerOne.score += 1
                if stage.level == 3:
                    playerOne.score += 4
                if stage.level == 4:
                    playerOne.score += 8

            if pygame.sprite.groupcollide(playerGroup, powerUpGroup, False, True):
                playerOne.playerWeapon = newGame.spawnedPower

            if pygame.sprite.groupcollide(playerGroup, enemyGroup, False, False):
                newGame.playSound('assets/sound/death.wav')
                playerOne.lives -= 1
                if playerOne.lives == -1:
                    newGame.playBackgroundMusic('assets/sound/game-over.wav', 'game-over')
                newGame.status = 'death'
                explosionGroup.add(Explosion(playerOne.x - 60, playerOne.y - 30))

            if playerOne.playerWeapon == 2:
                if pygame.sprite.groupcollide(enemyGroup, bulletGroup, True, False):
                    bulletGroup.update(playerOne.weapon.bulletSpeed, 1)
                    if stage.level == 1 or stage.level == 2:
                        playerOne.score += 1
                    if stage.level == 3:
                        playerOne.score += 4
                    if stage.level == 4:
                        playerOne.score += 8
            else:
                if pygame.sprite.groupcollide(enemyGroup, bulletGroup, True, True):
                    if stage.level == 1 or stage.level == 2:
                        playerOne.score += 1
                    if stage.level == 3:
                        playerOne.score += 4
                    if stage.level == 4:
                        playerOne.score += 8

            if pygame.sprite.groupcollide(playerGroup, enemyBulletGroup, True, True):
                newGame.playSound('assets/sound/death.wav')
                playerOne.lives -= 1
                if playerOne.lives == -1:
                    newGame.playBackgroundMusic('assets/sound/game-over.wav', 'game-over')
                newGame.status = 'death'
                explosionGroup.add(Explosion(playerOne.x - 60, playerOne.y - 30))

            if playerOne.x <= 13:
                playerOne.x = 13
            elif playerOne.x >= 726:
                playerOne.x = 726

            if playerOne.score == 440:
                newGame.status = 'win'
                newGame.playBackgroundMusic('assets/sound/win.wav', 'win')

            if playerOne.score == newGame.nextLevel and not newGame.status == 'win':
                newGame.updateNextLevelScore(stage.level + 1)
                stage.level += 1
                newGame.status = 'waiting'
                stage.status = 'waiting'
                playerOne.playerUltimate += 1
                playerOne.x = 370
                playerOne.y = 723

            if playerOne.score >= 200 and not newGame.firstWin:
                newGame.winTextTimer += 1
                if newGame.winTextTimer < 1000:
                    newGame.printText('You    Saved    the', '#006600', 190, 325, 40)
                    newGame.printText('Anima Galaxy!', '#592c82', 220, 380, 40)

                if 1000 < newGame.winTextTimer < 2000:
                    newGame.printText('Keep Going!', '#006600', 225, 400, 50)

                if newGame.winTextTimer > 2000:
                    newGame.firstWin = True
            powerUpGroup.draw(newGame.screen)
            powerUpGroup.update()
            newGame.simpleRenderer(playerOne.x, playerOne.y, playerOne.icon)

            allyGroup.draw(newGame.screen)
            allyGroup.update(allyBulletGroup)

            allyBulletGroup.draw(newGame.screen)
            allyBulletGroup.update(3, 0)

        elif newGame.status == 'death':
            newGame.moveBackground()
            newGame.updateLives(playerOne.lives, playerOne.icon)
            playerOne.movement = 0
            if explosionGroup.update():
                explosionGroup.update()

            explosionGroup.draw(newGame.screen)

            if stage.level == 1:
                playerOne.score = 0
            if stage.level == 2:
                playerOne.score = 25
            if stage.level == 3:
                playerOne.score = 80
            if stage.level == 4:
                playerOne.score = 151

            if playerOne.lives == -1:
                newGame.printText('GAME OVER!', '#CF000F', 180, 330, 70)
                newGame.printText('PRESS ENTER', '#CF000F', 280, 420, 30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            playerOne.x = 370
                            playerOne.y = 723
                            playerOne.lives = 3
                            playerOne.score = 0
                            stage.level = 1
                            stage.status = 'waiting'
                            newGame.status = 'waiting'

                            mainMenu()

            if playerOne.lives >=0:
                newGame.printText('YOU DIED!', '#CF000F', 210, 330, 70)
                newGame.printText('PRESS ENTER TO TRY AGAIN', '#CF000F', 160, 420, 30)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            playerOne.x = 370
                            playerOne.y = 723
                            stage.status = 'waiting'
                            newGame.status = 'waiting'

        elif newGame.status == 'win':
            newGame.moveBackground()
            newGame.simpleRenderer(playerOne.x, playerOne.y, playerOne.icon)
            newGame.printText('YOU WIN!', '#006600', 220, 330, 70)
            newGame.printText('PRESS ENTER', '#006600', 270, 420, 30)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        playerOne.x = 370
                        playerOne.y = 723
                        playerOne.lives = 3
                        playerOne.score = 0
                        stage.level = 1
                        stage.status = 'waiting'
                        newGame.status = 'waiting'

                        mainMenu()

        playerOne.drawUltimate(newGame)
        newGame.updateScore(playerOne.score)
        newGame.updateObjective()
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
                    menuAlien.moveDownOption(newGame)

                if event.key == pygame.K_UP:
                    pygame.draw.rect(newGame.screen, (0, 0, 0), menuAlien.rect)
                    menuAlien.moveUpOption(newGame)

                if event.key == pygame.K_SPACE:
                    if menuAlien.menuButton == "music":
                        newGame.pausePlayMusic(musicButton)

                    if menuAlien.menuButton == "sfx":
                        newGame.pausePlaySFX(soundFxButton)

                    if menuAlien.menuButton == "ship":
                        newGame.playSound('assets/sound/menu-change.wav')
                        changeShip()

                    if menuAlien.menuButton == "back":
                        newGame.playSound('assets/sound/menu-change.wav')
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