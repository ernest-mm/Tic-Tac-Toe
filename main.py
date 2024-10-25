import pygame, sys
from pygame.locals import *

# Initializing Pygame

pygame.init()

# Creating the game window

GAMEWINDOWWIDTH = 1920
GAMEWINDOWHEIGHT = 1080
GAMEWINDOW = pygame.display.set_mode((GAMEWINDOWWIDTH, GAMEWINDOWHEIGHT))
pygame.display.set_caption('Tic Tac Toe')
# ICON_SURFACE = pygame.image.load("32X32.png")
# pygame.display.set_icon(ICON_SUFACE)

def mainMenu():

    # Buttons
    NEWGAMEBUTTON = pygame.Rect(640, 450, 640, 90)
    OPTIONSBUTTON = pygame.Rect(640, 570, 640, 90)
    CREDITSBUTTON = pygame.Rect(640, 690, 640, 90)
    QUITBUTTON = pygame.Rect(640, 810, 640, 90)

    running = True

    while running:
        pygame.draw.rect(GAMEWINDOW, (255, 0, 0), NEWGAMEBUTTON)
        pygame.draw.rect(GAMEWINDOW, (255, 0, 0), OPTIONSBUTTON)
        pygame.draw.rect(GAMEWINDOW, (255, 0, 0), CREDITSBUTTON)
        pygame.draw.rect(GAMEWINDOW, (255, 0, 0), QUITBUTTON)

        # Checking if the mouse is on our buttons

        mousePos = pygame.mouse.get_pos()

        if NEWGAMEBUTTON.collidepoint(mousePos):
           pygame.draw.rect(GAMEWINDOW, (135, 0, 0), NEWGAMEBUTTON)
        if OPTIONSBUTTON.collidepoint(mousePos):
            pygame.draw.rect(GAMEWINDOW, (135, 0, 0), OPTIONSBUTTON)
        if CREDITSBUTTON.collidepoint(mousePos):
            pygame.draw.rect(GAMEWINDOW, (135, 0, 0), CREDITSBUTTON)
        if QUITBUTTON.collidepoint(mousePos):
            pygame.draw.rect(GAMEWINDOW, (135, 0, 0), QUITBUTTON)

        for event in pygame.event.get():
            if event.type == QUIT:
                running == False
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

if __name__ == '__main__':
    mainMenu()