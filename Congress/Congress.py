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


def check_isolated_pieces(board: Board, player_num):

    fused = board.get_fused_board()
    isolated_count = 0
    positions = []
    
    for i in range(8):
        for j in range(8):
            # Check if there is a pawn in a case
            if fused[i][j] % 10 == player_num:
                isolated = True
                
                #Si isolé return False
                # Check all directions
                # check on top
                if i > 0 and fused[i-1][j] % 10 == player_num:
                    isolated = False
                
                # Check bottom
                if i < 7 and fused[i+1][j] % 10 == player_num:
                    isolated = False
                
                # Check left
                if j > 0 and fused[i][j-1] % 10 == player_num:
                    isolated = False
                
                # Check right
                if j < 7 and fused[i][j+1] % 10 == player_num:
                    isolated = False
                
                if isolated:
                    isolated_count += 1
                    positions.append((i, j))
    
    return isolated_count, positions


def victory_conditions_congress(board: Board):
   
    isolated_p1, positions_p1 = check_isolated_pieces(board, 1)
    isolated_p2, positions_p2 = check_isolated_pieces(board, 2)
    
    if isolated_p1 == 0:
        return 1, "Joueur 1 a gagné - Tous ses pions sont connectés!"
    elif isolated_p2 == 0:
        return 2, "Joueur 2 a gagné - Tous ses pions sont connectés!"
    else:
        return None, f"La partie continue. Pions isolés: Joueur 1: {isolated_p1}, Joueur 2: {isolated_p2}"