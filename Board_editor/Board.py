class Board:
    
    #in the following list:
    #the number 1 = blue
    #the number 2 = green
    #the number 3 = yellow
    #the number 4 = red 
    
    
    #then the second number represent the player 
    #0 if there is no player on the case
    #1 for player 1
    #2 for player 2
    
    #exemple:
    # red case with a pawn of player 1 = 41
    # red case with a pawn of player 2 = 42
    # yellow case with a pawn of player 1 = 31
    # red case with no player = 40
    
    
    #finally
    #the number 5 = a corner
    
    #exemple:
    #a corner with no pawn = 50
    #a corner with a pawn of player 1 = 51
               
    def __init__(self):
        self.__board = {
            1: [[10, 20, 30, 40], [40, 30, 10, 10], [30, 40, 20, 20], [20, 10, 40, 30]],
            2: [[30, 20, 10, 40], [40, 20, 10, 30], [10, 40, 30, 20], [20, 30, 40, 10]],
            3: [[30, 20, 40, 10], [20, 30, 20, 40], [10, 40, 10, 30], [40, 30, 10, 20]],
            4: [[10, 20, 30, 40], [40, 20, 10, 10], [20, 30, 40, 30], [30, 40, 10, 20]],
            "Corners": [50, 50, 50, 50]
        }

    def board_fusion(self, board1, board2, board3, board4):
        fused = [[0 for _ in range(8)] for _ in range(8)]
        for i in range(4):
            for j in range(4):
                fused[i][j] = board1[i][j]
                fused[i][j + 4] = board2[i][j]
                fused[i + 4][j] = board3[i][j]
                fused[i + 4][j + 4] = board4[i][j]
        return fused

    def get_fused_board(self):
        return self.board_fusion(
            self.__board[1],
            self.__board[2],
            self.__board[3],
            self.__board[4]
        )

    def get_board_corner(self):
        return self.__board["Corners"]

    def get_selected_board(self, selected_board):
        if selected_board:
            return self.__board[selected_board]
        else:
            raise ValueError(f"Invalid board selection: {selected_board}")

    def set_selected_board(self, selected_board, new_board):
        if selected_board:
            self.__board[selected_board] = new_board
        else:
            raise ValueError("Invalid board selection")

    def shiftboard(self, board1_id, board2_id):
        self.__board[board1_id], self.__board[board2_id] = self.__board[board2_id], self.__board[board1_id]

    def rotate_right(self, board):
        return [list(reversed(col)) for col in zip(*board)]

    def rotate_left(self, board):
        return [[board[j][3 - i] for j in range(4)] for i in range(4)]

    def rotate_side(self, board):
        return [[board[3 - i][3 - j] for j in range(4)] for i in range(4)]