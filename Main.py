import pygame
import sys
from Player.Player import Player
from Katarenga.Katarenga import Katarenga
from Katarenga.Katarenga_ui import Katarenga_ui
from Board_editor.Board import Board
from Board_editor.Board_ui import Board_ui
from Board_editor.Board_editor_ui import Board_editor_ui
from Congress.Congress_ui import Congress_ui
from Isolation.Isolation_ui import Isolation_ui



class Main_menu:
    def __init__(self, width=800, height=600, title="Katarenga"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True
        
        #ajout des boutons pour acceder au differents modes de jeux
        
        self.buttons = [
            {"label": "Katarenga", "rect": pygame.Rect(300, 50, 200, 50), "color": (70, 130, 180)},
            {"label": "Congress", "rect": pygame.Rect(300, 150, 200, 50), "color": (60, 179, 113)},
            {"label": "Isolation", "rect": pygame.Rect(300, 250, 200, 50), "color": (220, 20, 60)},
            {"label": "Board Editor", "rect": pygame.Rect(300, 350, 200, 50), "color": (255, 140, 0)},
            {"label": "Leave Game", "rect": pygame.Rect(300, 450, 200, 50), "color": (186, 85, 211)}
        ]

        self.font = pygame.font.SysFont(None, 36)

    def run(self):
        #main loop of the interface
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        #fonction for the gestions of the inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event.pos)
                
    def handle_click(self, position):
            #gestion of the redirection for the different buttons
            for button in self.buttons:
                if button["rect"].collidepoint(position):
                    label = button["label"]
                    board_obj = Board()
                    if label == "Katarenga":
                        print("Lauching Katarenga...")
                        player = Player(8,8)  
                        board_ui_obj = Board_ui()
                        katarenga = Katarenga(player)            # crée l'objet Board
                        game = Katarenga_ui(board_obj,board_ui_obj,katarenga)       # crée le jeu Katarenga
                        game.run()                        # lance le jeu
                    elif label == "Congress":
                        print("Lauching Congress...")
                        game = Congress_ui(board_obj)
                        game.run()
                    elif label == "Isolation":
                        print("Lauching Isolation...")
                        game = Isolation_ui(board_obj)
                        game.run()
                    elif label == "Board Editor":
                        print("Lauching the Board Editor...")
                        game = Board_editor_ui(board_obj)
                        game.run()
                    elif label == "Leave Game":
                        print("Leaving the Game...")
                        self.running = False

    def update(self):
        pass

    def draw(self):
        self.__screen.fill((30, 30, 30))
        for button in self.buttons:
            pygame.draw.rect(self.__screen, button["color"], button["rect"])
            self.draw_text(button["label"], button["rect"])
        
    def draw_text(self, text, rect):
        txt_surface = self.font.render(text, True, (255, 255, 255))
        txt_rect = txt_surface.get_rect(center=rect.center)
        self.__screen.blit(txt_surface, txt_rect)

if __name__ == "__main__":
    app = Main_menu()
    app.run()
