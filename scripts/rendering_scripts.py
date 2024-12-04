import pygame
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *

def render_paper(surface: pygame.Surface, screen_infos: dict) -> pygame.Surface:
    """
    Takes a surface and return a paper background
    """
    surface.fill(IVORY)
    
    # Drawing the marging

    pygame.draw.line(surface, LIGHT_RED, (scaled_down(240), 0), (scaled_down(240), screen_infos["width"]), scaled_down(LINE_SIZE))

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
    Takes a dictionary containing the text's font, width, height and the top left tuple;
    A tuple containing the top left position of the text;
    A surface;
    And 
    Render that on that surface
    """

    surface.blit(text_infos["text"], text_infos["top_left"])

    return surface

def render_new_game_button(surface: pygame.Surface, screen_infos: dict, mouse_pos: tuple) -> dict:
    """
    This function will render a 'new game' button text on the main menu,
    and will return the 'new game' button informations.
    """
    new_game_button_infos = buttons_text(FONT_PATH, scaled_down(198), "NEW GAME", BLACK, True)

    new_game_button_infos["top_left"] = ((screen_infos["width"]//2)- new_game_button_infos["width"]//2, scaled_down(1164))
    new_game_button_infos["rect"] = pygame.Rect(new_game_button_infos["top_left"][0], new_game_button_infos["top_left"][1],
                                                new_game_button_infos["width"], new_game_button_infos["height"]
                                )
    if new_game_button_infos["rect"].collidepoint(mouse_pos):
        new_game_button_infos = buttons_text(FONT_PATH, scaled_down(198), "NEW GAME", BLACK, True, True)
        new_game_button_infos["top_left"] = ((screen_infos["width"]//2)- new_game_button_infos["width"]//2, scaled_down(1164))
        new_game_button_infos["rect"] = pygame.Rect(new_game_button_infos["top_left"][0], new_game_button_infos["top_left"][1],
                                                    new_game_button_infos["width"], new_game_button_infos["height"]
                                    )
        render_buttons_text(new_game_button_infos, surface)
    else:
        # Erasing the bold text first
        pygame.draw.rect(surface, POSTIT_BLUE, new_game_button_infos["rect"])

        render_buttons_text(new_game_button_infos, surface)

    return new_game_button_infos

def render_credits_button(surface: pygame.Surface, screen_infos: dict, mouse_pos: tuple) -> dict:
    """
    This function will render a 'new game' button text on the main menu,
    and will return the 'new game' button informations.
    """
    credits_button_infos = buttons_text(FONT_PATH, scaled_down(198), "CREDITS", BLACK, True)

    credits_button_infos["top_left"] = ((screen_infos["width"]//2)- credits_button_infos["width"]//2, scaled_down(1416))
    credits_button_infos["rect"] = pygame.Rect(credits_button_infos["top_left"][0], credits_button_infos["top_left"][1],
                                                credits_button_infos["width"], credits_button_infos["height"]
                                )
            
    if credits_button_infos["rect"].collidepoint(mouse_pos):
        credits_button_infos = buttons_text(FONT_PATH, scaled_down(198), "CREDITS", BLACK, True, True)
        credits_button_infos["top_left"] = ((screen_infos["width"]//2)- credits_button_infos["width"]//2, scaled_down(1416))
        credits_button_infos["rect"] = pygame.Rect(credits_button_infos["top_left"][0], credits_button_infos["top_left"][1],
                                                    credits_button_infos["width"], credits_button_infos["height"]
                                    )
        render_buttons_text(credits_button_infos, surface)
    else:
        # Erasing the bold text first
        pygame.draw.rect(surface, POSTIT_BLUE, credits_button_infos["rect"])

        render_buttons_text(credits_button_infos, surface)

    return credits_button_infos

def render_quit_button(surface: pygame.Surface, screen_infos: dict, mouse_pos: tuple) -> dict:
    """
    This function will render a 'new game' button text on the main menu,
    and will return the 'new game' button informations.
    """
    quit_button_infos = buttons_text(FONT_PATH, scaled_down(198), "QUIT", BLACK, True)
    quit_button_infos["top_left"] = ((screen_infos["width"]//2)- quit_button_infos["width"]//2, scaled_down(1668))
    quit_button_infos["rect"] = pygame.Rect(quit_button_infos["top_left"][0], quit_button_infos["top_left"][1],
                                            quit_button_infos["width"], quit_button_infos["height"]
                            )
            
    if quit_button_infos["rect"].collidepoint(mouse_pos):
        quit_button_infos = buttons_text(FONT_PATH, scaled_down(198), "QUIT", BLACK, True, True)
        quit_button_infos["top_left"] = ((screen_infos["width"]//2)- quit_button_infos["width"]//2, scaled_down(1668))
        quit_button_infos["rect"] = pygame.Rect(quit_button_infos["top_left"][0], quit_button_infos["top_left"][1],
                                                quit_button_infos["width"], quit_button_infos["height"]
                                )
        render_buttons_text(quit_button_infos, surface)
    else:
        # Erasing the bold text first
        pygame.draw.rect(surface, POSTIT_BLUE, quit_button_infos["rect"])

        render_buttons_text(quit_button_infos, surface)

    return quit_button_infos


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

def render_x_and_o_scores(surface: pygame.Surface, screen_infos: dict, x_score: int, o_score:int) -> None:
    """
    Render X's and O's scores on the screen.
    """
    # The score will have 10 digits maximum

    digits_number = 10
    x_score_str = str(x_score)
    o_score_str = str(o_score)
    x_score_color = BLACK
    o_score_color = BLACK

    if len(str(x_score)) < digits_number:
        x_score_str = "0"*(digits_number - len(str(x_score))) + x_score_str
    else:
        x_score_str = "Math ERROR"
        x_score_color = RED
    
    if len(str(o_score)) < digits_number:
        o_score_str = "0"*(digits_number - len(str(o_score))) + o_score_str
    else:
        o_score_str = "Math ERROR"
        o_score_color = RED

    # Rendering the X's score
    
    x_score_text_infos = buttons_text(FONT_PATH, scaled_down(198), "X's SCORE:", BLACK, True)
    x_score_text_infos["top_left"] = (scaled_down(246), scaled_down(30))
    render_buttons_text(x_score_text_infos, surface)
    
    x_score_num_text = buttons_text(FONT_PATH, scaled_down(168), x_score_str, x_score_color, True)
    x_score_num_text["top_left"] = (scaled_down(246), scaled_down(192))
    render_buttons_text(x_score_num_text, surface)

    o_score_text_infos = buttons_text(FONT_PATH, scaled_down(198), "O's SCORE:", BLACK, True)
    o_score_text_infos["top_left"] = (screen_infos["width"] - (x_score_text_infos["width"] + scaled_down(246)), scaled_down(30))
    render_buttons_text(o_score_text_infos, surface)
    
    o_score_num_text = buttons_text(FONT_PATH, scaled_down(168), o_score_str, o_score_color, True)
    o_score_num_text["top_left"] = (screen_infos["width"] - (x_score_text_infos["width"] + scaled_down(246)), scaled_down(192))
    render_buttons_text(o_score_num_text, surface)
    
    return None


def render_turn(screen_infos: dict, surface: pygame.Surface, turn: str) -> None:
    """
    This function will render the informations of the player who is playing on a postit on the top center of the screen.
    """
    if turn != "X's" and turn != "O's":
        raise ValueError("Turn must be X's or O's")
    if turn == "X's":
        postit_color = POSTIT_RED
    else:
        postit_color = POSTIT_BLUE
    
    turn_text_infos = buttons_text(FONT_PATH, scaled_down(198), turn + " TURN", BLACK, True)
    turn_text_x_pos = (screen_infos["width"] - (turn_text_infos["width"]+60))//2
    turn_text_y_pos = scaled_down(90)
    turn_text_infos["top_left"] = (turn_text_x_pos, turn_text_y_pos)

    turn_postit = pygame.Rect((turn_text_x_pos - 48), (turn_text_y_pos - 24), (turn_text_infos["width"] + 96), (turn_text_infos["height"] + 48))

    pygame.draw.rect(surface, postit_color, turn_postit)

    render_buttons_text(turn_text_infos, surface)

    return None