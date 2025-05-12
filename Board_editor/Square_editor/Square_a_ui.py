import pygame
import sys

from Board_editor.Board import Board
from Board_editor.Board_ui import Board_ui

class Square_a_ui:
    def __init__(self, width=800, height=600, title="Square A Editor"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True
        
        
        self.board_obj = Board()
        self.board_ui = Board_ui()
        
        
        self.board = self.board_obj._Board__board_a
        
        
        self.cell_size = 100
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

        self.color_count = [0] * len(self.colors)
        self.color_limit = 4
        self.color_limit = False

    def run(self):
        while self.running:
            self.handle_events()
            
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
        x, y = position
        col = x // self.cell_size
        row = y // self.cell_size

        if 0 <= row < 4 and 0 <= col < 4:
            value = self.board[row][col]
            color_code = value // 10
            
            print(f"Clicked cell ({row}, {col}): Value {value}, Color {color_code}")
            
            # Cycle through the colors when the cell is clicked
            current_color_code = self.board[row][col] // 10
            new_color_code = (current_color_code + 1) % len(self.colors)
            self.board[row][col] = new_color_code * 10 + (self.board[row][col] % 10)
            
    
    def draw(self):
        self.__screen.fill((30, 30, 30))

        for row in range(4):
            for col in range(4):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
            
                color = self.board_ui.get_color_from_board(self.board[row][col] // 10)         
                pygame.draw.rect(self.__screen, color, rect)
                pygame.draw.rect(self.__screen, (255, 255, 255), rect, 1)
                


if __name__ == "__main__":
    app = Square_a_ui()
    app.run()