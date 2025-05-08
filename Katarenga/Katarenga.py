from Player.Player import Player
from Board_editor.Board import Board

class Katarenga:

    def victory_conditions(player: Player, board: Board):
        # check the number of pieces for a player
        if player.get_pieces_remaining_p1() <= 0:
            print(f"{player.get_p_2_name()} gagne avec full capture")
            return True
        if player.get_pieces_remaining_p2() <= 0:
            print(f"{player.get_p_1_name()} gagne avec full capture")
            return True

        # check if a pawn is in a corner
        for val in board.get_board_corner():
            if val == 51:
                print(f"{player.get_p_1_name()} pions dans un corner")
                return True
            elif val == 52:
                print(f"{player.get_p_2_name()} pions dans un corner")
                return True

        return False


    def place_pawn(player: Player, board):
        fused = board

        # Pawns from player 2 (TOP)
        for col in range(8):
            if col % 2 == 0:
                player.fused[0][col] = (player.fused[0][col] // 10) * 10 + 2
            else:
                player.fused[1][col] = (player.fused[1][col] // 10) * 10 + 2

        # Pawns from player 1 (BOTTOM)
        for col in range(8):
            if col % 2 == 1:
                player.fused[6][col] = (player.fused[6][col] // 10) * 10 + 1
            else:
                player.fused[7][col] = (player.fused[7][col] // 10) * 10 + 1

        return fused

