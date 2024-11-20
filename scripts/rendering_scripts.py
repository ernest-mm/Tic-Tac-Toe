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

def buttons_text(font_path: str, font_size: int, text: str, text_color: tuple, anti_aliasing: bool = True) -> dict:
    pygame.font.init()
    font = pygame.font.Font(font_path, font_size)
    text = font.render(text, anti_aliasing, text_color)
    text_w, text_h = text.get_size()
    return_value = {
        "text": text,
        "width": text_w,
        "height": text_h
    }
    return return_value
