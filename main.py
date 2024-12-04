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
    
    def main_menu(self):
        render_paper(self.game_surface, self.screen_infos)

        # Creating the main menu sticky notes backgroung

        background = pygame.image.load("assets/images/"+self.screen_infos["resolution"]+"_main_menu.png")
        self.game_surface.blit(background, (0, 0))

        while True:
            # Creating the text buttons

            mouse_pos = pygame.mouse.get_pos()

            new_game_button_infos = render_new_game_button(self.game_surface, self.screen_infos, mouse_pos)
            credits_button_infos = render_credits_button(self.game_surface, self.screen_infos, mouse_pos)
            quit_button_infos = render_quit_button(self.game_surface, self.screen_infos, mouse_pos)

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

        # Rendering 'X' and 'O' text on surfaces to be put at positions that are off the screen
        x_text = buttons_text(FONT_PATH, scaled_down(INSIDE_RECT_W_AND_H), "X", POSTIT_RED, True)
        o_text = buttons_text(FONT_PATH, scaled_down(INSIDE_RECT_W_AND_H), "O", POSTIT_BLUE, True)

        x_text_x_pos = scaled_down(6000000)
        x_text_y_pos = scaled_down(6000000)

        o_text_x_pos = scaled_down(6000000)
        o_text_y_pos = scaled_down(6000000)

        x_text_surf = pygame.Surface((scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)))
        o_text_surf = pygame.Surface((scaled_down(INSIDE_RECT_W_AND_H), scaled_down(INSIDE_RECT_W_AND_H)))

        while True:

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_back_button(self.game_surface, mouse_pos)

            render_x_and_o_scores(self.game_surface, self.screen_infos, x_score, o_score)

            render_turn(self.screen_infos, self.game_surface, player_turn)

            self.game_board.render(BLACK)

            colliding_box = self.game_board.get_colliding_rect(mouse_pos)

            # Blitting the 'X' and 'O' text to their Surfaces and bliting them to the screen

            x_text_surf.blit(x_text["text"], (0, 0))
            o_text_surf.blit(o_text["text"], (0, 0))

            self.game_surface.blit(x_text_surf, (x_text_x_pos, x_text_y_pos))
            self.game_surface.blit(o_text_surf, (o_text_x_pos, o_text_y_pos))

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
                            x_text_x_pos = colliding_box[1][0]
                            x_text_y_pos = colliding_box[1][1]

            
            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

    def credits_menu(self):
        render_paper(self.game_surface, self.screen_infos)

        while True:

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_back_button(self.game_surface, mouse_pos)

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