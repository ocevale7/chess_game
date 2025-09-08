
def echec(game,couleur,echequier):
    if couleur == 0: #Vérifie si les blancs sont échecs
        for i in game.all_noirs_alive:
            if i.get_id() in echequier:
                pos_pieces = i.recup_all_pos((i.rect.x//100,i.rect.y//100),echequier,False)
                for mange in pos_pieces:
                    for _id in game.all_rois_blancs:
                        if echequier[mange] == _id.get_id():
                            return True
        return False
    else: #Vérifie si les noirs sont échecs
        for i in game.all_blancs_alive:
            if i.get_id() in echequier:
                pos_pieces = i.recup_all_pos((i.rect.x//100,i.rect.y//100),echequier,False)
                for mange in pos_pieces:
                    for _id in game.all_rois_noirs:
                        if echequier[mange] == _id.get_id():
                            return True
        return False

def mat(game,couleur):
    echequier_base = game.get_echequier().copy()

    oui = 0
    non = 0
    
    if couleur == 0:
        for i in game.all_blancs_alive:
            x,y = (i.rect.x//100,i.rect.y//100)
            pos_pieces = i.recup_all_pos((x,y),echequier_base)
            for pos in pos_pieces:
                echequier = echequier_base.copy()
                del echequier[(x,y)]
                echequier[pos] = i.get_id()
                if echec(game,couleur,echequier):
                    non +=1
                oui +=1
        return oui == non
    else:
        for i in game.all_noirs_alive:
            x,y = (i.rect.x//100,i.rect.y//100)
            pos_pieces = i.recup_all_pos((x,y),echequier_base)
            for pos in pos_pieces:
                echequier = echequier_base.copy()
                del echequier[(x,y)]
                echequier[pos] = i.get_id()
                if echec(game,couleur,echequier):
                    non +=1
                oui +=1
        return oui == non
                
                
