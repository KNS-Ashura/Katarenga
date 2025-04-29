class Board:
    def __init__(self):
        self.__board_a = [[1, 2, 3, 4], [4, 3, 1, 1], [3, 4, 2, 2], [2, 1, 4, 3]]
        self.__board_b = [[3, 2, 1, 4], [4, 2, 1, 3], [1, 4, 3, 2], [2, 3, 4, 1]]
        self.__board_c = [[3, 2, 4, 1], [2, 3, 2, 4], [1, 4, 1, 3], [4, 3, 1, 2]]
        self.__board_d = [[1, 2, 3, 4], [4, 2, 1, 1], [2, 3, 4, 3], [3, 4, 1, 2]]
        self.__board_corner = [0,0,0,0]

    def rotate_right(board):
        return [[board[3 - j][i] for j in range(4)] for i in range(4)]

    def rotate_left(board):
        return [[board[j][3 - i] for j in range(4)] for i in range(4)]

    def rotate_side(board):
        return [[board[3 - i][3 - j] for j in range(4)] for i in range(4)]

    def board_fusion(board1, board2, board3, board4):
        fused = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(4):
            for j in range(4):
                fused[i][j] = board1[i][j]
                fused[i][j + 4] = board2[i][j]
                fused[i + 4][j] = board3[i][j]
                fused[i + 4][j + 4] = board4[i][j]
        return fused

    def get_fused_board(self):
        return Board.board_fusion(self.__board_a, self.__board_b, self.__board_c, self.__board_d)
    
    def get_board_corner(self):
        return self.__board_corner