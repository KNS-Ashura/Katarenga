class Joueur:
    def __init__(self, pieces_remaining_p1, pieces_remaining_p2):
        
        self.__player_1 = 1
        self.__player_2 = 2
        
        self.__player_1_name = ""
        self.__player_2_name = ""
        
        self.__active_player = 1
    
        self.__pieces_remaining_p1 = pieces_remaining_p1
        self.__pieces_remaining_p2 = pieces_remaining_p2


#PLAYER 1

    def get_pieces_remaining_p1(self):
        return self.__pieces_remaining_p1
    
    def set_pieces_remaining_p1(self):
        self.__pieces_remaining_p1 = 8

    def get_p_1(self):
        return self.__player_1

    def delete_piece_p1(self):
        self.__pieces_remaining_p1 -= 1

    def get_p_1_name(self):
        return self.__player_1_name

    def set_p_1_name(self,new_value):
        self.__player_1_name = new_value

#PLAYER 2
    def get_pieces_remaining_p2(self):
        return self.__pieces_remaining_p2
    

    def set_pieces_remaining_p2(self):
        self.__pieces_remaining_p2 = 8


    def get_p_2(self):
        return self.__player_2
    
    def get_p_2_name(self):
        return self.__player_2_name
    
    def set_p_2_name(self,new_value):
        self.__player_2_name = new_value

    def delete_piece_p2(self):
        self.__pieces_remaining_p2 -= 1


#Gestion player
    def Change_player(self):
        if self.__active_player == 1:
            self.__active_player = 2
        else:
            self.__active_player = 1
            
    def get_board_corners(self):
        return self.__board_corner
        
    

        
    
        
