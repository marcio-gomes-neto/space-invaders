import pygame
import math
from entities.player import Player
from entities.gamewindow import GameWindow
from entities.bullet import Bullet
from pygame import mixer

# initializing pygame
newGame = GameWindow(800, 800, 'data/spaceship.png', 'Space Invaders')
newGame.prepareBackground('data/background.png')

playerOne = Player(370, 723, "data/spaceship.png", 0)

font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255, 255, 255))
    newGame.screen.blit(game_over_text, (190, 250))


# Background Sound
mixer.music.load('data/background.wav')
mixer.music.play()

# player


# Invader
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 0

for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load('data/alien.png'))
    invader_X.append(400)
    invader_Y.append(10)
    invader_Xchange.append(0.8)
    invader_Ychange.append(50)

# Bullet
# rest - bullet is not moving
# fire - bullet is moving
gunner = Bullet(0, 715, 'data/bullet.png', 1, 'data/bullet.wav')
bullet_state = "rest"


# Collision Concept
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) +
                         (math.pow(y1 - y2, 2)))
    if distance <= 50:
        return True
    else:
        return False

def invader(x, y, i):
    newGame.screen.blit(invaderImage[i], (x, y))


def bullet(x, y):
    global bullet_state
    newGame.screen.blit(gunner.icon, (x + 16, y))
    bullet_state = "fire"

scroll = 0
tiles = 2
# game loop
running = True
while running:
    # INSIDE OF THE GAME LOOP
    for i in range(0, tiles):
        newGame.screen.blit(newGame.bg, (0, -i * newGame.bgHeigth + scroll))

    scroll += 0.3
    if abs(scroll) > newGame.bgHeigth:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controlling the player movement
        # from the arrow keys
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerOne.moveLeft()
            if event.key == pygame.K_RIGHT:
                playerOne.moveRight()
            if event.key == pygame.K_SPACE:
                gunner.x = playerOne.x + 4
                bullet(gunner.x, gunner.y)
                gunner.sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerOne.stopLeft()
            if event.key == pygame.K_RIGHT:
                playerOne.stopRight()

    # adding the change in the player position
    playerOne.x += playerOne.movement
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]

    # bullet movement
    if gunner.y <= 0:
        gunner.y = 715
        bullet_state = "rest"
    if bullet_state is "fire":
        bullet(gunner.x, gunner.y)
        gunner.y -= gunner.bulletSpeed

    # movement of the invader
    for i in range(no_of_invaders):

        if invader_Y[i] >= 450:
            if abs(playerOne.x - invader_X[i]) < 80:
                for j in range(no_of_invaders):
                    invader_Y[j] = 2000
                    explosion_sound = mixer.Sound('data/explosion.wav')
                    explosion_sound.play()
                game_over()
                break

        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]

        # Collision
        collision = isCollision(gunner.x, invader_X[i],
                                gunner.y, invader_Y[i])
        if collision:
            playerOne.score += 1
            gunner.y = 715
            bullet_state = "rest"
            invader_X[i] = 64
            invader_Y[i] = 30
            invader_Xchange[i] *= -1

        invader(invader_X[i], invader_Y[i], i)

    # restricting the spaceship so that
    # it doesn't go out of screen
    if playerOne.x <= 13:
        playerOne.x = 13;
    elif playerOne.x >= 726:
        playerOne.x = 726

    newGame.simpleRenderer(playerOne.x, playerOne.y, playerOne.icon)
    newGame.updateScore(playerOne.score)
    pygame.display.update()