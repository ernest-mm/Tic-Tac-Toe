import pygame
import sys
from typing import Optional
from fractions import Fraction

# pygame.SCALED can be used to easily scale up the display with a game surface blitted on it, 
# but it's hard to scale down all the sprites.
# This script will chose what assets' resolution will be used in the game based on the user's display resolution.

def get_dimensions() -> tuple[int, int]:
    """
    Returns the user's display width and height
    """
    pygame.init()

    display_info = pygame.display.Info()

    # Check for errors

    if display_info.current_w == -1 or display_info.current_h == -1:
        print("Error: Unable to retrieve display dimensions.")
        pygame.quit()
        sys.exit()

    else:
        pygame.quit()
        return display_info.current_w, display_info.current_h


def get_supported_res(width: int, height: int, supported_displays: dict[tuple[int, int], str]) -> tuple[int, int]: 
    """
    Returns either the user's display resolution if it is supported or a resolution smaller but close enough to it
    """

    if (width, height) in supported_displays.keys():
        return (width, height)
    else:

        # Looking for a supported resolution smaller than the user display but close enough to it

        closest_res = None
        difference = [None, None]

        for res in supported_displays.keys():
            if (difference[0] == None and
                difference[1] == None and 
                width - res[0] >= 0 and 
                height - res[1] >= 0):

                difference[0] = width - res[0]
                difference[1] = height - res[1]
                closest_res = res

            elif (width - res[0] >= 0 and
                  height - res[1] >= 0):
                
                if (width - res[0] <= difference[0]) and (height - res[1] <= difference[1]):
                    difference[0] = width - res[0]
                    difference[1] = height - res[1]
                    closest_res = res
        
        if closest_res is None:
            raise ValueError("No suitable resolution found for the display.")

        return closest_res
    
    
def is_factor(supported_displays: dict[tuple[int, int], str], developer_res: tuple[int, int]) -> bool:
    for key in supported_displays.keys():
        if developer_res[0] % key[0] != 0 or developer_res[1] % key[1] != 0:
            return False
        elif developer_res[0] // key[0] != developer_res[1] // key[1]:
            return False
    return True


def get_screen_infos(developer_res: tuple[int, int] = (3840, 2160)) -> dict:
    """
    Takes the width and the height of the resolution you're developping on.
    Returns a dictionary containing the informations that will be used in the pygame.display.set_mode() with the pygame.SCALED argument.
    """

    # Supported display resolutions (key == tuple of width and height, value == resolution name)
    supported_displays = {
        (3840, 2160): "4K",
        (1920, 1080): "1080p",
        (1280, 720): "720p",
        (768, 432): "432p"
        }
    
    # Checking if every supported display resolution is a factor of the dev's display resolution
    if is_factor(supported_displays, developer_res) == False:
        return "Error: The developer's resolution should be a multiple of every supported display resolution"

    
    display_width, display_height = get_dimensions()

    supported_res = get_supported_res(display_width, display_height, supported_displays)

    screen_infos = {
        "width": supported_res[0],
        "height": supported_res[1],
        "resolution": supported_displays[supported_res],
        "scale": Fraction(1, developer_res[0]) * Fraction(supported_res[0], 1)
    }

    return screen_infos

def scaled(screen_infos: dict, width_or_height: int) -> int:
    """
    Takes a width or height in the developer's resolution and returns a value converted to the user's supported resolution
    """
    scale = screen_infos["scale"]
    scaled = int(Fraction(width_or_height, 1) * scale)

    return scaled
    
if __name__ == "__main__":
    print(get_screen_infos())
