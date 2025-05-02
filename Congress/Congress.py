from Player.Player import Player
from Board_editor.Board import Board

obj = Player
def starting_pos_congress(board: Board):

    fused = board.get_fused_board()

    #pieces player 1

    fused[0][1] +=   1
    fused[0][4] +=   1 
    fused[1][7] +=   1
    fused[4][7] +=   1
    fused[7][6] +=   1
    fused[7][3] +=   1 
    fused[3][0] +=   1 
    fused[6][0] +=   1

    #pieces player 2

    fused[1][0] +=   2
    fused[4][0] +=   2
    fused[6][7] +=   2
    fused[3][7] +=   2
    fused[0][3] +=   2
    fused[0][6] +=   2
    fused[7][4] +=   2
    fused[7][1] +=   2


#ca marche pas je check plus tard
#check if pieces are orthogonal or not

# def victory_conditions_congress(player: Player, board: Board, fused):
#     for i in range(8):
#         for j in range(8):
#             if fused[i][0] == fused[j][0] or fused[i][1] == fused[j][1] or fused[1][i] == fused[1][j] or fused[0][i] == fused[0][j]:
#                 return True #orthogonal
#             else: 
#                 return False #No orthogonal