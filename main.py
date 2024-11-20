import pygame
import sys
from scripts.display_resolution import get_screen_infos, scaled_down
from scripts.constants import *
from scripts.rendering_scripts import render_paper

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

        pygame.font.init()
        font = pygame.font.Font("assets/fonts/PatrickHand-Regular.ttf", scaled_down(198))
        text = font.render("NEW GAME", True, BLACK)
        text_w, text_h = text.get_size()
        text_top_left = ((self.screen_infos["width"]//2)- text_w//2, scaled_down(1164))
        self.game_surface.blit(text, text_top_left)

        text = font.render("CREDITS", True, BLACK)
        text_w, text_h = text.get_size()
        text_top_left = ((self.screen_infos["width"]//2)- text_w//2, scaled_down(1416))
        self.game_surface.blit(text, text_top_left)

        text = font.render("QUIT", True, BLACK)
        text_w, text_h = text.get_size()
        text_top_left = ((self.screen_infos["width"]//2)- text_w//2, scaled_down(1668))
        self.game_surface.blit(text, text_top_left)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(pygame.transform.scale(self.game_surface, self.screen_infos["size"]), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)


game = Game()
game.main_menu()
# def mainMenu():
#     GAMEWINDOW.fill((0, 0, 0))
#     # Test BG image:
#     TESTBG = pygame.image.load("testBG.png").convert()
#     GAMEWINDOW.blit(TESTBG, (0, 0))

#     # Buttons
#     NEWGAMEBUTTON = pygame.Rect(640, 450, 640, 90)
#     OPTIONSBUTTON = pygame.Rect(640, 570, 640, 90)
#     CREDITSBUTTON = pygame.Rect(640, 690, 640, 90)
#     QUITBUTTON = pygame.Rect(640, 810, 640, 90)

#     # The gameState variable will help us see which menu the program should be in
#     gameState = None

#     running = True

#     while running:
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), NEWGAMEBUTTON)
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), OPTIONSBUTTON)
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), CREDITSBUTTON)
#         pygame.draw.rect(GAMEWINDOW, (255, 0, 0), QUITBUTTON)

#         # Checking if the mouse is on our buttons

#         mousePos = pygame.mouse.get_pos()

#         if NEWGAMEBUTTON.collidepoint(mousePos):
#            pygame.draw.rect(GAMEWINDOW, (135, 0, 0), NEWGAMEBUTTON)
#         if OPTIONSBUTTON.collidepoint(mousePos):
#             pygame.draw.rect(GAMEWINDOW, (135, 0, 0), OPTIONSBUTTON)
#         if CREDITSBUTTON.collidepoint(mousePos):
#             pygame.draw.rect(GAMEWINDOW, (135, 0, 0), CREDITSBUTTON)
#         if QUITBUTTON.collidepoint(mousePos):
#             pygame.draw.rect(GAMEWINDOW, (135, 0, 0), QUITBUTTON)

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == MOUSEBUTTONDOWN:
#                 # Checking what button has been clicked on
#                 if NEWGAMEBUTTON.collidepoint(mousePos):
#                     gameState = game()
#                     running = False
#                 elif OPTIONSBUTTON.collidepoint(mousePos):
#                     gameState = options()
#                     running = False
#                 elif CREDITSBUTTON.collidepoint(mousePos):
#                     gameState = credits()
#                     running = False
#                 elif QUITBUTTON.collidepoint(mousePos):
#                     pygame.quit()
#                     sys.exit()

#         pygame.display.update()
    
#     return gameState()

# def game():
#     while True:
#         GAMEWINDOW.fill("black")
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# def options():
#     while True:
#         GAMEWINDOW.fill("black")
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# def credits():
#     while True:
#         GAMEWINDOW.fill("black")
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#         pygame.display.update()

# if __name__ == '__main__':
#     mainMenu()