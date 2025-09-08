import pygame

class cavalier_blanc(pygame.sprite.Sprite):

    value = 3
    color = "blanc"
    name = "cavalier"

    def __init__(self,game,x,y,num):

        super().__init__()
        
        self.__game = game
        self.all_pos = []
        
        self.image = pygame.image.load('assets/cavalier_blanc.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.__id = num

    def get_game(self):
        return self.__game
    def get_id(self):
        return self.__id
    def get_pos(self):
        return (self.rect.x//100,self.rect.y//100)
        
    def set_pos(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def veref_pos(self,anc_pos,new_pos,plateau):
        game = self.get_game()
        plateau = game.get_echequier()
        return (new_pos in self.recup_all_pos(anc_pos,plateau),plateau[(new_pos)])

    def ajoute_pos(self,plateau,x,y,new_x,new_y,check_echec):
        game = self.get_game()
        plateau[(new_x,new_y)] = plateau[(x,y)]
        del plateau[(x,y)]
        if check_echec:
            if not(game.is_echec(0,plateau)):
                self.all_pos.append((new_x,new_y))
        else:
            self.all_pos.append((new_x,new_y))
        
    def recup_all_pos(self,pos,plateau,check_echec = True):
        x,y = pos
        game = self.get_game()
        self.all_pos = []
        if -1 < x+1 < 8 and -1 < y+2 < 8:
            if not(plateau[(x+1,y+2)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+1,y+2,check_echec)
        if -1 < x-1 < 8 and -1 < y+2 < 8:
            if not(plateau[(x-1,y+2)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-1,y+2,check_echec)
        if -1 < x-2 < 8 and -1 < y+1 < 8:
            if not(plateau[(x-2,y+1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-2,y+1,check_echec)
        if -1 < x-2 < 8 and -1 < y-1 < 8:
            if not(plateau[(x-2,y-1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-2,y-1,check_echec)
        if -1 < x-1 < 8 and -1 < y-2 < 8:
            if not(plateau[(x-1,y-2)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-1,y-2,check_echec)
        if -1 < x+1 < 8 and -1 < y-2 < 8:
            if not(plateau[(x+1,y-2)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+1,y-2,check_echec)
        if -1 < x+2 < 8 and -1 < y-1 < 8:
            if not(plateau[(x+2,y-1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+2,y-1,check_echec)
        if -1 < x+2 < 8 and -1 < y+1 < 8:
            if not(plateau[(x+2,y+1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+2,y+1,check_echec)

        return self.all_pos

    def remove(self):
        game = self.get_game()
        game.all_blancs_alive.remove(self)
