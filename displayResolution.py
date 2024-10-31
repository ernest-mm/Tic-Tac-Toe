# Data taken from the steam's hardware and software survey https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam

import pygame
import sys

pygame.init()

# Suported display resolutions (key = width, value == height)
supportedDisplays = {
    3840: 2160,
    2560: 1440,
    1920: 1080,
    1280: 720,
    }
# supportedHeights = {720, 800, 1024, 1080, 1200, 1440, 1600, 2160, 2400}

# Getting the user's display dimensions
displayInfo = pygame.display.Info()
displayWidth = displayInfo.current_w
displayHeight = displayInfo.current_h

# Check for errors
if displayWidth == -1 or displayHeight == -1:
    print("Error: Unable to retrieve display dimensions.")
    pygame.quit()
    sys.exit()

# Setting up the display
screen = pygame.display.set_mode((displayWidth, displayHeight))

# Creating the game surface based on the user's display dimensions
letterBoxes = None
pillarBoxes = None

if displayWidth in supportedDisplays.keys():
    if displayHeight == supportedDisplays[displayWidth]:
        gameScreenTopLeft = (0, 0)
    elif displayHeight > supportedDisplays[displayWidth]:
        letterBoxes = displayHeight - supportedDisplays[displayWidth]
        gameScreenTopLeft = (0, letterBoxes//2)
    else:
        # I have no idea right now
        pass
elif displayHeight in supportedDisplays.values():
    width = next((key for key, value in supportedDisplays.items() if value == displayHeight), None)
    if displayWidth > width:
        pillarBoxes = displayWidth - width
        gameScreenTopLeft = (pillarBoxes//2, 0)
    else:
        # I have no idea
        pass
else:
    # Looking for the height with the smallest pillarboxes
    pillarBoxes = displayWidth
    bestWidth = None
    for width in supportedDisplays.keys():
        temp = displayWidth - width
        if temp > 0 and temp < pillarBoxes:
            pillarBoxes = temp
            bestWidth = width

    # Calculating the letterboxes
    if displayHeight > supportedDisplays[bestWidth]:
        letterBoxes = displayHeight - supportedDisplays[bestWidth]

    gameScreenTopLeft = (pillarBoxes//2, letterBoxes//2)

# Creating the game surface

gameScreenHeight = displayHeight - letterBoxes
gameScreenWidth = displayWidth - pillarBoxes
gameScreen = pygame.Surface((gameScreenWidth, gameScreenHeight))

# Blitting the game surface to the display

screen.blit(gameScreen, gameScreenTopLeft)

pygame.quit()
sys.exit()