class Joueur:
    def __init__(self, couleur, position_depart, nb_pieces):
        self.__couleur = couleur
        self.__position_depart = position_depart
        self.__pieces_restantes = nb_pieces

    def get_couleur(self):
        return self.__couleur

    def get_position_depart(self):
        return self.__position_depart

    def get_nb_pieces(self):
        return self.__pieces_restantes

    def supprimer_une_piece(self):
        if self.__pieces_restantes > 0:
            self.__pieces_restantes -= 1


class Katarenga:
    def __init__(self, n):
        self.n = n

        
        self.__joueurs = [
            Joueur("blue", (0, 0), n**2 // 4),
            Joueur("red", (n - 1, n - 1), n**2 // 4)
        ]
        
        
        self.__joueur_actif_index = 0
        self.__joueur_actif = self.__joueurs[self.__joueur_actif_index]

    def get_joueur_actif(self):
        return self.__joueur_actif

    def get_joueur_actif_index(self):
        return self.__joueur_actif_index

    def get_joueur_inactif(self):
        return self.__joueurs[1 - self.__joueur_actif_index]

    def set_joueur_actif(self, joueur_index):
        self.__joueur_actif_index = joueur_index
        self.__joueur_actif = self.__joueurs[joueur_index]

    def changer_joueur(self):
        self.__joueur_actif_index = 1 - self.__joueur_actif_index
        self.__joueur_actif = self.__joueurs[self.__joueur_actif_index]