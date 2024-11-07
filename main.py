import pygame
import sys
from pygame.locals import *
import displayResolution

pygame.init()

# Creating the screen and the game window

screen = pygame.display.set_mode(displayResolution.getDisplayDimensions(), FULLSCREEN + NOFRAME + SCALED)
gameScreenInfos = displayResolution.getGameScreenInfos()
gameScreen = pygame.Surface((gameScreenInfos["width"], gameScreenInfos["height"]))

pygame.display.set_caption('Tic Tac Toe')
# ICON_SURFACE = pygame.image.load("32X32.png")
# # pygame.display.set_icon(ICON_SUFACE)

clock = pygame.time.Clock()

# def mainMenu():
#     GAMEWINDOW.fill((0, 0, 0))
#     # Test BG image:
#     TESTBG = pygame.image.load("testBG.png").convert()
#     GAMEWINDOW.blit(TESTBG, (0, 0))

#     # Buttons
#     NEWGAMEBUTTON = pygame.Rect(640, 450, 640, 90)
#     OPTIONSBUTTON = pygame.Rect(640, 570, 640, 90)
#     CREDITSBUTTON = pygame.Rect(640, 690, 640, 90)
#     QUITBUTTON = pygame.Rect(640, 810, 640, 90)

#     # The gameState variable will help us see which menu the program should be in
#     gameState = None

#     running = True

#     while running:
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), NEWGAMEBUTTON)
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), OPTIONSBUTTON)
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), CREDITSBUTTON)
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), QUITBUTTON)

#         # Checking if the mouse is on our buttons

#         mousePos = pygame.mouse.get_pos()

#         if NEWGAMEBUTTON.collidepoint(mousePos):
#            pygame.draw.rect(GAMEWINDOW, (135, 0, 0), NEWGAMEBUTTON)
#         if OPTIONSBUTTON.collidepoint(mousePos):
#             pygame.draw.rect(GAMEWINDOW, (135, 0, 0), OPTIONSBUTTON)
#         if CREDITSBUTTON.collidepoint(mousePos):
#             pygame.draw.rect(GAMEWINDOW, (135, 0, 0), CREDITSBUTTON)
#         if QUITBUTTON.collidepoint(mousePos):
#             pygame.draw.rect(GAMEWINDOW, (135, 0, 0), QUITBUTTON)

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == MOUSEBUTTONDOWN:
#                 # Checking what button has been clicked on
#                 if NEWGAMEBUTTON.collidepoint(mousePos):
#                     gameState = game()
#                     running = False
#                 elif OPTIONSBUTTON.collidepoint(mousePos):
#                     gameState = options()
#                     running = False
#                 elif CREDITSBUTTON.collidepoint(mousePos):
#                     gameState = credits()
#                     running = False
#                 elif QUITBUTTON.collidepoint(mousePos):
#                     pygame.quit()
#                     sys.exit()

#         pygame.display.update()
    
#     return gameState()

# def game():
#     while True:
#         GAMEWINDOW.fill("black")
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# def options():
#     while True:
#         GAMEWINDOW.fill("black")
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# def credits():
#     while True:
#         GAMEWINDOW.fill("black")
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# if __name__ == '__main__':
#     mainMenu()