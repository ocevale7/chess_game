import pygame

from class_echequier import echequier

from fleches_help import Fleche_aide

from class_pion_blanc import pion_blanc
from class_pion_noir import pion_noir
from class_tour_noir import tour_noir
from class_tour_blanc import tour_blanc
from class_fou_blanc import fou_blanc
from class_fou_noir import fou_noir
from class_cavalier_blanc import cavalier_blanc
from class_cavalier_noir import cavalier_noir
from class_dame_blanc import dame_blanc
from class_dame_noir import dame_noir
from class_roi_blanc import roi_blanc
from class_roi_noir import roi_noir

from methode_echecs import *
from methode_tide import *

from class_bot import Bot

from aide import Aide

from random import randint

class Game():

    def __init__(self,profondeur,tourne_auto,edit,rapport):

        self.compteur = 0
        
        self.rapport = rapport

        self.echequier = echequier(edit)
        self.n_pieces = 32

        self.all_aides = pygame.sprite.Group()

        self.dico_piece_id = {0 : None}
        self.list_all_move_in_game = list()

        self.all_pieces_mortes = pygame.sprite.Group()

        self.all_pions_blancs = pygame.sprite.Group()
        self.all_tours_blancs = pygame.sprite.Group()
        self.all_cavaliers_blancs = pygame.sprite.Group()
        self.all_fous_blancs = pygame.sprite.Group()
        self.all_dames_blancs = pygame.sprite.Group()
        self.all_rois_blancs = pygame.sprite.Group()
        
        self.all_id_blancs = []
        
        self.all_pions_noirs = pygame.sprite.Group()
        self.all_tours_noirs = pygame.sprite.Group()
        self.all_cavaliers_noirs = pygame.sprite.Group()
        self.all_fous_noirs = pygame.sprite.Group()
        self.all_dames_noirs = pygame.sprite.Group()
        self.all_rois_noirs = pygame.sprite.Group()
        
        self.all_id_noirs = []
        
        self.all_noirs_alive = pygame.sprite.Group()
        self.all_blancs_alive = pygame.sprite.Group()
        
        if not(edit):
            for i in range(8):
                self.ajoute_pion_blanc(i,1,i+9)
            self.ajoute_tour_blanc(0,0,1)
            self.ajoute_tour_blanc(7,0,8)
            self.ajoute_fou_blanc(2,0,3)
            self.ajoute_fou_blanc(5,0,6)
            self.ajoute_cavalier_blanc(1,0,2)
            self.ajoute_cavalier_blanc(6,0,7)
            self.ajoute_dame_blanc(4,0,5)
            self.ajoute_roi_blanc(3,0,4)

            for i in range(8):
                self.ajoute_pion_noir(i,6,i+17)
            self.ajoute_tour_noir(0,7,25)
            self.ajoute_tour_noir(7,7,32)
            self.ajoute_fou_noir(2,7,27)
            self.ajoute_fou_noir(5,7,30)
            self.ajoute_cavalier_noir(1,7,26)
            self.ajoute_cavalier_noir(6,7,31)
            self.ajoute_dame_noir(4,7,29)
            self.ajoute_roi_noir(3,7,28)
            
            self.recup_all_alive()
            self.recup_all_id()      

        self.ordi_blanc = Bot(self,self.echequier,profondeur,0)
        self.ordi_noir = Bot(self,self.echequier,profondeur,1)

        self.echec_blanc = False
        self.echec_noir = False

        self.tour = 0
        self.pos_in_list = 0
        self.running = 0
        self.dico_mort = {"pb" : 0,
                          "tb" : 0,
                          "cb" : 0,
                          "fb" : 0,
                          "db" : 0,
                          "pn" : 0,
                          "tn" : 0,
                          "cn" : 0,
                          "fn" : 0,
                          "dn" : 0}

        self.tourne = tourne_auto
        self.edit = edit
        
        self.all_fleches_help = pygame.sprite.Group()

    def get_echequier(self):
        return self.echequier
    def update_echequier(self,new):
        self.echequier = new
        
    def ajoute_pion_blanc(self,x,y,numero):
        self.all_id_blancs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_pions_blancs.add(pion_blanc(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_tour_blanc(self,x,y,numero):
        self.all_id_blancs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_tours_blancs.add(tour_blanc(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_cavalier_blanc(self,x,y,numero):
        self.all_id_blancs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_cavaliers_blancs.add(cavalier_blanc(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_fou_blanc(self,x,y,numero):
        self.all_id_blancs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_fous_blancs.add(fou_blanc(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_dame_blanc(self,x,y,numero):
        self.all_id_blancs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_dames_blancs.add(dame_blanc(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_roi_blanc(self,x,y,numero):
        self.all_id_blancs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_rois_blancs.add(roi_blanc(self,x,y,numero))
        self.update_echequier(self.echequier)
        
    def ajoute_pion_noir(self,x,y,numero):
        self.all_id_noirs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_pions_noirs.add(pion_noir(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_tour_noir(self,x,y,numero):
        self.all_id_noirs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_tours_noirs.add(tour_noir(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_cavalier_noir(self,x,y,numero):
        self.all_id_noirs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_cavaliers_noirs.add(cavalier_noir(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_fou_noir(self,x,y,numero):
        self.all_id_noirs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_fous_noirs.add(fou_noir(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_dame_noir(self,x,y,numero):
        self.all_id_noirs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_dames_noirs.add(dame_noir(self,x,y,numero))
        self.update_echequier(self.echequier)
    def ajoute_roi_noir(self,x,y,numero):
        self.all_id_noirs.append(numero)
        self.echequier[(x,y)] = numero
        self.all_rois_noirs.add(roi_noir(self,x,y,numero))
        self.update_echequier(self.echequier)
    
    def recup_all_alive(self):
        self.all_blancs_alive.add(self.all_tours_blancs)
        self.all_blancs_alive.add(self.all_pions_blancs)
        self.all_blancs_alive.add(self.all_cavaliers_blancs)
        self.all_blancs_alive.add(self.all_fous_blancs)
        self.all_blancs_alive.add(self.all_dames_blancs)
        self.all_blancs_alive.add(self.all_rois_blancs)
        self.all_noirs_alive.add(self.all_tours_noirs)
        self.all_noirs_alive.add(self.all_pions_noirs)
        self.all_noirs_alive.add(self.all_cavaliers_noirs)
        self.all_noirs_alive.add(self.all_fous_noirs)
        self.all_noirs_alive.add(self.all_dames_noirs)
        self.all_noirs_alive.add(self.all_rois_noirs)
    
    def recup_all_id(self):
        for i in self.all_pions_blancs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_tours_blancs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_cavaliers_blancs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_fous_blancs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_rois_blancs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_dames_blancs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_pions_noirs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_tours_noirs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_cavaliers_noirs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_fous_noirs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_rois_noirs:
            self.dico_piece_id[i.get_id()] = i
        for i in self.all_dames_noirs:
            self.dico_piece_id[i.get_id()] = i

    def is_echec(self,couleur,echequier):
        return echec(self,couleur,echequier)
    def is_mat(self,couleur):
        return mat(self,couleur)
    
    def is_pat(self,couleur,echequier):
        return pat(self,echequier,couleur)
    def manque_materiel(self,couleur,echequier):
        return materiel(self,echequier,couleur)
    def is_repeat(self):
        return repeat(self)

    def ajoute_aide(self,x,y):
        self.all_aides.add(Aide(self,x,y))

    def change_blanc(self,piece):
        x,y = piece.get_pos()
        echequier = self.get_echequier()
        if echequier.sens == 1:
            if y == 0:
                self.n_pieces += 1
                echequier[(x,y)] = self.n_pieces
                piece.remove()
                new_piece = dame_blanc(self,x,y,self.n_pieces)
                self.all_dames_blancs.add(new_piece)
                self.all_blancs_alive.add(new_piece)
                self.all_id_blancs.append(self.n_pieces)
                return (True,new_piece)
            return (False,0)
        else:
            x,y = piece.get_pos()
        echequier = self.get_echequier()
        if y == 7:
            self.n_pieces += 1
            echequier[(x,y)] = self.n_pieces
            piece.remove()
            new_piece = dame_blanc(self,x,y,self.n_pieces)
            self.all_dames_blancs.add(new_piece)
            self.all_blancs_alive.add(new_piece)
            self.all_id_blancs.append(self.n_pieces)
            return (True,new_piece)
        return (False,0)

    def change_noir(self,piece):
        x,y = piece.get_pos()
        echequier = self.get_echequier()
        if echequier.sens == 0:
            if y == 0:
                self.n_pieces += 1
                echequier[(x,y)] = self.n_pieces
                piece.remove()
                new_piece = dame_noir(self,x,y,self.n_pieces)
                self.all_dames_noirs.add(new_piece)
                self.all_noirs_alive.add(new_piece)
                self.all_id_noirs.append(self.n_pieces)
                return (True,new_piece)
            return (False,0)
        else:
            x,y = piece.get_pos()
            echequier = self.get_echequier()
            if y == 7:
                self.n_pieces += 1
                echequier[(x,y)] = self.n_pieces
                piece.remove()
                new_piece = dame_blanc(self,x,y,self.n_pieces)
                self.all_dames_blancs.add(new_piece)
                self.all_blancs_alive.add(new_piece)
                self.all_id_blancs.append(self.n_pieces)
                return (True,new_piece)
            return (False,0)
        
    def remove_arrow(self):
        for i in self.all_fleches_help:
            i.remove(self)
    
    def arrow(self,debut,fin):
        if debut[0] != fin[0] and debut[1] != fin[1]:
            print(debut)
            print(fin)
            if abs(debut[0]-fin[0]) > abs(debut[1]-fin[1]):
                if debut[0] < fin[0]:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",0))
                    for i in range(debut[0]+1,fin[0]):
                        self.all_fleches_help.add(Fleche_aide(self,(i,debut[1]),"milieu",0))
                    if debut[1] < fin[1]:
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],debut[1]),"tournant",270))
                        for i in range(debut[1]+1,fin[1]):
                            self.all_fleches_help.add(Fleche_aide(self,(fin[0],i),"milieu",270))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",270))
                    elif debut[1] > fin[1]:
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],debut[1]),"tournant",180))
                        for i in range(fin[1]+1,debut[1]):
                            self.all_fleches_help.add(Fleche_aide(self,(fin[0],i),"milieu",90))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",90))
                        
                elif debut[0] > fin[0]:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",180))
                    for i in range(fin[0]+1,debut[0]):
                        self.all_fleches_help.add(Fleche_aide(self,(i,debut[1]),"milieu",0))
                    if debut[1] < fin[1]:
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],debut[1]),"tournant",0))
                        for i in range(debut[1]+1,fin[1]):
                            self.all_fleches_help.add(Fleche_aide(self,(fin[0],i),"milieu",270))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",270))
                    elif debut[1] > fin[1]:
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],debut[1]),"tournant",90))
                        for i in range(fin[1]+1,debut[1]):
                            self.all_fleches_help.add(Fleche_aide(self(fin[0],i),"milieu",90))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",90))
            elif abs(debut[0]-fin[0]) < abs(debut[1]-fin[1]):
                if debut[1] < fin[1]:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",270))
                    for i in range(debut[1]+1,fin[1]):
                        self.all_fleches_help.add(Fleche_aide(self,(debut[0],i),"milieu",90))
                    if debut[0] < fin[0]:
                        self.all_fleches_help.add(Fleche_aide(self,(debut[0],fin[1]),"tournant",90))
                        for i in range(debut[0]+1,fin[0]):
                            self.all_fleches_help.add(Fleche_aide(self,(i,fin[1]),"milieu",0))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",0))
                    elif debut[0] > fin[0]:
                        self.all_fleches_help.add(Fleche_aide(self,(debut[0],fin[1]),"tournant",180))
                        for i in range(fin[0]+1,debut[0]):
                            self.all_fleches_help.add(Fleche_aide(self,(i,fin[1]),"milieu",0))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",180))
                elif debut[1] > fin[1]:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",90))
                    for i in range(fin[1]+1,debut[1]):
                        self.all_fleches_help.add(Fleche_aide(self,(debut[0],i),"milieu",90))
                    if debut[0] < fin[0]:
                        self.all_fleches_help.add(Fleche_aide(self,(debut[0],fin[1]),"tournant",0))
                        for i in range(debut[0]+1,fin[0]):
                            self.all_fleches_help.add(Fleche_aide(self,(i,fin[1]),"milieu",0))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",0))
                    elif debut[0] > fin[0]:
                        self.all_fleches_help.add(Fleche_aide(self,(debut[0],fin[1]),"tournant",270))
                        for i in range(fin[0]+1,debut[0]):
                            self.all_fleches_help.add(Fleche_aide(self,(i,fin[1]),"milieu",0))
                        self.all_fleches_help.add(Fleche_aide(self,(fin[0],fin[1]),"fin",180))
            else:
                self.all_fleches_help.add(Fleche_aide(self,debut,"debut",30))
                self.all_fleches_help.add(Fleche_aide(self,(debut[0]+1,debut[1]+1),"milieu",30))
        else:
            if debut[0] == fin[0] and debut[1] != fin[1]:
                if debut[1] < fin[1]:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",270))
                    self.all_fleches_help.add(Fleche_aide(self,fin,"fin",270))
                else:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",90))
                    self.all_fleches_help.add(Fleche_aide(self,fin,"fin",90))
                for i in range(min(debut[1],fin[1])+1,max(debut[1],fin[1])):
                    self.all_fleches_help.add(Fleche_aide(self,(debut[0],i),"milieu",90))
            elif debut[0] != fin[0] and debut[1] == fin[1]:
                if debut[0] < fin[0]:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",0))
                    self.all_fleches_help.add(Fleche_aide(self,fin,"fin",0))
                else:
                    self.all_fleches_help.add(Fleche_aide(self,debut,"debut",180))
                    self.all_fleches_help.add(Fleche_aide(self,fin,"fin",180))
                    
                for i in range(min(debut[0],fin[0])+1,max(debut[0],fin[0])):
                    self.all_fleches_help.add(Fleche_aide(self,(i,debut[1]),"milieu",0))
            else:
                self.all_fleches_help.add(Fleche_aide(self,debut,"case",0))
        
        
        
                    
