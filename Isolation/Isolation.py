from Player.Player import Player
from Board_editor.Board import Board

obj = Player


def victory_conditions_isolation(player: Player, board: Board):
    
    remaining_p1 = player.get_pieces_remaining_p1()
    remaining_p2 = player.get_pieces_remaining_p2()

    if remaining_p1 == 0 and remaining_p2 == 1:
        return "Joueur 2 a gagné"
    elif remaining_p1 == 1 and remaining_p2 == 0:
        return "Joueur 1 a gagné"
    elif remaining_p1 == 0 and remaining_p2 == 0:
        return "Match nul"
    else:
        return "La partie continue"