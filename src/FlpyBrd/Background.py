class Background:
    import pygame
    width = 500
    height = 500
    xpos = width / 2
    ypos = height / 2
    screen = pygame.display.set_mode((width,height))
    loadStart = pygame.image.load("startscreen.png")
    startScreenSize = pygame.transform.scale(loadStart, (width, height))