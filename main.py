import pygame
import sys
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *
from scripts.rendering_scripts import render_paper, render_new_game_button, render_credits_button, render_quit_button, render_back_button, render_x_and_o_scores, render_turn

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

        while True:

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_back_button(self.game_surface, mouse_pos)

            render_x_and_o_scores(self.game_surface, self.screen_infos, x_score, o_score)

            render_turn(self.screen_infos, self.game_surface, player_turn)


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