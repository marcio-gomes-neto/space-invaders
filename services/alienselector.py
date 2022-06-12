import pygame


class MenuAlien(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super(MenuAlien, self).__init__()
        # adding all the images to sprite array
        self.x = posX
        self.y = posY
        self.animation = False
        self.images = []
        self.images.append(pygame.image.load('assets/icon/menu/frame1.gif'))
        self.images.append(pygame.image.load('assets/icon/menu/frame2.gif'))
        self.images.append(pygame.image.load('assets/icon/menu/frame3.gif'))
        self.images.append(pygame.image.load('assets/icon/menu/frame4.gif'))
        self.images.append(pygame.image.load('assets/icon/menu/frame5.gif'))
        self.images.append(pygame.image.load('assets/icon/menu/frame6.gif'))

        self.menuButton = None
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(posX, posY))

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    def moveDown(self):
        if self.y == 700:
            return
        self.rect = self.image.get_rect(center=(self.x, self.y + 110))
        self.y += 110

        if self.menuButton == "play":
            self.menuButton = "options"
        else:
            self.menuButton = "quit"

    def moveUp(self):
        if self.y == 480:
            return
        self.rect = self.image.get_rect(center=(self.x, self.y - 110))
        self.y -= 110

        if self.menuButton == "quit":
            self.menuButton = "options"
        else:
            self.menuButton = "play"

    def moveDownOption(self):
        if self.menuButton == "back":
            return

        if self.menuButton == "music":
            self.menuButton = "sfx"
            self.rect = self.image.get_rect(center=(self.x, self.y + 120))
            self.y = 300

        elif self.menuButton == "sfx":
            self.menuButton = "ship"
            self.rect = self.image.get_rect(center=(self.x, self.y + 120))
            self.y = 420
        else:
            self.menuButton = "back"
            self.rect = self.image.get_rect(center=(self.x, 720))
            self.y = 720

    def moveUpOption(self):
        if self.menuButton == "music":
            return

        if self.menuButton == "sfx":
            self.menuButton = "music"
            self.rect = self.image.get_rect(center=(self.x, 180))
            self.y = 180

        elif self.menuButton == "ship":
            self.menuButton = "sfx"
            self.rect = self.image.get_rect(center=(self.x, 300))
            self.y = 300
        else:
            self.menuButton = "ship"
            self.rect = self.image.get_rect(center=(self.x, 420))
            self.y = 420
