import pygame
import sys

from Katarenga.Katarenga import Katarenga
from Board_editor import Board
from Board_editor import Board_ui 
from Player.Player import Player

class Katarenga_ui:
    def __init__(self, board_obj, board_ui_obj, width=640, height=640, title="Katarenga Board"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = board_obj.get_fused_board()
        self.board_ui = board_ui_obj
        self.cell_size = 60
        self.copied_value = None

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.gameloop()
            self.draw()
            self.board_ui.draw_all_corners(self.__screen)
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
        offset_x = (self.__width - self.cell_size * 8) // 2
        offset_y = (self.__height - self.cell_size * 8) // 2

        col = (x - offset_x) // self.cell_size
        row = (y - offset_y) // self.cell_size

        if 0 <= row < 8 and 0 <= col < 8:
            value = self.board[row][col]
            color_code = value // 10
            player_code = value % 10

            self.copied_value = value
            print(f"Valeur copiée de la case ({row}, {col}) : {self.copied_value}")

            player_code = (player_code + 1) % 3
            self.board[row][col] = color_code * 10 + player_code
            self.update()
            
    def gameloop(self):
        Katarenga.place_pawn(Player(0,0), self.board)

    def update(self):
        self.draw()

    def draw(self):
        self.__screen.fill((30, 30, 30))
        offset_x = (self.__width - self.cell_size * 8) // 2
        offset_y = (self.__height - self.cell_size * 8) // 2

        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(
                    offset_x + col * self.cell_size,
                    offset_y + row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                color = self.board_ui.get_color_from_board(self.board[row][col] // 10)         
                pygame.draw.rect(self.__screen, color, rect)
                pygame.draw.rect(self.__screen, (255, 255, 255), rect, 1)
                player_code = self.board[row][col] % 10
                if player_code != 0:
                    self.draw_text(str(player_code), rect)
                    pygame.draw.circle(self.__screen, (255, 255, 255), rect.center, self.cell_size // 2 - 5)
                    
    def draw_text(self, text, rect):
        font = pygame.font.SysFont(None, 24)
        txt_surface = font.render(text, True, (255, 255, 255))
        txt_rect = txt_surface.get_rect(center=rect.center)
        self.__screen.blit(txt_surface, txt_rect)


if __name__ == "__main__":
    board_obj = Board()
    board_ui_obj = Board_ui()
    app = Katarenga_ui(board_obj,board_ui_obj)
    player = Player()
    app.run()