class Bird:
    import pygame
    width = 100
    height = 100
    xpos = width/2
    ypos = height/2

    loadBird = pygame.image.load("beebrd.png")
    birdSize = pygame.transform.scale(loadBird, (width, height))