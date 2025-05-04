import pygame
import sys

class Board_ui:
    def __init__(self, width=800, height=600, title="Katarenga"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True

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

    def update(self):
        pass

    def draw(self):
        self.__screen.fill((30, 30, 30))

    def get_color_from_board(self, code):
        if code == 1:
            return (0, 0, 255)  
        elif code == 2:
            return (0, 255, 0)  
        elif code == 3:
            return (255, 255, 0)
        elif code == 4:
            return (255, 0, 0)  
        elif code == 5:
            return (128, 0, 128)
        else:
            return (50, 50, 50) 

if __name__ == "__main__":
    app = Board_ui()
    app.run()
