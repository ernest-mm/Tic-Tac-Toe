import pygame
import sys
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *
from scripts.rendering_scripts import *
from scripts.sounds import load_sound, play_sound
from scripts.game_board import Game_board

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        self.screen_infos = get_screen_infos(DEVELOPMENT_RESOLUTION)
        self.screen = pygame.display.set_mode(self.screen_infos["size"], pygame.SCALED + pygame.NOFRAME)
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        self.ICON = pygame.image.load("src/assets/images/ICON.png")
        pygame.display.set_icon(self.ICON)

        # Creating the game surface
        self.game_surface = pygame.Surface(self.screen_infos["size"])

        # Creating the game board
        self.game_board = Game_board(self.game_surface)

        # Initial position of the 'X' and 'O' text surfaces
        self.x_text_x_pos = None
        self.x_text_y_pos = None

        self.o_text_x_pos = None
        self.o_text_y_pos = None

        # Creating a matrix that will store the results
        self.results = [
            [str(), str(), str()],
            [str(), str(), str()],
            [str(), str(), str()]
        ]

        # Creating a set that will stores boxes that have been clicked on
        self.clicked_on = set()

        # Initial turn
        self.player_turn = "X's"

        # Loading the sounds
        try:
            self.paper_sound = load_sound(PAPER_SOUND_PATH)
            self.pen_writing_sound = load_sound(PEN_WRITING_SOUND_PATH)
        except (
            load_sound(PAPER_SOUND_PATH) is None
            or load_sound(PEN_WRITING_SOUND_PATH) is None
        ):
            raise TypeError("Failed to load pygame.mixer.Sound") 

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
    
    def reset_game(self):
        """
        Reset the game without impacting the score.
        """
        # Clearing the screen
        render_paper(self.game_surface, self.screen_infos)

        # Going back to the initial position of the text surfaces
        self.x_text_x_pos = None
        self.x_text_y_pos = None

        self.o_text_x_pos = None
        self.o_text_y_pos = None

        # Clearing the matrix that will store the results
        self.results = [
            [str(), str(), str()],
            [str(), str(), str()],
            [str(), str(), str()]
        ]

        # Clearing the set that will stores boxes that have been clicked on
        self.clicked_on = set()

        # Restarting the turn
        self.player_turn = "X's"

    
    def main_menu(self):
        render_paper(self.game_surface, self.screen_infos)

        # Creating the main menu sticky notes backgroung

        background = pygame.image.load("src/assets/images/"+self.screen_infos["resolution"]+"_main_menu.png")
        self.game_surface.blit(background, (0, 0))

        while True:
            # Creating the text buttons

            mouse_pos = pygame.mouse.get_pos()

            new_game_button_infos = render_a_button(self.game_surface, "NEW GAME", scaled_down(1248), self.screen_infos, mouse_pos)
            quit_button_infos = render_a_button(self.game_surface, "QUIT", scaled_down(1584), self.screen_infos, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Checking what button has been clicked on
                    if new_game_button_infos["rect"].collidepoint(mouse_pos):
                        # Playing the paper sound
                        play_sound(self.paper_sound)
                        return Game.run(self)
                    if quit_button_infos["rect"].collidepoint(mouse_pos):
                        # Playing the paper sound
                        play_sound(self.paper_sound)
                        # Waiting for the sound to finnish playing
                        pygame.time.delay(831)
                        pygame.quit()
                        sys.exit()

            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        # Reseting the game to earase previous values
        self.reset_game()  

        render_paper(self.game_surface, self.screen_infos)

        x_score = 0
        o_score = 0

        # Creating 'X' and 'O' text and their surfaces
        x_text = get_text_object(FONT_PATH, scaled_down(INSIDE_RECT_W_AND_H), "X", POSTIT_RED, True)
        o_text = get_text_object(FONT_PATH, scaled_down(INSIDE_RECT_W_AND_H), "O", POSTIT_BLUE, True)

        # Creating text's surfaces
        x_text_surf = pygame.Surface((scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)), pygame.SRCALPHA)
        o_text_surf = pygame.Surface((scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)), pygame.SRCALPHA)

        # Bliting the text to their surfaces
        x_text_surf.blit(pygame.transform.scale(x_text["text"], (scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H))), (0, 0))
        o_text_surf.blit(pygame.transform.scale(o_text["text"], (scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H))), (0, 0))
        

        while True:
            # Blitting the 'X' and 'O' Surfaces to the screen
            if self.x_text_x_pos != None and self.x_text_y_pos != None:
                self.game_surface.blit(x_text_surf, (self.x_text_x_pos, self.x_text_y_pos))
            if self.o_text_x_pos != None and self.o_text_y_pos != None:
                self.game_surface.blit(o_text_surf, (self.o_text_x_pos, self.o_text_y_pos))

            # Checking if the game has been won or if it's tied
            winner = self.check_for_winner()

            if (winner != None) or (len(self.clicked_on) >= 9):
                if winner:
                    if winner == "X's":
                        x_score += 1
                    elif winner == "O's":
                        o_score += 1
                else:
                    winner = "THE GAME IS A TIE!"

                # Playing the paper sound
                play_sound(self.paper_sound)
                    
                # Winner's or tie message
                won_msg(self.game_surface, winner, self.screen_infos, scaled_down(408))

                self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
                pygame.display.update()
                self.clock.tick(FPS)

                pygame.time.delay(3000)  # Winner's message lasts for 3 seconds 

                # Reseting the game
                self.reset_game()         

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_a_button(self.game_surface, "BACK", 0, self.screen_infos, mouse_pos, True)

            render_x_and_o_scores(self.game_surface, self.screen_infos, x_score, o_score)

            render_turn(self.screen_infos, self.game_surface, self.player_turn)

            self.game_board.render(BLACK)

            colliding_box = self.game_board.get_colliding_rect(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Checking if the back button has been clicked on
                    if back_button_infos["rect"].collidepoint(mouse_pos):
                        # Playing the paper sound
                        play_sound(self.paper_sound)
                        return Game.main_menu(self)
                    # Checking if a box from the game board has been clicked on
                    if colliding_box is not None:
                        if self.player_turn == "X's":
                            if colliding_box[0] in self.clicked_on:
                                pass
                            else:
                                self.x_text_x_pos = colliding_box[1][0]
                                self.x_text_y_pos = colliding_box[1][1]
                                self.clicked_on.add(colliding_box[0])

                                # Playing the pen writing sound
                                play_sound(self.pen_writing_sound)

                                # Putting the choice into the results' matrix
                                row = int(colliding_box[0][1])
                                column = int(colliding_box[0][4])
                                self.results[row][column] = self.player_turn

                                self.player_turn = "O's"
                        else:
                            if colliding_box[0] in self.clicked_on:
                                pass
                            else:
                                self.o_text_x_pos = colliding_box[1][0]
                                self.o_text_y_pos = colliding_box[1][1]
                                self.clicked_on.add(colliding_box[0])

                                # Playing the pen writing sound
                                play_sound(self.pen_writing_sound)

                                # Putting the choice into the results' matrix
                                row = int(colliding_box[0][1])
                                column = int(colliding_box[0][4])
                                self.results[row][column] = self.player_turn

                                self.player_turn = "X's"
            
            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.main_menu()