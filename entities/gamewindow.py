import pygame



class GameWindow:
    def __init__(self, x, y, iconPath, description):
        pygame.init()
        self.x = x
        self.y = y

        img = pygame.image.load(iconPath)
        pygame.display.set_icon(img)
        pygame.display.set_caption(description)

        self.screen = pygame.display.set_mode((self.x, self.y))
        self.clock = pygame.time.Clock()


    def prepareBackground(self, bgPath):
        self.bg = pygame.image.load(bgPath).convert()
        self.bgHeigth = self.bg.get_height()

    def updateScore(self, score):
        font = pygame.font.Font('freesansbold.ttf', 20)
        score = font.render("Points: " + str(score), True, (255, 255, 255))
        self.screen.blit(score, (5, 5))

    def simpleRenderer(self, x, y, icon):
        self.screen.blit(icon, (x, y))

