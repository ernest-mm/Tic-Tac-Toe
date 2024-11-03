import pygame
import sys
from typing import Optional

def getDisplayDimensions() -> tuple[int, int]:
    """
    Returns the user's display width and height
    """
    displayInfo = pygame.display.Info()
    return displayInfo.current_w, displayInfo.current_h

def checkSupportedResolutions(width: int, height: int, supportedDisplays: dict[tuple[int, int], str]) -> tuple[bool, bool, Optional[tuple[int, int]]]: 
    """
    Check if the user's display resolution is supported
    """

    if (width, height) in supportedDisplays.keys():
        resolutionKey = (width, height)
        return True, True, resolutionKey
    else:
        resolutionKey = None
    
    # Checking if only the width or the height is supported

    widthIsSupported = any(width in key for key in supportedDisplays)
    heightIsSupported = any(height in key for key in supportedDisplays)

    # Getting the height's or width's key
    
    if widthIsSupported:
        resolutionKey = next((key for key in supportedDisplays if width in key), None)
    elif heightIsSupported:
        resolutionKey = next((key for key in supportedDisplays if height in key), None)

    return widthIsSupported, heightIsSupported, resolutionKey


def getGameScreenInfos() -> dict:
    pygame.init()

    # Suported display resolutions (key == tuple of width and height, value == resolution name)
    supportedDisplays = {
        (3840, 2160): "4K",
        (2560, 1440): "1440p",
        (1920, 1080): "1080p",
        (1280, 720): "720p"
        }
    
    displayWidth, displayHeight = getDisplayDimensions()

    # Check for errors
    if displayWidth == -1 or displayHeight == -1:
        print("Error: Unable to retrieve display dimensions.")
        pygame.quit()
        sys.exit()

    # Creating the game surface based on the user's display dimensions
    letterBoxes = int(0)
    pillarBoxes = int(0)
    resolution = None

    widthIsSupported, heightIsSupported, resolutionKey = checkSupportedResolutions(displayWidth, displayHeight, supportedDisplays)
    
    if widthIsSupported and heightIsSupported:
        resolution = supportedDisplays[resolutionKey]
        gameScreenTopLeft = (0, 0)

    elif widthIsSupported:
        if displayHeight > resolutionKey[1]:
            letterBoxes = displayHeight - resolutionKey[1]
            resolution = supportedDisplays[resolutionKey]
            gameScreenTopLeft = (0, letterBoxes//2)
        else:
            # Sprites transformation
            pass
    elif heightIsSupported:
        if displayWidth > resolutionKey[0]:
            pillarBoxes = displayWidth - resolutionKey[0]
            resolution = supportedDisplays[resolutionKey]
            gameScreenTopLeft = (pillarBoxes//2, 0)
        else:
            # Sprites transformation
            pass

    else:
        # Looking for the height with the smallest pillarboxes
        pillarBoxes = displayWidth
        bestWidth = None
        for key in supportedDisplays.keys():
            temp = displayWidth - key[0]
            if temp > 0 and temp < pillarBoxes:
                pillarBoxes = temp
                bestWidth = key[0]
                resolutionKey = key

            # Calculating the letterboxes
            if displayHeight > resolutionKey[1]:
                letterBoxes = displayHeight - resolutionKey[1]
            
            # Checking if the pillarboxes are smaller than the letterboxes to see if we can scretch the sprites
            if pillarBoxes < letterBoxes:
                # The transform assets stuffs
                pass
            else: 
                resolution = supportedDisplays[resolutionKey]
                gameScreenTopLeft = (pillarBoxes//2, letterBoxes//2)

    # Gathering the game screen infos

    gameScreenInfos = {
        "width": displayWidth - pillarBoxes,
        "height": displayHeight - letterBoxes,
        "topLeft": gameScreenTopLeft,
        "resolution": resolution
    }

    pygame.quit()

    return gameScreenInfos

if __name__ == "__main__":
    gameScreenInfos = getGameScreenInfos()
    print(gameScreenInfos)
