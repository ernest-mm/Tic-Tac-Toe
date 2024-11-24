import pygame
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *

def render_paper(surface: pygame.Surface, screen_infos: dict) -> pygame.Surface:
    """
    Takes a surface and return a paper background
    """
    surface.fill(IVORY)
    
    # Drawing the marging

    pygame.draw.line(surface, LIGHT_RED, (scaled_down(240), 0), (scaled_down(240), screen_infos["width"]), scaled_down(6))

    # Drawing the lines

    for i in range(scaled_down(240), screen_infos["height"], scaled_down(120)):
        pygame.draw.line(surface, LIGHT_BLUE, (0, i), (screen_infos["width"], i), scaled_down(6))

    return surface

def buttons_text(font_path: str, font_size: int, text: str, text_color: tuple, anti_aliasing: bool, is_bold: bool = False) -> dict:
    pygame.font.init()
    font = pygame.font.Font(font_path, font_size)

    if is_bold:
        base_text = font.render(text, anti_aliasing, text_color)
        text_surface = pygame.Surface(base_text.get_size(), pygame.SRCALPHA)

        offsets = [(0, 0), (1, 0), (0, 1), (1, 1),
                   (2, 0), (0, 2), (2, 1), (1, 2),
                   (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)
        ]

        for dx, dy in offsets:
            text_surface.blit(font.render(text, anti_aliasing, text_color), (dx, dy))

        text_w, text_h = text_surface.get_size()

    else:
        text_surface = font.render(text, anti_aliasing, text_color)
        text_w, text_h = text_surface.get_size()

    return_value = {
        "text": text_surface,
        "width": text_w,
        "height": text_h
    }
    return return_value

def render_buttons_text(text_infos: dict, surface: pygame.Surface) -> pygame.Surface:
    """
    Takes a dictionary containing the text's font, width, height and the top left tup;e;
    A tuple containing the top left position of the text;
    A surface;
    And 
    Render that on that surface
    """

    surface.blit(text_infos["text"], text_infos["top_left"])

    return surface