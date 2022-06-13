import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super(Explosion, self).__init__()
        # adding all the images to sprite array
        self.x = posX
        self.y = posY
        self.animation = False
        self.counter = 0
        self.images = []
        self.images.append(pygame.image.load('assets/icon/explosion/exp1.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp2.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp3.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp4.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp5.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp6.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp7.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp8.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp9.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp10.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp11.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp12.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp13.png'))
        self.images.append(pygame.image.load('assets/icon/explosion/exp14.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(posX, posY))

    def update(self):
        self.image = pygame.transform.scale(self.image, (300, 146))
        explosionSpeed = 35
        self.counter += 1
        if self.index == 13:
            self.kill()
            return False

        if self.counter >= explosionSpeed and self.index <= len(self.images):
            self.counter = 0
            self.index += 1
            self.image = pygame.transform.scale(self.images[self.index], (300, 146))

        return True

