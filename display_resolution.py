import pygame
from typing import Optional
from fractions import Fraction

# pygame.SCALED can be used to easily scale up the display with a game surface blitted on it, 
# but it's hard to scale down all the sprites.
# This script will chose what assets' resolution will be used in the game based on the user's display resolution.

def get_dimensions() -> tuple[int, int]:
    """
    Returns the user's display width and height.
    Raises a ValueError if the dimensions cannot be retrieved.
    """
    if not pygame.get_init(): # Check if Pygame is already initialized
        pygame.init()

    try:
        display_info = pygame.display.Info()

        # Check for errors

        if display_info.current_w == -1 or display_info.current_h == -1:
            raise ValueError("Unable to retrieve display dimensions.")

        width, height = display_info.current_w, display_info.current_h

        return width, height
    
    finally:
        # Only quit pygame if it was initialized by this function
        if pygame.get_init():  # Check if we initialized it here
            pygame.quit()



def get_supported_res(width: int, height: int, supported_displays: dict[tuple[int, int], str]) -> tuple[int, int]: 
    """
    Returns either the user's display resolution if it is supported, or a resolution smaller but close enough to it.
    Raises a ValueError if no suitable resolution is found.    
    """

    if not supported_displays:
        raise ValueError("No supported display resolutions provided.")

    if (width, height) in supported_displays:
        return (width, height)
    else:

        # Looking for a supported resolution smaller than the user display but close enough to it

        closest_res = None
        min_diff = float('inf')

        for res in supported_displays.keys():
            res_width, res_height = res
            if width >= res_width and height >= res_height:
                # Euclidean distance between the resolutions
                diff = ((res_width - width) ** 2 + (res_height - height) ** 2) ** 0.5

                if diff < min_diff:
                    min_diff = diff
                    closest_res = res
        
        if closest_res is None:
            raise ValueError(f"No suitable resolution found for {width}x{height}.")

        return closest_res
    

def is_factor(supported_displays: dict[tuple[int, int], str], development_resolution: tuple[int, int]) -> bool:
    """
    Checks if the development_resolution is a factor of all resolutions in supported_displays.
    A resolution is considered a factor if both dimensions are divisible and have the same aspect ratio.
    """
    
    dev_width, dev_height = development_resolution
    
    for (res_width, res_height) in supported_displays.keys():
        # Check if the development resolution is divisible by the current resolution
        if dev_width % res_width != 0 or dev_height % res_height != 0:
            return False
        
        # Check if the aspect ratios match
        width_ratio = dev_width // res_width
        height_ratio = dev_height // res_height
        if width_ratio != height_ratio:
            return False
    
    return True


def get_screen_infos(development_resolution: tuple[int, int] = (3840, 2160)) -> dict:
    """
    Takes the width and the height of the resolution you're developing on.
    Returns a dictionary containing the information needed for pygame.display.set_mode() with the pygame.SCALED argument.
    
    Args:
        development_resolution (tuple[int, int]): The resolution the developer is working on. Default is 4K (3840x2160).

    Returns:
        dict: A dictionary containing the supported resolution's width, height, resolution name, and scaling factor.
    """

    # Supported display resolutions (key == tuple of width and height, value == resolution name)
    supported_displays = {
        (3840, 2160): "4K",
        (1920, 1080): "1080p",
        (1280, 720): "720p",
        (768, 432): "432p"
        }
    
    # Checking if every supported display resolution is a factor of the dev's display resolution
    if not is_factor(supported_displays, development_resolution):
        raise ValueError(f"The developer's resolution {development_resolution} should be a multiple of every supported display resolution.")

    # Getting the display dimensions
    display_width, display_height = get_dimensions()

    # Getting the best supported resolution for the current display dimensions
    supported_res = get_supported_res(display_width, display_height, supported_displays)

    scale = Fraction(supported_res[0], development_resolution[0])


    screen_infos = {
        "width": supported_res[0],
        "height": supported_res[1],
        "resolution": supported_displays[supported_res],
        "scale": scale
    }

    return screen_infos

def scaled_down(screen_infos: dict, value: int) -> int:
    """
    Takes a value (x, y, width, or height) in the developer's resolution and returns a value converted to the user's supported resolution.
    
    Args:
        screen_infos (dict): A dictionary containing screen information, including the scale factor.
        value (int): A dimension (x, y, width, or height) in the developer's resolution.

    Returns:
        int: The scaled dimension according to the supported resolution.
    """
    scale = screen_infos["scale"]

    if scale == 0:
        raise ValueError("Scale factor cannot be zero.")
    
    scaled = int(value * scale)

    return scaled
    
if __name__ == "__main__":
    print(get_screen_infos())
