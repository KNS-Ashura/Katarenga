import pygame
import sys

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
            {"label": "Katarenga", "rect": pygame.Rect(300, 150, 200, 50), "color": (70, 130, 180)},
            {"label": "Congress", "rect": pygame.Rect(300, 250, 200, 50), "color": (60, 179, 113)},
            {"label": "Isolation", "rect": pygame.Rect(300, 350, 200, 50), "color": (220, 20, 60)}
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event.pos)
                
    def handle_click(self, position):
        for button in self.buttons:
            if button["rect"].collidepoint(position):
                label = button["label"]
                if label == "Menu":
                    print("Redirection vers le menu...")
                    # Tu peux lancer une autre classe ici
                elif label == "Options":
                    print("Redirection vers les options...")
                elif label == "Quitter":
                    print("Fermeture...")
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
