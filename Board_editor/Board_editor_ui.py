import pygame
import sys

from Board_editor.Board import Board

class Board_editor_ui:
    def __init__(self, width=800, height=600, title="Katarenga"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.buttons = [
            {"label": "Square A", "rect": pygame.Rect(300, 50, 200, 50), "color": (70, 130, 180)},
            {"label": "Square B", "rect": pygame.Rect(300, 150, 200, 50), "color": (60, 179, 113)},
            {"label": "Square C", "rect": pygame.Rect(300, 250, 200, 50), "color": (220, 20, 60)},
            {"label": "Square D", "rect": pygame.Rect(300, 350, 200, 50), "color": (255, 140, 0)},
            {"label": "Moves Squares", "rect": pygame.Rect(300, 450, 200, 50), "color": (186, 85, 211)},
            {"label": "Go to menu", "rect": pygame.Rect(300, 450, 200, 50), "color": (234,182,118)}
        ]
        
        self.font = pygame.font.SysFont(None, 36)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def handle_click(self, position):
            #gestion of the redirection for the different buttons
            for button in self.buttons:
                if button["rect"].collidepoint(position):
                    label = button["label"]
                    board_obj = Board()
                    if label == "Katarenga":
                        print("Lauching Katarenga...")
                    elif label == "Congress":
                        print("Lauching Congress...")
                    elif label == "Isolation":
                        print("Lauching Isolation...")
                    elif label == "Board Editor":
                        print("Lauching the Board Editor...")
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
    app = Board_editor_ui()
    app.run()
