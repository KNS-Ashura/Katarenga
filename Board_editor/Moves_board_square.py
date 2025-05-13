import pygame
import sys

from Board_editor.Board import Board
from Board_editor.Board_ui import Board_ui

class Square_all_ui:
    def __init__(self, board_obj, width=800, height=850, title="Square ABCD Editor"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.board_obj = board_obj
        self.board_ui = Board_ui()

        # Get the 4 boards
        self.boards = {
            'A': self.board_obj.get_selected_board(1),
            'B': self.board_obj.get_selected_board(2),
            'C': self.board_obj.get_selected_board(3),
            'D': self.board_obj.get_selected_board(4)
        }

        self.cell_size = 80
        self.grid_size = self.cell_size * 8  # 8x8

        # Title setup
        self.title_font = pygame.font.SysFont(None, 48)
        self.title_surface = self.title_font.render("All Squares A-B-C-D", True, (255, 255, 255))
        self.title_rect = self.title_surface.get_rect(center=(self.__width // 2, 30))

        # Offset to center the grid
        self.top_offset = self.title_rect.bottom + 20
        self.left_offset = (self.__width - self.grid_size) // 2

        # Buttons setup
        self.button_font = pygame.font.SysFont(None, 36)
        self.back_button_rect = pygame.Rect(20, self.__height - 60, 120, 40)
        self.save_button_rect = pygame.Rect(self.__width - 140, self.__height - 60, 120, 40)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event.pos)

    def handle_click(self, position):
        x, y = position

        # Boutons
        if self.back_button_rect.collidepoint(x, y):
            self.running = False
            return

        if self.save_button_rect.collidepoint(x, y):
            print("Save pressed")
            self.board_obj.set_selected_board(1, self.boards['A'])
            self.board_obj.set_selected_board(2, self.boards['B'])
            self.board_obj.set_selected_board(3, self.boards['C'])
            self.board_obj.set_selected_board(4, self.boards['D'])
            return

        # Click dans la grille
        if y < self.top_offset or x < self.left_offset:
            return

        col = (x - self.left_offset) // self.cell_size
        row = (y - self.top_offset) // self.cell_size

        if 0 <= row < 8 and 0 <= col < 8:
            # Déterminer quel board est cliqué
            if row < 4 and col < 4:
                board_key = 'A'
                board_row, board_col = row, col
            elif row < 4 and col >= 4:
                board_key = 'B'
                board_row, board_col = row, col - 4
            elif row >= 4 and col < 4:
                board_key = 'C'
                board_row, board_col = row - 4, col
            else:
                board_key = 'D'
                board_row, board_col = row - 4, col - 4

            value = self.boards[board_key][board_row][board_col]
            current_color = value // 10
            new_color = (current_color % 4) + 1
            self.boards[board_key][board_row][board_col] = new_color * 10 + (value % 10)

    def draw(self):
        self.__screen.fill((30, 30, 30))
        self.__screen.blit(self.title_surface, self.title_rect)

        for row in range(8):
            for col in range(8):
                # Déterminer à quel board cela correspond
                if row < 4 and col < 4:
                    board = self.boards['A']
                    board_row, board_col = row, col
                elif row < 4 and col >= 4:
                    board = self.boards['B']
                    board_row, board_col = row, col - 4
                elif row >= 4 and col < 4:
                    board = self.boards['C']
                    board_row, board_col = row - 4, col
                else:
                    board = self.boards['D']
                    board_row, board_col = row - 4, col - 4

                rect = pygame.Rect(
                    col * self.cell_size + self.left_offset,
                    row * self.cell_size + self.top_offset,
                    self.cell_size,
                    self.cell_size
                )

                color = self.board_ui.get_color_from_board(board[board_row][board_col] // 10)
                pygame.draw.rect(self.__screen, color, rect)
                pygame.draw.rect(self.__screen, (255, 255, 255), rect, 1)

        # Boutons
        pygame.draw.rect(self.__screen, (70, 70, 70), self.back_button_rect)
        pygame.draw.rect(self.__screen, (255, 255, 255), self.back_button_rect, 2)
        back_text = self.button_font.render("Back", True, (255, 255, 255))
        self.__screen.blit(back_text, back_text.get_rect(center=self.back_button_rect.center))

        pygame.draw.rect(self.__screen, (70, 70, 70), self.save_button_rect)
        pygame.draw.rect(self.__screen, (255, 255, 255), self.save_button_rect, 2)
        save_text = self.button_font.render("Save", True, (255, 255, 255))
        self.__screen.blit(save_text, save_text.get_rect(center=self.save_button_rect.center))

if __name__ == "__main__":
    board_obj = Board()
    app = Square_all_ui(board_obj)
    app.run()