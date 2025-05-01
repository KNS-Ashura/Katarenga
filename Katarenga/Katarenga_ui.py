import pygame
import sys

from Board_editor import Board

class Katarenga_ui:
    def __init__(self, board_obj, width=640, height=640, title="Katarenga Board"):
        pygame.init()
        self.__width = width
        self.__height = height
        self.__title = title
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = board_obj.get_fused_board()
        self.cell_size = 60

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
        x, y = position
        col = x // self.cell_size
        row = y // self.cell_size
        if 0 <= row < 8 and 0 <= col < 8:
            #operation to find where the player's mouse clicked
            value = self.board[row][col]
            color_code = value // 10
            player_code = value % 10
            
            player_code = (player_code + 1) % 3
            self.board[row][col] = color_code * 10 + player_code

    def update(self):
        pass

    def draw(self):
        self.__screen.fill((30, 30, 30))
        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                color = self.get_color_from_code(self.board[row][col] // 10)
                pygame.draw.rect(self.__screen, color, rect)
                pygame.draw.rect(self.__screen, (255, 255, 255), rect, 1)
                player_code = self.board[row][col] % 10
                if player_code != 0:
                    self.draw_text(str(player_code), rect)

    def get_color_from_code(self, code):
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

    def draw_text(self, text, rect):
        font = pygame.font.SysFont(None, 24)
        txt_surface = font.render(text, True, (255, 255, 255))
        txt_rect = txt_surface.get_rect(center=rect.center)
        self.__screen.blit(txt_surface, txt_rect)


if __name__ == "__main__":
    board_obj = Board()
    app = Katarenga_ui(board_obj)
    app.run()