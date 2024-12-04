import pygame
from scripts.display_resolution import scaled_down
from scripts.constants import *

class Game_board:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface

    def render_square(self, color: tuple, top_left_x: int, top_left_y: int, width_and_height: int) -> None:
        """
        Render a square on the screen.
        WARNING: Integer values (except for color values) should be scaled down.
        """
        top_left = (top_left_x, top_left_y)

        # Top horizontal border
        pygame.draw.line(
            self.surface,
            color,
            top_left,
            (top_left_x + width_and_height, top_left_y),
            scaled_down(LINE_SIZE)
        )
        # Left vertical border
        pygame.draw.line(
            self.surface,
            color,
            top_left,
            (top_left_x, top_left_y + width_and_height),
            scaled_down(LINE_SIZE)
        )
        # Down horizontal border
        pygame.draw.line(
            self.surface,
            color,
            (top_left_x, top_left_y + width_and_height),
            (top_left_x + width_and_height, top_left_y + width_and_height),
            scaled_down(LINE_SIZE)
        )
        # Right vertical border
        pygame.draw.line(
            self.surface,
            color,
            (top_left_x + width_and_height, top_left_y),
            (top_left_x + width_and_height, top_left_y + width_and_height),
            scaled_down(LINE_SIZE)
        )

        return None


    def render(self, color: tuple) -> None:
        """
        Takes a surface, a color and render the 3X3 game board on the screen.
        """

        # Rendering the square
        self.render_square(color, scaled_down(GAMEBOARD_TOP_LEFT_X), scaled_down(GAMEBOARD_TOP_LEFT_Y), scaled_down(GAMEBOARD_W_AND_H))

        # Rendering the vertical inside lines (from left to right)
        pygame.draw.line(
            self.surface,
            color,
            (scaled_down(GAMEBOARD_TOP_LEFT_X + INSIDE_RECT_W_AND_H), scaled_down(GAMEBOARD_TOP_LEFT_Y)),
            (scaled_down(GAMEBOARD_TOP_LEFT_X + INSIDE_RECT_W_AND_H), scaled_down(GAMEBOARD_TOP_LEFT_Y + GAMEBOARD_W_AND_H)),
            scaled_down(LINE_SIZE)
        )
        pygame.draw.line(
            self.surface,
            color,
            (scaled_down(GAMEBOARD_TOP_LEFT_X + (INSIDE_RECT_W_AND_H*2)), scaled_down(GAMEBOARD_TOP_LEFT_Y)),
            (scaled_down(GAMEBOARD_TOP_LEFT_X + (INSIDE_RECT_W_AND_H*2)), scaled_down(GAMEBOARD_TOP_LEFT_Y + GAMEBOARD_W_AND_H)),
            scaled_down(LINE_SIZE)
        )
        # Rendering the horizontal inside lines (starting from the top one)
        pygame.draw.line(
            self.surface,
            color,
            (scaled_down(GAMEBOARD_TOP_LEFT_X), scaled_down(GAMEBOARD_TOP_LEFT_Y + INSIDE_RECT_W_AND_H)),
            (scaled_down(GAMEBOARD_TOP_LEFT_X + GAMEBOARD_W_AND_H), scaled_down(GAMEBOARD_TOP_LEFT_Y + INSIDE_RECT_W_AND_H)),
            scaled_down(LINE_SIZE)
        )
        pygame.draw.line(
            self.surface,
            color,
            (scaled_down(GAMEBOARD_TOP_LEFT_X), scaled_down(GAMEBOARD_TOP_LEFT_Y + (INSIDE_RECT_W_AND_H*2))),
            (scaled_down(GAMEBOARD_TOP_LEFT_X + GAMEBOARD_W_AND_H), scaled_down(GAMEBOARD_TOP_LEFT_Y + (INSIDE_RECT_W_AND_H*2))),
            scaled_down(LINE_SIZE)
        )

        return None
    
    def get_board_matrix(self) -> dict:
        """
        Return a dictionary containing all the 9X9 rects objects.
        The keys are the a tuple of row and column (row: int, column: int).
        The values are a tuple (Rect: pygame.Rect, (top_left_x, top_left_y): tuple)
        """

        top_left_x = scaled_down(GAMEBOARD_TOP_LEFT_X)
        top_left_y = scaled_down(GAMEBOARD_TOP_LEFT_Y)

        game_board_rects = dict()
        

        for row in range(3):
            if row == 0:
                top_left_y = scaled_down(GAMEBOARD_TOP_LEFT_Y)
            elif row == 1:
                top_left_y = scaled_down(GAMEBOARD_TOP_LEFT_Y) + scaled_down(INSIDE_RECT_W_AND_H)
            else:
                top_left_y = scaled_down(GAMEBOARD_TOP_LEFT_Y) + (scaled_down(INSIDE_RECT_W_AND_H)*2)
            for column in range(3):
                if column == 0:
                    top_left_x = scaled_down(GAMEBOARD_TOP_LEFT_X)
                elif column == 1:
                    top_left_x = scaled_down(GAMEBOARD_TOP_LEFT_X) + scaled_down(INSIDE_RECT_W_AND_H)
                else:
                    top_left_x = scaled_down(GAMEBOARD_TOP_LEFT_X) + (scaled_down(INSIDE_RECT_W_AND_H)*2)
                
                rect_key = "(" + str(row) + ", " + str(column) + ")"
                game_board_rects[rect_key] = (pygame.Rect(top_left_x, top_left_y, scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)), (top_left_x, top_left_y))

        return game_board_rects
    
    
    def get_colliding_rect(self, mouse_pos) -> tuple:
        """
        Return the string index of the rect object that's colliding with the mouse and its top left.
        Return None if the mouse is not colliding with any gameboard's rect.
        """
        board_matrix = self.get_board_matrix()
        for key in board_matrix:
            rect = board_matrix[key][0]
            top_left_x, top_left_y = board_matrix[key][1]

            if rect.collidepoint(mouse_pos):
                self.render_square(RED, top_left_x, top_left_y, scaled_down(INSIDE_RECT_W_AND_H))
                return (key, (top_left_x, top_left_y))

        return None
