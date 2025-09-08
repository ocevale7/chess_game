import pygame

class dame_blanc(pygame.sprite.Sprite):

    value = 9
    color = "blanc"
    name = 'dame'

    def __init__(self,game,x,y,num):

        super().__init__()
        
        self.__game = game
        self.all_pos = []
        
        self.image = pygame.image.load('assets/dame_blanche.png')
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

        for i in range(x+1,8):
            if plateau[(i,y)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,i,y,check_echec)
            elif plateau[(i,y)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,i,y,check_echec)
                break
            else:
                break

        for i in range(1,x+1):
            i = x-i
            if plateau[(i,y)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,i,y,check_echec)
            elif plateau[(i,y)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,i,y,check_echec)
                break
            else:
                break

        for i in range(y+1,8):
            if plateau[(x,i)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,x,i,check_echec)
            elif plateau[(x,i)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,x,i,check_echec)
                break
            else:
                break

        for i in range(1,y+1):
            i = y-i
            if plateau[(x,i)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,x,i,check_echec)
            elif plateau[(x,i)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,x,i,check_echec)
                break
            else:
                break

        diff_x = 8-x
        diff_y = 8-y
        if diff_x < diff_y:
            mini = diff_x
        else:
            mini = diff_y
        for i in range(1,mini):
            if plateau[(x+i,y+i)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,x+i,y+i,check_echec)
            elif plateau[(x+i,y+i)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,x+i,y+i,check_echec)
                break
            else:
                break
        diff_x = x + 1
        if diff_x < diff_y:
            mini = diff_x
        else:
            mini = diff_y
        for i in range(1,mini):
            if plateau[(x-i,y+i)] == 0:
               self.ajoute_pos(plateau.copy(),x,y,x-i,y+i,check_echec)
            elif plateau[(x-i,y+i)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,x-i,y+i,check_echec)
                break
            else:
                break
        diff_y = y + 1
        if diff_x < diff_y:
            mini = diff_x
        else:
            mini = diff_y
        for i in range(1,mini):
            if plateau[(x-i,y-i)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,x-i,y-i,check_echec)
            elif plateau[(x-i,y-i)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,x-i,y-i,check_echec)
                break
            else:
                break
        diff_x = 8-x
        if diff_x < diff_y:
            mini = diff_x
        else:
            mini = diff_y
        for i in range(1,mini):
            if plateau[(x+i,y-i)] == 0:
                self.ajoute_pos(plateau.copy(),x,y,x+i,y-i,check_echec)
            elif plateau[(x+i,y-i)] in game.all_id_noirs:
                self.ajoute_pos(plateau.copy(),x,y,x+i,y-i,check_echec)
                break
            else:
                break
        return self.all_pos

    def remove(self):
        game = self.get_game()
        game.all_blancs_alive.remove(self)
            
                    
