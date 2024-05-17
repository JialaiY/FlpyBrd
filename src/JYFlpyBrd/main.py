# Made by Jialai Ying
import pygame
import random
from Bee import Bee
from Hive import Hive
from Pillar import Pillar
from sys import exit
pygame.init()
loadScreen = Hive.screenSize
running = True
initial = True
initBee = True
isAlive = True
PillarTimer = 200
BeeTimer = 0
clock = pygame.time.Clock()
xBee, yBee = Bee.xpos, Bee.ypos
userInput = pygame.key.get_pressed()
BeePos = (Bee.xpos, Bee.ypos)
font = pygame.font.SysFont('Segoe', 26)
Pillars = pygame.sprite.Group()
Bee1 = pygame.sprite.GroupSingle()
Bee1.add(Bee(xBee, yBee, Bee.beeSize))
while running == True:
    Hive.screen.blit(loadScreen, (0, 0))
    if PillarTimer <= 0:
        xTop, xBottom = Hive.width + Pillar.width, Hive.width + Pillar.width
        yTop = 0
        yBottom = yTop + Pillar.height + random.randrange(120, 180)
        Pillars.add(Pillar(xTop, yTop, Pillar.PillarSizeTop, 'top'))
        Pillars.add(Pillar(xBottom, yBottom, Pillar.PillarSizeBottom, 'bottom'))
        PillarTimer = 250
    PillarTimer -= 1
    if Bee1.sprite.alive == True and loadScreen == Hive.startedSize:
        Pillars.update()
    if loadScreen == Hive.startedSize:
        Bee1.update(userInput)
    if initBee == True:
        xBee += 10
        initBee = False
    if PillarTimer <= 0:
        xTop, xBottom = Hive.width + Pillar.width, Hive.width + Pillar.width
        yTop = 0
        yBottom = yTop + Pillar.height + random.randrange(120, 180)
        Pillars.add(Pillar(xTop, yTop, Pillar.PillarSizeTop, 'top'))
        Pillars.add(Pillar(xBottom, yBottom, Pillar.PillarSizeBottom, 'bottom'))
        PillarTimer = 250
    PillarTimer -= 1
    Pillars.draw(Hive.screen)
    Bee1.draw(Hive.screen)
    scoreText = font.render('score: ' + str(Bee.score), True, (255, 255, 255))
    Hive.screen.blit(scoreText, (20, 20))
    clock.tick(60)
    pygame.display.update()
    if initial == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                loadScreen = Hive.startedSize
                initial = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    PillarCollision = pygame.sprite.spritecollide(Bee1.sprites()[0], Pillars, False)
    if PillarCollision:
        Bee1.sprite.alive = False
pygame.quit()
exit()