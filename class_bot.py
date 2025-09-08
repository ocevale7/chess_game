from random import randint

class Bot:

    def __init__(self,Game,plateau,taille,couleur):

        self.game = Game
        self.__echequier = plateau
        self.__profondeur = taille
        self.c = couleur # 0 = blanc, 1 = noir

        self.all_suite = []

    def set_echequier(self,plateau):
        self.__echequier = plateau
    def get_echequier(self):
        return self.__echequier

    def get_profondeur(self):
        return self.__profondeur
    def set_profondeur(self,prof):
        self.__profondeur = prof      

    def heuristique(self,plateau):

        val_bot = 0
        val_player = 0
        
        if self.game.is_mat(self.c):
            return float("-inf")
        if self.game.is_mat(1 - self.c):
            return float("inf")

        for i in range(8):
            for j in range(8):
                if plateau[i,j] != 0:
                    p = self.game.dico_piece_id[plateau[i,j]]
                    if (p.color == "noir" and self.c == 1) or (p.color == "blanc" and self.c == 0):
                        val_bot += p.value
                    else:
                        val_player += p.value
        
        
        return val_bot - val_player
    
    def tri_par_prises(self, plateau, coups):
        
        def swap(l, i, j):
            buff = l[i]
            l[i] = l[j]
            l[j] = buff
        
        #Récupère les valeurs associées à chaque prises
        n = len(coups)
        l = []
        for i in range(n):
            if plateau[coups[i][1][0],coups[i][1][1]] != 0:
                p = self.game.dico_piece_id[plateau[coups[i][1][0],coups[i][1][1]]]
                l.append(p.value)
            else:
                l.append(0)
        #tri
        for i in range(n-1):
            m = i
            for j in range(i+1, n):
                if l[j] >= l[m]:
                    m = j
            swap(l, i, m)
            swap(coups, i, m)
                    
    
    def successeur(self, player, plateau):
        coups = list()
        for i in range(8):
            for j in range(8):
                if plateau[i,j] != 0:
                    p = self.game.dico_piece_id[plateau[i,j]]
                    if (p.color == "noir" and player == 1) or (p.color == "blanc" and player == 0):
                        possibilites = p.recup_all_pos((i,j),plateau)
                        for pos in possibilites:
                            coups.append(((i,j),pos))
        return coups
    
    def joue_fict(self, plateau, coup):
        ancien,nouveau = coup
        new_plateau = plateau.copy()
        new_plateau[nouveau] = new_plateau[ancien]
        new_plateau[ancien] = 0
        return new_plateau         
    
    def alpha_beta(self, plateau, player, profondeur, alpha, beta):
        if player == self.c :
            if self.game.is_mat(player):
                return float("-inf")
            else:
                if profondeur == 0:
                    return self.heuristique(plateau)
                else:
                    coups = self.successeur(player,plateau)
                    self.tri_par_prises(plateau, coups)
                    v = float("-inf")
                    for i in range(len(coups)):
                        new = self.joue_fict(plateau,coups[i])
                        v = max(v, self.alpha_beta(new,1-player,profondeur-1,alpha,beta))
                        if v >= beta:
                            return v
                        alpha = max(v, alpha)
                    return v
        else:
            if self.game.is_mat(player):
                return float("inf")
            else:
                if profondeur == 0:
                    return self.heuristique(plateau)
                else:
                    coups = self.successeur(player,plateau)
                    self.tri_par_prises(plateau, coups)
                    v = float("inf")
                    for i in range(len(coups)):
                        new = self.joue_fict(plateau,coups[i])
                        v = min(v, self.alpha_beta(new,1-player,profondeur-1,alpha,beta))
                        if v <= alpha:
                            return v
                        beta = min(v, beta)
                    return v
                
    def choix_prof(self):
        plateau = self.get_echequier()
        coups = self.successeur(self.c, plateau)
        self.tri_par_prises(plateau, coups)
        profondeur = self.get_profondeur()
        liste_of_meme_value = [(self.alpha_beta(self.joue_fict(plateau,coups[0]),1-self.c,profondeur, float("-inf"), float("inf")),0)]
        
        for i in range(1,len(coups)):
            new = self.joue_fict(plateau,coups[i])
            val = self.alpha_beta(new,1-self.c,profondeur, float("-inf"), float("inf"))
            print("%d/%d"%(i,len(coups)-1))
            print(coups[i])
            print(val)
            if liste_of_meme_value[0][0] < val:
                liste_of_meme_value = [(val,i)]
            elif liste_of_meme_value[0][0] == val:
                liste_of_meme_value.append((val,i))
        
        m = randint(0,len(liste_of_meme_value) - 1)
        print(m)
        return coups[liste_of_meme_value[m][1]]
        