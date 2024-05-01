class Pillar:
    import pygame
    width = 200
    height = 200
    xpos = width/2
    ypos = height/2

    loadStart = pygame.image.load("honeycomb.png")
    startScreenSize = pygame.transform.scale(loadStart, (width, height))