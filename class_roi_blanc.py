import pygame

class roi_blanc(pygame.sprite.Sprite):

    value = 10
    color = "blanc"
    name = 'roi'
    can_rock_blanc = True

    def __init__(self,game,x,y,num):

        super().__init__()
        
        self.__game = game
        self.all_pos = list()
        
        self.image = pygame.image.load('assets/roi_blanc.png')
        self.rect = self.image.get_rect()
        self.rect.x = x*100
        self.rect.y = y*100

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

        if -1 < x-1 < 8 and -1 < y-1 < 8:
            if not(plateau[(x-1,y-1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-1,y-1,check_echec)

        if -1 < x < 8 and -1 < y-1 < 8:   
            if not(plateau[(x,y-1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x,y-1,check_echec)

        if -1 < x+1 < 8 and -1 < y-1 < 8:    
            if not(plateau[(x+1,y-1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+1,y-1,check_echec)

        if -1 < x+1 < 8 and -1 < y < 8:    
            if not(plateau[(x+1,y)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+1,y,check_echec)

        if -1 < x+1 < 8 and -1 < y+1 < 8:    
            if not(plateau[(x+1,y+1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x+1,y+1,check_echec)

        if -1 < x < 8 and -1 < y+1 < 8:    
            if not(plateau[(x,y+1)] in game.all_id_blancs):
               self.ajoute_pos(plateau.copy(),x,y,x,y+1,check_echec)

        if -1 < x-1 < 8 and -1 < y+1 < 8:    
            if not(plateau[(x-1,y+1)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-1,y+1,check_echec)

        if -1 < x-1 < 8 and -1 < y < 8:   
            if not(plateau[(x-1,y)] in game.all_id_blancs):
                self.ajoute_pos(plateau.copy(),x,y,x-1,y,check_echec)

        
        if plateau.sens == 1:
            if y == 7 and x == 4 and plateau[(x+1,y)] == 0 and plateau[(x+2,y)] == 0 and plateau[(x+3,y)] == 1 and self.can_rock_blanc:
                plateau_copy_1 = plateau.copy()
                plateau_copy_1[(x+1,y)] = plateau[(x,y)]
                del plateau_copy_1[(x+1,y)]
                if check_echec:
                    if not(game.is_echec(0,plateau_copy_1)):
                        plateau_copy_2 = plateau.copy()
                        plateau_copy_2[(x+2,y)] = plateau[(x,y)]
                        del plateau_copy_2[(x+2,y)]
                        if not(game.is_echec(0,plateau_copy_2)):
                            self.all_pos.append((x+2,y))
                else:
                    self.all_pos.append((x+2,y))
                    
                        
            if y == 7 and x == 4 and plateau[(x-1,y)] == 0 and plateau[(x-2,y)] == 0 and plateau[(x-3,y)] == 0 and plateau[(x-4,y)] == 8 and self.can_rock_blanc:
                plateau_copy_1 = plateau.copy()
                plateau_copy_1[(x-1,y)] = plateau[(x,y)]
                del plateau_copy_1[(x-1,y)]
                if check_echec:
                    if not(game.is_echec(0,plateau_copy_1)):
                        plateau_copy_2 = plateau.copy()
                        plateau_copy_2[(x-2,y)] = plateau[(x,y)]
                        del plateau_copy_2[(x-2,y)]
                        if not(game.is_echec(0,plateau_copy_2)):
                            plateau_copy_3 = plateau.copy()
                            plateau_copy_3[(x-3,y)] = plateau[(x,y)]
                            del plateau_copy_3[(x-3,y)]
                            if not(game.is_echec(0,plateau_copy_3)):
                                self.all_pos.append((x-2,y))
                else:
                    self.all_pos.append((x-2,y))
        else:
            if y == 0 and x == 3 and plateau[(x-1,y)] == 0 and plateau[(x-2,y)] == 0 and plateau[(x-3,y)] == 1 and self.can_rock_blanc:
                plateau_copy_1 = plateau.copy()
                plateau_copy_1[(x-1,y)] = plateau[(x,y)]
                del plateau_copy_1[(x-1,y)]
                if check_echec:
                    if not(game.is_echec(0,plateau_copy_1)):
                        plateau_copy_2 = plateau.copy()
                        plateau_copy_2[(x-2,y)] = plateau[(x,y)]
                        del plateau_copy_2[(x-2,y)]
                        if not(game.is_echec(0,plateau_copy_2)):
                            self.all_pos.append((x-2,y))
                else:
                    self.all_pos.append((x-2,y))
            if y == 0 and x == 3 and plateau[(x+1,y)] == 0 and plateau[(x+2,y)] == 0 and plateau[(x+3,y)] == 0 and plateau[(x+4,y)] == 8 and self.can_rock_blanc:
                plateau_copy_1 = plateau.copy()
                plateau_copy_1[(x+1,y)] = plateau[(x,y)]
                del plateau_copy_1[(x+1,y)]
                if check_echec:
                    if not(game.is_echec(0,plateau_copy_1)):
                        plateau_copy_2 = plateau.copy()
                        plateau_copy_2[(x+2,y)] = plateau[(x,y)]
                        del plateau_copy_2[(x+2,y)]
                        if not(game.is_echec(0,plateau_copy_2)):
                            plateau_copy_3 = plateau.copy()
                            plateau_copy_3[(x+3,y)] = plateau[(x,y)]
                            del plateau_copy_3[(x+3,y)]
                            if not(game.is_echec(0,plateau_copy_3)):
                                self.all_pos.append((x+2,y))
                else:
                    self.all_pos.append((x+2,y))
            

        return self.all_pos

    def remove(self):
        game = self.get_game()
        game.all_blancs_alive.remove(self)
