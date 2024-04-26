# Made by Jialai Ying
import pygame
pygame.init()

# Setup
running = False
width = 300
height = 500
xpos = width / 2
ypos = height / 2
screen = pygame.display.set_mode((width,height))
loadStart = pygame.image.load("startscreen.png")
startScreenSize = pygame.transform.scale(loadStart, (width, height))
screen.blit(startScreenSize, (0,0))
pygame.display.update()



# Quit
while running == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()