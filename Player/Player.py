class Joueur:
    def __init__(self):
        
        self.__player_1 = 1
        self.__player_2 = 2
        
        self.__player_1_name = ""
        self.__player_2_name = ""
        
        self.__active_player = 1
        
    def get_p_1(self):
        return self.__player_1
    
    def get_p_2(self):
        return self.__player_2
    
    def get_p_1_name(self):
        return self.__player_1_name
    
    def get_p_2_name(self):
        return self.__player_2_name
    
    def Change_player(self):
        if self.__active_player == 1:
            self.__active_player = 2
        else:
            self.__active_player = 1
            
    def set_p_1_name(self,new_value):
        self.__player_1_name = new_value
        
    def set_p_2_name(self,new_value):
        self.__player_2_name = new_value

        
    
        
