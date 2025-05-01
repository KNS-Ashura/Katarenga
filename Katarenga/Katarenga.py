from Player import Joueur
from Board import Board

def victory_conditions(joueur: Joueur, board: Board):
    # verifie le nbr de piece d'un joueur
    if joueur.get_pieces_remaining_p1() <= 0:
        print(f"{joueur.get_p_2_name()} gagne avec full capture")
        return True
    if joueur.get_pieces_remaining_p2() <= 0:
        print(f"{joueur.get_p_1_name()} gagne avec full capture")
        return True

    # verifie si un pion est sur un corner
    for val in board.get_board_corner():
        if val == 51:
            print(f"{joueur.get_p_1_name()} pions dans un corner")
            return True
        elif val == 52:
            print(f"{joueur.get_p_2_name()} pions dans un corner")
            return True

    return False