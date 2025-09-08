import pygame

class pion_blanc(pygame.sprite.Sprite):

    value = 1
    color = "blanc"
    name = 'pion'

    def __init__(self,game,x,y,num):
        super().__init__()
        
        self.__game = game
        self.all_pos = list()
        
        self.image = pygame.image.load('assets/pion_blanc.png')
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
        if (new_pos in self.recup_all_pos(anc_pos,plateau)):
            if (new_pos[0] == anc_pos[0]-1) and (new_pos[1] == anc_pos[1]-1) and (plateau[(new_pos)] == 0):
                return True,"prise_passant_g_b"
            elif (new_pos[0] == anc_pos[0]+1) and (new_pos[1] == anc_pos[1]-1) and (plateau[(new_pos)] == 0):
                return True,"prise_passant_d_b"
            else:
                return True,plateau[(new_pos)]
        else:
            return False,plateau[(new_pos)]

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

        if plateau.sens == 1:
            if y != 0:
                if plateau[(x,y-1)] == 0:
                    self.ajoute_pos(plateau.copy(),x,y,x,y-1,check_echec)
                    if y == 6 and plateau[(x,y-2)] == 0:
                        self.ajoute_pos(plateau.copy(),x,y,x,y-2,check_echec)
                    
            if x != 7 and y != 0:
                if plateau[(x+1,y-1)] in game.all_id_noirs:
                    self.ajoute_pos(plateau.copy(),x,y,x+1,y-1,check_echec)
                if not(check_echec):
                    self.ajoute_pos(plateau.copy(),x,y,x+1,y-1,check_echec)
            if x != 0 and y != 0:
                if plateau[(x-1,y-1)] in game.all_id_noirs:
                    self.ajoute_pos(plateau.copy(),x,y,x-1,y-1,check_echec)
                if not(check_echec):
                    self.ajoute_pos(plateau.copy(),x,y,x-1,y-1,check_echec)
            if y==3:
                if x != 7:
                    if game.dico_piece_id[plateau[(x+1,y)]] in game.all_pions_noirs and plateau[(x+1,y-1)] == 0:
                        echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-1].copy()
                        last_echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-2].copy()

                        pion_move = echequier[(x+1,y)]
                        echequier[(x+1,y)] = 0
                        echequier[(x+1,y-2)] = pion_move

                        est_la_mm = True

                        for i in range(8):
                           for j in range(8):
                               if echequier[(i,j)] != last_echequier[(i,j)]:
                                   est_la_mm = False

                        if est_la_mm:
                            self.ajoute_pos(plateau.copy(),x,y,x+1,y-1,check_echec)
                            
                if x != 0:
                    if game.dico_piece_id[plateau[(x-1,y)]] in game.all_pions_noirs and plateau[(x-1,y-1)] == 0:
                        echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-1].copy()
                        last_echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-2].copy()

                        pion_move = echequier[(x-1,y)]
                        echequier[(x-1,y)] = 0
                        echequier[(x-1,y-2)] = pion_move

                        est_la_mm = True

                        for i in range(8):
                           for j in range(8):
                               if echequier[(i,j)] != last_echequier[(i,j)]:
                                   est_la_mm = False

                        if est_la_mm:
                            self.ajoute_pos(plateau.copy(),x,y,x-1,y-1,check_echec)
        else:
            if y != 7:
                if plateau[(x,y+1)] == 0:
                    self.ajoute_pos(plateau.copy(),x,y,x,y+1,check_echec)
                    if y == 1 and plateau[(x,y+2)] == 0:
                        self.ajoute_pos(plateau.copy(),x,y,x,y+2,check_echec)
            if x != 7 and y != 7:
                if plateau[(x+1,y+1)] in game.all_id_noirs:
                    self.ajoute_pos(plateau.copy(),x,y,x+1,y+1,check_echec)
                if not(check_echec):
                    self.ajoute_pos(plateau.copy(),x,y,x+1,y+1,check_echec)
            if x != 0 and y != 7:
                if plateau[(x-1,y+1)] in game.all_id_noirs:
                    self.ajoute_pos(plateau.copy(),x,y,x-1,y+1,check_echec)
                if not(check_echec):
                    self.ajoute_pos(plateau.copy(),x,y,x-1,y+1,check_echec)
            if y==4:
                if x != 7:
                    if game.dico_piece_id[plateau[(x+1,y)]] in game.all_pions_noirs and plateau[(x+1,y+1)] == 0:
                        echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-1].copy()
                        last_echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-2].copy()

                        pion_move = echequier[(x+1,y)]
                        echequier[(x+1,y)] = 0
                        echequier[(x+1,y+2)] = pion_move

                        est_la_mm = True

                        for i in range(8):
                           for j in range(8):
                               if echequier[(i,j)] != last_echequier[(i,j)]:
                                   est_la_mm = False

                        if est_la_mm:
                            self.ajoute_pos(plateau.copy(),x,y,x+1,y+1,check_echec)
                            
                if x != 0:
                    if game.dico_piece_id[plateau[(x-1,y)]] in game.all_pions_noirs and plateau[(x-1,y+1)] == 0:
                        echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-1].copy()
                        last_echequier = game.list_all_move_in_game[len(game.list_all_move_in_game)-2].copy()

                        pion_move = echequier[(x-1,y)]
                        echequier[(x-1,y)] = 0
                        echequier[(x-1,y+2)] = pion_move

                        est_la_mm = True

                        for i in range(8):
                           for j in range(8):
                               if echequier[(i,j)] != last_echequier[(i,j)]:
                                   est_la_mm = False

                        if est_la_mm:
                            self.ajoute_pos(plateau.copy(),x,y,x-1,y+1,check_echec)
            

        return self.all_pos

    def remove(self):
        game = self.get_game()
        game.all_blancs_alive.remove(self)
        
