class Katarenga:

    def __init__(self,player):
        self.player = player

    def victory_conditions(player, board):
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


    def place_pawn(self,board):
        for i in range(8):
            board[0][i] += 2
            board[7][i] += 1

