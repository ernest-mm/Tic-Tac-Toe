import pygame
import sys
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *
from scripts.rendering_scripts import *
from scripts.game_board import Game_board

class Game:
    def __init__(self):
        pygame.init()

        self.screen_infos = get_screen_infos(DEVELOPMENT_RESOLUTION)
        self.screen = pygame.display.set_mode(self.screen_infos["size"], pygame.SCALED + pygame.FULLSCREEN + pygame.NOFRAME)
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        self.ICON = None
        # pygame.display.set_icon(self.ICON)

        # Creating the game surface
        self.game_surface = pygame.Surface(self.screen_infos["size"])

        # Creating the game board
        self.game_board = Game_board(self.game_surface)

        # Creating a matrix that will store the results
        self.results = [
            [str(), str(), str()],
            [str(), str(), str()],
            [str(), str(), str()]
        ]


    def check_for_winner(self):
        # Check all rows for a winner
        for row in self.results:
            if row[0] == row[1] == row[2] and row[0] != "":
                return row[0]  # Return "X's" or "O's" as the winner

        # Check all columns for a winner
        for col in range(3):
            if self.results[0][col] == self.results[1][col] == self.results[2][col] and self.results[0][col] != "":
                return self.results[0][col]  # Return "X's" or "O's" as the winner

        # Check diagonals for a winner
        if self.results[0][0] == self.results[1][1] == self.results[2][2] and self.results[0][0] != "":
            return self.results[0][0]  # Return "X's" or "O's" as the winner
        if self.results[0][2] == self.results[1][1] == self.results[2][0] and self.results[0][2] != "":
            return self.results[0][2]  # Return "X's" or "O's" as the winner

        # If no winner, return None
        return None

    
    def main_menu(self):
        render_paper(self.game_surface, self.screen_infos)

        # Creating the main menu sticky notes backgroung

        background = pygame.image.load("assets/images/"+self.screen_infos["resolution"]+"_main_menu.png")
        self.game_surface.blit(background, (0, 0))

        while True:
            # Creating the text buttons

            mouse_pos = pygame.mouse.get_pos()

            new_game_button_infos = render_a_button(self.game_surface, "NEW GAME", scaled_down(1164), self.screen_infos, mouse_pos)
            credits_button_infos = render_a_button(self.game_surface, "CREDITS", scaled_down(1416), self.screen_infos, mouse_pos)
            quit_button_infos = render_a_button(self.game_surface, "QUIT", scaled_down(1668), self.screen_infos, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Checking what button has been clicked on
                    if new_game_button_infos["rect"].collidepoint(mouse_pos):
                        return Game.run(self)
                    if credits_button_infos["rect"].collidepoint(mouse_pos):
                        return Game.credits_menu(self)
                    if quit_button_infos["rect"].collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        render_paper(self.game_surface, self.screen_infos)

        x_score = 0
        o_score = 0

        player_turn = "X's"

        # Creating 'X' and 'O' text and their surfaces
        x_text = get_text_object(FONT_PATH, scaled_down(INSIDE_RECT_W_AND_H), "X", POSTIT_RED, True)
        o_text = get_text_object(FONT_PATH, scaled_down(INSIDE_RECT_W_AND_H), "O", POSTIT_BLUE, True)

        # Creating text's surfaces
        x_text_surf = pygame.Surface((scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)), pygame.SRCALPHA)
        o_text_surf = pygame.Surface((scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)), pygame.SRCALPHA)

        # Bliting the text to their surfaces
        x_text_surf.blit(pygame.transform.scale(x_text["text"], (scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H))), (0, 0))
        o_text_surf.blit(pygame.transform.scale(o_text["text"], (scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H))), (0, 0))

        # Initial position of the text surfaces
        x_text_x_pos = None
        x_text_y_pos = None

        o_text_x_pos = None
        o_text_y_pos = None

        # Creating a set that will stores boxes that have been clicked on
        clicked_on = set()

        while True:
            # Checking if the game has been won
            winner = self.check_for_winner()

            if winner:
                if winner == "X's":
                    x_score += 1
                elif winner == "O's":
                    o_score += 1
                # Reset game logic (clear board, etc.)

                # Clearing the screen
                render_paper(self.game_surface, self.screen_infos)

                # Going back to the initial position of the text surfaces
                x_text_x_pos = None
                x_text_y_pos = None

                o_text_x_pos = None
                o_text_y_pos = None

                # Clearing a matrix that will store the results
                self.results = [
                    [str(), str(), str()],
                    [str(), str(), str()],
                    [str(), str(), str()]
                ]

                # Creating a set that will stores boxes that have been clicked on
                clicked_on = set()

                # Restarting the turn
                player_turn = "X's"          

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_a_button(self.game_surface, "BACK", 0, self.screen_infos, mouse_pos, True)

            render_x_and_o_scores(self.game_surface, self.screen_infos, x_score, o_score)

            render_turn(self.screen_infos, self.game_surface, player_turn)

            self.game_board.render(BLACK)

            # Blitting the 'X' and 'O' Surfaces to the screen
            if x_text_x_pos != None and x_text_y_pos != None:
                self.game_surface.blit(x_text_surf, (x_text_x_pos, x_text_y_pos))
            if o_text_x_pos != None and o_text_y_pos != None:
                self.game_surface.blit(o_text_surf, (o_text_x_pos, o_text_y_pos))

            colliding_box = self.game_board.get_colliding_rect(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Checking if the back button has been clicked on
                    if back_button_infos["rect"].collidepoint(mouse_pos):
                        return Game.main_menu(self)
                    # Checking if a box from the game board has been clicked on
                    if colliding_box is not None:
                        if player_turn == "X's":
                            if colliding_box[0] in clicked_on:
                                pass
                            else:
                                x_text_x_pos = colliding_box[1][0]
                                x_text_y_pos = colliding_box[1][1]
                                clicked_on.add(colliding_box[0])

                                # Putting the choice into the results' matrix
                                row = int(colliding_box[0][1])
                                column = int(colliding_box[0][4])
                                self.results[row][column] = player_turn

                                player_turn = "O's"
                        else:
                            if colliding_box[0] in clicked_on:
                                pass
                            else:
                                o_text_x_pos = colliding_box[1][0]
                                o_text_y_pos = colliding_box[1][1]
                                clicked_on.add(colliding_box[0])

                                # Putting the choice into the results' matrix
                                row = int(colliding_box[0][1])
                                column = int(colliding_box[0][4])
                                self.results[row][column] = player_turn

                                player_turn = "X's"


            
            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

    def credits_menu(self):
        render_paper(self.game_surface, self.screen_infos)

        while True:

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_a_button(self.game_surface, "BACK", 0, self.screen_infos, mouse_pos, True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Checking if the back button has been clicked on
                    if back_button_infos["rect"].collidepoint(mouse_pos):
                        return Game.main_menu(self)

            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)


game = Game()
game.main_menu()