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

        self.board = self.board_obj.get_selected_board(1)

        self.cell_size = 100
        self.grid_size = self.cell_size * 4  # 4x4 cells = 400 pixels

        # Title gestion
        self.title_font = pygame.font.SysFont(None, 48)
        self.title_surface = self.title_font.render("Square A", True, (255, 255, 255))
        self.title_rect = self.title_surface.get_rect(center=(self.__width // 2, 30))

        # Offsets for center board
        self.top_offset = self.title_rect.bottom + 20  # space under the title
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
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event.pos)

    def handle_click(self, position):
        x, y = position

        # Check if click is on the "Back" button
        if self.back_button_rect.collidepoint(x, y):
            self.running = False
            return

        # Check if click is on the "Save" button
        if self.save_button_rect.collidepoint(x, y):
            print("Save pressed")
            return

        # Check if click is within the board area
        if y < self.top_offset or x < self.left_offset:
            return

        col = (x - self.left_offset) // self.cell_size
        row = (y - self.top_offset) // self.cell_size

        if 0 <= row < 4 and 0 <= col < 4:
            value = self.board[row][col]
            color_code = value // 10

            print(f"Clicked cell ({row}, {col}): Value {value}, Color {color_code}")

            # Colors cycles
            current_color_code = self.board[row][col] // 10
            new_color_code = (current_color_code % 4) + 1
            self.board[row][col] = new_color_code * 10 + (self.board[row][col] % 10)

            print(f"Updated board: {self.board}")

    def draw(self):
        self.__screen.fill((30, 30, 30))

        # Print TITLE
        self.__screen.blit(self.title_surface, self.title_rect)

        # Draw Board
        for row in range(4):
            for col in range(4):
                rect = pygame.Rect(
                    col * self.cell_size + self.left_offset,
                    row * self.cell_size + self.top_offset,
                    self.cell_size,
                    self.cell_size
                )

                color = self.board_ui.get_color_from_board(self.board[row][col] // 10)
                pygame.draw.rect(self.__screen, color, rect)
                pygame.draw.rect(self.__screen, (255, 255, 255), rect, 1)

        # Draw "Back" button
        pygame.draw.rect(self.__screen, (70, 70, 70), self.back_button_rect)
        pygame.draw.rect(self.__screen, (255, 255, 255), self.back_button_rect, 2)
        back_text = self.button_font.render("Back", True, (255, 255, 255))
        self.__screen.blit(back_text, back_text.get_rect(center=self.back_button_rect.center))

        # Draw "Save" button
        pygame.draw.rect(self.__screen, (70, 70, 70), self.save_button_rect)
        pygame.draw.rect(self.__screen, (255, 255, 255), self.save_button_rect, 2)
        save_text = self.button_font.render("Save", True, (255, 255, 255))
        self.__screen.blit(save_text, save_text.get_rect(center=self.save_button_rect.center))

if __name__ == "__main__":
    app = Square_a_ui()
    app.run()
