import pygame
from Hive import Hive
from Bee import Bee
import random
class Pillar(pygame.sprite.Sprite):
    scored = False

    width = 200
    height = 200
    xpos = Hive.width + width
    ypos = Hive.height - height/2

    loadPillarTop = pygame.image.load("JYPipeTop.png")
    loadPillarBottom = pygame.image.load("JyPipeBottom.png")
    
    PillarSizeTop = pygame.transform.scale(loadPillarTop, (width, height))
    PillarSizeBottom = pygame.transform.scale(loadPillarBottom, (width, height))

    # Constructor which sets x, y, and image variables to be assigned
    def __init__(self, x, y, image, PillarType):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, = x,y
        self.PillarType = PillarType
    def update(self):
        self.rect.x -= 2 # speed
        if self.rect.x <= -Hive.width:
            self.kill()
        if Bee.xpos + Bee.width/2 > self.rect.topright[0] and self.scored == False and self.PillarType == 'bottom':
            Bee.score += 1
            self.scored = True