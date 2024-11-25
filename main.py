import pygame
import sys
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *
from scripts.rendering_scripts import render_paper, buttons_text, render_buttons_text, render_back_button

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
            # Creating the text buttons, checking if the mouse is hovering over them and rendering accordingly

            mouse_pos = pygame.mouse.get_pos()

            # New game button

            new_game_button_infos = buttons_text(FONT_PATH, scaled_down(198), "NEW GAME", BLACK, True)
            new_game_button_infos["top_left"] = ((self.screen_infos["width"]//2)- new_game_button_infos["width"]//2, scaled_down(1164))
            new_game_button_infos["rect"] = pygame.Rect(new_game_button_infos["top_left"][0], new_game_button_infos["top_left"][1],
                                                        new_game_button_infos["width"], new_game_button_infos["height"]
                                        )
            
            if new_game_button_infos["rect"].collidepoint(mouse_pos):
                new_game_button_infos = buttons_text(FONT_PATH, scaled_down(198), "NEW GAME", BLACK, True, True)
                new_game_button_infos["top_left"] = ((self.screen_infos["width"]//2)- new_game_button_infos["width"]//2, scaled_down(1164))
                new_game_button_infos["rect"] = pygame.Rect(new_game_button_infos["top_left"][0], new_game_button_infos["top_left"][1],
                                                        new_game_button_infos["width"], new_game_button_infos["height"]
                                        )
                render_buttons_text(new_game_button_infos, self.game_surface)
            else:
                # Erasing the bold text first
                pygame.draw.rect(self.game_surface, POSTIT_BLUE, new_game_button_infos["rect"])

                render_buttons_text(new_game_button_infos, self.game_surface)

            # Credits button

            credits_button_infos = buttons_text(FONT_PATH, scaled_down(198), "CREDITS", BLACK, True)
            credits_button_infos["top_left"] = ((self.screen_infos["width"]//2)- credits_button_infos["width"]//2, scaled_down(1416))
            credits_button_infos["rect"] = pygame.Rect(credits_button_infos["top_left"][0], credits_button_infos["top_left"][1],
                                                        credits_button_infos["width"], credits_button_infos["height"]
                                        )
            
            if credits_button_infos["rect"].collidepoint(mouse_pos):
                credits_button_infos = buttons_text(FONT_PATH, scaled_down(198), "CREDITS", BLACK, True, True)
                credits_button_infos["top_left"] = ((self.screen_infos["width"]//2)- credits_button_infos["width"]//2, scaled_down(1416))
                credits_button_infos["rect"] = pygame.Rect(credits_button_infos["top_left"][0], credits_button_infos["top_left"][1],
                                                        credits_button_infos["width"], credits_button_infos["height"]
                                        )
                render_buttons_text(credits_button_infos, self.game_surface)
            else:
                # Erasing the bold text first
                pygame.draw.rect(self.game_surface, POSTIT_BLUE, credits_button_infos["rect"])

                render_buttons_text(credits_button_infos, self.game_surface)

            # Quit button

            quit_button_infos = buttons_text(FONT_PATH, scaled_down(198), "QUIT", BLACK, True)
            quit_button_infos["top_left"] = ((self.screen_infos["width"]//2)- quit_button_infos["width"]//2, scaled_down(1668))
            quit_button_infos["rect"] = pygame.Rect(quit_button_infos["top_left"][0], quit_button_infos["top_left"][1],
                                                        quit_button_infos["width"], quit_button_infos["height"]
                                        )
            
            if quit_button_infos["rect"].collidepoint(mouse_pos):
                quit_button_infos = buttons_text(FONT_PATH, scaled_down(198), "QUIT", BLACK, True, True)
                quit_button_infos["top_left"] = ((self.screen_infos["width"]//2)- quit_button_infos["width"]//2, scaled_down(1668))
                quit_button_infos["rect"] = pygame.Rect(quit_button_infos["top_left"][0], quit_button_infos["top_left"][1],
                                                        quit_button_infos["width"], quit_button_infos["height"]
                                        )
                render_buttons_text(quit_button_infos, self.game_surface)
            else:
                # Erasing the bold text first
                pygame.draw.rect(self.game_surface, POSTIT_BLUE, quit_button_infos["rect"])

                render_buttons_text(quit_button_infos, self.game_surface)
            
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
        while True:

            mouse_pos = pygame.mouse.get_pos()

            back_button_infos = render_back_button(self.game_surface, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

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