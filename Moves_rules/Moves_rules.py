class Moves_rules:
    def __init__(self, board):
        self.__board = board

    def yellow_case_move(self, x_start, y_start, x_end, y_end):
        dx, dy = x_end - x_start, y_end - y_start
        if abs(dx) != abs(dy): return False
        sx, sy = dx//abs(dx), dy//abs(dy)
        for i in range(1, abs(dx)):
            if self.__board[x_start + sx*i][y_start + sy*i]: return False
        d = self.__board[x_end][y_end]
        return d == 0 or d == 1

    def blue_case_move(self, x_start, y_start, x_end, y_end):
        if abs(x_end - x_start) > 1 or abs(y_end - y_start) > 1: return False
        return self.__board[x_end][y_end] == 0

    def green_case_move(self, x_start, y_start, x_end, y_end):
        dx, dy = x_end - x_start, y_end - y_start
        if (dx, dy) not in {(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)}:
            return False
        return self.__board[x_end][y_end] == 0

    def red_case_move(self, x_start, y_start, x_end, y_end):
        if x_start != x_end and y_start != y_end: return False
        dx, dy = x_end - x_start, y_end - y_start
        sx = 0 if dx == 0 else (1 if dx > 0 else -1)
        sy = 0 if dy == 0 else (1 if dy > 0 else -1)
        x, y = x_start + sx, y_start + sy
        while (x, y) != (x_end, y_end):
            if self.__board[x][y]: return False
            x += sx; y += sy
        d = self.__board[x_end][y_end]
        return d == 0 or d == 4
    
    def verify_move(self, case_color, x_start, y_start, x_end, y_end):
        couleur = case_color // 10
        if couleur == 1 :
            return self.blue_case_move(x_start, y_start, x_end, y_end)
        if couleur == 2 :
            return self.green_case_move(x_start, y_start, x_end, y_end)
        if couleur == 3 :
            return self.yellow_case_move(x_start, y_start, x_end, y_end)
        if couleur == 4 :
            return self.red_case_move(x_start, y_start, x_end, y_end)
        if couleur == 5 :
            return False