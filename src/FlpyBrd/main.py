# Made by Jialai Ying
import pygame
from Bird import Bird
from Pillar import Pillar
from Background import Background

pygame.init()
running = True
while running == True:

    # Drawing Code
    Background.screen.blit(Background.startScreenSize, (0,0))
    Background.screen.blit(Bird.birdSize, (Bird.xpos, Bird.ypos))
    Background.screen.blit(Pillar.startScreenSize, (0,0))
    pygame.display.update()

    # Enter Game

    if intial == True:
        for event in pygame.event.get():
     

    # Object Detection


    # Exit Code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()