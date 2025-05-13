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
        self.__board_a = [[10, 20, 30, 40], [40, 30, 10, 10], [30, 40, 20, 20], [20, 10, 40, 30]]
        self.__board_b = [[30, 20, 10, 40], [40, 20, 10, 30], [10, 40, 30, 20], [20, 30, 40, 10]]
        self.__board_c = [[30, 20, 40, 10], [20, 30, 20, 40], [10, 40, 10, 30], [40, 30, 10, 20]]
        self.__board_d = [[10, 20, 30, 40], [40, 20, 10, 10], [20, 30, 40, 30], [30, 40, 10, 20]]
        self.__board_corner = [50,50,50,50]
        self.__selected_board = self.board_fusion(self.__board_a, self.__board_b, self.__board_c, self.__board_d)
        
        
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
        return self.board_fusion(self.__board_a, self.__board_b, self.__board_c, self.__board_d)
    
    def get_board_corner(self):
        return self.__board_corner
    
    def get_selected_board(self, selected_board):
        print(f"Attempting to get selected board: {selected_board}")  # Pour le débogage
        if selected_board == 1 or selected_board == 'A':
            self.__selected_board = self.__board_a
            print("caca")
        elif selected_board == 2 or selected_board == 'B':
            self.__selected_board = self.__board_b
        elif selected_board == 3 or selected_board == 'C':
            self.__selected_board = self.__board_c
        elif selected_board == 4 or selected_board == 'D':
            self.__selected_board = self.__board_d
        else:
            raise ValueError(f"Invalid board selection: {selected_board}")
        return self.__selected_board
    
    def set_selected_board(self,selected_board, new_board):
        if selected_board == 1 or selected_board == 'A':
            self.__board_a = new_board
        elif selected_board == 2 or selected_board == 'B': 
            self.__board_b = new_board
        elif selected_board == 3 or selected_board == 'C':
            self.__board_c = new_board
        elif selected_board == 4 or selected_board == 'D':
            self.__board_d = new_board
        else:
            raise ValueError("Invalid board selection")
        
    def shiftboard(self,board1,board2):
        board1,board2 = board2,board1
        return board1,board2
        
        

    def rotate_right(self, board):
        # Effectuer la rotation vers la droite
        rotated_board = [list(reversed(col)) for col in zip(*board)]  # Rotation 90°
        return rotated_board

    def rotate_left(board):
        return [[board[j][3 - i] for j in range(4)] for i in range(4)]

    def rotate_side(board):
        return [[board[3 - i][3 - j] for j in range(4)] for i in range(4)]

