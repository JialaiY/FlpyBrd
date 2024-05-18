import pygame
from Hive import Hive

class Bee(pygame.sprite.Sprite):
    scale = 2

    loadBee = pygame.image.load("Bird.png")
    beeSize = pygame.transform.scale_by(loadBee, (scale, scale))

    width = loadBee.get_height() * scale
    height = loadBee.get_height() * scale
    xpos = 100
    ypos = Hive.height/2 - width
    score = 0

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, userInput):
        
        # Gravity
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.vel == 0:
            self.flap = False
        if self.rect.y < Hive.height - self.width:
            self.rect.y += int(self.vel)

        # Detect click
        if pygame.mouse.get_pressed()[0] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7
        if self.alive == False:
            self.vel = 7