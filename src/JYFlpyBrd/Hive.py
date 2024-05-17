class Hive:
  import pygame

  width = 500
  height = 500
  xpos = width/2
  ypos = height/2

  # Set the surface

  screen = pygame.display.set_mode((width, height))

  # Initial load

  loadStart = pygame.image.load("JYStartScreen.png")
  loadStarted = pygame.image.load("JYScreenStarted.png")

  # Resize the initial load

  screenSize = pygame.transform.scale(loadStart, (width, height))
  startedSize = pygame.transform.scale(loadStarted, (width, height))