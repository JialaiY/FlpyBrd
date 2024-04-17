# Made by Jialai Ying
import pygame
pygame.init()
running = False
width = 500
height = 500
xpos = width / 2
ypos = height / 2
screen = pygame.display.set_mode((width,height))
loadStart = pygame.image.load("startscreen.png")
startScreenSize = pygame.transform.scale(loadStart, (width, height))

screen.blit(startScreenSize, (0,0))

pygame.display.update()

while running == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()