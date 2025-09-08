import numpy as np

class echequier:

    sens = 0

    def __init__(self,edit):
        self.__plateau = np.array([0 for i in range(64)],int).reshape(8,8)
        
    def __repr__(self):
        return str(self.get_plateau())
    
    def get_plateau(self):
        return self.__plateau

    def __getitem__(self,co):
        return self.get_plateau()[co[1],co[0]]

    def __contains__(self,elt):
        plateau = self.get_plateau()
        for x in range(8):
            for y in range(8):
                if plateau[(x,y)] == elt:
                    return True
        return False

    def __setitem__(self,co,piece):
        self.get_plateau()[co[1],co[0]] = piece

    def __delitem__(self,co):
        self.get_plateau()[co[1],co[0]] = 0

    def copy(self):
        new = echequier(False)
        for x in range(8):
            for y in range(8):
                new[(x,y)] = self[(x,y)]
        return new

    def __echange(self,a,b):
        echequier = self.get_plateau()
        echequier[a],echequier[b] = echequier[b],echequier[a]

    def turn(self):
        echequier = self.get_plateau()
        for x in range(8):
            for y in range(4):
                self.__echange((x,y),(7-x,7-y))
        if self.sens == 0:
            self.sens = 1
        else :
            self.sens = 0
        
        
                

        
