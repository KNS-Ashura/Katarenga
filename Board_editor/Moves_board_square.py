import pygame
import sys

from Board_editor.Board import Board
from Board_editor.Board_ui import Board_ui

class Moves_board_square:
    def __init__(self, board_obj, width=640, height=640, title="Square 1234 Editor"):
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
            1: self.board_obj.get_selected_board(1),
            2: self.board_obj.get_selected_board(2),
            3: self.board_obj.get_selected_board(3),
            4: self.board_obj.get_selected_board(4)
        }

        self.cell_size = 57
        self.grid_size = self.cell_size * 8  # 8x8

        # Title setup
        self.title_font = pygame.font.SysFont(None, 48)
        self.title_surface = self.title_font.render("All Squares 1-2-3-4", True, (255, 255, 255))
        self.title_rect = self.title_surface.get_rect(center=(self.__width // 2, 30))

        # Offset to center the grid
        self.top_offset = self.title_rect.bottom + 20
        self.left_offset = (self.__width - self.grid_size) // 2

        # Buttons setup
        self.button_font = pygame.font.SysFont(None, 36)
        self.back_button_rect = pygame.Rect(20, self.__height - 60, 120, 40)
        self.save_button_rect = pygame.Rect(self.__width - 140, self.__height - 60, 120, 40)
        
        self.selected_board_key = None  # 1, 2, 3 ou 4
        self.registered_board = None  # Board object pour la case sélectionnée
        self.i = 0

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
            elif event.type == pygame.KEYDOWN:
                self.handle_key(event)

    def handle_click(self, position):
        x, y = position

        # Boutons
        if self.back_button_rect.collidepoint(x, y):
            print("Back button clicked")
            self.running = False
            return

        if self.save_button_rect.collidepoint(x, y):
            print("Save button clicked")
            self.board_obj.set_selected_board(1, self.boards[1])
            self.board_obj.set_selected_board(2, self.boards[2])
            self.board_obj.set_selected_board(3, self.boards[3])
            self.board_obj.set_selected_board(4, self.boards[4])
            return

        # Click dans la grille
        if y < self.top_offset or x < self.left_offset:
            return

        col = (x - self.left_offset) // self.cell_size
        row = (y - self.top_offset) // self.cell_size

        if 0 <= row < 8 and 0 <= col < 8:
            # Déterminer quel board est cliqué
            if row < 4 and col < 4:
                board_key = 1
                self.registered_board = self.boards[1]
                self.i = 1
                
            elif row < 4 and col >= 4:
                board_key = 2
                self.registered_board = self.boards[2]
                self.i = 2
                
            elif row >= 4 and col < 4:
                board_key = 3
                self.registered_board = self.boards[3]
                self.i = 3
                
            else:
                board_key = 4
                self.registered_board = self.boards[4]
                self.i = 4

            # Mise à jour de la valeur de la case
            self.selected_board_key = board_key
            print(f"Selected board: {board_key}")  # Debugging message

    def handle_key(self, event):
        if self.selected_board_key:
            print(f"Selected board key: {self.selected_board_key}")  # Pour vérifier la valeur
            selected_board = self.board_obj.get_selected_board(self.selected_board_key)
            print(f"Selected board before rotation: {selected_board}")
            
            # Appliquer la rotation à ce tableau
            rotated_board = self.board_obj.rotate_right(selected_board)
            print(f"Rotated board: {rotated_board}")
            
            # Mettre à jour le tableau sélectionné avec la nouvelle rotation
            self.board_obj.set_selected_board(self.selected_board_key, rotated_board)

            # Après avoir mis à jour le tableau, actualise la grille
            self.boards[self.selected_board_key] = rotated_board

    def draw(self):
        self.__screen.fill((30, 30, 30))
        self.__screen.blit(self.title_surface, self.title_rect)

        # Dessiner les boards mis à jour
        for row in range(8):
            for col in range(8):
                # Déterminer à quel board cela correspond
                if row < 4 and col < 4:
                    board = self.boards[1]
                    board_row, board_col = row, col
                elif row < 4 and col >= 4:
                    board = self.boards[2]
                    board_row, board_col = row, col - 4
                elif row >= 4 and col < 4:
                    board = self.boards[3]
                    board_row, board_col = row - 4, col
                else:
                    board = self.boards[4]
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

        # Surlignage du board sélectionné
        if self.selected_board_key:
            highlight_color = (100, 0, 0)
            thickness = 4

            if self.selected_board_key == 1:
                top_left = (self.left_offset, self.top_offset)
            elif self.selected_board_key == 2:
                top_left = (self.left_offset + 4 * self.cell_size, self.top_offset)
            elif self.selected_board_key == 3:
                top_left = (self.left_offset, self.top_offset + 4 * self.cell_size)
            elif self.selected_board_key == 4:
                top_left = (self.left_offset + 4 * self.cell_size, self.top_offset + 4 * self.cell_size)

            rect = pygame.Rect(top_left[0], top_left[1], 4 * self.cell_size, 4 * self.cell_size)
            pygame.draw.rect(self.__screen, highlight_color, rect, thickness)

        # Dessiner les boutons
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
    app = Moves_board_square(board_obj)
    app.run()