import pygame
import random
from scripts.display_resolution import scaled_down
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

def get_text_object(font_path: str, font_size: int, text: str, text_color: tuple, anti_aliasing: bool, is_bold: bool = False) -> dict:
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

def render_text(text_infos: dict, surface: pygame.Surface) -> pygame.Surface:
    """
    Takes a dictionary containing the text's font, width, height and the top left tuple;
    A tuple containing the top left position of the text;
    A surface;
    And 
    Render that on that surface
    """

    surface.blit(text_infos["text"], text_infos["top_left"])

    return surface

def render_a_button(surface: pygame.Surface, button_name: str, top_left_y: int, screen_infos: dict, mouse_pos: tuple, is_back_button: bool = False) -> dict:
    """
    This function will render a button text on the main menu,
    and will return the button informations.
    """
    button_infos = get_text_object(FONT_PATH, scaled_down(198), button_name, BLACK, True)
    postit_color = POSTIT_BLUE

    if is_back_button:
        postit = pygame.Rect(scaled_down(120), scaled_down(1680), scaled_down(480), scaled_down(360))
        postit_color = POSTIT_RED
        pygame.draw.rect(surface, postit_color, postit)
        top_left_x = scaled_down(120) + (scaled_down(480) - button_infos["width"])//2
        top_left_y = scaled_down(1680) + (scaled_down(360) - button_infos["height"])//2

    else:
        top_left_x = (screen_infos["width"]//2) - (button_infos["width"]//2)

    button_infos["top_left"] = (top_left_x, top_left_y)
    button_infos["rect"] = pygame.Rect(top_left_x, top_left_y,
                                        button_infos["width"], button_infos["height"]
                        )
    if button_infos["rect"].collidepoint(mouse_pos):
        button_infos = get_text_object(FONT_PATH, scaled_down(198), button_name, BLACK, True, True)
        button_infos["top_left"] = (top_left_x, top_left_y)
        button_infos["rect"] = pygame.Rect(top_left_x, top_left_y,
                                            button_infos["width"], button_infos["height"]
                            )
    else:
        # Erasing the bold text first
        pygame.draw.rect(surface, postit_color, button_infos["rect"])

    render_text(button_infos, surface)

    return button_infos

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
    
    x_score_text_infos = get_text_object(FONT_PATH, scaled_down(198), "X's SCORE:", BLACK, True)
    x_score_text_infos["top_left"] = (scaled_down(246), scaled_down(30))
    render_text(x_score_text_infos, surface)
    
    x_score_num_text = get_text_object(FONT_PATH, scaled_down(168), x_score_str, x_score_color, True)
    x_score_num_text["top_left"] = (scaled_down(246), scaled_down(192))
    render_text(x_score_num_text, surface)

    o_score_text_infos = get_text_object(FONT_PATH, scaled_down(198), "O's SCORE:", BLACK, True)
    o_score_text_infos["top_left"] = (screen_infos["width"] - (x_score_text_infos["width"] + scaled_down(246)), scaled_down(30))
    render_text(o_score_text_infos, surface)
    
    o_score_num_text = get_text_object(FONT_PATH, scaled_down(168), o_score_str, o_score_color, True)
    o_score_num_text["top_left"] = (screen_infos["width"] - (x_score_text_infos["width"] + scaled_down(246)), scaled_down(192))
    render_text(o_score_num_text, surface)
    
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
    
    turn_text_infos = get_text_object(FONT_PATH, scaled_down(198), turn + " TURN", BLACK, True)
    turn_text_x_pos = (screen_infos["width"] - (turn_text_infos["width"]+60))//2
    turn_text_y_pos = scaled_down(90)
    turn_text_infos["top_left"] = (turn_text_x_pos, turn_text_y_pos)

    turn_postit = pygame.Rect((turn_text_x_pos - 48), (turn_text_y_pos - 24), (turn_text_infos["width"] + 96), (turn_text_infos["height"] + 48))

    pygame.draw.rect(surface, postit_color, turn_postit)

    render_text(turn_text_infos, surface)

    return None

def won_msg(surface: pygame.Surface, winner: str, screen_infos: dict, msg_size: int, tie: bool = False):
    """
    Will render a won message at the center of the screen.
    """
    msg = f"{winner[0]} HAS WON"

    if winner == "X's":
        postit_color = POSTIT_RED
    elif winner == "O's":
        postit_color = POSTIT_BLUE
    else:
        postit_color = RED
        msg = winner

    won_msg = get_text_object(FONT_PATH, msg_size, msg, BLACK, True)
    won_msg_x, won_msg_y = (screen_infos["width"] - won_msg["width"])//2, (screen_infos["height"] - won_msg["height"])//2
    won_msg["top_left"] = (won_msg_x, won_msg_y)

    msg_postit_w = won_msg["width"] + scaled_down(48)
    msg_postit_h = won_msg["height"] + scaled_down(36)
    msg_postit_x, msg_postit_y = won_msg_x - scaled_down(48//2), won_msg_y - scaled_down(36//2)

    msg_postit = pygame.Rect(msg_postit_x, msg_postit_y, msg_postit_w, msg_postit_h)

    pygame.draw.rect(surface, postit_color, msg_postit)
    render_text(won_msg, surface)