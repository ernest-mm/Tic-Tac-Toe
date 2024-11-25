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

def render_back_button(surface: pygame.Surface, mouse_pos: tuple) -> dict:
    """
    This function will render a 'back' button text on a postit on the bottom left of the screen,
    and will return the back button informations.
    """
    postit = pygame.Rect(scaled_down(120), scaled_down(1680), scaled_down(480), scaled_down(360))

    pygame.draw.rect(surface, POSTIT_RED, postit)

    back_button_infos = buttons_text(FONT_PATH, scaled_down(198), "BACK", BLACK, True)

    # Calculating the back button text top left to make it in the center of our postit.

    back_button_infos["top_left"] = (scaled_down(120) + (scaled_down(480) - back_button_infos["width"])//2, 
                                     scaled_down(1680) + (scaled_down(360) - back_button_infos["height"])//2)
    back_button_infos["rect"] = pygame.Rect(back_button_infos["top_left"][0], back_button_infos["top_left"][1],
                                                        back_button_infos["width"], back_button_infos["height"]
                                        )
    
    if back_button_infos["rect"].collidepoint(mouse_pos):
        back_button_infos = buttons_text(FONT_PATH, scaled_down(198), "BACK", BLACK, True, True)
        back_button_infos["top_left"] = (scaled_down(120) + (scaled_down(480) - back_button_infos["width"])//2, 
                                     scaled_down(1680) + (scaled_down(360) - back_button_infos["height"])//2)
        back_button_infos["rect"] = pygame.Rect(back_button_infos["top_left"][0], back_button_infos["top_left"][1],
                                                        back_button_infos["width"], back_button_infos["height"]
                                        )
        render_buttons_text(back_button_infos, surface)
    else:
        # Erasing the bold text first
        pygame.draw.rect(surface, POSTIT_RED, back_button_infos["rect"])

        render_buttons_text(back_button_infos, surface)

    return back_button_infos